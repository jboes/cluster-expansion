#!/usr/bin/env python
from neural.bp import BPNeural
calc = BPNeural(dblabel='a0',
                label='l3n20',
                hiddenlayers=(3, 20))
calc.train('data.db')
