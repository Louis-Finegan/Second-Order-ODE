# Second Order ODEs with `SciPy`

Solves a second order Linear ODE of the form:

$$\frac{d^2y}{dt^2} + a(t)\frac{dy}{dt} + b(t)y = c(t)$$

With initial conditions $y(0) = y_0$ and $y^\prime(0) = y^\prime_0$.

Coefficients are functions of $t$ and are defined explicitly in `note.ipynb`

`second_order_ode` module in the `ode.py` file and is imported into `note.ipynb`.

## Required packages and libaries

1. `numpy`

2. `scipy` using the `integrate` module 

3. `matplotlib` using the `pyplot` module

