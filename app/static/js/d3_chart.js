// Asegúrate de que D3.js esté cargado antes de ejecutar cualquier código

document.addEventListener('DOMContentLoaded', function () {
    // Datos de ejemplo (deberías integrarlos con tu backend)
    const data = [
        { region_id: 1, country_name: 'País A', gdp: 1000, composition_food_organic_waste_percent: 20, composition_glass_percent: 5, composition_metal_percent: 10, composition_other_percent: 30, composition_paper_cardboard_percent: 15, composition_plastic_percent: 10, composition_rubber_leather_percent: 10 },
        { region_id: 2, country_name: 'País B', gdp: 1200, composition_food_organic_waste_percent: 15, composition_glass_percent: 10, composition_metal_percent: 5, composition_other_percent: 35, composition_paper_cardboard_percent: 20, composition_plastic_percent: 10, composition_rubber_leather_percent: 5 },
        // Agrega más datos aquí
    ];

    // Gráfico de barras (Ejemplo: porcentaje de desperdicio de alimentos orgánicos)
    const barChart = d3.select("#barChart");
    const barWidth = 500;
    const barHeight = 300;

    const barSvg = barChart.append("svg")
        .attr("width", barWidth)
        .attr("height", barHeight);

    const barMargin = { top: 20, right: 30, bottom: 40, left: 40 };
    const barX = d3.scaleBand()
        .domain(data.map(d => d.country_name))
        .range([barMargin.left, barWidth - barMargin.right])
        .padding(0.1);

    const barY = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.composition_food_organic_waste_percent)])
        .nice()
        .range([barHeight - barMargin.bottom, barMargin.top]);

    barSvg.append("g")
        .selectAll(".bar")
        .data(data)
        .enter().append("rect")
        .attr("class", "bar")
        .attr("x", d => barX(d.country_name))
        .attr("y", d => barY(d.composition_food_organic_waste_percent))
        .attr("width", barX.bandwidth())
        .attr("height", d => barHeight - barMargin.bottom - barY(d.composition_food_organic_waste_percent))
        .attr("fill", "steelblue");

    barSvg.append("g")
        .selectAll(".text")
        .data(data)
        .enter().append("text")
        .attr("class", "label")
        .attr("x", d => barX(d.country_name) + barX.bandwidth() / 2)
        .attr("y", d => barY(d.composition_food_organic_waste_percent) - 5)
        .attr("text-anchor", "middle")
        .text(d => `${d.composition_food_organic_waste_percent}%`);

    barSvg.append("g")
        .attr("transform", `translate(0,${barHeight - barMargin.bottom})`)
        .call(d3.axisBottom(barX));

    barSvg.append("g")
        .attr("transform", `translate(${barMargin.left},0)`)
        .call(d3.axisLeft(barY));

    // Gráfico de líneas (Ejemplo: GDP por región)
    const lineChart = d3.select("#lineChart");
    const lineWidth = 500;
    const lineHeight = 300;

    const lineSvg = lineChart.append("svg")
        .attr("width", lineWidth)
        .attr("height", lineHeight);

    const lineX = d3.scaleLinear()
        .domain([0, data.length - 1])
        .range([barMargin.left, lineWidth - barMargin.right]);

    const lineY = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.gdp)])
        .nice()
        .range([lineHeight - barMargin.bottom, barMargin.top]);

    const line = d3.line()
        .x((d, i) => lineX(i))
        .y(d => lineY(d.gdp));

    lineSvg.append("path")
        .data([data])
        .attr("class", "line")
        .attr("d", line)
        .attr("fill", "none")
        .attr("stroke", "green")
        .attr("stroke-width", 2);

    lineSvg.append("g")
        .attr("transform", `translate(0,${lineHeight - barMargin.bottom})`)
        .call(d3.axisBottom(lineX).ticks(data.length));

    lineSvg.append("g")
        .attr("transform", `translate(${barMargin.left},0)`)
        .call(d3.axisLeft(lineY));

    // Gráfico de torta (Ejemplo: composición de desperdicios por material)
    const pieChart = d3.select("#pieChart");
    const pieWidth = 500;
    const pieHeight = 500;
    const pieRadius = Math.min(pieWidth, pieHeight) / 2;

    const pieSvg = pieChart.append("svg")
        .attr("width", pieWidth)
        .attr("height", pieHeight)
        .append("g")
        .attr("transform", `translate(${pieWidth / 2},${pieHeight / 2})`);

    const pieData = [
        { name: "Comida/Orgánico", value: data[0].composition_food_organic_waste_percent },
        { name: "Vidrio", value: data[0].composition_glass_percent },
        { name: "Metal", value: data[0].composition_metal_percent },
        { name: "Otros", value: data[0].composition_other_percent },
        { name: "Papel/Cartón", value: data[0].composition_paper_cardboard_percent },
        { name: "Plástico", value: data[0].composition_plastic_percent },
        { name: "Hule/Cuero", value: data[0].composition_rubber_leather_percent },
    ];

    const pie = d3.pie()
        .value(d => d.value);

    const arc = d3.arc()
        .outerRadius(pieRadius - 10)
        .innerRadius(0);

    const pieChartG = pieSvg.selectAll(".arc")
        .data(pie(pieData))
        .enter().append("g")
        .attr("class", "arc");

    pieChartG.append("path")
        .attr("d", arc)
        .attr("fill", (d, i) => d3.schemeCategory10[i]);

    pieChartG.append("text")
        .attr("transform", d => `translate(${arc.centroid(d)})`)
        .attr("dy", ".35em")
        .attr("text-anchor", "middle")
        .text(d => d.data.name);

});
