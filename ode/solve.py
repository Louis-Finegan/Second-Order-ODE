
# Used libaries.
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve

class second_order_ode:
    def __init__(self, a, b, c, y0: list) -> None:
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

    def eigen_values(self) -> tuple:
        if self.a**2 - 4*self.b < 0:
            m_1 = complex(-self.a/2, + np.sqrt(- self.a**2 + 4*self.b)/2)
            m_2 = complex(-self.a/2, - np.sqrt(- self.a**2 + 4*self.b)/2)

        elif self.a**2 - 4*self.b == 0:
            m_1 = -self.a/2
            m_2 = -self.a/2

        else:
            m_1 = -self.a/2 + np.sqrt(self.a**2 - 4*self.b)/2
            m_2 = -self.a/2 - np.sqrt(self.a**2 - 4*self.b)/2
        
        return (m_1, m_2)

    
    def equilibrium(self):
        
        def eq_equation(y):
            return [y[1], - self.a*y[1] - self.b*y[0]]

        equilibrium = fsolve(eq_equation, [0.0, 0.0])

        return equilibrium

class first_order_system:
    
    def __init__(self, equation_1, equation_2, y0: list) -> None:
        self.n = 100
        self.dt = 1/self.n
        self.t_int = [0, 10]
        self.equation_1 = equation_1
        self.equation_2 = equation_2
        self.y0 = y0

    def solve_system(self):
        def equation(t, y):
            x, y = y
            dydt = [self.equation_1(x, y), self.equation_2(x, y)]
            return dydt

        solution = solve_ivp(lambda t, y: equation(t, y), 
                            self.t_int, 
                            self.y0, 
                            t_eval=np.arange(self.t_int[0], 
                                            self.t_int[1], 
                                            self.dt))

        return solution.y[0], solution.y[1]

    def equilibrium(self):
        
        def eq_equation(y):
            return [self.equation_1(y[0], y[1]), self.equation_2(y[0], y[1])]

        equilibrium = fsolve(eq_equation, [0.0, 0.0])

        return equilibrium
