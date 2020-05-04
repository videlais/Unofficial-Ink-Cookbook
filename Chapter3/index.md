# Chapter 3: Writing Your First Ink Story

- [Chapter 3: Writing Your First Ink Story](#chapter-3-writing-your-first-ink-story)
  - [Common Terms](#common-terms)
  - [Creating a New Project](#creating-a-new-project)
    - [Playing with Preview](#playing-with-preview)
    - [Comments](#comments)
    - [Tags](#tags)
  - [Creating Flows](#creating-flows)
    - [Styling Choice Output](#styling-choice-output)
    - [Adding More Choices](#adding-more-choices)
  - [Try It](#try-it)

**Summary:** In this chapter, the terms weave, flow, and divert will be reviewed and the basics of writing and using the Preview pane in the Inky editor will be explained.

---

## Common Terms

Every language has its own terms for its elements. Ink is no different, and explains how to write and understand code in relationship to a project through the following terms:

- *Choice:* Some text defining a possible branching path
- *Weave:* Collection of choices
- *Flow:* A user-created path through the available choices

Ink uses the metaphor of threads and sewing to describe projects. The total collection of all choices is a project's *weave*. Through making *choices*, a user creates a *flow* through the overall *weave*.

**Note:** This book uses the term *option* for what the user sees and clicks on to interact with in an Inky project. *Choices* are what an author creates; a user interacts with *options*.

## Creating a New Project

Using the Inky editor, go to File → New Project to create a new project. In the editor pane, write the following:

```ink
Hello, handsome!
```

After text has been added to a project, the Preview pane shows it. This updates every time there is a pause in the typing.

Underneath the previous text, add the following:

```ink
* Choose to Write More
* Give up on a New Project
```

Choices will be covered more in the next chapter, but they are the basic building block of any Ink project. They are what a user interacts with when playing an Ink game, and how the other key concepts in Ink relate to each other within the Flow of a project.

Through adding Choices, the preview pane in Inky can be used to "choose," and then rewind or restart a story. When working with the Inky Editor, this can help in moving through a story’s *weave*, and in testing how different parts.

### Playing with Preview

Testing a project in the Inky Editor is one of the most important skills to learn when working with Ink. Based on the example now written in the editor, its different choices and their outcomes can be examined.

First, click on the "Choose to Write More" option in the Preview pane. It will be shown and then the End of Story text will be shown.

**Note:** Whenever a story ends, the "End of Story" text is shown in the Inky Editor. This signals that there is no more content in the story.

Click the "Restart" button in the Inky Editor. (It is the double-arrow, the rightmost icon above the Preview Pane area.) This will restart the story back before any choices were made.

This time, click on the "Give up on a New Project" option. Notice that it too will be shown and then the same "End of Story" text is shown.

Right now, these two choices do not amount to much. Clicking on either will choose that option and then end the story right there.

### Comments

So far, only code has been added to Ink projects. There is also another type of text that can be added that helps with understanding how code works: comments.

In programming terminology, a comment is some text that is included in code but is ignored when it is run.

*A comment is text written for an author or as a reminder of how something works*.

Comments can also simply be used as notes to help keep track of things in a project as an author works on it.

Comments in Ink are added through using two forward slashes, `//`. Anything that follows the slashes until the next line is considered a new comment. This also includes adding comments on lines after code as well.

Anything from the two slashes to the end of the line is a comment and ignored by Ink.

```ink
// These are all comments.
// Ink skips over anything written with two forward-slashes

Hello! // Comments can also be written after code, too!
```

### Tags

If comments are text written for authors and other developers, *tags* can be thought of as instructions for *other programs*.

Ink supports adding *tags*, text starting with a hash, `#` and extending to the end of a line. When Ink encounters these, it ignores them.

```ink
This is an example using tags. # See?
```

In the above example, the output would be the following:

```text
This is an example using tags.
```

When using the Inky preview pane, it would also show the following on a separate line in a lighter color:

```ink
 # See?
```

In Ink, tags are optional text that it ignores as part of the story output. However, internally, it keeps track of the tags it encounters and, when working with other programs, these tags can have special meaning.

For example, when working with the Ink for Web output option in Inky, the tag `# CLEAR` has a special meaning: it clears the text from the screen!

When working with other programs like Unity, tags can also be used to add greater semantic meaning to the text, adding in, for example, tone, confidence, or other information to what a character is speaking in a part of the story.

```ink
Your dad slams his hand on the table. "No! I won't allow you to date her! I forbid you from seeing that girl!" # mood: angry

"But dad!" you scream. "I love her!" # mood: pleading
```

In the above example, *mood* is used as part of a tag with a colon and then a value. In Ink, this would simply be another tag and ignore. However, in Unity or another program, it could read and parse the tag to add greater emotional context to a scene or how a character's text should be displayed.

**Note:** Tags are parsed between story 'stopping points'. In Ink, the story continues until it finds a choice. At that point, it waits for input. Internally, Ink would process all tags up to that point and then also stop.

Tags are also associated with a single line. If used at the end of a line, they would be associated with that line. If a tag is used before a line, it becomes associated with the next output line.

For example, the following example's use of a tag would be associated with the next line.

```ink
# AUTHOR: Jane

My life really began after I died.
```

**Note:** Determining which line a tag is associated with can be determined in the Inky preview pane through verifying where they show up. If they are shown after a line in the preview, they are associated with that line.

## Creating Flows

More text can be added to a choice by placing it "under" each.

Consider the following code:

```ink
* Choose to Write More
Look! I am writing more!
* Give up on a New Project
Nope. I have given up writing in Ink!
```

Add the same new lines under each choice and then restart the project.

This time, choose the "Give up on a New Project" option. Now, not only will the text of the choice show up, but so will the text "underneath" it as well! The same is also true of the other choice if the story is restarted and the other option picked instead.

### Styling Choice Output

To avoid confusion, the common style when adding text to the output of a choice is to indent it. Pressing the TAB key or using two spaces between the edge of the editor and the content of the choice is the preferred way of showing that certain text is associated with a choice.

```ink
* Choose to Write More
    Look! I am writing more!
* Give up on a New Project
    Nope. I have given up writing in Ink!
```

This styling approach also extends to multiple levels of choice output. If one choice is "under" another, the amount of indentation would continue. It is not uncommon, in larger projects, to see many different levels of indentation, each signaling various choices and their output all coexisting at once.

### Adding More Choices

Adding an additional choices to the existing code is as easy as including extra asterisks and then more text of the choice option for the user.

```ink
* Choose to Write More
    Look! I am writing more!
    ** Do I continue?
        Yes, I do!
* Give up on a New Project
    Nope. I have given up writing in Ink!
```

Like with the indentation, additional asterisks for choices mark that some are also "under" others. Enter the above code into the project or otherwise add a new choice option under one of the first ones.

Restart the story.

Following the above code, one path through the story is to click on "Choose to Write More" and then "Do I continue?" before the story finally ends.

It has two *choices*, one *weave*, and two possible *flows* composed of the paths through the project!

## Try It

Create a new Ink project called “FirstStory.ink” and save the file. In the code area, add the following:

```ink
You stand before a cave entrance. There are three passages forward.
```

This will be a cave exploration example with two initial choices.

Copy or type the following code for the first set of choices:

```ink
* Go Deeper
* Retreat
```

Under the choice *Go Deeper*, add the following text:

```ink
    It gets very dark quickly.
        ** Do you keep going?
            You keep going and going into the cave. You believe you see some light and head towards it as the darkness recedes.

            You see what looks like an exit from the cave.

            You take it and find yourself emerging into a forest.
```

Now, as the player enters the save, they are given a choice that leads to another. The flow is a path from one to another, but there is only ever one choice per set.

**Example:**

```ink
You stand before a cave entrance.

* Go Deeper
    It gets very dark quickly.
        ** Do you keep going?
            You keep going and going into the cave. You believe you see some light and head towards it as the darkness recedes.

            You see what looks like an exit from the cave.

            You take it and find yourself emerging into a forest.
* Retreat
  You leave the cave.
```
