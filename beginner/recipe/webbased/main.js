let chadtea = {
    "recipe-info":{
        "recipename":"Chad Tea",
        "recipetype":"Breakfast",
        "recipeservings":"One Serving",
        "recipedifficulty":"Easy"
    },
    "recipe-image":"images/tea.jpg",
    "recipe-ingredients": ["3 Tbs. green tea leaves",
    "4 oz. (8 Tbs.) unsalted butter","1/2 cup firmly packed light brown sugar",
    "1/4 cup mild honey","6-3/4 oz. (1-1/2 cups) unbleached all-purpose flour",
    "1 tsp. ground ginger","1/4 tsp. table salt","2 large eggs",
    "1 tsp. vanilla extract","1 tsp. finely grated orange zest",
    "1 tsp. baking soda","1/3 cup (1-3/4 oz.) dried cranberries; more for garnish",
    "4 oz. (1 cup) confectioners’ sugar, sifted"],
    "recipe-preparation":"Position a rack in the center of the oven and heat the oven to 350°F. Line 12 standard-size muffin cups with paper liners.\nBring 1 cup water to a boil, remove from the heat, stir in the tea, and steep for 5 minutes. Strain through a fine-mesh sieve, pressing to extract as much liquid as possible.\nIn a 2-quart saucepan, melt the butter over medium-low heat. Stir in the brown sugar and honey, and set aside to cool.\nIn a food processor or large bowl, combine the flour, ginger, and salt, and pulse to blend. Scrape in the butter mixture and blend. Add the eggs, vanilla, and orange zest and process until combined.\nStir the baking soda into 1/2 cup of the tea. Add to the batter along with the cranberries, and pulse. Portion the batter among the muffin cups, filling each about full. Bake, rotating halfway through, until a toothpick inserted in the center of the muffins comes out with moist crumbs clinging to it, about 15 minutes. Cool in the pan on a rack. Once cool, remove the muffins from the pan.\nIn a small bowl, combine the confectioners’ sugar with 1 Tbs. of the remaining tea. Whisk, adding more tea 1 tsp. at a time as necessary to make a thick but pourable icing. Drizzle over the cooled muffins, sprinkle with a few dried cranberries, and let set about 15 minutes before serving. The muffins are best the day they’re baked.\n"
};

let recipetitle = document.getElementById("recipe-title");
let mealtype = document.getElementById("mealtype");
let recipeservings = document.getElementById("recipeservings");
let recipedifficulty = document.getElementById("recipedifficulty");
let recipeimage = document.getElementById("recipeimage");
let ingredients = document.getElementById("ingredients");
let instructions = document.getElementById("instructions");

// sets the recipe information
function setRecipeHeader(recipeinfo){
    recipetitle.innerHTML = recipeinfo["recipename"];
    mealtype.innerHTML = recipeinfo["recipetype"];
    recipeservings.innerHTML = recipeinfo["recipeservings"];
    recipedifficulty.innerHTML = recipeinfo["recipedifficulty"];
    return;    
}

// sets the recipe image
function setImage(imagelocation){
    recipeimage.src = imagelocation;
}

// sets the recipe ingredients
function setRecipeIngredients(ingredientlist){
    
    for (let i = 0; i < ingredientlist.length; i++){
        let listelement = document.createElement("li");
        listelement.appendChild(document.createTextNode(ingredientlist[i]));
        // add the list element to the ingredients
        ingredients.appendChild(listelement);
    }
}

// sets the recipe instruction
function setRecipeInstructions(instructionparagraph){
    instructions.innerHTML = instructionparagraph;
}

setRecipeHeader(chadtea["recipe-info"]);
setImage(chadtea["recipe-image"]);
setRecipeIngredients(chadtea["recipe-ingredients"]);
setRecipeInstructions(chadtea["recipe-preparation"]);