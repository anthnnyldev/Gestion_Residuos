const pointsHistoryData = {
    labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    datasets: [{
        label: 'Puntos Acumulados',
        data: [50, 75, 120, 150, 200, 250],
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
        fill: true
    }]
};

const pointsCategoryData = {
    labels: ['Reciclaje', 'Donaciones', 'Voluntariado'],
    datasets: [{
        label: 'Puntos por Categoría',
        data: [80, 120, 60],
        backgroundColor: ['#4CAF50', '#FF6384', '#36A2EB'],
    }]
};

const pointsComparisonData = {
    labels: ['Usuario A', 'Usuario B', 'Usuario C', 'Usuario D'],
    datasets: [{
        label: 'Comparación de Puntos',
        data: [150, 200, 180, 90],
        backgroundColor: 'rgba(255, 159, 64, 0.6)',
        borderColor: 'rgba(255, 159, 64, 1)',
        borderWidth: 1
    }]
};

// Nuevo gráfico de distribución de puntos por mes
const pointsMonthlyDistributionData = {
    labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    datasets: [{
        label: 'Distribución de Puntos por Mes',
        data: [100, 150, 90, 130, 170, 210],
        backgroundColor: 'rgba(153, 102, 255, 0.2)',
        borderColor: 'rgba(153, 102, 255, 1)',
        borderWidth: 1
    }]
};

window.onload = function() {
    // Inicialización de gráficos existentes
    const pointsHistoryCtx = document.getElementById('pointsHistoryChart').getContext('2d');
    new Chart(pointsHistoryCtx, {
        type: 'line',
        data: pointsHistoryData,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    const pointsCategoryCtx = document.getElementById('pointsCategoryChart').getContext('2d');
    new Chart(pointsCategoryCtx, {
        type: 'doughnut',
        data: pointsCategoryData,
        options: {
            responsive: true,
            maintainAspectRatio: false,
        }
    });

    const pointsComparisonCtx = document.getElementById('pointsComparisonChart').getContext('2d');
    new Chart(pointsComparisonCtx, {
        type: 'bar',
        data: pointsComparisonData,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Nuevo gráfico de distribución de puntos por mes
    const pointsMonthlyDistributionCtx = document.getElementById('pointsMonthlyDistributionChart').getContext('2d');
    new Chart(pointsMonthlyDistributionCtx, {
        type: 'bar',
        data: pointsMonthlyDistributionData,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
};
