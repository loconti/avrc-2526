# Browser Choropleth Examples

This folder reproduces the interactive **London crime score by MSOA** choropleth from [01-choroplet.ipynb](/Users/rschifan/Library/CloudStorage/GoogleDrive-rossano.schifanella@unito.it/My%20Drive/teaching/2026/complex_network/dataviz/tutorials/03-geographical-plotting/01-choroplet.ipynb) with three browser mapping libraries:

- `index.html`
- `leaflet-london-crime-choropleth.html`
- `deck-gl-london-crime-choropleth.html`
- `maplibre-london-crime-choropleth.html`
- `prepare_london_crime_choropleth.py`

All three examples use exactly the same:

- source layer: `London_IMD_MSOA.shp`
- variable: `crime`
- CRS for web output: `EPSG:4326`
- classification: `Quantiles(k=5)`
- palette: 5-class `YlOrRd`
- legend wording
- tooltip fields: `msoa11nm`, `lad11nm`, `crime`
- detail fields: `msoa11nm`, `lad11nm`, `crime`, `imd`
- same responsive initial extent based on the shared London bounds

## Interaction Design

- **Leaflet** uses a standard click popup.
- **MapLibre** uses a standard click popup.
- **deck.gl** uses the native hover tooltip together with a click modal.

The detail container differs in `deck.gl`, but the information shown on click is the same across the three examples.

## Shared Data

The browser examples do not compute their own bins. They read two prepared files from `data/`:

- `london-imd-crime-quantiles.geojson`
- `london-imd-crime-quantiles-meta.json`

The GeoJSON contains the geometry and the attributes used in the map. The metadata file stores the class breaks, legend labels, palette, title text, and map extent. That keeps the three examples visually and analytically consistent.

The metadata file also stores the shared border styling and the initial map view settings used by the examples.

## Regenerate the Data

From this directory, run:

```bash
python3 prepare_london_crime_choropleth.py
```

## Serve the Examples Locally

Because the HTML files fetch local data, open them through a local web server instead of `file://`.

```bash
cd tutorials/03-geographical-plotting/browser-choropleth-examples
python3 -m http.server 8000
```

Then open the landing page:

- `http://localhost:8000/`

From there you can navigate to the three individual examples. You can also open them directly:

- `http://localhost:8000/leaflet-london-crime-choropleth.html`
- `http://localhost:8000/deck-gl-london-crime-choropleth.html`
- `http://localhost:8000/maplibre-london-crime-choropleth.html`

## Pedagogical Focus

- **Leaflet** shows the classic raster-basemap-plus-GeoJSON workflow.
- **deck.gl** shows the same map as a composition of rendering layers and view-state logic.
- **MapLibre** shows the open-source GL-style workflow without changing the choropleth logic.

## Practical Note

These examples use CDN-hosted JavaScript libraries and online raster tiles. The local data is served from this directory, but the libraries and basemap still require internet access.
