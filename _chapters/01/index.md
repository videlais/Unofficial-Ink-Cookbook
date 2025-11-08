---
title: "Writing Your First Ink Story"
order: 1
chapter_number: 1
layout: chapter
---

## Chapter Summary

This chapter introduces the basic building blocks of ink programming. You will learn how to write simple stories, create choices for players, and build branching narratives using weaves. By working through the interactive examples, you'll gain experience with ink's fundamental concepts.

## Learning Objectives

By the end of this chapter, you will be able to:

- Define key ink terminology including flow, choices, weave, lines, and glue.
- Create simple stories using ink's top-to-bottom flow structure.
- Construct basic choices and weaves to create branching narratives.
- Apply selective output to control what text appears to players.
- Use comments to document and annotate your code.
- Build complex weaves with multiple levels of choices.

## Table of Contents

- [Chapter Summary](#chapter-summary)
- [Learning Objectives](#learning-objectives)
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Understanding Flow](#understanding-flow)
  - [Code Example 1.1: Beginning with ink](#code-example-11-beginning-with-ink)
  - [Interactive Example 1.1: Beginning with ink](#interactive-example-11-beginning-with-ink)
  - [Code Example 1.2: Multiple sentences](#code-example-12-multiple-sentences)
  - [Interactive Example 1.2: Multiple sentences](#interactive-example-12-multiple-sentences)
- [Introducing Lines and Glue](#introducing-lines-and-glue)
  - [Code Example 1.3: Using Glue](#code-example-13-using-glue)
  - [Interactive Example 1.3: Using glue](#interactive-example-13-using-glue)
- [Introducing Choices](#introducing-choices)
  - [Code Example 1.4: Adding Choices](#code-example-14-adding-choices)
  - [Interactive Example 1.4: Adding Choices](#interactive-example-14-adding-choices)
- [Introducing Weaves](#introducing-weaves)
  - [Code Example 1.5: Understanding a Weave](#code-example-15-understanding-a-weave)
  - [Interactive Example 1.5: Understanding a Weave](#interactive-example-15-understanding-a-weave)
- [Source and Output](#source-and-output)
  - [Using Selective Output](#using-selective-output)
  - [Code Example 1.6: Using Selective Output](#code-example-16-using-selective-output)
  - [Interactive Example 1.6: Using Selective Output](#interactive-example-16-using-selective-output)
- [Complex Weaves](#complex-weaves)
  - [Weaves inside Weaves](#weaves-inside-weaves)
  - [Code Example 1.7: Complex Weaves](#code-example-17-complex-weaves)
  - [Interactive Example 1.7: Complex Weaves](#interactive-example-17-complex-weaves)
  - [Code Example 1.8: Reading Weaves](#code-example-18-reading-weaves)
  - [Interactive Example 1.8: Reading Weaves](#interactive-example-18-reading-weaves)
- [Gathering Points](#gathering-points)
  - [Code Example 1.9: Using Gathering Points](#code-example-19-using-gathering-points)
  - [Interactive Example 1.9: Using Gathering Points](#interactive-example-19-using-gathering-points)
  - [Code Example 1.10: Multi-Level Gathering Points](#code-example-110-multi-level-gathering-points)
  - [Interactive Example 1.10: Multi-Level Gathering Points](#interactive-example-110-multi-level-gathering-points)
- [Comments](#comments)
  - [Code Example 1.11: Using Comments](#code-example-111-using-comments)
  - [Interactive Example 1.11: Using Comments](#interactive-example-111-using-comments)
- [Summary](#summary)
- [Review Questions](#review-questions)
- [Try It](#try-it)

---

## Introduction

Before we can begin to create interactive stories, we need to review the fundamental concepts of ink. These include **flow**, the movement of a story from top to bottom unless interrupted; **choices**, how interactivity is added to a story; and **weave**, how we achieve branching in an interactive story.

Across this chapter, we will review these core concepts and how others like **glue** and **selective output** can be used to allow authors to affect what a player sees for output.

> **Note** If an interactive example does not load, you can view the [source code]({{ site.baseurl }}/_examples/chapter01/) directly. Use Tab and Enter keys to navigate choices in the interactive examples.

Let's begin with the most common concept in ink, **flow**.

---

## Understanding Flow

ink was designed to help writers create narrative content.

A simple story can often appear as one or more sentences.

### Code Example 1.1: Beginning with ink

```ink
Hello!
```

### Interactive Example 1.1: Beginning with ink

{% include ink-player.html
   story="chapter01/first-ink"
   title="Example: Beginning with ink"
   height="350px"
%}

In ink, *flow* runs from top to bottom. The first sentence is shown and then any others. This can often make writing in ink the same as writing in other text editing software.

### Code Example 1.2: Multiple sentences

```ink
This is a single sentence.

This is another.

This is all valid ink code!
```

### Interactive Example 1.2: Multiple sentences

{% include ink-player.html
   story="chapter01/second-ink"
   title="Example: Seeing Flow"
   height="350px"
%}

## Introducing Lines and Glue

A line is a single continuous section of textual content. A simple example would be a single sentence. It would be one *line*.

In ink, what is and is not one line can be affected by another concept, *glue*. To create a single line from multiple sentences, we can "glue" them together.

In ink, the use of the less-than and greater-than symbols together create glue, `<>`.

> **Tip** Glue is useful when combining dialogue with speaker tags, joining sentence fragments, or creating seamless text flow where you want to avoid unwanted line breaks.

### Code Example 1.3: Using Glue

```ink
This is <>
all <>
one line to ink!
```

### Interactive Example 1.3: Using glue

{% include ink-player.html
   story="chapter01/third-ink"
   title="Example: Using Glue"
   height="350px"
%}

## Introducing Choices

Players interact with a work through *choices*. In ink, we add choices to a story using the asterisk, `*`.

A line beginning with an asterisk is a *choice*.

Choices are the basic building block of any ink project. They affect the *flow*, branching it in a different path than it started.

### Code Example 1.4: Adding Choices

```ink
This is one line.

* This line is a choice!
```

### Interactive Example 1.4: Adding Choices

{% include ink-player.html
   story="chapter01/fourth-ink"
   title="Example: Adding Choices"
   height="350px"
%}

When using choices, we are creating a *weave*.

## Introducing Weaves

A *weave* is one or more choices as a collection. When written together, they are grouped as one single weave.

### Code Example 1.5: Understanding a Weave

```ink
This is one line.

* This is a choice!
* This is another choice!
```

### Interactive Example 1.5: Understanding a Weave

{% include ink-player.html
   story="chapter01/fifth-ink"
   title="Example: Understanding a Weave"
   height="350px"
%}

When making a *choice*, its text becomes the next line in the story.

We can also control if the text of a choice will be shown to a player or not. You'll learn more about advanced choice types in Chapter 2.

## Source and Output

ink is a programming language. This means the "source" or original content may not match the output.

We can see a simple example with glue. What an author writes and what a player might see can be different.

When working with choices, we can also use an additional concept known as *selective output*.

### Using Selective Output

The use of an opening and closing square bracket around some text makes it *selective*. When combined with a choice, the text enclosed in the square brackets will be removed from the next line of output a player would see.

> **Tip** Selective output is commonly used to create shorter, clearer choice labels while maintaining natural narrative flow in the story text. For example, `* [Look around]` appears as just "Look around" to the player, but nothing is added to the story output.

### Code Example 1.6: Using Selective Output

```ink
You are standing in a room.

* [Look around] You scan the room carefully.
* Look at the door
  The door is old and wooden.
```

Notice the difference: the first choice uses `[Look around]` so only "You scan the room carefully." appears in the output. The second choice shows "Look at the door" followed by the description.

### Interactive Example 1.6: Using Selective Output

{% include ink-player.html
   story="chapter01/sixth-ink"
   title="Example: Using Selective Output"
   height="350px"
%}

In the same way glue and selective output can add extra symbols and text in the source of a story, we can also add notes to ourselves and others in the code.

> **Warning** Common mistakes beginners make include: forgetting the space after asterisks in choices (`*Choice` won't work, use `* Choice`), mixing tabs and spaces in weaves (be consistent!), and mismatched square brackets in selective output (always use pairs: `[text]`).

## Complex Weaves

A weave is not limited to one level of choices. We can create branches that branch.

### Weaves inside Weaves

For each level of a weave, we add an additional asterisk, `*`. Assuming the previous branch was chosen, what follows the choice becomes itself a branch.

### Code Example 1.7: Complex Weaves

```ink
* This is a choice.
** This is a sub-branch of the first weave.
* This is another choice.
** This is also a sub-branch of the first weave.
```

### Interactive Example 1.7: Complex Weaves

{% include ink-player.html
   story="chapter01/seventh-ink"
   title="Example: Complex Weaves"
   height="350px"
%}

To help readability for authors, we often tab each progressive branch of a complex weave.

> **Tip** Spacing before a line does not affect its meaning in ink. Use indentation to make your code more readable for yourself and others.

### Code Example 1.8: Reading Weaves

```ink
* This is a choice.
    ** This is a sub-branch of the first weave.
* This is another choice.
    ** This is also a sub-branch of the first weave.
```

Because the spacing before a line does not affect its meaning, [Example 1.7](#code-example-17-complex-weaves) and [Example 1.8](#code-example-18-reading-weaves) produce the same output.

### Interactive Example 1.8: Reading Weaves

{% include ink-player.html
   story="chapter01/eighth-ink"
   title="Example: Reading Weaves"
   height="350px"
%}

Weaves can easily become complex. To help us better manage them, ink has a companion concept named **gathering points**.

## Gathering Points

As we add more weaves to our code, we risk having multiple branches with their own branches with their own branches. This can quickly become too complex to easily understand!

In ink, we can "collapse" a weave back down to a point. We call this a **gathering point**.

> **Warning** In narrative design, we use the term *combinatorial explosion* to describe how branches can lead to more and more branches, creating seemingly endless choices for a player.

When a hyphen, `-`, is on a line following a weave, all choices within the weave "gather" to that point.

### Code Example 1.9: Using Gathering Points

```ink
The emperor stands before you.

"Pick your reward," he states, motioning to servants to bring treasures into the room.

* [Jewels]
* [Gold]
* [Swords]
-

The emperor nods. "Very good. Now take your treasure and leave."
```

### Interactive Example 1.9: Using Gathering Points

{% include ink-player.html
   story="chapter01/emperor"
   title="Example: Using Gathering Points"
   height="350px"
%}

Each level of a weave can use its own gathering point. This can be important to allow complex structures to "bottleneck" as choices would otherwise branch outward.

For each "level" of a weave, we need the same number of hyphens. For example, if there are two asterisks, `**`, two hyphens, `--`, would be needed to gather the level.

### Code Example 1.10: Multi-Level Gathering Points

```ink
You enter a mysterious shop.

* Browse the weapons
    ** [Pick up a sword]
        The sword feels heavy in your hand.
    ** [Pick up a bow]
        The bow is beautifully carved.
    --
    The shopkeeper nods approvingly at your selection.
    
* Browse the potions
    ** [Red potion]
        It smells of cinnamon.
    ** [Blue potion]
        It glows faintly.
    --
    "Careful with those," warns the shopkeeper.
    
-

"Will you be purchasing today?" asks the shopkeeper.

* "Yes, I'll take it."
* "No, just looking."
-

You leave the shop.
```

In this example:

- The double hyphen (`--`) gathers the weapon sub-choices and the potion sub-choices separately.
- The single hyphen (`-`) gathers the main shop browsing choices together.
- Another single hyphen (`-`) gathers the final purchase decision.

This creates a structure where different branches can converge at different points, giving you fine control over your narrative flow.

### Interactive Example 1.10: Multi-Level Gathering Points

{% include ink-player.html
   story="chapter01/multi-gather"
   title="Example: Multi-Level Gathering Points"
   height="450px"
%}

> **Important** Each level of weave (marked by the number of asterisks) has its own corresponding level of gathering point (marked by the same number of hyphens). A `**` choice gathers at `--`, while a `*` choice gathers at `-`.

As our stories become more complex, we often want to add notes for ourselves and others. To help us with this, ink has an important concept named **comments**.

## Comments

There is also another type of text that can be added that helps with understanding how code works: comments.

> **Note** In programming terminology, a comment is some text that is included in code but is ignored when it is run.

Comments in ink are added through using two forward slashes, `//`. Anything that follows the slashes until the next line is considered a comment. This also includes adding comments on lines after code as well. In later chapters, you'll see how comments help document complex logic and game state.

### Code Example 1.11: Using Comments

```ink
// These are all comments.
// ink skips over anything written with two forward-slashes.

Hello! // Comments can also be written after code, too!
```

### Interactive Example 1.11: Using Comments

{% include ink-player.html
   story="chapter01/ninth-ink"
   title="Example: Using Comments"
   height="350px"
%}

---

## Summary

This chapter introduced the fundamental concepts of writing in ink. You learned that ink uses a top-to-bottom concept known as **flow** where text appears sequentially, and that lines can be joined together using glue (`<>`).

**Choices,** marked with asterisks (`*`), allow players to make decisions that branch the story in different directions. Multiple choices form a **weave**, and weaves can be nested to create complex branching narratives.

You learned how **gathering points**, marked with hyphens (`-`), allow you to collapse multiple branches back to a single point in the story. Multi-level weaves require matching levels of gathering points—`**` choices gather at `--`, `***` choices at `---`, and so on.

You also learned how to use **selective output** with square brackets (`[]`) to control what text appears to players, and how to add **comments** using double slashes (`//`) to document your code.

## Review Questions

Before moving on, test your understanding:

1. What symbol is used to create choices in ink?
2. How do you "glue" text together to prevent line breaks?
3. What's the difference between a *choice* and a *weave*?
4. How do you prevent choice text from appearing in the story output?
5. What symbol creates a gathering point, and how many do you need for a `**` choice?
6. What happens to text written after `//` in your ink code?

## Try It

The following is the start of a project.

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

**Challenge:** Extend this story by adding:

- A third initial choice at the cave entrance
- More nested choices in the forest scene
- Gathering points to bring branches back together
- Comments explaining what each branch does
