console.log("started")

console.log(in_progress)
console.log(completed)
console.log(pending)
console.log(total)

const ctx = document.getElementById('pie_chart');
new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['completed', 'in progress', 'not started'],
        datasets: [{

            data: [ completed, in_progress, total - in_progress - completed],
            borderWidth: 1,
            backgroundColor:[
                "green",
                "rgb(0,0,255)",
                "rgb(255,0,0)"
            ]
        }]
    },
    options: {
        plugins: {
            legend: {
                display: true,
                position: 'right',
                // fontSize: 30;
                boxWidth: 1000,
                boxHeight: 2000,
                onClick: null,
                labels: {
                    boxHeight: 50,
                    boxWidth: 50,
                    font: {
                        size: 20
                    }
                }
            },
        },

        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// bar chart 

const ctx2 = document.getElementById('bar_chart');
new Chart(ctx2, {
    type: 'bar',
    data: {
        labels: ['completed', 'in progress', 'not started'],
        datasets: [{
            // label: null,
            data: [ completed, in_progress, total - in_progress - completed],
            borderWidth: 1,
            backgroundColor: [
                // 'rgb(0, 255, 0)',
                "green",
                'rgb(54, 162, 235)',
                'rgb(255, 0, 0)'
            ],
        }]
    },
    options: {
        legend: {
            display: true,
            position: 'right',
            boxWidth: 20,
            boxHeight: 2,
            onClick: null,
            labels: {
                boxHeight: 50,
                boxWidth: 50,
                font: {
                    size: 20
                }
            }
        },
        responsive: true,
        scales: {
            x: {
                ticks: {
                    
                        font: {
                            size: 20
                        }

            
                }
            },

            y: {
                ticks: {
                    
                        font: {
                            size: 20
                        }
            
                }
            }
        }





    }
});