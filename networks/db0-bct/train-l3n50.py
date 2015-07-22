#!/usr/bin/env python
from neural.bp import BPNeural
calc = BPNeural(dblabel='a0',
                label='l3n50',
                hiddenlayers=(3, 50))
calc.train('data.db')
