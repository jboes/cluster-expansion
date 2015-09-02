#!/usr/bin/env python
from neural.bp import BPNeural
calc = BPNeural(dblabel='../',
                label='./',
                hiddenlayers=(2, 30))
calc.train('../data.db')
