document.addEventListener('DOMContentLoaded', function () {
    const chart_1 = Highcharts.chart('forecast-1', {
        chart: {type: 'line'},
        title: {
            text: 'Temperature & Dew Point',
            style: { "color": "#333333", "fontSize": "13px", "fontWeight": "bold" }
        },
        xAxis: {
            gridLineWidth: 1,
            tickInterval: 2,
            type: 'datetime'
        },
        yAxis: {
            title: {
                text: 'Temp (°C)',
                style: {"fontSize": "11px"}
            },
            tickInterval: 2
        },
        series: [{
            name: 'Temp',
            data: [-2.5,-2.4,-1.5,-0.4,0.5,0.7,1.4,1.9,2.3,2.5,3.0,2.7,1.7,0.8,-1.4,-2.4]
        },{
            name: 'Dew Point',
            data: [-5.5,-4.4,-3.5,-2.4,-0.5,-0.7,1.4,0.9,0.3,1.5,-0.8,-1.2,-1.7,-2.8,-3.4,-5.4]
        }],
        credits: {enabled: false},
        colors: ['#c42525', '#8bbc21'],
        plotOptions: {
            series: {
                marker: {symbol: 'circle', radius: 3}
            },
        },
        legend: {
            backgroundColor: '#fafafa',
            borderColor: '#bfbfbf',
            borderWidth: 1,
            itemStyle: {"fontSize": "10px"}
        },
    });

    const chart_2 = Highcharts.chart('forecast-2', {
        chart: {type: 'line'},
        title: {
            text: 'Clouds & Precipitations',
            style: { "color": "#333333", "fontSize": "13px", "fontWeight": "bold" }
        },
        xAxis: {
            gridLineWidth: 1,
            tickInterval: 2,
            type: 'datetime'
        },
        yAxis: [{
            title: {
                text: 'Clouds (%)',
                style: {"fontSize": "11px"}
            },
            tickInterval: 1
        },{ 
            title: {
                text: 'Precip (mm)',
                style: {"fontSize": "11px"}
            },
            opposite: true,
            tickInterval: 1
        }],
        series: [{
            name: 'Clouds',
            yAxis: 0,
            data: [78,79,80,80,82,82,82,84,85,85,86,89,89,88,88,87]
        },{
            name: 'Precip',
            yAxis: 1,
            data: [-2.5,-2.4,-1.5,-0.4,0.5,0.7,1.4,1.9,2.3,2.5,3.0,2.7,1.7,0.8,-1.4,-2.4]
        }],
        credits: {enabled: false},
        colors: ['#0d233a', '#2f7ed8'],
        plotOptions: {
            series: {
                fillColor: null,
                marker: {symbol: 'circle', radius: 3}
            },
        },
        legend: {
            backgroundColor: '#fafafa',
            borderColor: '#bfbfbf',
            borderWidth: 1,
            itemStyle: {"fontSize": "10px"}
        },
    });

    const chart_3 = Highcharts.chart('forecast-3', {
        chart: {type: 'line'},
        title: {
            text: 'Wind & Gusts',
            style: { "color": "#333333", "fontSize": "13px", "fontWeight": "bold" }
        },
        xAxis: {
            gridLineWidth: 1,
            tickInterval: 2,
            type: 'datetime'
        },
        yAxis: {
            title: {
                text: 'Wind (m/s)',
                style: {"fontSize": "11px"}
            },
            tickInterval: 1
        },
        series: [{
            name: 'Wind',
            data: [2.5,2.4,1.5,0.4,0.5,0.7,1.4,1.9,2.3,2.5,3.0,2.7,1.7,0.8,1.4,2.4]
        },{
            name: 'Gusts',
            data: [4.5,3.2,2.5,0.7,1.5,3.7,2.4,3.9,4.3,5.5,5.0,3.7,2.7,2.8,2.4,1.4]
        }],
        credits: {enabled: false},
        colors: ['#f28f43', '#77a1e5'],
        plotOptions: {
            series: {
                marker: {symbol: 'circle', radius: 3}
            },
        },
        legend: {
            backgroundColor: '#fafafa',
            borderColor: '#bfbfbf',
            borderWidth: 1,
            itemStyle: {"fontSize": "10px"}
        },
    });
});
