#!/usr/bin/env python
from neural.bp import BPNeural
calc = BPNeural(dblabel='a0',
                label='l4n20',
                hiddenlayers=(4, 20))
calc.train('data.db')
