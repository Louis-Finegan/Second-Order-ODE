
# Used libaries.
import numpy as np
from scipy.integrate import solve_ivp


class second_order_ode:
    def __init__(self, a: any, b: any, c: any, y0: list) -> None:
        self.n = 100
        self.dt = 1/self.n
        self.t_int = [0, 10]
        self.a = a
        self.b = b
        self.c = c
        self.y0 = y0

    # used `solve_ivp()` to solve second order ode as a system of odes.
    def solve_ode(self) -> tuple:
        def equation(t, y):
            y, yprime = y
            dydt = [yprime, - self.a(t)*yprime - self.b(t)*y + self.c(t)]
            return dydt

        solution = solve_ivp(lambda t, y: equation(t, y), 
                            self.t_int, 
                            self.y0, 
                            t_eval=np.arange(self.t_int[0], 
                                            self.t_int[1], 
                                            self.dt))

        return solution.y[0], solution.y[1]

