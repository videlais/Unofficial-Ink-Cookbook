---
title: "Diverts and Knots"
order: 2
chapter_number: 2
layout: chapter
---

## Chapter Summary

In this chapter, you will learn about knots, diverts, stitches, and how weaves affect the flow of complex, non-linear stories. Building on Chapter 1's foundation of choices and weaves, you'll discover how to organize stories into reusable sections, create loops and explorable spaces, and build sophisticated narrative structures that go beyond simple branching.

## Learning Objectives

By the end of this chapter, you will be able to:

- Design knots and diverts to organize story structure.
- Differentiate between regular choices and sticky choices.
- Construct looping patterns while avoiding infinite loops.

## Table of Contents

- [Chapter Summary](#chapter-summary)
- [Learning Objectives](#learning-objectives)
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Making Choices](#making-choices)
- [Section of a Story](#section-of-a-story)
  - [Code Example 2.1: Introducing Knots](#code-example-21-introducing-knots)
- [Diverts and Knots](#diverts-and-knots)
  - [Code Example 2.2: Using Knots](#code-example-22-using-knots)
  - [Interactive Example 2.2: Using Knots](#interactive-example-22-using-knots)
- [Using DONE and END](#using-done-and-end)
  - [Code Example 2.3: Using DONE](#code-example-23-using-done)
  - [Interactive Example 2.3: Using DONE](#interactive-example-23-using-done)
- [Loops with Knots](#loops-with-knots)
  - [Code Example 2.4: Creating loops](#code-example-24-creating-loops)
  - [Interactive Example 2.4: Creating Loops](#interactive-example-24-creating-loops)
- [Using Choices and Sticky Choices](#using-choices-and-sticky-choices)
  - [Code Example 2.5: Sticky Loops](#code-example-25-sticky-loops)
  - [Interactive Example 2.5: Sticky Loops](#interactive-example-25-sticky-loops)
- [Avoiding Infinite Looping](#avoiding-infinite-looping)
  - [Code Example 2.6: Longer Loops](#code-example-26-longer-loops)
  - [Interactive Example 2.6: Longer Loops](#interactive-example-26-longer-loops)
  - [Code Example 2.7: Island Adventures](#code-example-27-island-adventures)
  - [Interactive Example 2.7: Island Adventures](#interactive-example-27-island-adventures)
- [Stitches](#stitches)
  - [Code Example 2.8: Introducing Stitches](#code-example-28-introducing-stitches)
  - [Interactive Example 2.8: Introducing Stitches](#interactive-example-28-introducing-stitches)
  - [Addressing Stitches](#addressing-stitches)
  - [Code Example 2.9: Navigating Between Stitches](#code-example-29-navigating-between-stitches)
  - [Interactive Example 2.9: Navigating Between Stitches](#interactive-example-29-navigating-between-stitches)
  - [Combining Stitches with Sticky Choices](#combining-stitches-with-sticky-choices)
  - [Code Example 2.10: Stitches with Sticky Choices](#code-example-210-stitches-with-sticky-choices)
  - [Interactive Example 2.10: Stitches with Sticky Choices](#interactive-example-210-stitches-with-sticky-choices)
- [Summary](#summary)
- [Review Questions](#review-questions)
- [Try It](#try-it)

---

## Introduction

In Chapter 1, you learned the fundamental building blocks of ink: flow, choices, weaves, and gathering points. These concepts allow you to create branching narratives where players make choices and experience different paths through your story.

However, all the stories we created in Chapter 1 were fundamentally *linear*—they flowed from beginning to end in one direction. Even with multiple branches, once a player made a choice, they continued forward and never returned to previous sections.

In this chapter, you'll learn how to create truly *non-linear* stories where players can revisit locations, explore hubs with multiple destinations, and experience story sections in different orders. You'll discover how to organize your story into reusable sections called **knots**, navigate between them using **diverts**, and create even smaller subsections called **stitches**.

These tools will allow you to build complex interactive narratives like exploration games, conversation systems, and location-based stories where player agency truly matters.

> **Note** If an interactive example does not load, you can view the [source code]({{ site.baseurl }}/_examples/chapter02/) directly. Use Tab and Enter keys to navigate choices in the interactive examples.

---

## Making Choices

Agency is at the center of how games are played. If a player feels like their decisions matter, they will invest in the story more. Presenting ways a player can choose is central to making an engaging story and ink project.

The ability to choose a path through a story's weave is core to how ink works. By showing the user different options, they can pick one and then follow different paths through the story.

In [Chapter 1]({{ site.baseurl }}/chapters/01/index), we reviewed how to use choices and create weaves. We also saw how gathering points can be used to "collapse" complex structures back to a single point, even across levels of a complex weave.

What is missing is how to create non-linear structures. We have seen how to branch a story, but these branches, using choices, are still fundamentally linear in nature.

## Section of a Story

Let's consider a simple example. In a longer story including merchants, a player may want to re-visit the same location multiple times. In what we know so far, we would need to copy and paste the same code to re-create this for the player.

In ink, there is an easier way. We can define sections of a story, named **knots**, and then visit them as needed. This allows us to re-use sections and also create a non-linear structure at the same time.

> **Note** The term "knot" comes from thinking about story structure as threads that weave together and tie off at specific points. A knot represents a significant location, scene, or moment in your narrative.

To create a **knot**, we begin a line with at least two equal signs, `==`, and then the name of the section.

> **Warning** In ink, the name of a knot cannot contain spaces. We can use letters, numbers, and the underscore, but no spaces. Use descriptive names like `merchants_shop` or `Chapter_3` instead of `merchants shop`.

While the use of a knot begins with two equal signs, `==`, many authors find it helpful to add more after the name of the knot on the same line. This is allowed in ink.

> **Tip** To help with readability, some authors add equal signs after the name of the knot as well. This approach would transform `== merchants_shop` into `== merchants_shop ==`, which might be easier to identify when scanning longer projects for particular knots.


### Code Example 2.1: Introducing Knots

```ink
This story has multiple sections.

== Section_1

== Section_2

== Section_3
```

While it may seem correct, **Example 2.1** has a major issue: the flow runs out!

Every section of a story, a knot, must also have an available path to an end.

To resolve this problem, we need another concept, a **divert**.

## Diverts and Knots

To move to a knot in ink, we use a **divert**, a combination of a hyphen and the greater-than sign, `->`. This combination "points" to some location in the story.

> **Tip** Think of a divert as a "go to" command. The arrow `->` literally points to where the story should flow next. This makes your code more readable—you can see the story's path just by following the arrows.

To fix the code in *Example 2.1*, we need to add diverts to not only access the knots themselves but to move out of them.

For this common issue, of needing to divert out of a knot, there is a special knot for this, `END`.

Updating the previous code, we can add diverts to move between the knots and finally end with `END`.

### Code Example 2.2: Using Knots

```ink
This story has multiple sections.
-> Section_1

== Section_1
This is section 1!
-> Section_2

== Section_2
This is section 2!
-> Section_3

== Section_3
This is section 3!
-> END
```

### Interactive Example 2.2: Using Knots

{% include ink-player.html
   story="chapter02/knots"
   title="Example: Using Knots"
   height="350px"
%}

## Using DONE and END

The special knot `END` *ends* the story. There is another special knot, `DONE`, for closing off of branches. In most cases, `END` and `DONE` will act the same.

> **Tip** Use `DONE` when you want to end a branch but might add more content later. Use `END` when you want to definitively end the entire story. While they function similarly, `DONE` signals "this branch is complete" while `END` signals "the story is over."

### Code Example 2.3: Using DONE

```ink
You find yourself at a crossroads in the forest.

* [Take the left path]
    You walk down the winding left path through dense trees. After a while, you reach a peaceful clearing with a small pond. You decide to rest here for the night.
    -> DONE

* [Take the right path]
    You follow the right path up a steep hill. At the top, you discover an abandoned watchtower. There's nothing more to explore here.
    -> DONE
```

### Interactive Example 2.3: Using DONE

{% include ink-player.html
   story="chapter02/crossroads"
   title="Example: Using DONE"
   height="350px"
%}

While the knots `DONE` and `END` can be helpful, if we want a non-linear or looping structures, we can re-visit knots.

## Loops with Knots

A loop can be created when one or more knots divert back to themselves.

> **Important** Loops are powerful but dangerous. Every loop needs an exit condition—a way for the player to break out and continue the story. Without an exit, you create an infinite loop that traps the player.

### Code Example 2.4: Creating loops

```ink
-> Next
== Next ==
* [This is next!]
  -> Next
```

### Interactive Example 2.4: Creating Loops

{% include ink-player.html
   story="chapter02/loops"
   title="Example: Creating Loops"
   height="350px"
%}

> **Note** Despite Example 2.4 seemingly looping back internally, the choice will disappear after its first usage.

When we introduce loops using diverts and knots, we can see a new issue. In *Example 2.4*, there is a loop, but there is also a problem: the choice is gone!

## Using Choices and Sticky Choices

Every choice in a weave is considered used up when it chosen. This makes story traversal, the movement across weaves, unique for a player.

There are also cases where we might want to "add back" a choice to a weave to help us in contexts where looping might happen. For those cases, ink has the concept of a **sticky choice**.

Normally, we use the asterisk, `*`, to create a choice from a line. We can also use the plus symbol, `+`, to create a choice. If used, it "adds back" the choice to the current weave after it has been chosen by a player.

> **Important** Regular choices (`*`) disappear after being selected. Sticky choices (`+`) remain available and can be selected multiple times. This distinction is crucial when designing loops and explorable spaces.

### Code Example 2.5: Sticky Loops

```ink
-> Next
== Next ==
+ [This is next!]
  -> Next
```

### Interactive Example 2.5: Sticky Loops

{% include ink-player.html
   story="chapter02/sticky"
   title="Example: Sticky Loops"
   height="350px"
%}

In the updated version of the previous *Example 2.4* in *Example 2.5*, the use of the sticky choice allows a player to continue to choose the same option, looping the story back to the same point.

When using loops, we need to be careful of accidentally creating an infinite loop.

## Avoiding Infinite Looping

When using knots and diverts to create a looping structure, it is important to include a choice to break the loop or divert to another knot in the story.

> **Warning** An infinite loop occurs when the story keeps cycling through the same content with no way to progress. Always test your loops to ensure players have a clear path forward.

Let's examine a longer example.

### Code Example 2.6: Longer Loops

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

### Interactive Example 2.6: Longer Loops

{% include ink-player.html
   story="chapter02/longer"
   title="Example: Longer Loops"
   height="350px"
%}

In *Example 2.6*, the choices are removed from the weave as they are chosen by the player. For two of the choices, they loop back to the same knot. If the player chooses the solution, "Run the other way", they are finally able to escape.

In this case, an infinite loop is prevented by guiding the player to the choice to progress the story while also creating suspense.

It is also possible to combine sticky and normal choices to allow some branches to loop while also providing an escape from an infinite loop.

Let's consider a different approach to the previous pattern using sticky choices:

### Code Example 2.7: Island Adventures

```ink
You awake on the shore. As the waves lap at you, your memory tries to fill itself back in from the night before and how you came to be here. There was a storm, yes. A mighty storm. And then... well, you are not as sure. Something about a storm, for sure.

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

### Interactive Example 2.7: Island Adventures

{% include ink-player.html
   story="chapter02/island"
   title="Example: Island Adventues"
   height="350px"
%}

In a similar approach to how *Example 2.6* used normal choices to eventually "force" the player to choose to leave the loop, *Example 2.7* provides sticky choices to allow them to stay longer. In this example, the use of sticky choices prolongs the loop while the single normal choice breaks it.

## Stitches

While knots allow us to organize our story into major sections, sometimes we need to break those sections into smaller, more manageable pieces. For this purpose, ink provides **stitches**.

A **stitch** is a sub-section within a knot. Think of knots as chapters in a book and stitches as sections within those chapters. Stitches help organize complex knots without creating entirely separate story sections.

To create a stitch, we use a single equals sign, `=`, followed by the stitch name. Stitches must be defined inside a knot and cannot exist on their own.

> **Important** Stitches belong to knots. You cannot create a stitch outside of a knot, and stitch names only need to be unique within their parent knot.

### Code Example 2.8: Introducing Stitches

```ink
You enter the castle.
-> Castle

== Castle ==
The grand hall stretches before you.

* [Explore the east wing]
    -> east_wing
* [Explore the west wing]
    -> west_wing

= east_wing
You walk down the eastern corridor. Portraits line the walls, their eyes seeming to follow you.
-> END

= west_wing
The western passage leads to the kitchen. The smell of fresh bread fills the air.
-> END
```

### Interactive Example 2.8: Introducing Stitches

{% include ink-player.html
   story="chapter02/stitches-basic"
   title="Example: Introducing Stitches"
   height="400px"
%}

### Addressing Stitches

To divert to a stitch, we use the knot name, followed by a period, then the stitch name: `-> KnotName.StitchName`. If you're already inside the knot, you can simply use the stitch name: `-> StitchName`.

> **Tip** When referencing a stitch from within the same knot, you can omit the knot name. This makes your code more readable and easier to maintain.

### Code Example 2.9: Navigating Between Stitches

```ink
You stand in the town square.
-> Town

== Town ==
= square
The fountain bubbles in the center of the square. Where do you want to go?

+ [Visit the market]
    -> market
+ [Visit the tavern]
    -> tavern
+ [Leave town]
    -> END

= market
The market is bustling with activity. Vendors call out their wares.

* [Buy some supplies]
    You purchase bread and water for your journey.
    -> square
* [Return to square]
    -> square

= tavern
The tavern is warm and inviting. A bard plays in the corner.

* [Order a drink]
    The innkeeper pours you a mug of ale.
    -> square
* [Return to square]
    -> square
```

### Interactive Example 2.9: Navigating Between Stitches

{% include ink-player.html
   story="chapter02/stitches-nav"
   title="Example: Navigating Between Stitches"
   height="450px"
%}

### Combining Stitches with Sticky Choices

Stitches work particularly well with sticky choices to create multiple locations where players can move between different areas.

### Code Example 2.10: Stitches with Sticky Choices

```ink
-> Museum

== Museum ==
= entrance
You're in the museum entrance hall. Glass cases display ancient artifacts.

+ [Examine the Egyptian exhibit]
    -> egyptian
+ [Examine the Greek exhibit]
    -> greek
+ [Visit the gift shop]
    -> gift_shop
* [Leave the museum]
    You exit the museum, satisfied with your visit.
    -> END

= egyptian
You study the hieroglyphics and golden masks. Fascinating!
-> entrance

= greek
Marble statues and pottery fragments tell stories of ancient gods.
-> entrance

= gift_shop
The gift shop sells postcards and replica artifacts.
-> entrance
```

### Interactive Example 2.10: Stitches with Sticky Choices

{% include ink-player.html
   story="chapter02/museum"
   title="Example: Stitches with Sticky Choices"
   height="450px"
%}

> **Note** In Example 2.10, the sticky choices (`+`) allow the player to explore different exhibits multiple times, while the regular choice (`*`) provides a way to exit. This is a common pattern for creating explorable spaces.

Stitches are powerful organizational tools that help keep your story code clean and manageable. They're especially useful when creating locations with multiple sub-locations or scenes with multiple actions.

---

## Summary

This chapter introduced the fundamental concepts for creating non-linear narratives in ink. You learned that **knots** are major sections of your story, defined with two or more equal signs (`==`), and that you can navigate between them using **diverts** (`->`).

You discovered the difference between `END` and `DONE`—both stop the flow, but `END` definitively ends the story while `DONE` closes off a branch. You also learned how to create **loops** by having knots divert back to themselves or each other, enabling players to revisit locations and content.

The distinction between **regular choices** (`*`) and **sticky choices** (`+`) is crucial for loop design. Regular choices disappear after selection, making each playthrough unique, while sticky choices remain available for repeated selection, perfect for explorable spaces.

You learned about the danger of **infinite loops** and how to prevent them by always providing an exit path. Examples showed how to combine regular and sticky choices to guide players toward story progression while still offering exploration.

Finally, you discovered **stitches**—subsections within knots marked with a single equals sign (`=`). Stitches help organize complex knots into manageable pieces, similar to how chapters contain sections. You learned how to address stitches using dot notation (`KnotName.StitchName`) and how to combine them with sticky choices to create rich, explorable locations.

These concepts form the foundation of non-linear storytelling in ink, allowing you to create everything from simple branching narratives to complex exploration games with multiple interconnected locations.

## Review Questions

Before moving on, test your understanding:

1. What symbol is used to create a knot in ink, and what naming restrictions apply?
2. How does a divert (`->`) differ from a choice (`*`)?
3. What's the difference between `END` and `DONE`?
4. What makes a sticky choice different from a regular choice, and when would you use each?
5. How do you prevent an infinite loop when creating a knot that diverts back to itself?
6. What symbol creates a stitch, and how is it different from a knot?
7. How do you address a stitch from outside its parent knot versus from within the same knot?
8. Why might you combine sticky choices with one regular choice in a loop structure?

## Try It

As seen in this chapter's examples, it is easy to create a complex branching story using a combination of choices, knots, diverts, and stitches. These basic building blocks of ink will form the backbone of most stories you create. Practicing with these kinds of ink code will help you get used to how ink works and will also prepare you for some of the more advanced content found in later chapters of this book.

Here's a starter project to extend:

```ink
You arrive at the town of Riverside.

-> Town_Square

== Town_Square ==
The town square bustles with activity. A fountain sits in the center.

* [Visit the market]
    -> Market
* [Visit the inn]
    -> Inn
* [Leave town]
    -> END

== Market ==
The market is crowded with vendors selling their wares.
-> Town_Square

== Inn ==
The inn is warm and welcoming. A fire crackles in the hearth.
-> Town_Square
```

As practice, complete the following objectives:

**Objective 1:** Add stitches to the Market knot to create at least two different vendors (like a blacksmith and a baker). Use sticky choices to allow the player to visit multiple vendors before returning to the town square.

**Objective 2:** Create a loop in the Inn knot where the player can talk to the innkeeper multiple times using sticky choices, but add one regular choice that allows them to leave and return to the town square.

**Objective 3:** Add a new knot called `River` that players can visit from the Town_Square. Inside the River knot, create at least two stitches (such as `fishing_spot` and `dock`) and use diverts to allow movement between them.

**Objective 4:** Test your story thoroughly to ensure there are no infinite loops. Make sure every knot and stitch has a clear path back to the town square or to the end of the story. Verify that all sticky choices have at least one regular choice to break the loop.

Once you've completed these objectives, have someone else play through your story to check for any issues you might have missed. Pay attention to whether they can navigate freely without getting stuck and whether the story flow feels natural.
