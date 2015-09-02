#!/usr/bin/env python
from neural.bp import BPNeural
calc = BPNeural(dblabel='../',
                label='./',
                hiddenlayers=(3, 50))
calc.train('../data.db')
