import numpy as np
x=np.arange(9).reshape((3,3))
print(x)
print(np.diag(x))
m=np.diag(np.diag(x) )
print(m)

fw = np.zeros((3, 5 + 1))
print("before :", fw[:, 1].shape)

print(0.00249325 + 0.0019431 + 0.00391118)

import pickle

with open("test.txt", "wb") as fp:
    pickle.dump(fw, fp)

with open("test.txt", "rb") as fp:
    b = pickle.load(fp)

print("after :", fw[:, 1].shape)
