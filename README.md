# Rubik's Cube Solver

## Info

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

### Single inner

| Notation |  Description |  Exp Notation | Base? |
| -------- | ------------ | ------------- | ----- |
| E        | With D       |               | x     |
| M        | With L       |               |       |
| S        | With F       |               |       |

### Double

| Notation |  Description |  Exp Notation | Base? |
| -------- | ------------ | ------------- | ----- |
| u        | Up           | U + E'        |       |
| r        | Right        | R + M'        |       |
| f        | Front        | F + M'        |       |
| d        | Down         | D + E         |       |
| l        | Left         | L + E         |       |
| b        | Back         | B + M         |       |

### Rotations

| Notation |  Description |  Exp Notation | Base? |
| -------- | ------------ | ------------- | ----- |
| X        | Up           |               | x\*   |
| Y        | Right        |               | x\*   |
| Z        | Front        |               | x\*   |

\* Though one of these can be swapped out with a of the others, so we'd really only need two of them.

## Methods

### Old Pochmann

[More info](https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-blindfolded-tutorial/)
