document.addEventListener('DOMContentLoaded', function() {
    const data = {{ country_data|safe }};
    
    // Gráfico de Pastel 3D: Composición de Residuos
    Plotly.newPlot('compositionPieChart', [{
        values: [data.food_waste, data.plastic_waste, data.paper_waste, data.metal_waste],
        labels: ['Orgánicos', 'Plástico', 'Papel', 'Metales'],
        type: 'pie',
        hole: 0.4,
        textinfo: 'label+percent',
        hoverinfo: 'label+percent+value',
        marker: { colors: ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'] },
        pull: [0.1, 0, 0, 0] // Emphasize the first segment
    }], {
        title: 'Composición de Residuos',
        height: 400,
        width: 500,
        showlegend: true,
        scene: { // Adds 3D rotation interaction
            dragmode: 'orbit',
            camera: { eye: {x: 1.5, y: 1.5, z: 0.8} }
        }
    });

    // Gráfico de Barras 3D: Tratamiento de Residuos
    Plotly.newPlot('treatmentBarChart', [{
        x: ['Reciclaje', 'Incineración', 'Relleno Sanitario'],
        y: [data.waste_treatment_recycling, data.waste_treatment_incineration, data.waste_treatment_landfill],
        type: 'bar',
        marker: { color: '#17becf' },
        text: [data.waste_treatment_recycling + '%', data.waste_treatment_incineration + '%', data.waste_treatment_landfill + '%'],
        textposition: 'auto',
        hoverinfo: 'text+name'
    }], {
        title: 'Tratamiento de Residuos',
        height: 400,
        width: 500,
        scene: { // Adds 3D rotation interaction
            dragmode: 'orbit',
            camera: { eye: {x: 1.5, y: 1.5, z: 0.8} }
        }
    });

    // Gráfico de Barras 3D: Cobertura de Recolección
    Plotly.newPlot('collectionCoverageBarChart', [{
        x: ['Rural', 'Urbano'],
        y: [data.waste_collection_rural, data.waste_collection_urban],
        type: 'bar',
        marker: { color: '#bcbd22' },
        text: [data.waste_collection_rural + '%', data.waste_collection_urban + '%'],
        textposition: 'auto',
        hoverinfo: 'text+name'
    }], {
        title: 'Cobertura de Recolección',
        height: 400,
        width: 500,
        scene: { // Adds 3D rotation interaction
            dragmode: 'orbit',
            camera: { eye: {x: 1.5, y: 1.5, z: 0.8} }
        }
    });

    // Gráfico de Barras 3D: Generación de Residuos Especiales
    Plotly.newPlot('specialWasteBarChart', [{
        x: ['Residuos Electrónicos', 'Residuos Industriales', 'Residuos Médicos'],
        y: [data.special_waste_electronic, data.special_waste_industrial, data.special_waste_medical],
        type: 'bar',
        marker: { color: '#7f7f7f' },
        text: [data.special_waste_electronic + ' toneladas', data.special_waste_industrial + ' toneladas', data.special_waste_medical + ' toneladas'],
        textposition: 'auto',
        hoverinfo: 'text+name'
    }], {
        title: 'Generación de Residuos Especiales',
        height: 400,
        width: 500,
        scene: { // Adds 3D rotation interaction
            dragmode: 'orbit',
            camera: { eye: {x: 1.5, y: 1.5, z: 0.8} }
        }
    });
});