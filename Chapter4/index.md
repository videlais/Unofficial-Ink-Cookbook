# Chapter 4: Understanding Choices

- [Chapter 4: Understanding Choices](#chapter-4-understanding-choices)
  - [Making Choices](#making-choices)
  - [Selective Output](#selective-output)
  - [Knots](#knots)
  - [Loops with Knots](#loops-with-knots)
    - [Avoiding Infinite Looping](#avoiding-infinite-looping)
  - [Sticky Choices](#sticky-choices)
  - [Conditional Choices](#conditional-choices)
    - [Multiple Conditionals](#multiple-conditionals)
    - [Advanced Choices](#advanced-choices)
  - [Glue](#glue)
  - [Try It](#try-it)

**Summary:** In this chapter, you will learn about Choices and their different types in Ink.

## Making Choices

Agency is at the center of how games are played. If a player feels like their decisions matter, they will invest in the story more. Presenting ways a player can "choose" is central to making an engaging story and Ink project.

The ability to choose a path through a story’s Weave is core to how Ink works. By showing the user different options, they can pick one and then follow different paths through the story..

Choices are created with the asterisk, `*`. When a line starts with this symbol, it becomes a choice for the player. When multiple are used, they are all options in that set.

```ink
* First Choice
* Second Choice
```

When used in a Flow, Inky will present the choices in the middle of the Preview pane.

Multiple uses of the `*` symbols signal new levels (sets) of choices. A single `*` symbol is the first and more `*` symbols signal that those choices lead to more.

```ink
* First Choice
** Sub-Choice
*** Sub-sub Choice
```

When one option leads to others, those will be shown after the content of the first one in the Preview Pane.

**Example:**

Consider how, in the previous chapter example, multiple levels were indented and multiple asterisks were used to create multiple paths through the example.

```ink
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
```

## Selective Output

When brackets are used within a choice, it is only shown in the choice itself. It is not part of the output.

```ink
* [Sneak in]
```

This can be combined with other text in the option to show one part in the choice (what the player clicks) and other in the result of the action.

Any text not in brackets will be shown in the output.

**Example:**

Normally, the text of the choice is shown. With selective output, however, the tone of a choice rather than its exact words can be shown to the user.

Consider the following example where selective output is used to remove the text of the choices while also presenting its emotional tone instead.

```ink
The general rejects your advances and pulls a pistol. "I don't know who you are, but you are not welcome here. Leave now!"

How do you respond?

* [Mad]
    You get angry with the general and also pull a pistol. "Don't you know who I am!?" you scream and you aim your pistol.
* [Flirty]
    "Come on, general. You don't want to shoot me," you say, cupping the pistol and slowly moving your hands down it.
```

## Knots

A *Knot* is a selection of content. They are created through using two or more equal signs (`=`) and the name of the knot. Optionally, and more commonly, they are also closed with three equal signs (`===`).

**Note:** The name of a knot cannot contain spaces or other special characters, but they can use the underscore in their names.

Moving between knots is done through a *Divert*. In Ink, this is an arrow, `->` that "points at" the Knot to move to next.

Simply creating knots is not enough. Knots **must not create dead ends in Ink**. At a minimum, a knot must divert to a specially-named label called "DONE" to complete it.

```ink
== Next ==
The end!
-> DONE
```

Combined with brackets for choices, the output of an option can be placed in knots.

**Example:**

Knots provide an easy way to define sections of a project into logical sections. For example, consider the following code where Knots are used as places:

```ink
The first-mate leans against the edge of the pier and looks out across the water. "Everything is all set," they say, turning away from the rising run across the water to look at you. "We can set sail at any time."

You look over at your ship and its crew. It is time to set out again.

-> Sailing

=== Sailing ===
* Port Delogue
    -> DONE
* Port Anderton
    -> DONE
```

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

When using knots and diverts to create a looping structure, it is important to include both choices and a way to break out of loop somehow. A very common mistake when writing a looping pattern of knots and diverts is to not include a choice and have the Inky Editor become unresponsive when it tries to follow the divert back to the knot over and over.

**Example:**

The use of a Divert to point to a Knot allows for looping back to a single knot within the story. Instead of moving between them, a single Knot can serve as the central "hub" for choices. Consider the following code:

```ink
Assassin! You watched the woman as she moved closer to you. As you move the candle you hold downward to get a better look, her sword reflects its light back to you.

-> Escape

== Escape ==
* [Try to fight her]
    You know there is no way you can win against here. You are just a monk and barely trained
    -> Escape
* [Run the other way]
    This seems like the best option. You take off running.
    -> DONE
* [Throw your candle at her]
    If you throw your candle, it could go out and you can barely see as it is.
    -> Escape
```

As the divert points back at the knot, multiple choices can be made. Yet, as the number of options reduce, the final one must, at some point, be picked in order to progress the story.

## Sticky Choices

```ink
+ This sticks around!
* This does not!
```

By default, an option will remove itself once chosen. As designed, a choice is a one-time event. It is chosen and the others in the set are ignored. However, choices can become "sticky" through using the plus `+` symbol. Instead of being removed, these choices will "stick around."

**Example:**

Normally, choices disappear after they are "used." Sticky choices, on the other hand, do not. As it comes to looping knots and those cases where revisiting a particular knot is the case, sticky choices can be very useful.

```ink
You awake on the shore. As the waves lap at you, your memory tries to fills itself back in from the night before and how you came to be here. There was a storm, yes. A might storm. And then... well, you are not as sure. Something about a storm, for sure.

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

## Conditional Choices

Combining diverts and knots, choices can also be conditionally shown. Because Knots have unique names, code can check if they have been visited or not. When placed in curly brackets, `{}`, the choice will show the text or not based on the name of the knot.

### Multiple Conditionals

Conditionals checking if a knot has been visited can also be used together, checking if the player has seen (or not) a set of different knots.

These can create a series of choices that have to be progressed through in order to continue, looping back and checking if other knots have been seen yet or not.

### Advanced Choices

Knot labels are not strictly Boolean (true or false) values. They are actually integers (numbers) and a count of how many times the player has seen the knot.

```ink
-> Pizza_Choices
=== Pizza_Choices ===
+ [Pizza?]
    -> Pizza
+ {Pizza > 0} [Salad?]
    We picked salad.
    -> DONE

=== Pizza ===
He shook his head. "I don't like pizza."
-> Pizza_Choices
```

Testing if the value of the knot label is less than one is the same as testing if it has not been seen yet. If it has been seen multiple times, the value will be higher.

Testing for multiple values allows for repeating the loop between choices and knots, allowing for the same choice to be chosen and the outcome changing when repeated.

## Glue

The default act is for each new line of text to have its own new line in the output. However, this can be changed using glue, a pairing of less-than and greater-than signs.

```ink
This text <>
run together <>
as the same line.
```

When working with diverts and knots, glue can be helpful to run text together.

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

**Example:**

The different uses of conditional choices can be combined together to keep track of if a Knot has been visited or not. Using the ability to know if a knots has been visited multiple times or not, choices can be revealed if other choices were first exhausted.

```ink
It was our first date and we hadn't made dinner plans.

He turned to me. "What should we eat?"

-> Pizza_Choices

=== Pizza_Choices ===
+ {Pizza < 1} [Pizza?]
    -> Pizza
+ {Pizza} {Salad < 1} [Salad?]
    -> Salad
+ {Pizza} {Salad} {Nothing < 2} [Nothing?]
    -> Nothing
+ {Pizza} {Salad} {Nothing} [Sushi?]
    -> Sushi

=== Pizza ===
He shook his head. "I don't like pizza."
-> Pizza_Choices

=== Sushi ===
"Sushi sounds good!"
-> DONE

=== Salad ===
"Not a salad."
-> Pizza_Choices

=== Nothing ===
{"We have to eat something!"|"Stop being silly!"}
-> Pizza_Choices
```

## Try It

As seen in this chapter’s examples, it is easy to create a complex branching story using a combination of choices, knots, and diverts. These basic building blocks of Ink will form the backbone of most stories you create. Practicing with these kinds of Ink code will help you get used to how Ink works and will also prepare you for some of the more advanced content found in later chapters of this book.

As practice, try doing the following:

First, create a simple branching story that uses choices, knots, and diverts. The story should have at least two choices, and player should have a set of at least two options within each of those two choices. The story should use at least two diverts, and those diverts should go to two different knots. You should pay attention to the narrative content of your story as you write, but don’t worry about the length of the story: focus more on creating the necessary Ink code to tell a short story that makes sense.

Now, revise your story: make at least one of the options inside of one of your two choices use selective output. Introduce at least one loop using a knot into the story and use a sticky choice inside it so that it works properly - but be sure it isn’t an infinite loop! While modifying the story you created may be a challenge because you have to rewrite some of the story content, think about ways you can change the narrative you created to include that kind of content instead of creating a new story from scratch.

Finally, revise your story again: add at least two conditional choices to the story. Make one of those into an advanced choice. Once you have done so, check the story for consistency: make sure the narrative still makes sense! You might also want to have someone else play through it to see if there are problems that you have not caught on your own.
