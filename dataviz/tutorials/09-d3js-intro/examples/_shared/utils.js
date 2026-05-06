// =============================================================================
// utils.js — shared helpers for the L9 examples.
//
// One global function: makeCanvas(selector, height, opts).
// Append it via <script src="../_shared/utils.js"></script> in each example;
// it adds `makeCanvas` to the global scope so the demo code can call it.
//
// Note: 09a primitive examples (rect, circle, line, …) and 09d data-helper
// examples (csv, group, format, …) intentionally do NOT use this helper.
// In 09a the SVG creation IS the lesson; in 09d there is no SVG to begin with.
// =============================================================================

// makeCanvas — append an <svg> with the standard margin convention.
//
// Returns { root, plot, innerW, innerH, margin, width }:
//   root   = the <svg> selection
//   plot   = the inner <g> shifted by the margins (every mark goes here)
//   innerW = width  − margin.left − margin.right
//   innerH = height − margin.top  − margin.bottom
//
// Pass { showPlotArea: true } to draw a faint rectangle behind the inner plot
// area — useful when teaching the margin convention.
function makeCanvas(selector, height, opts = {}) {
    const m = { top: 24, right: 30, bottom: 36, left: 50, ...(opts.margin || {}) };
    const width  = opts.width ?? 700;
    const innerW = width  - m.left - m.right;
    const innerH = height - m.top  - m.bottom;
    const root = d3.select(selector)
        .append("svg")
            .attr("width", width)
            .attr("height", height)
            .attr("viewBox", `0 0 ${width} ${height}`)
            .attr("preserveAspectRatio", "xMidYMid meet");
    const plot = root.append("g")
        .attr("transform", `translate(${m.left}, ${m.top})`);
    if (opts.showPlotArea) {
        plot.append("rect")
            .attr("width", innerW)
            .attr("height", innerH)
            .attr("fill", "#f8f9fa")
            .attr("stroke", "#dee2e6");
    }
    return { root, plot, innerW, innerH, margin: m, width };
}
