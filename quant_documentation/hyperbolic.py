import numpy as np

def hyperbolic(x):
      """ Using the hyperbolic function 
    
      .. _target hyperbolic_function:

      .. math::

        f(x) = \\frac{1}{2} \\left(x + \sqrt{1 + x^2} \\right)

      Args:
          x (tensor(shape=(...))): M-dimensional tensor

      Returns:
          y (tensor(shape=(...))): Hyperbolic function

      .. jupyter-execute::          

          import matplotlib.pyplot as plt
          import quant_documentation.hyperbolic as hyperbolic
          import numpy as np
          x = np.linspace(-1.0,1.0,11)
          y = hyperbolic.hyperbolic(x)
          plt.plot(x,y)
          
      """
      
      return (x + np.sqrt(1. + x*x))/2.