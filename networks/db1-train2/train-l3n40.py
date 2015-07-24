#!/usr/bin/env python
from neural.bp import BPNeural
calc = BPNeural(dblabel='a0',
                label='l3n40',
                hiddenlayers=(3, 40))
calc.train('data.db')
