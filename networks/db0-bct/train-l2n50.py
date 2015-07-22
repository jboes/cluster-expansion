#!/usr/bin/env python
from neural.bp import BPNeural
calc = BPNeural(dblabel='a0',
                label='l2n50',
                hiddenlayers=(2, 50))
calc.train('data.db')
