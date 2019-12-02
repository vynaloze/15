# Requirements
- python 3.7+

# Running
## Solver
`python -m solver.main [algorithm flag] [value] < data/example.input > data/solution.output`
- for `bfs`, `dfs`, `idfs` value is move order
- for `bf`, `astar`, `sma` value is heuristic id h0, h1 or h2

e.g.

`python -m solver.main --bfs U D R L < data/example.input > data/solution.output`
`python -m solver.main --astar h1 < data/example.input > data/solution.output`

## Viewer
`python -m viewer.main --board data/example.input --solution data/solution.output`