# Analisi e Visualizzazione delle Reti Complesse 2025/26

Course materials for **Network Science** at the University of Turin (UNITO).

📄 **[Syllabus](ns_syllabus.pdf)**

## Contents

| Folder | Description |
|---|---|
| `slides/` | Lecture slides (PDF) |
| `tutorials/src/` | Jupyter tutorial notebooks |
| `tutorials/datasets/` | Network datasets |

## Lectures

| # | Topic | Slides | Notebook |
|---|---|---|---|
| 1 | Introduction | [ns01-intro.pdf](slides/ns01-intro.pdf) | |
| 2–3 | Recap on Graphs | [ns02-03-graphs.pdf](slides/ns02-03-graphs.pdf) | [01-intro-graphs.ipynb](tutorials/src/01-intro-graphs.ipynb) |

## Getting started

### Requirements

```bash
pip install networkx matplotlib numpy jupyter
```

### Run the notebooks

```bash
git clone https://github.com/rschifan/avrc-2526.git
cd avrc-2526
jupyter notebook tutorials/src/
```

## Course utilities

[`tutorials/src/netsci_utils.py`](tutorials/src/netsci_utils.py) provides shared helpers used across all notebooks:

- `draw_graph(G)` — consistent graph drawing
- `compute_ccdf(sequence)` / `plot_ccdf(...)` — degree distribution plots
- `print_network_stats(G)` — summary statistics
- `load_openflights_usa()` / `load_friends()` — dataset loaders

All notebooks import it with:
```python
from netsci_utils import *
set_seeds()
```

## Instructor

Prof. Rossano Schifanella — [rossano.schifanella@unito.it](mailto:rossano.schifanella@unito.it)
