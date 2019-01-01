import sys
import os
arg = sys.argv
for i in arg[1:]:
     os.system("potrace -b svg -b pdf "+i)
