<br />
<p style="text-align: center" align="center">
  <a href="https://github.com/kana800/myProjects">
	:penguin:
  </a>
  <h3 align="center">Lorem Ipsum Generator</h3>
  <p align="center">
    <br />
    <a href="https://github.com/kana800/myProjects/edit/master/1-Beginner/">Project List</a>
    ·
    <a href="https://github.com/kana800/myProjects/issues">Report Bug</a>
    ·
    <a href="https://github.com/kana800/myProjects/issues">Request Feature</a>
  </p>
</p>

### [Web Based](webbased)

we are using npm package called `lorem ipsum` to generate the text. you need to download `lorem ipsum` to makesure the program works in your pc.

#### What I Learnt

I learned about [importing node modules](https://medium.com/weekly-webtips/import-use-npm-modules-in-the-browser-easily-e70d6c84fc31) into javascript.

#### Preview

<p align="center">
	<img src=".images/preview.png"></img>
</p>


#### Improvements

Instead of creating a `textarea` element, I can make an element in the `index.html` file and change the `textContent` of that `element`.

<details>
  <summary>This would reduce code</summary>

  ```javascript
    let loremcontent = document.createElement("textarea");
    loremcontent.textContent = content;
    /*clearing the previous content from the div*/
    loremdiv.textContent = "";
    loremdiv.appendChild(loremcontent);
  ```

  we can replace the above snippet with

  ```javascript
  let loremcontent = document.getElementById("loremcontent");
  loremcontent.textContent = generatedContent;
  ```
</details>


<details>
<summary>Project Information</summary>

**Tier:** 1-Beginner

Lorem Ipsum is simply dummy text of the printing and typesetting industry.
This app should generate passages of lorem ipsum text suitable for use as placeholder copy in web pages, graphics, and more.

## User Stories

-   [x] User can type into an input field the number of paragraphs of lorem ipsum to be generated
-   [x] Use can see the generated paragraphs of lorem ipsum and is able to copy them

## Trello Board

You can track your progress by cloning this [Trello Board](https://trello.com/b/T0xA0Glj/lorem-ipsum-generator)

## Useful links and resources

-   [lorem-ipsum npm package](https://www.npmjs.com/package/lorem-ipsum)
-   [lorem-ipsum CDN](https://www.jsdelivr.com/package/npm/lorem-ipsum)

## Example projects

-   [Lipsum.com](https://www.lipsum.com/)
</details>
