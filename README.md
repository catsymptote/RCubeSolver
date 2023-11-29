# Rubik's Cube Solver

## Status
[Title](https://jperm.net/3x3/moves)

## To-do's
Make a set of moves into a Moves class, or something similar, which inherits from a list, and can take in and out both string-formatted moves and list formattes moves. The `Algorithm` class is an early prototype of this. Continue there.

Printing should convert to string. Repr could be str(list)?

Reduce unnecessary moves from algs. E.g., "R U U" can be recuded to "R". This should also be applied to the scrambler. Though it should keep the right amount of scramble moves. So add moves until the recudes version is $N$ moves long.

Stop if solved-addition to the solver. With the scramble "U", the simplest solution is "U'". The solvers solution is 111 moves long, starting with "U' R' ...". If it stopped when solved, it would just stop after the first move. This method will probably be slow, as it would have to check if solved $N$ times for $N$ moves, and rarely actually optimize. Therefore it could be added to a set of slow-optimizers. Maybe split into fast and slow? Not sure.

Make a move rotator. If an algorithm does X ... X', then "..." can be rotated with X, and X dropped.

Make a move length comparator. How effective are the different reducers? Compare. Do sciece. Maybe make into a separate sub-project?


## Move Notation

[Rubik's cube notation](https://ruwix.com/the-rubiks-cube/notation/)

### Single outer

| Notation |  Description |  Exp Notation | Base? |
| -------- | ------------ | ------------- | ----- |
| U        | Up           |               | x     |
| R        | Right        |               |       |
| F        | Front        |               |       |
| D        | Down         |               |       |
| L        | Left         |               |       |
| B        | Back         |               |       |

### Double

| Notation |  Description |  Exp Notation | Base? |
| -------- | ------------ | ------------- | ----- |
| u        | Up           | U + E'        |       |
| r        | Right        | R + M'        |       |
| f        | Front        | F + M'        |       |
| d        | Down         | D + E         |       |
| l        | Left         | L + E         |       |
| b        | Back         | B + M         |       |

### Single inner

| Notation |  Description |  Exp Notation | Base? |
| -------- | ------------ | ------------- | ----- |
| E        | With D       |               | x     |
| M        | With L       |               |       |
| S        | With F       |               |       |

### Rotations

| Notation |  Description |  Exp Notation | Base? |
| -------- | ------------ | ------------- | ----- |
| X        | With D       |               | x\*   |
| Y        | With L       |               | x\*   |
| Z        | With F       |               | x\*   |

\* Though one of these can be swapped out with a of the others, so we'd really only need two of them.

### Base moves
A few of the moves are dirrectley implemented into the `Cube` class, and is therefore a *base move*. Most of them, however, are simply composite moves. A `U`, being a base move, is performed directley. An `R` is, however, not a base move, and is therefore not performed directly. It is rather converted/translated into a set of the base moves. In this case, `R` $\rightarrow$ `Z' U Z`.
Though as `Z'` is also not part of the base moves, it further translated into `Z Z Z`. Thus, a simple `R` is translated into:

`R` $\rightarrow$ `Z Z Z U Z`

Performing all these extra moves is of course very inefficient. A solution to make this move efficient is to hardcode more base moves, or to implement a more efficient and more generalized solution. Is this possible? Maybe.


## Algorithm notation

Algorithms can be written in the `alg_lookup` lookup table. They can be written in as strings (see `alg_lookup` for examples), but should always be used in the form of a list. E.g.,

```python
["R", "U", "R'", "U'"]
```

## Methods

### Old Pochmann

[More info](https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-blindfolded-tutorial/)

Notation: Uppercase letters are edgesm while lowercase letters are corners.
Edge buffer is `B` and corner buffer is `a`.

## Technical

### Printing
We use `colorama` to print the cube with ANSI colors. One can choose to color the background or the foreground.
["Source"](https://stackoverflow.com/questions/54587206/how-to-change-python-background-to-a-certain-colour-with-colorama).
