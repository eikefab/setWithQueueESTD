from setwithqueue import *

set = SetWithQueue()

set.add(1)
set.add(2)
set.remove(1)
set.add(1)
set.add(3)
set.remove(2)
set.remove(3)

print(set)