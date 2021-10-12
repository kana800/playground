// importing lorem ipsum package
import { LoremIpsum } from "lorem-ipsum";

let generator = document.getElementById("generator");

generator.addEventListener("click",generateLorem);


const lorem = new LoremIpsum({
    sentencesPerParagraph:{
        max: 8,
        min: 4
    },
    wordsPerSentence: {
        max: 16,
        min: 4
    }
});

function generateLorem(){
    let words = lorem.generateWords(1);
    console.log(words);        
}