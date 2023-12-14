import sys
import numpy as np

from typing import List


class Ocean:
    state: List[List[int]]

    def __init__(self, init_state: List[List[int]]):
        self.state = init_state

    def __str__(self) -> str:
        return "\n".join(["".join(str(el) for el in row) for row in self.state])

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.state!r})"

    def gen_next_quantum(self) -> "Ocean":
        num_rows, num_cols = len(self.state), len(self.state[0])
        new_state = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        old_state = np.pad(np.array(self.state.copy()), 1)

        for row in range(1, num_rows+1):
            for col in range(1, num_cols+1):
                animals = {i: 0 for i in range(4)}

                for step_x in [-1, 0, 1]:
                    for step_y in [-1, 0, 1]:
                        if abs(step_x) + abs(step_y) != 0:
                            animals[old_state[row+step_x][col+step_y]] += 1
                        else:
                            continue

                if (old_state[row][col] == 2) and ((animals[2] >= 4) or (animals[2] <= 1)):
                    new_state[row-1][col-1] = 0

                elif (old_state[row][col] == 3) and ((animals[3] >= 4) or (animals[3] <= 1)):
                    new_state[row-1][col-1] = 0

                elif old_state[row][col] == 0:
                    if animals[2] == 3:
                        new_state[row-1][col-1] = 2
                    elif animals[3] == 3:
                        new_state[row-1][col-1] = 3
                    else:
                        new_state[row-1][col-1] = old_state[row][col]

                else:
                    new_state[row-1][col-1] = old_state[row][col]

        self.state = new_state
        return self.state


if __name__ == "__main__":
    n_quantums = int(sys.stdin.readline())
    n_rows, n_clms = (int(i) for i in sys.stdin.readline().split())
    init_state_ = []
    for i in range(n_rows):
        line = [int(i) for i in sys.stdin.readline().split()]
        init_state_.append(line)

    ocean = Ocean(init_state=init_state_)
    for _ in range(n_quantums):
        ocean = ocean.gen_next_quantum()
    print(ocean)
