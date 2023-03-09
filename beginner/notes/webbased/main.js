// global variables
var filename = document.getElementById("filename"); 
var textcontent = document.getElementById("textarea");
let addnotebtn = document.getElementById("addnote");
var notebox = document.getElementById("notebox");

// event listeners
addnotebtn.addEventListener("click",storeContent);

let t_filename = "Test Note#1";
let t_content = "cool dude";
storeinLocalStorage(t_filename, t_content);
element = createNoteBox(t_filename, t_content);
addtoDiv(element);

/*creating a test item*/
function storeinLocalStorage(filename, content){
    var myStorage = window.localStorage;
    // if the item is present update the content
    // of the file
    if (localStorage.getItem(filename)){
        alert("Note Present!");
        return;
    }else{
        localStorage.setItem(filename,content);
        element = createNoteBox(f_filename, f_content);
        addtoDiv(element);
    }
    return;
}

function createNoteBox(filename, content){
    /*
    main container for the notes, this container consist of the
    heading an notebox paragraph div
    */
    let div = document.createElement('div');
    div.className = "notebox-content";
    div.id = "notebox-content";

    let heading = document.createElement('h3');
    // adding the filename for as the head
    heading.textContent = filename;
    // adding the heading for the file
    div.appendChild(heading);

    // delete button
    let deletebtn = document.createElement('button');
    deletebtn.id = "deletenote";
    deletebtn.name = filename;
    deletebtn.innerHTML = "delete note";    
    deletebtn.onclick = deleteContent;
    // note contents
    let noteboxParagraph = document.createElement('div');
    noteboxParagraph.className = "notebox-content";
    noteboxParagraph.innerHTML = `<p>${content}</p>`;

    div.appendChild(noteboxParagraph);
    div.appendChild(deletebtn);


    return div;
}

function addtoDiv(element){
    notebox.appendChild(element)
}

function storeinLocalStorage(filename, content){
    var myStorage = window.localStorage;
    // if the item is present update the content
    // of the file
    if (localStorage.getItem(filename)){
        alert("Note Present!");
        return;
    }else{
        localStorage.setItem(filename,content);
        element = createNoteBox(filename, content);
        addtoDiv(element);
    }
    return;
}

function storeContent(e){
    var f_content = textcontent.value;
    var f_filename = filename.value;
    storeinLocalStorage(f_filename, f_content);
}

function deleteContent(e){
    var myStorage = window.localStorage;
    // removing from the local storage
    myStorage.removeItem(e.target.name);
    // removing the parent node
    parentobject = e.target.parentNode;
    parentobject.remove();
}