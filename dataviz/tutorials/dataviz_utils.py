"""
dataviz_utils.py -- Shared utilities for Data Visualization course tutorials.

Usage:
    from dataviz_utils import *
    set_seeds()

Students can read this file to understand the helper functions and defaults
used across the visualization tutorials.

The module deliberately exposes a small public surface because course notebooks
import it with ``from dataviz_utils import *`` by convention.

The plotting defaults are inspired by Nicolas P. Rougier's
``Scientific Visualization: Python + Matplotlib`` code examples:
Matplotlib-first rcParams, restrained framing, outward ticks, and direct
labeling/annotation helpers that favor clarity over theme-heavy styling.
"""

from __future__ import annotations

import random
import warnings
from pathlib import Path

# scipy 1.16 changed gaussian_kde.neff to a computed property that calls
# np.vecdot internally; seaborn 0.13.x triggers numerical edge cases in that
# path (divide-by-zero / overflow / invalid-value) that are harmless but
# produce confusing noise in teaching notebooks.
warnings.filterwarnings(
    "ignore",
    message=r"(divide by zero|overflow|invalid value) encountered in vecdot",
    category=RuntimeWarning,
    module=r"scipy\._lib\._util",
)

import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
import numpy as np
import pandas as pd
import seaborn as sns

RANDOM_SEED = 42
FIGURE_SIZE = (7.0, 4.5)
FIGURE_SIZE_WIDE = (9.0, 4.5)
FIGURE_SIZE_SQUARE = (5.5, 5.5)
FIGURE_SIZE_MATRIX = (7.0, 5.5)
FIGURE_DPI = 150
SAVEFIG_DPI = 360
FONT_SIZE = 11
SANS_SERIF_STACK = [
    "Fira Sans Condensed",
    "Source Sans 3",
    "Source Sans Pro",
    "Fira Sans",
    "Inter",
    "Arial",
    "DejaVu Sans",
]
SERIF_STACK = [
    "Source Serif 4",
    "Source Serif Pro",
    "Georgia",
    "DejaVu Serif",
]
MONOSPACE_STACK = [
    "Source Code Pro",
    "IBM Plex Mono",
    "Menlo",
    "DejaVu Sans Mono",
]

DV_PALETTE = {
    "blue": "#4C78A8",
    "orange": "#F58518",
    "green": "#54A24B",
    "red": "#E45756",
    "purple": "#B279A2",
    "teal": "#72B7B2",
    "gold": "#ECA82C",
    "gray": "#666666",
}

CONTINENT_PALETTE = {
    "Africa": "#009E73",
    "Americas": "#D55E00",
    "Asia": "#0072B2",
    "Europe": "#CC79A7",
    "Oceania": "#E69F00",
}

CATEGORICAL_PALETTE = [
    "#0072B2",
    "#E69F00",
    "#009E73",
    "#D55E00",
    "#CC79A7",
    "#56B4E9",
    "#F0E442",
    "#000000",  # canonical 8th Okabe-Ito colour (black); added so that 8-way
                # categorical partitions don't wrap and produce duplicates.
]

CMAP_SEQUENTIAL = "viridis"
CMAP_DIVERGING = "coolwarm"
TEXT_OUTLINE = [pe.Stroke(linewidth=2.5, foreground="white"), pe.Normal()]


def _make_font_scale(base: float = 12.0) -> dict[str, float]:
    """Return a small semantic typography scale for teaching notebooks."""
    return {
        "base": base,
        "direct_label": base * 0.90,
        "annotation": base * 0.84,
        "dense_label": base * 0.78,
        "panel_title": base * 1.12,
        "figure_title": base * 1.40,
    }


def make_figure_size_scale(
    *,
    focus: tuple[float, float] | None = None,
    standard: tuple[float, float] | None = None,
    wide: tuple[float, float] | None = None,
    matrix: tuple[float, float] | None = None,
) -> dict[str, tuple[float, float]]:
    """Return figure-size categories derived from the shared course constants."""
    return {
        "focus": FIGURE_SIZE_SQUARE if focus is None else focus,
        "standard": FIGURE_SIZE if standard is None else standard,
        "wide": FIGURE_SIZE_WIDE if wide is None else wide,
        "matrix": FIGURE_SIZE_MATRIX if matrix is None else matrix,
    }


def lighten_color(color: str, amount: float = 0.65) -> tuple[float, float, float]:
    """Blend a color toward white by the requested amount."""
    base = np.array(to_rgb(color))
    return tuple(np.clip(1 - amount * (1 - base), 0, 1))


def _enable_retina_output() -> None:
    try:
        from matplotlib_inline.backend_inline import set_matplotlib_formats

        set_matplotlib_formats("retina")
    except Exception:
        pass


def _course_rc(
    *,
    figure_size: tuple[float, float],
    figure_dpi: int,
    savefig_dpi: int,
    font_size: float,
    grid: bool,
) -> dict[str, object]:
    return {
        "figure.figsize": figure_size,
        "figure.dpi": figure_dpi,
        "savefig.dpi": savefig_dpi,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.08,
        "savefig.facecolor": "white",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "font.size": font_size,
        "font.family": "sans-serif",
        "font.sans-serif": SANS_SERIF_STACK,
        "font.serif": SERIF_STACK,
        "font.monospace": MONOSPACE_STACK,
        "axes.axisbelow": True,
        "axes.linewidth": 1.0,
        "axes.edgecolor": "#111111",
        "axes.titlelocation": "left",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.spines.bottom": True,
        "axes.spines.left": True,
        "axes.grid": grid,
        "grid.color": "#000000",
        "grid.alpha": 0.10,
        "grid.linewidth": 0.10,
        "xtick.bottom": True,
        "xtick.top": False,
        "ytick.left": True,
        "ytick.right": False,
        "xtick.direction": "out",
        "ytick.direction": "out",
        "xtick.major.size": 5,
        "ytick.major.size": 5,
        "xtick.major.width": 1.0,
        "ytick.major.width": 1.0,
        "xtick.minor.size": 3,
        "ytick.minor.size": 3,
        "xtick.minor.width": 0.5,
        "ytick.minor.width": 0.5,
        "xtick.minor.visible": True,
        "ytick.minor.visible": True,
        "xtick.major.pad": 4,
        "ytick.major.pad": 4,
        "lines.linewidth": 2.0,
        "lines.markersize": 5,
        "legend.frameon": False,
        "legend.facecolor": "none",
        "legend.edgecolor": "none",
        "legend.framealpha": 0.0,
        "legend.borderaxespad": 0.4,
        "legend.handlelength": 1.4,
        "legend.handletextpad": 0.5,
    }


def set_seeds(seed: int = RANDOM_SEED) -> None:
    random.seed(seed)
    np.random.seed(seed)


def _constrained_layout_rc() -> dict[str, object]:
    """
    Return the appropriate rcParams for constrained layout across Matplotlib versions.

    Newer Matplotlib releases expose ``figure.layout = "constrained"`` while
    older releases still use ``figure.constrained_layout.use = True``.
    """
    if "figure.layout" in plt.rcParams:
        return {"figure.layout": "constrained"}
    if "figure.constrained_layout.use" in plt.rcParams:
        return {"figure.constrained_layout.use": True}
    return {}


def setup_matplotlib() -> None:
    plt.rcParams.update(
        _course_rc(
            figure_size=FIGURE_SIZE,
            figure_dpi=FIGURE_DPI,
            savefig_dpi=SAVEFIG_DPI,
            font_size=FONT_SIZE,
            grid=True,
        )
    )
    plt.rcParams.update(
        {
            "axes.titlesize": "large",
            "axes.titleweight": "regular",
            "axes.labelsize": "medium",
            "axes.labelpad": 6,
            "xtick.labelsize": "small",
            "ytick.labelsize": "small",
            "legend.fontsize": "small",
            "legend.title_fontsize": "small",
            "figure.titleweight": "regular",
            "axes.xmargin": 0.02,
            "axes.ymargin": 0.08,
        }
    )
    plt.rcParams.update(_constrained_layout_rc())
    _enable_retina_output()


def apply_teaching_rc(
    *,
    font_base: float = 12.0,
    figure_dpi: int = 170,
    savefig_dpi: int = 360,
    grid: bool = False,
    line_width: float = 2.2,
    marker_size: float = 5,
    xmargin: float = 0.02,
    ymargin: float = 0.05,
) -> dict[str, float]:
    """
    Apply a lecture-friendly Matplotlib style and return semantic text sizes.

    The returned dictionary is meant to be unpacked by notebooks that need a
    small number of reusable label sizes without scattering raw ``fontsize``
    numbers across many cells.
    """
    scale = _make_font_scale(font_base)
    plt.rcParams.update(
        _course_rc(
            figure_size=FIGURE_SIZE,
            figure_dpi=figure_dpi,
            savefig_dpi=savefig_dpi,
            font_size=scale["base"],
            grid=grid,
        )
    )
    plt.rcParams.update(
        {
            "axes.titlesize": "x-large",
            "axes.titleweight": "regular",
            "axes.titlepad": 12,
            "axes.labelsize": "large",
            "axes.labelpad": 8,
            "xtick.labelsize": "medium",
            "ytick.labelsize": "medium",
            "legend.fontsize": "medium",
            "legend.title_fontsize": "medium",
            "figure.titlesize": "xx-large",
            "figure.titleweight": "regular",
            "lines.linewidth": line_width,
            "lines.markersize": marker_size,
            "axes.xmargin": xmargin,
            "axes.ymargin": ymargin,
        }
    )
    _enable_retina_output()
    return scale


def style_axis(
    ax,
    *,
    title: str | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
    xscale: str | None = None,
    yscale: str | None = None,
    legend: bool = False,
    grid: bool = True,
):
    if title is not None:
        ax.set_title(title)
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    if xscale is not None:
        ax.set_xscale(xscale)
    if yscale is not None:
        ax.set_yscale(yscale)
    if grid:
        ax.grid(True)
    else:
        ax.grid(False)
    if legend:
        ax.legend(frameon=False)
    return ax


def annotate_series_end(
    ax,
    x,
    y,
    label: str,
    color: str,
    *,
    dx: float = 8,
    dy: float = 0,
    fontsize: float = 9.5,
):
    ax.annotate(
        label,
        xy=(x, y),
        xytext=(dx, dy),
        textcoords="offset points",
        ha="left",
        va="center",
        fontsize=fontsize,
        color=color,
        path_effects=TEXT_OUTLINE,
    )


def add_cell_grid(ax, nrows: int, ncols: int, *, color: str = "white", linewidth: float = 1.2):
    ax.set_xticks(np.arange(-0.5, ncols, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, nrows, 1), minor=True)
    ax.grid(which="minor", color=color, linewidth=linewidth)
    ax.tick_params(which="minor", bottom=False, left=False)


def find_repo_root() -> Path:
    cwd = Path.cwd().resolve()
    for candidate in [cwd, *cwd.parents]:
        if (candidate / "tutorials" / "datasets").exists():
            return candidate
    raise FileNotFoundError("Could not locate the repo root from the current working directory.")


REPO_ROOT = find_repo_root()
DATA_DIR = REPO_ROOT / "tutorials" / "datasets"


def load_gapminder() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "gapminder.csv")


def load_penguins(dropna: bool = True) -> pd.DataFrame:
    df = pd.read_csv(DATA_DIR / "penguins.csv")
    return df.dropna().copy() if dropna else df


def load_bivariate_normal_demo(size: int = 240) -> np.ndarray:
    x = np.linspace(-3.0, 3.0, size)
    y = np.linspace(-2.5, 2.5, size)
    X, Y = np.meshgrid(x, y)
    Z1 = np.exp(-((X - 0.8) ** 2 + (Y - 0.4) ** 2) / 0.8)
    Z2 = 0.7 * np.exp(-((X + 1.1) ** 2 + (Y + 0.7) ** 2) / 1.2)
    Z3 = 0.35 * np.exp(-((X + 0.2) ** 2 + (Y - 1.2) ** 2) / 0.3)
    return Z1 + Z2 + Z3


# ---- Node-overlap helpers (teaching version introduced in notebook 02) ----
# These are used across the network-visualization notebooks to (a) measure how
# many rendered node markers overlap on a given panel size and (b) remove that
# overlap with a size-aware weighted relaxation pass. The inline versions in
# notebook 02 remain the step-by-step walkthrough; these copies exist so
# downstream notebooks can simply import and apply the tool.
import math

STANDARD_PANEL_SIZE = (4.8, 4.4)
DISPLAY_GAP_PT = 0.0
OVERLAP_TOL_PT = 1e-9


def compute_node_radii(node_sizes, linewidth=0.7):
    """Convert matplotlib ``node_size`` (area in points²) into a rendered radius in points."""
    return {
        node: math.sqrt(size / math.pi) + 0.5 * linewidth
        for node, size in node_sizes.items()
    }


def points_per_data_unit(xlim, ylim, panel_size):
    """Points (1/72 in) per one unit of data coordinates, assuming ``ax.set_aspect('equal')``."""
    x_span = max(xlim[1] - xlim[0], 1e-9)
    y_span = max(ylim[1] - ylim[0], 1e-9)
    scale_in = min(panel_size[0] / x_span, panel_size[1] / y_span)
    return 72.0 * scale_in


def overlap_diagnostics(
    pos,
    radii,
    *,
    panel_size=STANDARD_PANEL_SIZE,
    xlim=(0.0, 1.0),
    ylim=(0.0, 1.0),
    min_gap_pt=DISPLAY_GAP_PT,
    tol_pt=OVERLAP_TOL_PT,
):
    """Return comparable overlap diagnostics on a fixed canonical plot box."""
    nodes = list(pos)
    if len(nodes) < 2:
        return {
            "overlap_pairs": 0,
            "overlap_node_fraction": 0.0,
            "overlap_nodes": [],
            "overlap_mask": np.zeros(0, dtype=bool),
        }

    pts_per_unit = points_per_data_unit(xlim, ylim, panel_size)
    coords = np.asarray([pos[node] for node in nodes], dtype=float)
    radius_values = np.asarray([radii[node] for node in nodes], dtype=float)

    diffs = coords[:, None, :] - coords[None, :, :]
    distances_pt = np.linalg.norm(diffs, axis=-1) * pts_per_unit
    required_pt = radius_values[:, None] + radius_values[None, :] + min_gap_pt

    collide = distances_pt + tol_pt < required_pt
    np.fill_diagonal(collide, False)

    overlap_mask = collide.any(axis=1)
    overlap_pairs = int(collide.sum() // 2)
    overlap_node_fraction = float(overlap_mask.mean())
    overlap_nodes = [node for node, flag in zip(nodes, overlap_mask) if flag]
    return {
        "overlap_pairs": overlap_pairs,
        "overlap_node_fraction": overlap_node_fraction,
        "overlap_nodes": overlap_nodes,
        "overlap_mask": overlap_mask,
    }


def overlap_metrics(pos, radii, **kwargs):
    diagnostics = overlap_diagnostics(pos, radii, **kwargs)
    return {
        "overlap_pairs": diagnostics["overlap_pairs"],
        "overlap_node_fraction": diagnostics["overlap_node_fraction"],
    }


def resolve_node_collisions(
    initial_pos,
    radii,
    *,
    panel_size=STANDARD_PANEL_SIZE,
    xlim=(0.0, 1.0),
    ylim=(0.0, 1.0),
    max_iter=1200,
    min_gap_pt=DISPLAY_GAP_PT,
    tol_pt=OVERLAP_TOL_PT,
    pull_strength=0.0,
    mass_power=2.0,
    step_cap=0.35,
):
    """Reduce overlap with a size-aware weighted relaxation pass.

    Larger nodes move less and smaller nodes move more when they collide,
    so the correction preserves the broad structure of the input layout
    while removing node-marker overlap in rendered space.

    After convergence the whole layout is translated (no scaling) so it
    sits centered inside the target frame; a pure translation cannot
    reintroduce overlap.
    """
    nodes = list(initial_pos)
    anchors = np.asarray([initial_pos[node] for node in nodes], dtype=float)
    coords = anchors.copy()
    radius_values = np.asarray([radii[node] for node in nodes], dtype=float)
    masses = np.maximum(radius_values, 1e-6) ** mass_power
    pts_per_unit = points_per_data_unit(xlim, ylim, panel_size)
    required_distances = (radius_values[:, None] + radius_values[None, :] + min_gap_pt) / pts_per_unit
    required_clip = (radius_values + min_gap_pt) / pts_per_unit
    tol_data = tol_pt / pts_per_unit
    n = len(nodes)

    for _ in range(max_iter):
        displacement = np.zeros_like(coords)
        moved = False

        for i in range(n):
            for j in range(i + 1, n):
                delta = coords[j] - coords[i]
                distance = np.linalg.norm(delta)
                required = required_distances[i, j]

                if distance + tol_data >= required:
                    continue

                moved = True
                if distance < 1e-12:
                    anchor_delta = anchors[j] - anchors[i]
                    if np.linalg.norm(anchor_delta) < 1e-12:
                        angle = 2 * np.pi * ((j - i) / max(n, 2))
                        direction = np.array([np.cos(angle), np.sin(angle)])
                    else:
                        direction = anchor_delta / np.linalg.norm(anchor_delta)
                else:
                    direction = delta / distance

                overlap = required - distance
                total_mass = masses[i] + masses[j]
                move_i = overlap * (masses[j] / total_mass)
                move_j = overlap * (masses[i] / total_mass)

                displacement[i] -= move_i * direction
                displacement[j] += move_j * direction

        if not moved:
            break

        norms = np.linalg.norm(displacement, axis=1)
        max_norm = max(norms.max(), 1e-9)
        if max_norm > step_cap:
            displacement *= step_cap / max_norm

        coords += displacement

        if pull_strength > 0:
            coords = (1 - pull_strength) * coords + pull_strength * anchors

    margin = float(required_clip.max())
    mins = coords.min(axis=0) - margin
    maxs = coords.max(axis=0) + margin
    frame_center = np.array([0.5 * (xlim[0] + xlim[1]), 0.5 * (ylim[0] + ylim[1])])
    layout_center = 0.5 * (mins + maxs)
    coords = coords + (frame_center - layout_center)

    return {node: coords[idx] for idx, node in enumerate(nodes)}


__all__ = [
    "np",
    "pd",
    "plt",
    "sns",
    "RANDOM_SEED",
    "FIGURE_SIZE",
    "FIGURE_SIZE_WIDE",
    "FIGURE_SIZE_SQUARE",
    "FIGURE_SIZE_MATRIX",
    "FIGURE_DPI",
    "SAVEFIG_DPI",
    "DV_PALETTE",
    "CONTINENT_PALETTE",
    "CATEGORICAL_PALETTE",
    "CMAP_SEQUENTIAL",
    "CMAP_DIVERGING",
    "TEXT_OUTLINE",
    "set_seeds",
    "setup_matplotlib",
    "make_figure_size_scale",
    "apply_teaching_rc",
    "lighten_color",
    "style_axis",
    "annotate_series_end",
    "add_cell_grid",
    "load_gapminder",
    "load_penguins",
    "load_bivariate_normal_demo",
    "STANDARD_PANEL_SIZE",
    "compute_node_radii",
    "overlap_metrics",
    "overlap_diagnostics",
    "resolve_node_collisions",
]
