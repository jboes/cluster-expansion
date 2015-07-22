#!/usr/bin/env python
from neural.bp import BPNeural
calc = BPNeural(dblabel='a0',
                label='l3n30',
                hiddenlayers=(3, 30))
calc.train('data.db')
