#!/usr/bin/env python

import numpy as np
from ase.atoms import Atoms
import random
from ase.units import kB
from ase.db import connect

def main(atoms, dbname, T=800, steps=10000):

    db = connect(dbname)

    # Setting up variables for Cannonical MC
    symbols = atoms.get_chemical_symbols()
    chem_bins = {sym: [] for sym in set(symbols)}

    for i, s in enumerate(symbols):
	chem_bins[s] += [i]

    # Calculate the initial energy and store it
    nrg = atoms.get_potential_energy()

    dummy = Atoms.copy(atoms)
    db.write(dummy, nrg=nrg)

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

# Select the 
db = connect('/home/jacob/research/cluster-expansion/MC/108-36.db')
E, ID = [], []
for d in db.select():
    E += [d.nrg]
    ID += [d.id]
E = np.array(E)
ID = np.array(ID)

i = list(E).index(min(E))
atoms = db.get_atoms(ID[i])

from amp import Amp

atoms.set_calculator(Amp('/home/jacob/research/cluster-expansion/networks/db5/40-7-7-1/trained-parameters.json'))

main(atoms, '/home/jacob/research/cluster-expansion/MC/lowT-108-36.db', T=100, steps=10000)
