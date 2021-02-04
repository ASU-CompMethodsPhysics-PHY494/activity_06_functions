# Activity 06: Functions
![GitHub Classroom Workflow](../../workflows/GitHub%20Classroom%20Workflow/badge.svg?branch=main) ![Points badge](../../blob/badges/.github/badges/points.svg)


Solve the following problems.

See https://asu-compmethodsphysics-phy494.github.io/ASU-PHY494/2021/02/04/04_Python_3/ for help.

## Create functions

1. create a file `myfuncs.py`
2. add a Heaviside function `heaviside()` to the file 
3. add a function `fahrenheit2kelvin()` to convert from Fahrenheit to
   Kelvin
4. add a function `kelvin2celsius()` to convert from Kelvin to Celsius
   (subtract 273.15).

Test your functions yourself in `ipython`:
```python
In [1]: %run myfuncs.py
In [2]: heaviside(5)
Out[2]: 1.0
In [3]: fahrenheit2kelvin(100)
Out[3]: 310.92777777777775
In [4]: kelvin2celsius(300)
Out[4]: 26.850000000000023
In [5]: kelvin2celsius(fahrenheit2kelvin(100))
Out[5]: 37.77777777777777
```

## Plotting the step function

Create a program `step_plot.py` that

1. defines the Heaviside step function `heaviside(x)` (you can copy your code from the previous problem)
2. generates a list of x values
   `x_values = [-4, -3.5, -3, ..., 0, 0.5, 1, 1.5, ... 4]`;
3. evaluates `heaviside(x)` for all x values and stores the results
   in a list `y_values`;
4. prints the lists of x and y = heaviside(x) values; it should look
   like
   ~~~
	-4.0 0.0
	-3.5 0.0
    ...
    3.5 1.0
	4.0 1.0 
   ~~~


BONUS: You can plot the Heaviside function with the `plot()` function from matplotlib:
```python
import matplotlib.pyplot as plt

plt.plot(x_values, y_values, '-o', color="red", linewidth=2)
plt.show()
```
(This is not tested.)

## BONUS: Function arguments

Add to your file `myfuncs.py` a function `area()` that
- takes two numbers as required arguments
- has an optional keyword argument *scale* that defaults to 1
- has an optional keyword argument *offset* that defaults to 0
- computes the (scaled) area of a rectangle A = scale * (x * y + offset)

(**Note**: This is a *BONUS* problem. This means that the points for
this problem are not required to get full marks. If you do not solve
this problem then your workflow badge will show a failure with 18/20
points. However, the maximum number of points as set in Canvas are set
to 18, so you will still score full points. You cannot score more than
18 points in Canvas.)