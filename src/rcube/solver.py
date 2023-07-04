from rcube.pochmann import Pochmann
from rcube.cube import Cube


class Solver:
    def __init__(self, solver_class=None):
        if solver_class is None:
            solver_class = Pochmann
        self.solver_obj = solver_class()

    def perform_moves(self, scramble_moves):
        # Perform moves
        pass
