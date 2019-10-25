
c=int(input('Press 0 for non-power saving mode, 1 for power saving mode: '))

if(c==0):
    from embed_max import *
else:
    from embed_min import *
