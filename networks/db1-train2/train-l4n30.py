#!/usr/bin/env python
from neural.bp import BPNeural
calc = BPNeural(dblabel='a0',
                label='l4n30',
                hiddenlayers=(4, 30))
calc.train('data.db')
