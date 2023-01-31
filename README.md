# Second Order ODEs and Systems of ODEs with `SciPy`

## Solves a second order Linear ODE 

Takes the form:

$$\frac{d^2y}{dt^2} + a(t)\frac{dy}{dt} + b(t)y = c(t)$$

With initial conditions $y(0) = y_0$ and $y^\prime(0) = y^\prime_0$.

Coefficients are functions of $t$ and are defined in `second_order.ipynb`

`second_order_ode` module in the `ode.py` file and is imported into `second_order.ipynb`.

## Solves a First Order System of ODEs

Takes the form:

$$\frac{dx}{dt} = F(x, y)$$

$$\frac{dy}{dt} = G(x, y)$$

With initial conditions $x(0) = x_0$ and $y(0) = y_0$.

$F$ and $G$ are defined in `first_order_system.ipynb`.

`first_order_system_ode` module in the `ode.py` file and is imported into `first_order_system.ipynb`.
 
## Required packages and libaries

1. `numpy`

2. `scipy` using the `integrate` module 

3. `matplotlib` using the `pyplot` module

