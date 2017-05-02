import sys

# Checking for libraries
# print 'numpy' in sys.modules
# print 'scipy' in sys.modules
# print 'matplotlib' in sys.modules
# print 'pandas' in sys.modules
# print 'sklearn' in sys.modules

# Check the versions of libraries

# Python version
print('Python: {}'.format(sys.version))

# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))

# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))

# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))

# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))

# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))
