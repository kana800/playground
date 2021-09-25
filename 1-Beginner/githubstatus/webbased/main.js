const request = require('request');
//var statusbar = document.getElementById("statuswindow");

function createStatusWidget(statusname, currentstatus){
    let div = document.createElement('div');
    div.className = "status-content";
    div.id = "status-content";

    div.innerHTML = `<p>${statusname}-${currentstatus}</p>`
    return div;    
}

function addtoDiv(element){
    statusbar.appendChild(element);
}

function getStatus(){
    request('https://www.githubstatus.com/',  { json: true }, (err, res, body) => {  
        let results = body.components;
        console.log(results);
        for (let i = 0; i < results.length; i++){
            //element = createStatusWidget(results[i]['name'],results[i]['status'])
            console.log(results[i]['name'] + " " + results[i]['status']);
            //addtoDiv(element);
        }
    });
}

getStatus();