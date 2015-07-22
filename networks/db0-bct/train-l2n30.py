#!/usr/bin/env python
from neural.bp import BPNeural
calc = BPNeural(dblabel='a0',
                label='l2n30',
                hiddenlayers=(2, 30))
calc.train('data.db')
