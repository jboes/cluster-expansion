#!/usr/bin/env python
from neural.bp import BPNeural
calc = BPNeural(dblabel='a0',
                label='l4n40',
                hiddenlayers=(4, 40))
calc.train('data.db')
