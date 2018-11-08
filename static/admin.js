var dataPoints = []
candidates.forEach(candidate =>{
  dataPoint = {label: candidate["name"], y:candidate["votes"]},
  dataPoints.push(dataPoint)
})

var chartContainer = document.querySelector('#chartContainer');

if (chartContainer) {
  var chart = new CanvasJS.Chart("chartContainer", {
    animationEnabled: true,
    theme: "theme2",
    data: [
      {
        type: "column",
        dataPoints: dataPoints
      }
    ]
  });

  chart.render();
}

// Pusher.logToConsole = true;

// // Configure Pusher instance
// const pusher = new Pusher('4756882ee036ff91c865', {
//   cluster: 'ap2',
//   encrypted: true
// });

// // Subscribe to poll trigger
// var channel = pusher.subscribe('poll');

// // Listen to vote event
// channel.bind('vote', function(data) {
//   dataPoints = dataPoints.map(dataPoint => {
//     console.log("data"+data[4])
//     if(dataPoint.label == data[4].name[0]) {
//       dataPoint.y += 10;
//     }

//     return dataPoint
//   });

//   // Re-render chart
//   chart.render()
// });