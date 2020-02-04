Chapter 3: Writing Your First Ink Story

Ink uses different terms for common elements of a story such as Weave, Flow, and Divert. Understanding these terms and their relationships to each other can help in writing code in Ink.

In this chapter, some common terms will be reviewed and the basics of writing and using the Preview pane in the Inky editor will be explained.

Common Terms

Every programming language has its own terms for its elements. Ink is no different and explains how to write and understand code in relationship to a project through the following terms:

Flow: The entire code of a project
Choice: Some text a user interacts with in order to progress the story
Weave: Collection of gather points and branching paths 

When a project is created using Ink, it has a Flow. This is all of the code of the project. Moving between Knots uses Diverts.

The entirely of all possible choices with a project is its Weave.

Creating a New Project and Flow

Using the Inky editor, go to File → New Project to create a new project. In the editor pane, write the following:

Hello, beautiful!

[Image of above text in Inky Editor]

After text has been added to the Flow of a project, the Preview pane shows it. This updates every time there is a pause in the typing.

Underneath the previous text, add the following:

* Choose to Write More
* Give up on a New Project

[Image of all text in the editor pane]

Choices will be covered more in the next chapter, but they are the basic building block of any Ink project. They are what a user interacts with when playing an Ink game and how the other terms, Knot, Divert, Stitch, and Weave all relate to each other within the Flow of an Ink project.

[Image of Preview pane with Rewind and Restart buttons]

Through adding Choices to a Flow, the preview pane in Inky can be used to “choose” and then rewind or restart a story. When working with the Inky Editor, this can help in moving through a story’s Weave and how different parts of its Flow relate to each other and if more or less Choices should be added.

Playing with Preview

Testing a project in the Inky Editor is one of the most important aspects of using it. Based on the example now written in the editor, its different choices and their outcomes can be examined in turn.

[Image of Preview Pane with current code shown and no choice taken]

First, click on the “Choose to Write More” choice. In the right-hand side, it will be shown and then the End of Story text will be shown.

Whenever a story ends, the “End of Story” text is shown in the Inky Editor. This signals that there is no more content in the story.

Click the “Restart” button in the Inky Editor. It is the double-arrow, rightmost icon above the Preview Pane area. This will restart the story back before any choices were made.

This time, click on the “Give up on a New Project” choice. Notice that it too will be shown and then the same “End of Story” text is shown. 

Right now, these two choices do not do much. Clicking on either will choose that option and then end the story right there.

## Comments

So far, only code has been added to Ink projects. There is also another type of text that can be added that helps with understanding how code works: comments.

In programming terminology, a comment is some bit of text that is included in code but is ignored by the computer itself. A comment is some text for another author or as a reminder of how something works. Comments can also simply be used as notes to help keep track of things in a project as an author works on it.

Comments in Ink are added through using two forward slashes, `//`. Anything that follows the slashes until the next line is considered a new comment. This also includes adding comments on lines after code as well. Anything from the two slashes to the end of the line is a comment and ignored by Ink.

```
// These are all comments.
// Ink skips over anything written with two forward-slashes

Hello! // Comments can also be written after code, too!
```

## Adding to Choices

More text can be added to a choice by placing it "under" the choice. 

Consider the following code:

```
* Choose to Write More
Look! I am writing more!
* Give up on a New Project
Nope. I have given up writing in Ink!
```

Add the same new lines under each choice and then restart the project. 

This time, choose the "Give up on a New Project" option. Now, not only will the text of the choice show up, but so will the text "underneath" it as well! The same is also true of the other choice if the story is restarted and the other option picked instead.

## Styling Choice Output

To avoid confusion, the common style when adding text to the output of a choice is to indent it. Pressing the TAB key or using a consistent several spaces between the edge of the editor and the content of the choice is the preferred way of showing that certain text is associated with a choice.

```
* Choose to Write More
    Look! I am writing more!
* Give up on a New Project
    Nope. I have given up writing in Ink!
```

This styling approach also extends to multiple levels of choice output. If one choice is "under" another, the amount of indentation would continue. It is not uncommon, in larger projects, to seeing many different levels of indentation, each signaling different choices and their output all coexisting at once.

## Adding More Choices

Working with indentation and being able to read between and around choices in Ink is an important skill. Adding an additional choice to the existing code is as easy as including extra asterisks and then the text of the choice option for the user.

```
* Choose to Write More
    Look! I am writing more!
    ** Do I continue?
        Yes, I do!
* Give up on a New Project
    Nope. I have given up writing in Ink!
```

Like the indentation, additional asterisks for choices mark that some are also "under" others. Enter the above code into the project or otherwise add a new choice option under one of the first ones. Restart the story.

Following the above code, one path through the story is to click on "Choose to Write More" and then "Do I continue?" before the story finally ends.

## Try it!

Create a new Ink project called “FirstStory.ink” and save the file. In the code area, add the following:

`You stand before a cave entrance. There are three passages forward.`

This will be a cave exploration example. There will be two initial choices of passages that will expand out into different areas. At each, the player will have the choice to retreat back the way they came in the cave.

Write the following code for the first set of choices:

```
* Go North
* Go South
* Go East
```

For each new path, there will be two choices. The first will allow the player to continue and the second will allow them to retreat from the cave.

Let’s look at the first choice and its branches:

```
* Go North
    It gets very dark quickly.
    ** Do you continue onward?
        You walk into the darkness. You reach out your hand to the wall and trace it into the utter darkness.
        *** Do you keep going?
            You keep going and going into the cave. You believe you see some light and head towards it as the darkness recedes.
            
            You see what looks like an exit from the cave.
            
            You take it and find yourself emerging into a forest.
            -> DONE
        *** Retreat
            -> DONE
    ** Retreat
        You have had enough and leave the cave the way you came.
        -> DONE
```

What’s with the arrow?

As will be covered in the next chapter, the arrow is a *Divert*. It is a way to move between different sections of a story. In this example, it is used to direct the story to move to its end, DONE. Any time a player selects, the Retreat option, it ends the current story.

Let’s now consider the next set of choices and their branches.

```
* Go South
    You make it 10 minutes into the cave and realize there is nothing but a deadend.
    -> DONE
```

This set ends very quickly.

The final set, however, expands outward into other branches.

```
* Go East
    You make your way through some moss and the occasional small trickle of water.
    ** Do you continue deeper?
        You make your way deeper into the cave system and find an underground lake. Peering at it, you see something shiny under the water.
        *** Do you dive into the water?
            You dive into the water and try to get closer.
            
            You go deeper and deeper, trying to make your way.
            
            Finally, you reach out and grab the item. You pick up a sword.
            
            You swim to the surface.
        *** Retreat
            -> DONE
    ** Retreat
        -> DONE
```

Through using multiple levels of indentation and asterisks, choices were added under others, creating a branching structure that started with three and then moved outward. A Divert was introduced as a way to quickly collapse certain paths to prevent the story from becoming too complex.

**Full Example:**

```
You stand before a cave entrance. There are three passages forward.

* Go North
    It gets very dark quickly.
    ** Do you continue onward?
        You walk into the darkness. You reach out your hand to the wall and trace it into the utter darkness.
        *** Do you keep going?
            You keep going and going into the cave. You believe you see some light and head towards it as the darkness recedes.
            
            You see what looks like an exit from the cave.
            
            You take it and find yourself emerging into a forest.
            -> DONE
        *** Retreat
            -> DONE
    ** Retreat
        You have had enough and leave the cave the way you came.
        -> DONE
* Go South
    You make it 10 minutes into the cave and realize there is nothing but a deadend.
    -> DONE
* Go East
    You make your way through some moss and the occasional small trickle of water.
    ** Do you continue deeper?
        You make your way deeper into the cave system and find an underground lake. Peering at it, you see something shiny under the water.
        *** Do you dive into the water?
            You dive into the water and try to get closer.
            
            You go deeper and deeper, trying to make your way.
            
            Finally, you reach out and grab the item. You pick up a sword.
            
            You swim to the surface.
        *** Retreat
            -> DONE
    ** Retreat
        -> DONE
```


