#!/usr/bin/env python
from neural.bp import BPNeural
calc = BPNeural(dblabel='../',
                label='./',
                hiddenlayers=(3, 40))
calc.train('../data.db')
