# Final-Project Proposals — How to Choose

*Analisi e Visualizzazione delle Reti Complesse — Network Science module.*

This folder contains five detailed, self-contained project proposals. Each proposal is a complete guide: dataset, research questions, methodology, visualization plan, expected findings, and deliverables. A group can pick a proposal, open the file, and start working the same afternoon.

The proposals cover different scales (from 77 to 334 863 nodes), different domains (literature, science, politics, social media, e-commerce), and different methodological styles (narrative-driven, benchmark-driven, polarisation, homophily, scalability). The goal is that every group finds a project matching its taste and skills.

All five proposals exercise the syllabus thoroughly. They share the same analytical backbone — descriptive measures, centralities, degree distributions, null models, community detection, and (optionally) dynamics — but each one tells a different story. **Choose by story first, by scale second.**

## At a glance

| # | Dataset | Nodes | Edges | Flavour | Story in one line |
|---|---|---:|---:|---|---|
| [01](project-proposal-01-les-miserables.pdf) | Les Misérables co-occurrence | 77 | 254 | narrative, literary | Quantitative portrait of a 19th-century novel. |
| [02](project-proposal-02-arxiv-grqc.pdf) | arXiv gr-qc collaborations | 5 242 | 14 496 | scale-free, small-world | Is the social structure of a scientific subfield well-described by the textbook models? |
| [03](project-proposal-03-political-blogs.pdf) | Political Blogs 2004 | 1 490 | 19 090 | polarisation, directed | How divided is the U.S. political blogosphere, and who are the few bridges? |
| [04](project-proposal-04-facebook-ego-networks.pdf) | Facebook ego networks | 4 039 | 88 234 | homophily, social circles | How well does algorithmic clustering recover the social groups users themselves define? |
| [05](project-proposal-05-amazon-copurchase.pdf) | Amazon co-purchase | 334 863 | 925 872 | scale, benchmark, recommendation | The canonical scalable-community-detection benchmark — Louvain vs. Leiden vs. Infomap on a real large graph. |

## Decision guide

- **Pick 01 (Les Misérables) if** your group loves storytelling and wants a clean, readable report. The dataset is small enough that every finding can be checked against the novel, and every character has a name. Do not mistake "small" for "easy": writing a clear, well-interpreted report on Les Misérables is as demanding as wrestling with a large messy dataset.
- **Pick 02 (arXiv gr-qc) if** your group wants the "classic network-science experience" on a canonical dataset: heavy tails, small-world, percolation, modularity. This is the textbook project.
- **Pick 03 (Political Blogs) if** your group is drawn to social or political narratives and wants to make claims about homophily, polarisation, and influence. The 2004 U.S. election context is easy for any reader to understand.
- **Pick 04 (Facebook ego networks) if** your group wants to use the widest range of course concepts on a single dataset. It covers almost every lecture of the syllabus, and it includes the rare advantage of an *overlapping* ground-truth partition.
- **Pick 05 (Amazon co-purchase) if** your group has engineering experience and wants to feel the difference between textbook and scalable algorithms first-hand. This is the most ambitious option and the one that best demonstrates mastery of **Lectures 14 and 15**.

## What makes a great exam project

A convincing project at this exam is **not** "I ran every algorithm in the syllabus". It is a **focused narrative supported by a small number of rigorous quantitative claims**.

The proposals in this folder are deliberately more expansive than what any one group should attempt. **Pick two or three research questions, treat each of them properly, and stop.** A report that answers three questions thoroughly will score higher than one that answers ten superficially.

Every proposal includes:

- an explicit **Expected findings** section, so you know what "good" looks like before you start;
- a **Hero figure** — one carefully-designed visualisation that earns its place in the report;
- a **Deliverables checklist** mapped to the brief in `netsci/slides/src/ns-final-project.md`.

Read the proposal you are considering from start to finish before committing. If anything is unclear, come to office hours — it is always easier to clarify early than to redirect mid-project.
