"""content of module_a.py:
# some_var = 1
"""

"""content of module_b.py:
# some_var = 0
"""

from module_a import *  # better: import module_a as a
from module_b import *  # better: import module_b as b


print(some_var)
# better: print(a.some_var)
# better: print(b.some_var)
