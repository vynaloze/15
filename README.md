# Requirements
- python 3.7+

# Running
## Solver
`python -m solver.main [algorithm flag] < data/example.input > data/solution.output`

e.g.

`python -m solver.main --bfs U D R L < data/example.input > data/solution.output`

## Viewer
`python -m viewer.main --board data/example.input --solution data/solution.output`