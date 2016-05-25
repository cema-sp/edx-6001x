def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    x = start
    rad = 0
    while x < stop:
        rad += f(x) * step
        x += step

    return rad

def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

print abs(radiationExposure(0, 5, 1) - 39.10318784326239) < 0.01
print abs(radiationExposure(5, 11, 1) - 22.94241041057671) < 0.01
print abs(radiationExposure(0, 11, 1) - 62.0455982538) < 0.01
print abs(radiationExposure(40, 100, 1.5) - 0.434612356115) < 0.01
