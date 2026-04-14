#!/usr/bin/env python3
"""Prepare shared browser-ready data for the choropleth HTML examples."""

from __future__ import annotations

import json
from pathlib import Path

import geopandas as gpd
import numpy as np
from mapclassify import Quantiles

ROOT = Path(__file__).resolve().parent
SOURCE_PATH = ROOT.parent / "data" / "shp" / "London_IMD_MSOA.shp"
OUTPUT_DIR = ROOT / "data"
OUTPUT_GEOJSON = OUTPUT_DIR / "london-imd-crime-quantiles.geojson"
OUTPUT_META = OUTPUT_DIR / "london-imd-crime-quantiles-meta.json"

# ColorBrewer YlOrRd with five ordered classes.
YLORRD_5 = [
    "#ffffb2",
    "#fecc5c",
    "#fd8d3c",
    "#f03b20",
    "#bd0026",
]


def format_interval(lower: float, upper: float) -> str:
    """Format a class interval exactly once for reuse in every browser example."""
    return f"{lower:.2f} to {upper:.2f}"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    gdf = (
        gpd.read_file(SOURCE_PATH)[["msoa11nm", "lad11nm", "crime", "imd", "geometry"]]
        .to_crs(4326)
        .copy()
    )

    crime_values = gdf["crime"].astype(float)
    imd_values = gdf["imd"].astype(float)
    gdf["feature_id"] = np.arange(len(gdf), dtype=int)

    classifier = Quantiles(crime_values, k=5)
    edges = np.r_[crime_values.min(), classifier.bins].astype(float)
    labels = [format_interval(lower, upper) for lower, upper in zip(edges[:-1], edges[1:])]

    gdf["crime"] = crime_values.round(3)
    gdf["imd"] = imd_values.round(3)
    gdf["crime_class"] = classifier.yb.astype(int)
    gdf["crime_class_label"] = gdf["crime_class"].map(dict(enumerate(labels)))

    geojson_payload = json.loads(gdf.to_json(drop_id=True))
    OUTPUT_GEOJSON.write_text(
        json.dumps(geojson_payload, separators=(",", ":")),
        encoding="utf-8",
    )

    bounds = gdf.total_bounds.astype(float).tolist()
    center = [
        round((bounds[0] + bounds[2]) / 2, 6),
        round((bounds[1] + bounds[3]) / 2, 6),
    ]

    meta = {
        "source_layer": "London_IMD_MSOA.shp",
        "output_crs": "EPSG:4326",
        "column": "crime",
        "scheme": "quantiles",
        "k": 5,
        "bins": [round(value, 6) for value in edges.tolist()],
        "labels": labels,
        "colors": YLORRD_5,
        "bounds": [round(value, 6) for value in bounds],
        "center": center,
        "zoom": 9.0,
        "fill_opacity": 0.75,
        "line_color": "#333333",
        "line_width": 0.6,
        "hover_line_color": "#111111",
        "hover_line_width": 1.4,
        "title": "London crime score by MSOA",
        "subtitle": "Quantile bins; hover for area names and click for details.",
        "legend_title": "Crime score (quantile bins)",
        "tooltip": {
            "fields": ["msoa11nm", "lad11nm", "crime"],
            "aliases": ["MSOA", "Borough", "Crime score"],
        },
        "popup": {
            "fields": ["msoa11nm", "lad11nm", "crime", "imd"],
            "aliases": ["MSOA", "Borough", "Crime score", "Overall IMD"],
        },
    }

    OUTPUT_META.write_text(json.dumps(meta, indent=2), encoding="utf-8")

    print(f"Wrote {OUTPUT_GEOJSON}")
    print(f"Wrote {OUTPUT_META}")
    print("Quantile breaks:", ", ".join(f"{value:.3f}" for value in edges))


if __name__ == "__main__":
    main()
