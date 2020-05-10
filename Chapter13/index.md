# Chapter 13: JavaScript Story API

- [Chapter 13: JavaScript Story API](#chapter-13-javascript-story-api)
  - [Reviewing Ink for Web](#reviewing-ink-for-web)
    - [Examining `main.js`](#examining-mainjs)
      - [Looping Story Content](#looping-story-content)
      - [*canContinue* and **Continue()** Pattern](#cancontinue-and-continue-pattern)
      - [Parsing Tags](#parsing-tags)
        - [Example Tag Parsing](#example-tag-parsing)
    - [Loading Choices](#loading-choices)
      - [Click to Load](#click-to-load)
    - [Summarizing `main.js`](#summarizing-mainjs)
  - [Getting and Setting Variables](#getting-and-setting-variables)
    - [Variables State Example](#variables-state-example)
    - [Accessing Variables State Properties](#accessing-variables-state-properties)
  - [*EvaluateFunction()*](#evaluatefunction)
  - [Observing Variables](#observing-variables)

**Summary:** In this chapter, you will learn more about the JavaScript Story API, how to use it, and how its functionality relate to each other.

> **Note:** Much of the code in this chapter assumes you know and can read JavaScript. Some of the underlining concepts and representations are explained, but this chapter's focus is on the Story API and not necessarily JavaScript itself.

---

## Reviewing Ink for Web

The "Ink for Web" functionality is used as part of Inky to make three JavaScript files: `ink.js`, `main.js`, and the `story.js`.

- `ink.js`: Ink engine in JavaScript
- `main.js`: JavaScript code to run the story
- `story.js`: Story encoded as JSON. (If a project does not have a name, Inky defaults to the `story.js` name.)

### Examining `main.js`

As the code to run the Ink story using its engine (API), the `main.js` file shows some of the ways in which JavaScript code can be written to work with an Ink story.

#### Looping Story Content

About a third through the `main.js` file will be the use of a property called *canContinue*. When using Ink with JavaScript, this is access into understanding the connection between the Ink engine and the story code!

```javascript
while(story.canContinue) {
  // Get ink to generate the next paragraph
  var paragraphText = story.Continue();
  var tags = story.currentTags;

  // Create paragraph element
  var paragraphElement = document.createElement('p');
  paragraphElement.innerHTML = paragraphText;
  storyContainer.appendChild(paragraphElement);
}
```

In the reduced code example above, the object **story** is a variable holding a reference to a **Story** object. It represents the entire story!

> **Note:** In object-oriented programming (OOP), data is stored in *objects*. These are special data structures with values that describe themselves and their status (*properties*) and have ways to access data or communicate with other code (*methods*).

One of its properties, *canContinue*, signals if there is more content in the story or not. It has either a `true` or `false` value. If there is more content (the story has not reached "End of Story"), it will be `true`.

Inside the `while()` loop are two other important things: the method **Continue()** and property *currentTags*.

#### *canContinue* and **Continue()** Pattern

Nearly all code that works with Ink and story content use some combination of the *canContinue* and **Continue()** pattern.

When working with Ink in JavaScript, it often appears as it does in the above example:

```javascript
while(story.canContinue) {
  let paragraphText = story.Continue();
}
```

The property *canContinue* lets the code know if there is more story content. Inside of loop checking this will also be the use of the method **Continue()**.

Assuming there is story content to load, the method **Continue()** loads it and returns any output. (This loads but **does not** return choices.)

The text loaded is determined through two factors:

- Is there a choice?
- Is this the end of of the story?

**Continue()** only continues up to the next set of choices in the story. It then pauses and waits for the methods related to choices to run.

Because there is a possibly of the story ending, **Continue()** will read through to the end and then change the value of *canContinue* internally.

If there is no more story content, **Continue()** should not be called. This will cause an error!

#### Parsing Tags

Inside of the looping pattern of *canContinue* and **Continue()** is often the use of the property *currentTags*.

After the method **Continue()** is called, this property will be populated with any tags related to the current text output loaded up to the next set of choices.

*currentTags* is an **Array** with each element the string contents of a tag starting after the use of the hash, `#`, and up to the end of the line. This means that additional code must be written to parse and understand these tags in order to use them.

##### Example Tag Parsing

In the `main.js` file, the use of `<String>`,**indexOf()** is used in the function **splitPropertyTag()** to find a colon, `:`, and then split the string value.

```javascript
// Helper for parsing out tags of the form:
//  # PROPERTY: value
// e.g. IMAGE: source path
function splitPropertyTag(tag) {
  var propertySplitIdx = tag.indexOf(":");
  if( propertySplitIdx != null ) {
    var property = tag.substr(0, propertySplitIdx).trim();
    var val = tag.substr(propertySplitIdx+1).trim();
    return {
      property: property,
      val: val
    };
  }

  return null;
}
```

### Loading Choices

While the *canContinue* and **Continue()** pattern appears earlier in the `main.js` file, it is most frequently *called* inside of another part of the code: creating choices!

> **Note:** The method **Continue()** must be called at least once to populate the property *currentChoices*!

In JavaScript, the property *currentChoices* is an Array of **Choice** objects. (Each has the properties *text*, the output of the choice, and *index*, its position within the current set of choices.)

In `main.js`, the iterator function **forEach()** is used to create content based on its elements. For each one, a new `<p>` is added with the class `.choice` and a hyperlink with the *text* of the **Choice** object.

```javascript
story.currentChoices.forEach(function(choice) {

  // Create paragraph with anchor element
  var choiceParagraphElement = document.createElement('p');
  choiceParagraphElement.classList.add("choice");
  choiceParagraphElement.innerHTML = `<a href='#'>${choice.text}</a>`
  storyContainer.appendChild(choiceParagraphElement);
});
```

#### Click to Load

Next in the code is the creation of *event listeners* for the hyperlinks of the choice generated previously through iterating through the property *currentChoices*.

> **Note:** In JavaScript terminology, an *event listener* is some code that "listens" for an event like clicking or the user typing and responds in some way to it.

```javascript
// Click on choice
var choiceAnchorEl = choiceParagraphElement.querySelectorAll("a")[0];

choiceAnchorEl.addEventListener("click", function(event) {

  // Don't follow <a> link
  event.preventDefault();

  // Remove all existing choices
  removeAll(".choice");

  // Tell the story where to go next
  story.ChooseChoiceIndex(choice.index);

  // And loop
  continueStory();
});
```

A choice is chosen when using the `main.js` JavaScript code when its hyperlink is clicked on by a user. When this happens, four things happen in order based on the above code:

- The use of the method **preventDefault()** stops the default action of the hyperlink, `<a>` element.

- All other choices are removed from the document based on their class, `.choice`.

- The method **ChooseChoiceIndex()** is used.

- The function **continueStory()** is called to load the next part of the story.

When passed a number (the *index* of a **Choice**), **ChooseChoiceIndex()** method tells Ink that a choice was chosen.

In the next *canContinue* and **Continue()** loop, the results of this choice would then be loaded next. And, in fact, that is the next line after using the **ChooseChoiceIndex()** method: calling *continueStory()* and looping again.

### Summarizing `main.js`

The control flow of the major activities of the `main.js` file can be summarized in the following way as it relates the Story API in JavaScript:

- Call `<Story>`.**Continue()** first. This initial load setup of the properties *canContinue*, *currentTags*, and *currentChoices*.

- If *canContinue* is `true`, call **Continue()**. Parse any tags using *currentTags*.

- Parse any existing choices using *currentChoice*. For each choice, setup an event listener to react on click events passing the method **ChooseChoiceIndex()** what choice was made.

- Continue the *canContinue* and **Continue()** pattern until there is no more content.

## Getting and Setting Variables

The Story API provides access to the property *variablesState*. This acts as a [Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) object to the running Ink code, allowing access to variables via their name.

### Variables State Example

**Example Ink:**

```ink
VAR example = "Looking good!"

Hi there! {example}
```

**Example JavaScript:**

```javascript
story.variablesState["example"] = "Looking awesome!";
```

**Example Output:**

```ink
Hi there! Looking awesome!
```

In the above Ink code, a variable named *example* is created. When the resulting HTML from the Ink for Web option is used, an additional line of JavaScript is added.

The use of `story.variablesState["example"]` gives access, via the **variablesState** proxy object, to the variable named "example". Its value can then be changed to a different value.

> **Reminder:** Variables exist with respect to story state and the use of the **Continue()** method. They are created or changed up to the last use of **Continue()** method, and any changes made to their values will not be reflected in output until it is called again.

### Accessing Variables State Properties

As a Proxy object in JavaScript, **variablesState** also allows access to variables via their "dot notation." Instead of using square brackets, variables can be accessed as properties of the **variablesState** object.

```javascript
story.variablesState.example = "Looking awesome!";
```

> **Note:** **variablesState** is a [*Proxy*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy). This means it seems like an object literal in JavaScript, but **is not**. Internally, it has its own methods for accessing and changing the variable property names.

Something that is not possible, however, is creating new properties using the **variablesState** Proxy object. It **is not** an object literal.

While it is possible to access variables created in Ink, more cannot be added. The Proxy acts as a way to *access* existing variables only.

## *EvaluateFunction()*

The function *EvaluateFunction()* is used to call Ink functions. It accepts the name of the function as a string, an optional array of arguments, and if both the result of the function and any text it would have displayed should be returned.

As the documentation mentions, if the third parameter is true, the returned object with have both returned, returned results, and output, the text of the function, as its properties.

Since it is possible to write functions that change the values of variables within Ink, the use of *EvaluateFunction()* means that they can be called from outside of the story with values passed into the function via the call.

In other words, it is possible to create an interface within an Ink story to changes its variables via different functions. These can then be called via *EvaluateFunction()* and passed values. Instead of needing to use variablesState directly, values can be changed and other work done from within the Ink story via different usages of *EvaluateFunction()*.

## Observing Variables

