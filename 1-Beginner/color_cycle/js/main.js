const colorselector=document.querySelector('#firstcolor');
const startButton=document.querySelector('#startbutton');
const filler=document.querySelector('body');
const outsideband=document.querySelector('.settings');


// event listener

colorselector.addEventListener('change',watchColorChange);
startButton.addEventListener('click',mainLoop);


function watchColorChange(e){
	filler.style.backgroundColor=e.target.value;
	outsideband.style.backgroundColor=e.target.value;
}

function mainLoop(e){
	console.log("fruit loops");
	filler.classList.toggle("animation");
}

