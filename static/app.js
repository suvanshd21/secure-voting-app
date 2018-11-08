

// var pollMembers = document.querySelectorAll('.poll-member')

// //var candidates = ['Go', 'Python', 'PHP', 'Ruby']
// console.log("working");
// // Sets up click events for all the cards on the DOM
// pollMembers.forEach((pollMember, index) => {
//   pollMember.addEventListener('click', (event) => {
//     console.log("clicked"),
//     handlePoll(index)
//   }, true)
// })

// Sends a POST request to the server using axios
var dispProgress = function(data) { 
    console.log("Hello")
  //axios.post('http://localhost:5000/disp_progress')
    console.log(data)
    for (i = 0; i < (data.length); i++) { 
    var total = 0
    for (j=0; j < (data.length); j++){
      total += data[j].votes
    }
    console.log(data[i].id,data[i].votes,total)
    document.getElementById(data[i].id).style.width = calculatePercentage(total, data[i].votes)
    document.getElementById(data[i].id).style.background = "#388e3c" 
  }
}

// Configure Pusher instance
const pusher = new Pusher('4756882ee036ff91c865', {
  cluster: 'ap2',
  encrypted: true
});

// Subscribe to poll trigger
var channel = pusher.subscribe('poll');

// Listen to vote event
channel.bind('vote', function(data) {
    console.log("hi")
    console.log(data)
    for (i = 0; i < (data.length); i++) { 
    var total = 0
    for (j=0; j < (data.length); j++){
      total += data[j].votes
    }
    console.log(data[i].id,data[i].votes,total)
    document.getElementById(data[i].id).style.width = calculatePercentage(total, data[i].votes)
    document.getElementById(data[i].id).style.background = "#388e3c" 
  }
});

var dispProgBar = function(data) {
    console.log("hi")
    console.log(data)
    for (i = 0; i < (data.length); i++) { 
    var total = 0
    for (j=0; j < (data.length); j++){
      total += data[j].votes
    }
    console.log(data[i].id,data[i].votes,total)
    document.getElementById(data[i].id).style.width = calculatePercentage(total, data[i].votes)
    document.getElementById(data[i].id).style.background = "#388e3c" 
  }
}

let calculatePercentage = function(total, amount) {
  return (amount / total) * 100 + "%"
}