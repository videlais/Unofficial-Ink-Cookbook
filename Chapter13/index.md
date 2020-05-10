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
    - [Fallback **Proxy** Support](#fallback-proxy-support)
  - [*EvaluateFunction()*](#evaluatefunction)
    - [Passing Arguments](#passing-arguments)
    - [Capturing Function Output](#capturing-function-output)
  - [Observing Variables](#observing-variables)
    - [**ObserveVariable()** Example](#observevariable-example)
    - [**ObserveVariables()** Example](#observevariables-example)
    - [Removing Observers](#removing-observers)

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

### Fallback **Proxy** Support

On platforms that do not support Proxies in JavaScript (Node.js v5, IE 11, Safari 9 and everything below), variables cannot be used through the proxy. However, the property *$* of the **variablesState** object can be used to provide the same access.

**Example:**

```javascript
story.variablesState.$("player_health", 100);
//story.variablesState["player_health"] = 100;

let health = story.variablesState.$("player_health");
//let health = story.variablesState["player_health"];
```

## *EvaluateFunction()*

The Story API provides the method **EvaluateFunction()** for calling Ink functions externally.

**Example Ink:**

```ink
What is it?

== function ExampleFunction() ==
~ return "It's it!"
```

**Example JavaScript:**

```javascript
let story = new inkjs.Story(storyContent);

let result = story.EvaluateFunction("ExampleFunction");

let paragraphText = story.Continue();
paragraphText += result;

console.log(paragraphText);
```

**Example Final Output:**

```ink
What is it?
It's it!
```

In the above code, a function is created in the Ink code. It is then saved with the Ink for Web option (or using the "Export story.js file..." option).

In the JavaScript code, the story is loaded and then the **story.EvaluateFunction()** method is called with the argument "ExampleFunction".

The variable *result* then holds the returning value from the internal Ink function (the String "It's it!"). This is then appended to the existing output.

Finally, the method **console.log()** is called with the new, combined value and showing it in the console.

### Passing Arguments

It is also possible to pass arguments into Ink functions using a second argument to the **story.EvaluateFunction()** method.

```javascript
story.EvaluateFunction("ink_function", ["arg1", "arg2"]);
```

Using an Array, any values sent will be passed to the internal Ink function and mapped to its own parameters in the same exact order of elements.

**Example Ink:**

```ink
I had visions, I was in them

== function ExampleFunction(arg1, arg2, arg3) ==
~ return "{arg1}<br>{arg2}<br>{arg3}"
```

**Example JavaScript:**

```javascript
let story = new inkjs.Story(storyContent);

let result = story.EvaluateFunction(
  "ExampleFunction",
  [
    "I was looking into the mirror",
    "To see a little bit clearer",
    "The rottenness and evil in me"
  ]
);

let paragraphText = story.Continue();
paragraphText += result;

console.log(paragraphText);
```

**Example Output:**

```ink
I had visions, I was in them
I was looking into the mirror To see a little bit clearer The rottenness and evil in me
```

In the above code, a function is created in Ink. It accepts three arguments that are combined and returned using its `return` statement.

In the JavaScript, the story is loaded and the internal function is called using its name of "ExampleFunction". It is also passed three arguments as part of the second argument to **story.EvaluateFunction()**.

Finally, like the previous example code, the output from the internal function is added to the existing story content.

### Capturing Function Output

The method **story.EvaluateFunction()** also accepts a third argument, a Boolean value.

```javascript
let result = story.EvaluateFunction("ink_function", ["arg1", "arg2"], true);
```

If the third argument is `true`, **story.EvaluateFunction()** will return an object instead of string output with two properties:

- *returned*: The returned value or `null` if there is no return value
- *output*: All output shown during the function

**Example Ink:**

```ink
Words like violence

== function ExampleFunction() ==
Break the silence
Come crashing in
Into my little world
~ return
```

**Example JavaScript:**

```javascript
let story = new inkjs.Story(storyContent);

let result = story.EvaluateFunction("ExampleFunction", [], true);

console.log(result);

let paragraphText = story.Continue();
paragraphText += result.output;

console.log(paragraphText);
```

**Example Output:**

```ink
Words like violence
Break the silence
Come crashing in
Into my little world
```

In the above code, a function is created in Ink that has output and does not return a value.

In the JavaScript code, the method **story.EvaluateFunction()** is given three parameters: the name of the function "ExampleFunction", an empty array of arguments, and the Boolean value `true`.

Because of the third argument, an object is returned from the method **story.EvaluateFunction()**. The property *output* of the returned object is then combined together with the previous story output.

## Observing Variables

For the common task of accessing and using the value of a variable from within Ink, the previously covered tools of the Proxy object **story.variablesStates** and the method **story.EvaluateFunction()** are not ideal.

The use of **story.variablesStates** would require constantly polling the values to see if had changed and then reacting in some way. The same is also true of **story.EvaluateFunction()**: an Ink function would need to be written whose sole purpose is reporting on a variable. That is a waste of time and code.

Instead, and to help with these use cases, the Story API provides two methods: **story.ObserveVariable()** and **story.ObserveVariables()**. These differ from the earlier code in one very important way: instead of needing to poll values, each method accepts a callback function that is called if the values of the variable(s) change!

> **Note:** In JavaScript, a *callback function* is a common pattern where usually an anonymous function (one without a name) is written to be called when something happens. As functions are a type of value in JavaScript, they can be passed into functions and called in another context.

### **ObserveVariable()** Example

The method **story.ObserveVariable()** accepts two arguments. The first, like with using **story.variablesStates**, is the name of the variable in quotation marks. The second is a callback function.

```javascript
story.ObserveVariable(
  "variableName",
  function(variableName, variableValue) {});
```

Variables are *global* in Ink. Once they are created, they can be accessed from any knot, stitch, or function. This also means their values can be changed from different points as well.

**Example Ink:**

```ink
VAR confidence = 0

-> Voting

=== Voting ===
Confidence: {confidence}

+ [Raise Confidence]
  ~ confidence += 10
  -> Voting
+ [Lower Confidence]
  ~ confidence -= 10
  -> Voting
```

**Example JavaScript:**

```javascript
let story = new inkjs.Story(storyContent);

story.ObserveVariable("confidence", function(variableName, variableValue) {
  console.log(variableName, variableValue);
});

let storyContainer = document.querySelector('#story');

continueStory();

function continueStory(firstTime) {

  // Generate story text - loop through available content
  while(story.canContinue) {

    // Get ink to generate the next paragraph
    let paragraphText = story.Continue();

    // Create paragraph element (initially hidden)
    let paragraphElement = document.createElement('p');
    paragraphElement.innerHTML = paragraphText;
    storyContainer.appendChild(paragraphElement);

  }

  // Create HTML choices from ink choices
  story.currentChoices.forEach(function(choice) {

    // Create paragraph with anchor element
    let choiceParagraphElement = document.createElement('p');
    choiceParagraphElement.classList.add("choice");
    choiceParagraphElement.innerHTML = `<a href='#'>${choice.text}</a>`
    storyContainer.appendChild(choiceParagraphElement);

    // Click on choice
    let choiceAnchorEl = choiceParagraphElement.querySelectorAll("a")[0];
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
  });
}

// Remove all elements that match the given selector.
function removeAll(selector) {
  let allElements = storyContainer.querySelectorAll(selector);
  for(var i=0; i<allElements.length; i++) {
    let el = allElements[i];
    el.parentNode.removeChild(el);
  }
}
```

**Example Output:**

```ink
confidence 10
confidence 0
confidence -10
confidence -20
confidence -10
```

In the above code, a variable *confidence* is created in Ink. A knot **Voting** is also created with two internal, sticky choices of *Raise Confidence* and *Lower Confidence*. For each, they adjust the value of *confidence* and then loop back to the start of the knot.

In the JavaScript code, things are slightly more complex. In order to handle clicking on the links, more code was needed to load the story, create its content, and allow for using the choices in HTML. However, the important line is the following:

```javascript
story.ObserveVariable(
  "confidence",
  function(variableName, variableValue) {
    console.log(variableName, variableValue);
  }
);
```

The use of the **story.ObserveVariable()** method sets up a "listener" for the internal, Ink variable *confidence*. Every time it changes, the callback function will be passed two arguments:

- *variableName*: Name of the variable being watched
- *variableValue*: Current value of the variable

> **Note:** Like other functionality when using the Story API, the **story.ObserveVariable()** method is affected by **Continue()**. If a variable is updated as part of internal Ink code, the method **story.ObserveVariable()** will only have the last updated value.
>
> However, as variables can be accessed via the Proxy object **story.variablesState**, this will also trigger the **story.ObserveVariable()** method. If a variable is updated via the Story API, it will trigger the **story.ObserveVariable()** method.

Inside the callback function, the variable name and its value are passed to the method **console.log()** and shown to the user via the console.

If either of the choices are made, the value of *confidence* is updated in Ink. This then signals to the Story API the values have been changed, which, in turn, uses the callback function setup with the **story.ObserveVariable()** method.

### **ObserveVariables()** Example

The method **story.ObserveVariables()** accepts two arguments. The first is an Array of variables to observe and the second is an Array of callback functions.

> **Note:** The order of each Array argument maps the other for **story.ObserveVariables()**. In other words, the first callback function is connected to the first variable. The second of each are also connected. This continues for each element in each array.

```javascript
story.ObserveVariables(
  [
    "variableName1",
    "variableName2"
  ],
  [
    function(variableName, variableValue) {},
    function(variableName, variableValue) {}
  ]
);
```

**Example Ink:**

```ink
VAR confidence = 0
VAR evidence = 0

-> Voting

=== Voting ===
Confidence: {confidence}
Evidence: {evidence}

+ [Raise Confidence]
  ~ confidence += 10
  -> Voting
+ [Lower Confidence]
  ~ confidence -= 10
  -> Voting
+ [Introduce Evidence]
  ~ evidence += 1
  -> Voting
+ [Remove Evidence]
  ~ evidence -= 1
  { evidence < 0:
    ~ evidence = 0
  }
  -> Voting
```

**Example JavaScript:**

```javascript
let story = new inkjs.Story(storyContent);

story.ObserveVariables(
  [
    "confidence",
    "evidence"
  ],
  [
    function(variableName, variableValue) {
      console.log("Confidence:", variableName, variableValue)
    },
    function(variableName, variableValue) {
      console.log("Evidence:", variableName, variableValue)
    }
  ]
);

let storyContainer = document.querySelector('#story');

continueStory();

function continueStory(firstTime) {

  // Generate story text - loop through available content
  while(story.canContinue) {

    // Get ink to generate the next paragraph
    let paragraphText = story.Continue();

    // Create paragraph element (initially hidden)
    let paragraphElement = document.createElement('p');
    paragraphElement.innerHTML = paragraphText;
    storyContainer.appendChild(paragraphElement);

  }

  // Create HTML choices from ink choices
  story.currentChoices.forEach(function(choice) {

    // Create paragraph with anchor element
    let choiceParagraphElement = document.createElement('p');
    choiceParagraphElement.classList.add("choice");
    choiceParagraphElement.innerHTML = `<a href='#'>${choice.text}</a>`
    storyContainer.appendChild(choiceParagraphElement);

    // Click on choice
    let choiceAnchorEl = choiceParagraphElement.querySelectorAll("a")[0];
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
  });
}

// Remove all elements that match the given selector.
function removeAll(selector)
{
    let allElements = storyContainer.querySelectorAll(selector);
    for(let i=0; i<allElements.length; i++) {
        let el = allElements[i];
        el.parentNode.removeChild(el);
    }
}
```

**Example Output:**

```ink
Confidence: confidence 10
Evidence: evidence 1
```

In the above code, two variables are created in Ink. When making choices in the knot **Voting**, their values are adjusted and a divert is used to loop.

In the JavaScript code, the method **story.ObserveVariables()** is used. It observes both the Ink variable *confidence* and *evidence*. If these values change, their associated callback functions are called.

> **Note:** Like with **ObserveVariable()**, all variables are affected by the Story API and **Continue()**.
>
> In the Ink code, the value of *evidence* is decreased in 1 in its section of the code. A conditional test then resets its value to 0 if it is below that. However, as these happen back-to-back and most importantly *before* the next use of **Continue()**, the JavaScript code will never see a negative value for Ink variable *evidence*.

### Removing Observers

The method **RemoveVariableObserver()**, as part of the Story API, *removes* observer functions from watching variables.

Unlike its sister methods **ObserveVariable()** and **ObserveVariables()**, **RemoveVariableObserver()** accepts either the function *or* the name of the variable to stop watching.

```javascript
story.RemoveVariableObserver(observerFunction, watchedVariable);
```

> **Note:** As anonymous functions are often used for callbacks, the optional use of a function argument is very helpful. Supplying only the name of the variable to stop watching is more common.

**Example Ink:**

```ink
VAR confidence = 0
VAR evidence = 0

-> Voting

=== Voting ===
Confidence: {confidence}
Evidence: {evidence}

+ [Raise Confidence]
  ~ confidence += 10
  -> Voting
+ [Lower Confidence]
  ~ confidence -= 10
  -> Voting
+ [Introduce Evidence]
  ~ evidence += 1
  -> Voting
+ [Remove Evidence]
  ~ evidence -= 1
  { evidence < 0:
    ~ evidence = 0
  }
  -> Voting
```

**Example JavaScript:**

```javascript
let story = new inkjs.Story(storyContent);

story.ObserveVariables(
  [
    "confidence",
    "evidence"
  ],
  [
    function(variableName, variableValue) {
      console.log("Confidence:", variableName, variableValue)
    },
    function(variableName, variableValue) {
      console.log("Evidence:", variableName, variableValue)
    }
  ]
);

story.RemoveVariableObserver(undefined, "confidence");

let storyContainer = document.querySelector('#story');

continueStory();

function continueStory(firstTime) {

  // Generate story text - loop through available content
  while(story.canContinue) {

    // Get ink to generate the next paragraph
    let paragraphText = story.Continue();

    // Create paragraph element (initially hidden)
    let paragraphElement = document.createElement('p');
    paragraphElement.innerHTML = paragraphText;
    storyContainer.appendChild(paragraphElement);

  }

  // Create HTML choices from ink choices
  story.currentChoices.forEach(function(choice) {

    // Create paragraph with anchor element
    let choiceParagraphElement = document.createElement('p');
    choiceParagraphElement.classList.add("choice");
    choiceParagraphElement.innerHTML = `<a href='#'>${choice.text}</a>`
    storyContainer.appendChild(choiceParagraphElement);

    // Click on choice
    let choiceAnchorEl = choiceParagraphElement.querySelectorAll("a")[0];
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
  });
}

// Remove all elements that match the given selector.
function removeAll(selector)
{
    let allElements = storyContainer.querySelectorAll(selector);
    for(let i=0; i<allElements.length; i++) {
        let el = allElements[i];
        el.parentNode.removeChild(el);
    }
}
```

**Example Output:**

```ink
Evidence: evidence 1
Evidence: evidence 0
```

In the above code, variables are created and their values changed in the Ink code.

In JavaScript, the method **ObserveVariables()** is used to create two observer functions on two Ink variables. However, the **RemoveVariableObserver()** method is then used to remove any observer functions on the Ink variable *confidence*.

In the use of the method **console.log()**, only the changes to the Ink variable *evidence* would be reported. The observer function for the Ink variable *confidence* was removed.
