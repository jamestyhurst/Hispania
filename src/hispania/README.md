# `src/hispania` — isolated playable stub

Not the game. Not a designer note. Does not rewrite `Research_Documents/`.

One Celtiberian body, one seeded encounter (`throw` / `close` / `yield`), optional allegiance from the root README (`rome` / `carthage` / `iberians`).

## Run

From the repository root:

```
PYTHONPATH=src python -m hispania --demo --seed 1
PYTHONPATH=src python -m hispania
PYTHONPATH=src python -m unittest discover -s tests
```

`--demo` skips prompts so the loop is scriptable. Interactive mode asks name, allegiance, and action when stdin is a TTY.
