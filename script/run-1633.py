#!/usr/bin/env python
# from ase.db import connect
from amp import Amp
from ase.md.langevin import Langevin
from ase.io.trajectory import Trajectory
from ase import units

images = Trajectory("/home-research/jboes/research/cluster-expansion/script/out-1633.traj", "r")
atoms = images[-1]

# db = connect("/home-research/jboes/research/cluster-expansion/temp/vegard-3x3.db")
# atoms = db.get_atoms(1633)

atoms.set_calculator(Amp("/home-research/jboes/research/cluster-expansion/networks/db5/40-7-7-1/"))

T = 500
dyn = Langevin(atoms, 5 * units.fs, T * units.kB, 0.002)

def printenergy(a=atoms):  # store a reference to atoms in the definition.
    """Function to print the potential, kinetic and total energy."""
    epot = a.get_potential_energy()
    ekin = a.get_kinetic_energy()

# Record the energies in the trajectory file
dyn.attach(printenergy, interval=1)

# We also want to save the positions of all atoms after every 100th time step.
traj = Trajectory("/home-research/jboes/research/cluster-expansion/script/out-1633.traj", "a", atoms)
dyn.attach(traj.write, interval=1)

# Now run the dynamics
dyn.run(5000)
