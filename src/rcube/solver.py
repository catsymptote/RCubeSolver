from rcube.pochmann_solver import PochmannSolver
from rcube.cube_interface import CubeInterface


class Solver:
    def __init__(self, solver_class=None):
        if solver_class is None:
            solver_class = PochmannSolver
        self.solver_obj = solver_class(CubeInterface())

    def perform_moves(self, scramble_moves):
        # Perform moves
        pass
