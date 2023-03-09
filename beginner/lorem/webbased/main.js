/*import loremipsum npm module into the script*/
const lorem = require("lorem-ipsum");

/* add event listener to the generate button*/
let generator = document.getElementById("generator");
let loremdiv = document.getElementById("loremdiv");
generator.addEventListener("click", generatelorem);

function generatelorem(){
    /*grabbing the number of paragraphs
     *the user wants to generate
    */
    let paragraphs = 
        document.getElementById("numberofparagraphs").value;

    
    const loremClass = new lorem.LoremIpsum({
        sentencesPerParagraph: {
            max: 8,
            min: 4
        },
        wordsPerSentence: {
            max: 16,
            min: 4
        }
    });

    /*generating the lorem ipsum content and
     *assigning it to a variable
     */
    let content  = loremClass.generateParagraphs(paragraphs);
    /*creating a text area widget and adding content generated
     *from loremipsum module into the widget. 
    */
    let loremcontent = document.createElement("textarea");
    loremcontent.textContent = content;
    /*clearing the previous content from the div*/
    loremdiv.textContent = "";
    loremdiv.appendChild(loremcontent);

    /*adding a copy button*/
    let copybutton = document.createElement("button");
    copybutton.innerText = "copy to clipboard";
    copybutton.onclick = () => {
        navigator.clipboard.writeText(content);
    }; 

    loremdiv.appendChild(copybutton);
}