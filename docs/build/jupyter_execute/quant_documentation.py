#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import quant_documentation.hyperbolic as hyperbolic
import numpy as np
x = np.linspace(-1.0,1.0,11)
y = hyperbolic.hyperbolic(x)
plt.plot(x,y)

