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
                raise ValueError(f'Invalid move: "{move1}" or "{move2}".')

        new_move = self.give_valid_amount(move1, amount)
        return new_move

    def reduce_by_combining(self) -> bool:
        new_moves = []
        changed_last_loop = True
        for index in range(len(self.moves) - 1):
            # Set flag and moves.
            changed_last_loop = False
            move1 = self.moves[index]
            move2 = self.moves[index + 1]

            # If reducable moves, combine and append new move.
            if self.is_same_move(move1, move2):
                new_move = self.combine_moves(move1, move2)
                print(move1, move2, new_move)
                if new_move is not None:  # Check if move is not None.
                    new_moves.append(new_move)
                    changed_last_loop = True
            
            # If no reduction possible, append move.
            else:
                new_moves.append(move1)

        if not changed_last_loop:
            new_moves += self.moves[-1:]

        changed = len(new_moves) != len(self.moves)
        self.moves = new_moves
        print(self.moves)
        return changed

    def reduce_by_combining_old(self) -> bool:
        modified = False
        index = 0
        while index < len(self.moves) - 1:
            if self.is_same_move(self.moves[index], self.moves[index + 1]):
                new_move = self.combine_moves(self.moves[index],
                                              self.moves[index + 1])
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
