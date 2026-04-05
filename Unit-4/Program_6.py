import matplotlib.pyplot as plt
import numpy as np

ages = np.random.randint(1, 100, 50)

bins = [0,10,20,30,40,50,60,120]

plt.hist(ages, bins=bins)
plt.show()
