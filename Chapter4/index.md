# Chapter 4: Understanding Choices

- [Chapter 4: Understanding Choices](#chapter-4-understanding-choices)
  - [Making Choices](#making-choices)
    - [Set Structure](#set-structure)
    - [Set Code Example](#set-code-example)
  - [Selective Output](#selective-output)
    - [Selective Output Code Example](#selective-output-code-example)
  - [Knots](#knots)
    - [**DONE** and **END**](#done-and-end)
      - [**DONE**](#done)
      - [**END**](#end)
    - [Diverts](#diverts)
    - [Diverting to **DONE** and **END**](#diverting-to-done-and-end)
    - [Knot Code Example](#knot-code-example)
  - [Revisiting Flow](#revisiting-flow)
  - [Loops with Knots](#loops-with-knots)
    - [Avoiding Infinite Looping](#avoiding-infinite-looping)
  - [Sticky Choices](#sticky-choices)
    - [Sticky Choice Code Example](#sticky-choice-code-example)
  - [Glue](#glue)
  - [Try It](#try-it)

**Summary:** In this chapter, you will learn about choices, diverts, and their different patterns in Ink.

---

## Making Choices

Agency is at the center of how games are played. If a player feels like their decisions matter, they will invest in the story more. Presenting ways a player can choose is central to making an engaging story and Ink project.

The ability to choose a path through a story’s weave is core to how Ink works. By showing the user different options, they can pick one and then follow different paths through the story.

Choices are created with the asterisk, `*`. When a line starts with this symbol, it becomes a choice for the player. When multiple are used, they are all options in that set.

**Set:** A *set of choices* are all choices at its current level. These choices with the same number of asterisks, `*`, within that section of the story.

```ink
* First Choice
* Second Choice
```

When used in a flow, Inky will present the choices in the middle of the Preview pane.

Multiple uses of the `*` symbols signal new levels (sets) of choices. A single `*` symbol is the first and more `*` symbols signal that those choices lead to more.

```ink
* First Choice
** Sub-Choice
*** Sub-sub Choice
```

When one option leads to others, those will be shown after the content of the first one in the Preview Pane.

### Set Structure

Consider how, in the previous chapter's **Try It** example, multiple levels were indented and asterisks were used to create flows through the example.

The first set started with the choice to *Go North*.

Inside that was also a single choice: *Do you continue onward?*.

Inside that were two choices in a single set: *Do you keep going?* and *Retreat*.

Their structure was the following:

```ink
* Go North
  ** Do you continue onward?
    *** Do you keep going?
    *** Retreat
```

### Set Code Example

```ink
* Go North
    It gets very dark quickly.
    ** Do you continue onward?
        You walk into the darkness. You reach out your hand to the wall and trace it into the utter darkness.
        *** Do you keep going?
            You keep going into the cave. You believe you see some light and head towards it as the darkness recedes.

            You see what looks like an exit from the cave.

            You take it and find yourself emerging into a forest.
            -> DONE
        *** Retreat
            -> DONE
```

---

## Selective Output

When brackets are used within a choice, it is only shown in the choice itself. It is not part of the output. This is known as *selective output*.

```ink
* [Sneak in]
```

This can be combined with other text in the option to show one part in the option (what the player clicks) and other in the result of the action.

Any text not in brackets will be shown in the output.

### Selective Output Code Example

Normally, the text of the choice is shown. With selective output, however, the tone of a choice rather than its exact words can be shown to the user. This could allow a player to choose how they want to respond without directly showing any extended output as part of the choice.

Consider the following example where selective output is used to remove the text of the choices while also presenting its emotional tone instead.

```ink
The general rejects your advances and pulls a pistol. "I don't know who you are, but you are not welcome here. Leave now!"

How do you respond?

* [Mad]
    You get angry with the general and also pull a pistol. "Don't you know who I am!?" you scream and you aim your pistol.
* [Flirty]
    "Come on, general. You don't want to shoot me," you say, cupping the pistol and slowly moving your hands down it.
```

---

## Knots

A *Knot* is a selection of content. They are created through using two or more equal signs (`=`) and the name of the knot. Optionally, and more commonly, they are also closed with three equal signs (`===`).

```ink
=== ConfrontCaptain ===
```

> **Note:** The name of a knot cannot contain spaces or other special characters, but they can use the underscore in their names.

### **DONE** and **END**

Ink reserves two knot names that cannot be used in a story. These are **DONE** and **END**. In Ink, these carry special meaning.

#### **DONE**

The **DONE** knot signals that a knot, stitch, or thread is done. In other words, if there is a point where a dead end would have happened, the knot **DONE** can be used to close off that dead end.

If there is no more content in a story, **DONE** also ends the story itself.

#### **END**

The knot **END** signals that the story should stop. It can be used to close off a complicated flow or to end a story in a certain location after a player reaches a natural end of a story.

Unlike **DONE** where a section comes to a close, **END**, as its name implies, *ends* the story.

### Diverts

Moving between knots is done through a *divert*. In Ink, this is an arrow, `->` that "points at" the Knot to move to next.

Simply creating knots is not enough. Knots **must not create dead ends in Ink**. At a minimum, a knot must divert to a specially-named knot called "DONE" to complete it.

```ink
-> Next
=== Next ===
The end!
-> DONE
```

Combined with brackets for choices, the output of an option can be placed in knots.

### Diverting to **DONE** and **END**

As was mentioned above, the knots **DONE** and **END** have special meanings. When a knot diverts to **DONE**, `-> DONE`, it marks that the knot is done. (If there is no more content, this also serves to end the story.)

```ink
There is no more content here. It's time to end this story!
-> The_End

=== The_End ===
Yup, this is end!
-> DONE
```

If code diverts to **END**, `-> END`, it ends the story.

Both can be used to prevent dead ends in the flow of a story and to create natural points where a story can move to another section or come to an end.

### Knot Code Example

Knots provide an easy way to divide up a project into logical sections. For example, consider the following code where a knot is used to contain a set of choices:

```ink
The first-mate leans against the edge of the pier and looks out across the water.

"Everything is all set," they say, turning away from the rising run across the water to look at you. "We can set sail at any time."

You look over your ship and its crew. Yes, it is time to set out again.

-> Sailing

=== Sailing ===
* Pirate Island
    -> DONE
* Port Anderson
    -> DONE
```

---

## Revisiting Flow

Diverts, as their name implies, *diverts* a story to a knot in the story. As was introduced in the previous chapter, a *flow* is a player's journey through all possible choices (the story's *weave*).

In the above example, the first divert `-> Sailing` moves the story to its knot, **Sailing**. Inside this knots is a set of choices, *Pirate Island* and *Port Anderson*.

One possible flow through this story would start with the knot **Sailing** and then follow one of its choices (*Pirate Island* and *Port Anderson*).

```ink
-> Sailing
  * Pirate Island
    -> DONE
  * Port Anderson
    -> DONE
```

As neither choice has content yet, and diverts cannot have dead ends, they also each contain a divert, `-> DONE` that ends the story.

---

## Loops with Knots

With both Knots and Diverts, a loop can be created where an option has a Divert that points to a Knot containing the original choice.

```ink
-> Next
== Next ==
+ [This is next!]
    -> Next
```

With a single choice within the set "pointing to" a DONE label, the others can be used to loop by diverting to the knot holding the choice.

### Avoiding Infinite Looping

When using knots and diverts to create a looping structure, it is important to include both choices and a way to break out of loop somehow.

A very common mistake when writing a looping pattern of knots and diverts is to not include a choice and have the Inky Editor become unresponsive when it tries to follow the divert back to the knot over and over.

**Bad Example:**

```ink
-> Next
== Next ==
-> Next
```

**Example:**

The use of a Divert to point to a Knot allows for looping back to a single knot within the story. Instead of moving between them, a single Knot can serve as the central "hub" for choices. Consider the following code:

```ink
Assassin! You watch the woman as she inches closer to you. As you move the candle to get a better look, her sword reflects its light back to you.

-> Escape

== Escape ==
* [Try to fight her]
    You know there is no way you can win against her. You are just a monk and barely trained
    -> Escape
* [Run the other way]
    This seems like the best option. You take off running.
    -> DONE
* [Throw your candle at her]
    If you throw your candle, it could go out and you can barely see as it is.
    -> Escape
```

As the divert points back at the knot, multiple choices can be made. Yet, as the number of options reduce, the final one must, at some point, be picked in order to progress the story.

---

## Sticky Choices

By default, an option will remove itself once chosen. As designed, a choice is a one-time event. It is chosen and the others in the set are ignored. However, choices can become "sticky" through using the plus `+` symbol. Instead of being removed, these choices will "stick around."

```ink
+ This sticks around!
* This does not!
```

### Sticky Choice Code Example

Normally, choices disappear after they are "used." Sticky choices, on the other hand, do not. As it comes to looping knots and those cases where revisiting a particular knot is the case, sticky choices can be very useful.

```ink
You awake on the shore. As the waves lap at you, your memory tries to fills itself back in from the night before and how you came to be here. There was a storm, yes. A mighty storm. And then... well, you are not as sure. Something about a storm, for sure.

-> Explore_the_Island

=== Explore_the_Island ===
+ [Drink Water]
    You drink some water from a stream in the forest.
    -> Explore_the_Island
+ [Hunt for Food]
    You find some small berries and roots.
    -> Explore_the_Island
* [Try to Sleep]
    You try to find a good place to take a nap. As you sleep, your mind fills in the pieces. There was a storm, yes, but before that there was a murder.

    You remember two shots ringing out during the rain. There was screaming.

    You wake up with the sun bearing down on you. Time has passed. You dust yourself off and try to make a fire before it gets too dark.
    -> DONE
```

---

## Glue

The default action is for each new line of text to have its own new line in the output. However, this can be changed using *glue*, a pairing of less-than and greater-than signs, `<>`.

```ink
This text <>
run together <>
as the same line.
```

When working with diverts and knots, glue can be helpful to run text together across them, linking the text even if the story is broken up into different parts.

```ink
This text <>
-> Next

== Next ==
runs together <>
-> Final

== Final ==
as the same line.
-> DONE
```

---

## Try It

As seen in this chapter’s examples, it is easy to create a complex branching story using a combination of choices, knots, and diverts. These basic building blocks of Ink will form the backbone of most stories you create. Practicing with these kinds of Ink code will help you get used to how Ink works and will also prepare you for some of the more advanced content found in later chapters of this book.

As practice, try doing the following:

First, create a simple branching story that uses choices, knots, and diverts.

The story should have at least two choices, and player should have a set of at least two options within each of those two choices. The story should use at least two diverts, and those diverts should go to two different knots.

You should pay attention to the narrative content of your story as you write, but don’t worry about the length of the story: focus more on creating the necessary Ink code to tell a short story that makes sense.

Now, revise your story: make at least one of the options inside of one of your two choices use selective output. Introduce at least one loop using a knot into the story and use a sticky choice inside it so that it works properly - but be sure it isn’t an infinite loop!

While modifying the story you created may be a challenge because you have to rewrite some of the story content, think about ways you can change the narrative you created to include that kind of content instead of creating a new story from scratch.

Finally, revise your story again: add at least two conditional choices to the story. Make one of those into an advanced choice. Once you have done so, check the story for consistency: make sure the narrative still makes sense! You might also want to have someone else play through it to see if there are problems that you have not caught on your own.
