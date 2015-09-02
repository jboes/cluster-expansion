#!/usr/bin/env python
from neural.bp import BPNeural
calc = BPNeural(dblabel='../',
                label='./',
                hiddenlayers=(4, 20))
calc.train('../data.db')
