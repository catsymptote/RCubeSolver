# Rubik's Cube Solver

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
