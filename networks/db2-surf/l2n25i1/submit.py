#!/usr/bin/env python
from neural.bp import BPNeural
calc = BPNeural(dblabel='../',
                label='./',
                hiddenlayers=(2, 25))
calc.train('../data.db')
