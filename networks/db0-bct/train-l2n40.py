#!/usr/bin/env python
from neural.bp import BPNeural
calc = BPNeural(dblabel='a0',
                label='l2n40',
                hiddenlayers=(2, 40))
calc.train('data.db')
