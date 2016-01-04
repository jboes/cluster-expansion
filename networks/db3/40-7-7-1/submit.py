#!/usr/bin/env python
from amp import Amp
from amp.descriptor import Behler
from amp.regression import NeuralNetwork

calc = Amp(label="./",
           dblabel="../",
           descriptor=Behler(cutoff=6.5),
           regression=NeuralNetwork(hiddenlayers=(2, 7)))

calc.train("../train.db",
           cores=16,
           force_goal=None,
           extend_variables=False)
