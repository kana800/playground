function checkCurrentBody(){
  return document.body.id;
}

function app(){  
  if (checkCurrentBody() == "") {
    // Event Listeners
    const submitbutton = document.getElementById('form');
    submitbutton.addEventListener('submit',(e) =>{

    e.preventDefault();
    username = document.getElementById("username");
    password = document.getElementById("pass");

    // storing the values in session
    sessionStorage.setItem('user',username.value);

    const ip = get_the_api();
    window.location.href='welcome_page.html';
  })
  }else if (checkCurrentBody()=="welcomepage"){
    addWelcomeText();
    // adding a listener to the logout button
    const logout = document.getElementById("logout");
    logout.addEventListener('click',(e) => {
      e.preventDefault();
      console.log("this button works");
      window.location.replace('index.html');
    })
  }
}

function get_the_api(){
  
  // link
  var endpoint = 'http://ip-api.com/json/?fields=status,query';
  var xhr = new XMLHttpRequest();
  // open a request
  xhr.open('GET', endpoint, true);
  xhr.onload = function(){
    if (this.status == 200) {
      var response = JSON.parse(this.responseText);
      
      //check if the response is successful from the status
      if (response.status !== 'success'){
        console.log('alert error')
        return ;
      }
      return response.query;
    }
  }
  xhr.send();
}

function addWelcomeText(){
  // function for the welcomepage
    if (checkCurrentBody() === 'welcomepage'){
        fetch('https://fourtonfish.com/hellosalut/?mode=auto')
        .then( function(response){
          return response.json()
        } )
        .then( function( jsonData ){
          welcome_text = jsonData['hello']+"! "+sessionStorage.getItem('user');
          document.getElementById("introduction").textContent = welcome_text;
        } );
    }
}

app();
