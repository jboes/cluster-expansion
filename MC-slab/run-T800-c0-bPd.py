#!/usr/bin/env python
from ase.lattice.cubic import FaceCenteredCubic as fcc
from ase.lattice.surface import surface
import numpy as np
from ase.atoms import Atoms
import random
from ase.units import kB
from ase.db import connect

def main(atoms, dbname, T, steps):

    db = connect(dbname)

    # Setting up variables for Cannonical MC
    symbols = atoms.get_chemical_symbols()
    chem_bins = {sym: [] for sym in set(symbols)}

    for i, s in enumerate(symbols):
        if atoms[i].position[2] > 10.:
	    chem_bins[s] += [i]

    # Calculate the initial energy and store it
    nrg = atoms.get_potential_energy()

    # dummy = Atoms.copy(atoms)
    # db.write(dummy, nrg=nrg)

    # Perform MC steps
    attempt, success = 0, 0
    while success < steps:

        # First, choose two chemicals to swap
        sym1, sym2 = random.sample(chem_bins.keys(), 2)
        random.shuffle(chem_bins[sym1])
        ind1 = chem_bins[sym1][-1]

        random.shuffle(chem_bins[sym2])
        ind2 = chem_bins[sym2][-1]

        # Create new atoms object to test
        new_atoms = Atoms.copy(atoms)
        new_atoms.set_calculator(atoms.get_calculator())

        # Update the atoms object
        new_atoms[ind1].symbol, new_atoms[ind2].symbol = sym2, sym1

        # Calculate the energy of the new system
        new_nrg = new_atoms.get_potential_energy()

        # Stores energy in continuously growing list
        # potentially memory intensive, but faster than writing to disk
        if new_nrg < nrg:
            atoms = new_atoms
            nrg = new_nrg
	    chem_bins[sym2][-1] = ind1
	    chem_bins[sym1][-1] = ind2

            dummy = Atoms.copy(atoms)
            db.write(dummy, nrg=nrg)
            success += 1

        elif np.exp(-(new_nrg - nrg) / (kB * T)) > np.random.rand():
            atoms = new_atoms
            nrg = new_nrg
	    chem_bins[sym2][-1] = ind1
	    chem_bins[sym1][-1] = ind2

            dummy = Atoms.copy(atoms)
            db.write(dummy, nrg=nrg)
            success += 1

        attempt += 1

    return success/attempt

from amp import Amp

atoms = fcc('Cu', latticeconstant=3.71025)
for j in range(1, 0+2):
    atoms[j].symbol = 'Pd'
atoms = surface(atoms, (1, 1, 1), 5)
atoms.center(vacuum=6., axis=2)
atoms.set_pbc([1, 1, 0])

index = [atom.index for atom in atoms if atom.position[2] < 10.]
if 'Pd' != 'None':
    for i in index:
	atoms[i].symbol = 'Pd'

atoms *= (5, 5, 1)

atoms.set_calculator(Amp('/home-research/jboes/research/cluster-expansion/networks/db6/40-7-7-1/'))

main(atoms, '/home-research/jboes/research/cluster-expansion/MC-slab/T800-c0-bPd.db', T=800, steps=4999)
