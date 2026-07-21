

import time
import numpy as np

# Create Python List
python_list = list(range(1000000))

# Measure Python List Performance
start = time.time()

result = []
for i in python_list:
    result.append(i * 2)

end = time.time()

python_time = end - start

print("Python List Time :", python_time, "seconds")


# Create NumPy Array
numpy_array = np.arange(1000000)

# Measure NumPy Performance
start = time.time()

result = numpy_array * 2

end = time.time()

numpy_time = end - start

print("NumPy Array Time :", numpy_time, "seconds")