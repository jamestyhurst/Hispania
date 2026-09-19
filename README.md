# Hispania

RPG game set in Iron Age Spain, where the player starts as a Celtiberian tribesman who must side with the Romans, Carthaginians, or Iberians.

The main inspiration is Alessandro Roberti's *A Legionary's Life* (2019): a personal war-RPG, not a grand-strategy map.

## Status

`master` is the 2020 stub.

This branch is implementation only. Research and James's 2026-09-19 direction live on draft PR #1 (`device/iphone/2026-09-18-research`). Do not treat this package as a designer note.

Playable slice: `src/hispania/`. Default start is a non-Celtic Iberian origin at a placeholder home oppidum, walking a data-driven sequence. Celtiberian is already a catalog origin. See `src/hispania/README.md`.

```
PYTHONPATH=src python -m hispania --demo --seed 1
PYTHONPATH=src python -m unittest discover -s tests
```
