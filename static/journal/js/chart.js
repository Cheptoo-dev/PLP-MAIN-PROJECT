// charts.js

// Chart.js setup script
document.addEventListener("DOMContentLoaded", function() {
    const ctx = document.getElementById('profitLossChart').getContext('2d');

    // Sample data (replace with actual data from Django views)
    const labels = JSON.parse(document.getElementById('dates-data').textContent);
    const data = JSON.parse(document.getElementById('profit-loss-data').textContent);

    const profitLossChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Profit/Loss',
                data: data,
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderWidth: 2,
                fill: true,
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Date'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Profit/Loss'
                    },
                    beginAtZero: true
                }
            }
        }
    });
});
