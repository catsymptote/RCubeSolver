from rcube.pochmann_solver import PochmannSolver
from rcube.cube import Cube


class Solver:
    def __init__(self, solver_class=None):
        if solver_class is None:
            solver_class = PochmannSolver
        self.solver_obj = solver_class(Cube())

    def perform_moves(self, scramble_moves):
        # Perform moves
        pass
