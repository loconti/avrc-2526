# Analisi e Visualizzazione delle Reti Complesse 2025/26

Course materials for **Network Science** at the University of Turin (UNITO).

---

## Module 1 — Network Science

📄 **[Syllabus](netsci/ns_syllabus.pdf)**

| Folder | Description |
|---|---|
| `netsci/slides/` | Lecture slides (PDF) |
| `netsci/tutorials/src/` | Jupyter tutorial notebooks |
| `netsci/tutorials/datasets/` | Network datasets |

### Lectures

| # | Topic | Slides | Notebook |
|---|---|---|---|
| 1 | Introduction | [ns01-intro.pdf](netsci/slides/ns01-intro.pdf) | |
| 2–3 | Recap on Graphs | [ns02-03-graphs.pdf](netsci/slides/ns02-03-graphs.pdf) | [02-03-intro-graphs.ipynb](netsci/tutorials/src/02-03-intro-graphs.ipynb) |
| 4 | Strong and Weak Ties | [ns04-strong-weak-ties.pdf](netsci/slides/ns04-strong-weak-ties.pdf) | [04-strong-weak-ties.ipynb](netsci/tutorials/src/04-strong-weak-ties.ipynb) |
| 5 | Homophily | [ns05-homophily.pdf](netsci/slides/ns05-homophily.pdf) | [05-homophily.ipynb](netsci/tutorials/src/05-homophily.ipynb) |
| 6 | Centrality Measures | [ns06-centrality-measures.pdf](netsci/slides/ns06-centrality-measures.pdf) | [06a-eigenvector-centrality.ipynb](netsci/tutorials/src/06a-eigenvector-centrality.ipynb), [06b-katz-centrality.ipynb](netsci/tutorials/src/06b-katz-centrality.ipynb), [06c-centralities.ipynb](netsci/tutorials/src/06c-centralities.ipynb) |
| 7 | Degree Distributions, Scale-Free Networks, and Robustness | [ns07-degree-distributions-scale-free-robustness.pdf](netsci/slides/ns07-degree-distributions-scale-free-robustness.pdf) | [07a-degree-distributions.ipynb](netsci/tutorials/src/07a-degree-distributions.ipynb), [07b-friendship-paradox.ipynb](netsci/tutorials/src/07b-friendship-paradox.ipynb), [07c-robustness.ipynb](netsci/tutorials/src/07c-robustness.ipynb) |
| 8 | Network Models | [ns08-network-models.pdf](netsci/slides/ns08-network-models.pdf) | [08a-configuration-model.ipynb](netsci/tutorials/src/08a-configuration-model.ipynb), [08b-er-random-graphs.ipynb](netsci/tutorials/src/08b-er-random-graphs.ipynb), [08c-watts-strogatz.ipynb](netsci/tutorials/src/08c-watts-strogatz.ipynb) |
| 9 | Preferential Attachment | [ns09-preferential-attachment.pdf](netsci/slides/ns09-preferential-attachment.pdf) | [09a-barabasi-albert.ipynb](netsci/tutorials/src/09a-barabasi-albert.ipynb) |
| 10 | Extensions of Preferential Attachment | [ns10-preferential-attachment-extensions.pdf](netsci/slides/ns10-preferential-attachment-extensions.pdf) | [10a-attractiveness-model.ipynb](netsci/tutorials/src/10a-attractiveness-model.ipynb), [10b-fitness-model.ipynb](netsci/tutorials/src/10b-fitness-model.ipynb), [10c-random-walk-model.ipynb](netsci/tutorials/src/10c-random-walk-model.ipynb), [10d-copy-model.ipynb](netsci/tutorials/src/10d-copy-model.ipynb) |
| 11 | Rich-Get-Richer and Power Laws | [ns11-rgr.pdf](netsci/slides/ns11-rgr.pdf) | [11a-powerlaw.ipynb](netsci/tutorials/src/11a-powerlaw.ipynb), [11b-rich-get-richer.ipynb](netsci/tutorials/src/11b-rich-get-richer.ipynb) |
| 12 | Communities | [ns12-communities.pdf](netsci/slides/ns12-communities.pdf) | [12-communities-fundamentals.ipynb](netsci/tutorials/src/12-communities-fundamentals.ipynb) |
| 13 | Community Detection | [ns13-community-detection.pdf](netsci/slides/ns13-community-detection.pdf) | [13-community-detection-modularity.ipynb](netsci/tutorials/src/13-community-detection-modularity.ipynb) |
| 14 | Community Benchmarks | [ns14-communities-benchmarks.pdf](netsci/slides/ns14-communities-benchmarks.pdf) | [14-label-propagation-and-evaluation.ipynb](netsci/tutorials/src/14-label-propagation-and-evaluation.ipynb) |

---

## Module 2 — Data Visualization

📄 **[Syllabus](dataviz/dv_syllabus.pdf)**

| Folder | Description |
|---|---|
| `dataviz/slides/` | Lecture slides (PDF) |
| `dataviz/tutorials/` | Tutorials and exercises |

### Lectures

| # | Topic | Slides | Tutorial |
|---|---|---|---|
| 1 | Introduction to Visual Perception | [dv01-intro-visual-perception.pdf](dataviz/slides/dv01-intro-visual-perception.pdf) | |
| 2 | Nested Model, Data & Task Abstractions | [dv02-model-data-task-abstractions.pdf](dataviz/slides/dv02-model-data-task-abstractions.pdf) | |
| 3 | Marks, Channels, and Color | [dv03-marks-channels-color.pdf](dataviz/slides/dv03-marks-channels-color.pdf) | |
| 4 | Tables | [dv04-tables.pdf](dataviz/slides/dv04-tables.pdf) | |
| 5 | Static Plotting in Python | [dv05-rules-of-thumbs.pdf](dataviz/slides/dv05-rules-of-thumbs.pdf) | [01-matplotlib/](dataviz/tutorials/01-matplotlib/), [02-seaborn/](dataviz/tutorials/02-seaborn/) |
| 6 | Geographical Plotting in Python | [dv06-geographical-plotting.pdf](dataviz/slides/dv06-geographical-plotting.pdf) | [03-geographical-plotting/](dataviz/tutorials/03-geographical-plotting/) |
| 7 | Static Networks in Python | | [01-networkx-drawing-basics.ipynb](dataviz/tutorials/04-networks/01-networkx-drawing-basics.ipynb), [02-network-layouts.ipynb](dataviz/tutorials/04-networks/02-network-layouts.ipynb), [03-network-labels.ipynb](dataviz/tutorials/04-networks/03-network-labels.ipynb), [04-game-of-thrones-network-case-study.ipynb](dataviz/tutorials/04-networks/04-game-of-thrones-network-case-study.ipynb), [05-networks-and-space.ipynb](dataviz/tutorials/04-networks/05-networks-and-space.ipynb), [06-networks-plotly.ipynb](dataviz/tutorials/04-networks/06-networks-plotly.ipynb) |
| 8 | Interactive Views | | |
| 9 | Introduction to D3.js | | |
| 10 | SVG, General Update Pattern, Transitions | | |
| 11 | Interactions and Event Listeners | | |
| 12 | Graphs Visualization | | |

---

## Instructor

Prof. Rossano Schifanella — [rossano.schifanella@unito.it](mailto:rossano.schifanella@unito.it)
