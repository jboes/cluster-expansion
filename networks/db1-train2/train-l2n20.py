#!/usr/bin/env python
from neural.bp import BPNeural
calc = BPNeural(dblabel='a0',
                label='l2n20',
                hiddenlayers=(2, 20))
calc.train('data.db')
