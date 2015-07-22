#!/usr/bin/env python
from neural.bp import BPNeural
calc = BPNeural(dblabel='a0',
                label='l4n50',
                hiddenlayers=(4, 50))
calc.train('data.db')
