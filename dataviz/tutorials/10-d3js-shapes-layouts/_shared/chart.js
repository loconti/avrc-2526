const CANVAS = {
    width:  700,
    margin: { top: 24, right: 30, bottom: 36, left: 50 }
};

function makeCanvas(selector, height, opts = {}) {
    const m = { ...CANVAS.margin, ...(opts.margin || {}) };
    const w = opts.width ?? CANVAS.width;
    const innerW = w - m.left - m.right;
    const innerH = height - m.top - m.bottom;
    const root = d3.select(selector).append("svg")
        .attr("width", w).attr("height", height)
        .style("background", "#fafafa").style("border", "1px solid #ddd");
    const plot = root.append("g")
        .attr("transform", `translate(${m.left}, ${m.top})`);
    if (opts.showPlotArea) {
        plot.append("rect")
            .attr("width", innerW).attr("height", innerH)
            .attr("fill", "#f8f9fa").attr("stroke", "#dee2e6");
    }
    return { root, plot, innerW, innerH, margin: m, width: w, height };
}
