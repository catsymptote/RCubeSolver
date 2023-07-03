class Reducer:
    def __init__(self, moves):
        self.moves = moves

    def is_inverse_move(self, move1, move2):
        if move1 + "'" == move2:
            return True
        return False

    def is_same_move(self, move1, move2):
        return move1[0] == move2[0]

    def give_valid_amount(self, move, amount) -> str | None:
        amount = amount % 4
        if amount not in [1, 2, 3]:
            return None

        modifiers = {1: "", 2: "2", 3: "'"}
        modifier = modifiers[amount]
        base_move = move[0]
        new_move = base_move + modifier
        return new_move

    def combine_moves(self, move1, move2):
        amount = 0
        for move in (move1, move2):
            if len(move) == 1:
                amount += 1
            elif move[1] == "'":
                amount -= 1
            elif move[1] == "2":
                amount += 2
            else:
                assert False, f'Should not happen. ("{move1}" and "{move2}".)'

        new_move = self.give_valid_amount(move1, amount)
        return new_move

    def reduce_by_combining(self) -> bool:
        modified = False
        index = 0
        while index < len(self.moves) - 1:
            if self.is_same_move(self.moves[index], self.moves[index + 1]):
                new_move = self.combine_moves(self.moves[index], self.moves[index + 1])
                if new_move:
                    # Modify
                    self.moves[index] = self.combine_moves(
                        self.moves[index], self.moves[index + 1]
                    )
                    del self.moves[index + 1]

                    modified = True
                    index -= 1
            index += 1
        return modified

    def reduce_by_undoing(self) -> bool:
        modified = False
        index = 0
        while index < len(self.moves) - 1:
            if self.is_inverse_move(self.moves[index], self.moves[index + 1]):
                # Modify
                del self.moves[index]
                del self.moves[index]

                modified = True
                index -= 1
            index += 1
        return modified

    def reduce(self):
        reduction_functions = [self.reduce_by_undoing, self.reduce_by_combining]
        flag = True
        while flag:
            flag = False
            for red_func in reduction_functions:
                if red_func():
                    flag = True

    def get_moves(self):
        return self.moves


def test_reducer():
    moves = ["R", "U", "R", "U", "R", "R'", "U"]
    expected_moves = ["R", "U", "R", "U2"]

    red = Reducer(moves)
    red.reduce()
    resulting_moves = red.get_moves()

    assert expected_moves == resulting_moves, f"{expected_moves}\n{resulting_moves}"
    print("Success!")


if __name__ == "__main__":
    test_reducer()
