# Chapter 13: JavaScript Story API

- [Chapter 13: JavaScript Story API](#chapter-13-javascript-story-api)
  - [JavaScript Story API](#javascript-story-api)
    - [Properties](#properties)
    - [Methods](#methods)
  - [Creating a JSON Story file](#creating-a-json-story-file)
  - [Getting and Setting Variables](#getting-and-setting-variables)
    - [*EvaluateFunction()*](#evaluatefunction)

**Summary:** In this chapter, you will learn more about the JavaScript Story API, how to use it, and how its functionality relate to each other.

---

## JavaScript Story API

Building from the last chapter, the Ink for Web option in Inky can be used to build more complex projects using the JavaScript Story API as part of inkjs. In fact, as it is integrated into the Inky Editor, editing the `main.js` file it produces shows an example of how to use the Story API in JavaScript!

In the last chapter, the "Ink for Web" functionality was used as part of Inky to make three JavaScript files: `ink.js`, `main.js`, and the `story.js`.

In reviewing the `main.js`, there were usages of a story object to check if the story could continue, what the next chunk of text was, and what any of the choices were.

There is not direct documentation for the JavaScript API. However, the C# documentation used with Unity shows the API for using the **Story** object.

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
