# Chapter 13: JavaScript Story API

- [Chapter 13: JavaScript Story API](#chapter-13-javascript-story-api)
  - [Reviewing Ink for Web](#reviewing-ink-for-web)
    - [Examining `main.js`](#examining-mainjs)
      - [Looping Story Content](#looping-story-content)
      - [*canContinue* and **Continue()** Pattern](#cancontinue-and-continue-pattern)
      - [Parsing Tags](#parsing-tags)
        - [Example Tag Parsing](#example-tag-parsing)
    - [Loading Choices](#loading-choices)
  - [JavaScript Story API](#javascript-story-api)
    - [Properties](#properties)
    - [Methods](#methods)
  - [Creating a JSON Story file](#creating-a-json-story-file)
  - [Getting and Setting Variables](#getting-and-setting-variables)
    - [*EvaluateFunction()*](#evaluatefunction)

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



## JavaScript Story API

The Ink for Web option in Inky can be used to build more complex projects using the JavaScript Story API as part of InkJS.

### Properties

- *canContinue*: Returns `true` if the story can continue to run or `false` otherwise.
- *currentChoices*: An array of the current choices. Each entry’s text property contains their text.
- *currentTags*: An array of any tags as part of current block.
- *globalTags*: An array of all the tags used in the story

### Methods

- *Continue()*: Returns the next text block and loads the next choices, if any.
- *ChooseChoiceIndex()*: Supplying a valid index matching the length of the array of currentChoices will consider that entry "clicked."

## Creating a JSON Story file

The Story API is created from reading a JSON file with a compiled story. In order to get that, an Ink file must be run through either inklecate, a command-line tool, or via the Inky editor using the File -> "Export to JSON.." option.

The difference between the `story.js` and the JSON file is actually only that the `story.js` has its JSON contents set as the value for variable called *storyContent*. It is often easier to simply load this file into the global namespace via a SCRIPT tag and then parse the object when working in a browser.

## Getting and Setting Variables

While the Story API provides access to the **Story** object and its properties and methods, global variables can also be accessed through the **variablesState** object.

Once a story has been created, its variables can be accessed through a Proxy via the **variablesState** property on the Story object. That is, the variables are not technically a part of the object, but act as a way to gain access and change their values.

For example, to change the variable name in the above code, it could be accessed via its name, name: `variablesState["name"]`. Changing this value would change it in the story itself.

### *EvaluateFunction()*

The function *EvaluateFunction()* is used to call Ink functions. It accepts the name of the function as a string, an optional array of arguments, and if both the result of the function and any text it would have displayed should be returned.

As the documentation mentions, if the third parameter is true, the returned object with have both returned, returned results, and output, the text of the function, as its properties.

Since it is possible to write functions that change the values of variables within Ink, the use of *EvaluateFunction()* means that they can be called from outside of the story with values passed into the function via the call.

In other words, it is possible to create an interface within an Ink story to changes its variables via different functions. These can then be called via *EvaluateFunction()* and passed values. Instead of needing to use variablesState directly, values can be changed and other work done from within the Ink story via different usages of *EvaluateFunction()*.
