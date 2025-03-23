import numpy as np
import time

np.random.seed(12345)
x = np.random.randn(3, 10_000)
M = np.eye(3)
 
repeats = 1_000
 
t0 = time.time()
 
# do work a lot!
for ri in range(repeats):
    out = np.sum(M @ x, axis=0)
 
dt = time.time() - t0
 
print(f"Execution time [numpy ] {dt} seconds")
