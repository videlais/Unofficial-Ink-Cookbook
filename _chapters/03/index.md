---
title: "Alternatives"
order: 3
chapter_number: 3
layout: chapter
---

## Chapter Summary

In this chapter, you will learn about alternatives and how to use sequences, cycles, and shuffles to create dynamic, varying text in your ink stories. Alternatives allow you to present different content each time the same section of your story is encountered, adding variety and replayability without writing repetitive code.

## Learning Objectives

By the end of this chapter, you will be able to:

- Create sequences that display different text in order.
- Implement cycles that repeat through content indefinitely.
- Use once-only alternatives for content that disappears after use.
- Generate random text using shuffles.
- Combine alternatives in nested structures for complex variation.
- Apply alternatives to create dynamic, re-playable narratives.

## Table of Contents

- [Chapter Summary](#chapter-summary)
- [Learning Objectives](#learning-objectives)
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Understanding Alternatives](#understanding-alternatives)
  - [Code Example 3.1: Basic Alternatives](#code-example-31-basic-alternatives)
  - [Interactive Example 3.1: Basic Alternatives](#interactive-example-31-basic-alternatives)
- [Sequences](#sequences)
  - [Code Example 3.2: Using Sequences](#code-example-32-using-sequences)
  - [Interactive Example 3.2: Using Sequences](#interactive-example-32-using-sequences)
- [Cycles](#cycles)
  - [Code Example 3.3: Using Cycles](#code-example-33-using-cycles)
  - [Interactive Example 3.3: Using Cycles](#interactive-example-33-using-cycles)
- [Once-Only Alternatives](#once-only-alternatives)
  - [Code Example 3.4: Once-Only](#code-example-34-once-only)
  - [Interactive Example 3.4: Once-Only](#interactive-example-34-once-only)
- [Shuffles](#shuffles)
  - [Code Example 3.5: Using Shuffles](#code-example-35-using-shuffles)
  - [Interactive Example 3.5: Using Shuffles](#interactive-example-35-using-shuffles)
- [Multi-Line Alternatives](#multi-line-alternatives)
  - [Multi-Line Sequences](#multi-line-sequences)
  - [Code Example 3.6: Multi-Line Sequences](#code-example-36-multi-line-sequences)
  - [Multiline Cycles](#multiline-cycles)
  - [Code Example 3.7: Multiline Cycles](#code-example-37-multiline-cycles)
  - [Multiline Once-Only](#multiline-once-only)
  - [Code Example 3.8: Multiline Once-Only](#code-example-38-multiline-once-only)
  - [Multi-line Shuffles](#multi-line-shuffles)
  - [Code Example 3.9: Multi-line Shuffles](#code-example-39-multi-line-shuffles)
- [Advanced Shuffles](#advanced-shuffles)
  - [Shuffle Once](#shuffle-once)
  - [Code Example 3.10: Shuffle Once](#code-example-310-shuffle-once)
  - [Shuffle Stopping](#shuffle-stopping)
  - [Code Example 3.11: Shuffle Stopping](#code-example-311-shuffle-stopping)
- [Advanced Alternatives](#advanced-alternatives)
  - [Blank Elements](#blank-elements)
  - [Code Example 3.12: Blank Elements](#code-example-312-blank-elements)
  - [Interactive Example 3.12: Blank Elements](#interactive-example-312-blank-elements)
  - [Nested Alternatives](#nested-alternatives)
  - [Code Example 3.13: Nested Alternatives](#code-example-313-nested-alternatives)
  - [Alternatives and Diverts](#alternatives-and-diverts)
  - [Code Example 3.14: Alternatives with Diverts](#code-example-314-alternatives-with-diverts)
  - [Interactive Example 3.14: Alternatives with Diverts](#interactive-example-314-alternatives-with-diverts)
- [Choice Text and Alternatives](#choice-text-and-alternatives)
  - [Code Example 3.15: Alternatives in Choices](#code-example-315-alternatives-in-choices)
  - [Interactive Example 3.15: Alternatives in Choices](#interactive-example-315-alternatives-in-choices)
- [Summary](#summary)
- [Review Questions](#review-questions)
- [Try It](#try-it)

---

## Introduction

In Chapters 1 and 2, you learned how to create branching narratives using choices, weaves, knots, and diverts. These tools allow you to build complex, non-linear stories where players make meaningful decisions that affect their experience.

However, you may have noticed a limitation: each time a player encounters the same knot or choice, they see exactly the same text. If your story has loops or allows players to revisit locations, this repetition can make your narrative feel static and predictable.

**Alternatives** solve this problem by allowing you to present different content each time the same section is encountered. Instead of writing duplicate knots with slightly different text, you can use alternatives to vary dialogue, descriptions, or even story paths automatically.

In this chapter, you'll learn about four main types of alternatives—**sequences**, **cycles**, **once-only**, and **shuffles**—each serving different narrative purposes. You'll also discover how to combine them in sophisticated ways to create dynamic, replayable stories that feel alive and responsive.

> **Note** If an interactive example does not load, you can view the [source code]({{ site.baseurl }}/_examples/chapter03/) directly. Use Tab and Enter keys to navigate choices in the interactive examples.

---

## Understanding Alternatives

Along with writing text, ink provides a powerful feature called **alternatives**—a programmable way to create sequences of text, cycling content, and randomized output from a collection.

In ink, alternatives are text or code within curly brackets, `{}`. When used in your story, they provide "alternative" content based on how many times they've been encountered.

> **Note** Think of alternatives as ink's way of remembering "how many times have I shown this text before?" and adjusting what appears next based on that memory.

Each element in an alternative is separated by the pipe character, `|`. Different alternative types use special characters at the start to control their behavior.

### Code Example 3.1: Basic Alternatives

```ink
The merchant greets you: "{Hello traveler!|Back again?|Still browsing?}"
```

This is a sequence—the simplest form of alternative. The first time it's encountered, it shows "Hello traveler!", the second time "Back again?", and the third time "Still browsing?" (which repeats thereafter).

### Interactive Example 3.1: Basic Alternatives

{% include ink-player.html
   story="chapter03/basic-alternatives"
   title="Example: Basic Alternatives"
   height="400px"
%}

> **Important** Alternatives automatically track how many times they've been encountered. Each alternative in your story has its own independent counter, allowing you to create rich, varied content throughout your narrative.

---

## Sequences

A **sequence** is a series of values that ink moves through in order until there are no more to show. Once a sequence reaches its last element, it continues showing that final element on all subsequent encounters.

> **Tip** Sequences are perfect for character dialogue that evolves over time, descriptions that get more detailed with each visit, or any content where you want natural progression from first encounter to later visits.

### Code Example 3.2: Using Sequences

```ink
-> Freaking_Out

== Freaking_Out ==
+ [Think more about it]
    {What should I do? | What if I didn't say anything? | Should I ask him out?}
    -> Freaking_Out
```

In this example:

- **First encounter:** "What should I do?"
- **Second encounter:** "What if I didn't say anything?"
- **Third encounter and beyond:** "Should I ask him out?"

### Interactive Example 3.2: Using Sequences

{% include ink-player.html
   story="chapter03/sequences"
   title="Example: Using Sequences"
   height="400px"
%}

---

## Cycles

A **cycle** is an alternative that repeats indefinitely. It "cycles" through all entries in order and then starts back at the first element again.

Cycles start with the ampersand symbol, `&`.

> **Tip** Cycles are ideal for content that should vary but never run out—like days of the week, rotating guard patrols, or changing weather patterns that repeat naturally.

### Code Example 3.3: Using Cycles

```ink
-> New_Day

== New_Day ==
+ [It's a new day!]
    It was {&Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday}.
    -> New_Day
```

Each time the player chooses to continue, the next day appears in sequence. After Sunday, it cycles back to Monday.

### Interactive Example 3.3: Using Cycles

{% include ink-player.html
   story="chapter03/cycles"
   title="Example: Using Cycles"
   height="400px"
%}

---

## Once-Only Alternatives

Instead of cycling through text indefinitely, ink also provides a **once-only** alternative that runs through its entries and then shows nothing. It only displays its elements "once."

Once-only alternatives start with the exclamation point, `!`.

> **Warning** Once-only alternatives become invisible after their last element is shown. Make sure this is the behavior you want, or use sequences (which repeat the last element) instead.

### Code Example 3.4: Once-Only

```ink
-> Confrontation

== Confrontation ==
+ [Demand they leave]
    {!"I don't want you around"|"You need to leave"|"Get out"}, I said.
    -> Confrontation
```

The dialogue escalates with each encounter, but after the third time, nothing appears—representing the character has said all they need to say.

### Interactive Example 3.4: Once-Only

{% include ink-player.html
   story="chapter03/once-only"
   title="Example: Once-Only"
   height="400px"
%}

---

## Shuffles

A **shuffle** is a special type of alternative that presents elements *randomly* instead of in sequence. It picks a new, random element from the entries each time it is encountered.

Shuffles start with a tilde, `~`.

> **Important** Shuffles introduce randomness into your story. Each playthrough can be different, and the same shuffle might show the same element twice in a row—it's truly random!

### Code Example 3.5: Using Shuffles

```ink
-> Random_Day

== Random_Day ==
+ [Check the calendar]
    It was {~Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday}.
    -> Random_Day
```

Unlike cycles, shuffles don't follow a predictable pattern. Each encounter randomly selects from all available elements.

### Interactive Example 3.5: Using Shuffles

{% include ink-player.html
   story="chapter03/shuffles"
   title="Example: Using Shuffles"
   height="400px"
%}

---

## Multi-Line Alternatives

Alternatives are often written inline using curly brackets with entries separated by pipe characters. However, they also have an extended **multi-line format** that's more readable for longer content.

> **Tip** Use multi-line format when your alternative elements are long, contain multiple sentences, or when you want to make your code easier to read and maintain.

When written in multi-line format, each element is separated by a newline and then a hyphen, `-`. Everything on the line following the hyphen is considered part of that element.

### Multi-Line Sequences

The keyword `stopping` is used for multiline sequence alternatives.

### Code Example 3.6: Multi-Line Sequences

```ink
{stopping:
  - I entered the ancient passage.
  - I walked into the ancient passage again.
  - "Hello, ancient passage! We are old friends now."
}
```

### Multiline Cycles

Multiline cycles use the `cycle` keyword.

### Code Example 3.7: Multiline Cycles

```ink
{cycle:
  - I waited.
  - I looked around for a moment.
  - I continued to wait.
}
```

### Multiline Once-Only

The once-only alternative uses the keyword `once` for multiline usage.

### Code Example 3.8: Multiline Once-Only

```ink
{once:
  - Could I really win?
  - Dare I continue?
}
```

### Multi-line Shuffles

Multi-line shuffles use the `shuffle` keyword.

### Code Example 3.9: Multi-line Shuffles

```ink
{shuffle:
  - King of Diamonds.
  - King of Spades.
  - King of Hearts
  - King of Clubs
}
```

---

## Advanced Shuffles

The keyword `shuffle` can be combined with `once` and `stopping` to create more sophisticated randomization patterns.

### Shuffle Once

When paired with the keyword `once`, shuffle picks a random element once and then shows nothing on additional encounters.

> **Tip** Shuffle once is perfect for random events that should only happen one time, like drawing a card from a deck that you won't return.

### Code Example 3.10: Shuffle Once

```ink
{shuffle once:
  - King of Diamonds.
  - King of Spades.
  - King of Hearts
  - King of Clubs
}
```

### Shuffle Stopping

Using `shuffle` and `stopping` together shows a random element (excluding the last one) until all others have been used, then only shows the last element.

> **Note** Shuffle stopping is useful when you want random variety but need to ensure a specific final outcome occurs after all other options are exhausted.

### Code Example 3.11: Shuffle Stopping

```ink
{shuffle stopping:
  - King of Diamonds.
  - King of Spades.
  - King of Hearts
  - King of Clubs
  - (No more kings.)
}
```

---

## Advanced Alternatives

The power of alternatives extends beyond simple text variation. You can use them in sophisticated ways to create dynamic, responsive narratives.

### Blank Elements

Alternatives can contain blank elements—empty entries that show nothing. This allows you to delay content until a certain number of encounters.

> **Important** Blank elements in alternatives act as "silent" encounters. They count toward the alternative's progression but display nothing, allowing you to create timed reveals.

### Code Example 3.12: Blank Elements

```ink
-> Check

== Check ==
+ [Check everything]
    {!||A light suddenly came on by itself!}
    -> Check
```

In this example:
- **First encounter:** Nothing (blank element)
- **Second encounter:** Nothing (blank element)
- **Third encounter and beyond:** "A light suddenly came on by itself!"

This creates suspense—the player checks the room twice with nothing happening, then on the third check, something occurs!

### Interactive Example 3.12: Blank Elements

{% include ink-player.html
   story="chapter03/blank-elements"
   title="Example: Blank Elements"
   height="400px"
%}

### Nested Alternatives

Alternatives can be nested inside other alternatives to create complex variation patterns.

> **Tip** Nested alternatives allow you to combine different types—like a shuffle containing sequences, or a cycle containing shuffles—for rich, varied content.

### Code Example 3.13: Nested Alternatives

```ink
The {~vampire {~runs|flies}|zombie {~scrambles|crawls}} toward you.
```

This creates multiple layers of randomization:

1. **Outer shuffle:** Randomly picks between "vampire" or "zombie"
2. **Inner shuffles:** If vampire, randomly picks "runs" or "flies"; if zombie, randomly picks "scrambles" or "crawls"

Possible outputs:
- "The vampire runs toward you."
- "The vampire flies toward you."
- "The zombie scrambles toward you."
- "The zombie crawls toward you."

### Alternatives and Diverts

Since alternatives can contain any ink content, they can include diverts to create randomized story paths.

> **Warning** Using diverts in alternatives creates branching based on randomness or repetition. Make sure each possible path makes narrative sense!

### Code Example 3.14: Alternatives with Diverts

```ink
I awake on the shore. I am attacked by a <>

{~->Shark|->Crab}

== Shark ==
shark!
-> DONE

== Crab ==
crab!
-> DONE
```

**Reminder:** The `<>` is glue, making the next line flow together with the previous text.

This randomly diverts to either the Shark or Crab knot, creating different encounters each playthrough.

### Interactive Example 3.14: Alternatives with Diverts

{% include ink-player.html
   story="chapter03/alternatives-diverts"
   title="Example: Alternatives with Diverts"
   height="400px"
%}

---

## Choice Text and Alternatives

Alternatives can be used within choice text to vary what players see each time they encounter the same choice.

> **Tip** To avoid the alternative being interpreted as a conditional (which we'll learn about in later chapters), include some text before the alternative in the choice.

### Code Example 3.15: Alternatives in Choices

```ink
-> GreetShoppers

== GreetShoppers ==
+ Hello. {&Hey there!|Welcome!|Have a good time!}
    -> GreetShoppers
```

Each time the player makes this choice, they see "Hello." followed by a different cycling greeting.

### Interactive Example 3.15: Alternatives in Choices

{% include ink-player.html
   story="chapter03/alternatives-choices"
   title="Example: Alternatives in Choices"
   height="400px"
%}

---

## Summary

This chapter introduced **alternatives**, ink's powerful system for varying content based on how many times it's been encountered. You learned four main types of alternatives:

**Sequences** display elements in order, stopping at and repeating the final element. They're perfect for evolving dialogue or progressive descriptions.

**Cycles** move through elements in order and then loop back to the beginning, ideal for naturally repeating content like days of the week or patrol routes.

**Once-only** alternatives display each element once and then show nothing, useful for escalating dialogue or events that exhaust themselves.

**Shuffles** pick random elements each time, creating unpredictability and variation in your narratives.

You also learned about **multi-line format** using keywords like `stopping`, `cycle`, `once`, and `shuffle` for more readable code with longer content.

Advanced techniques covered include **shuffle once** (random then nothing) and **shuffle stopping** (random then fixed final element), **blank elements** for timed reveals, **nested alternatives** for complex variation patterns, **alternatives with diverts** for randomized story paths, and **alternatives in choice text** for varying player options.

Alternatives are essential for creating dynamic, replayable narratives. They allow your stories to feel alive and responsive, varying naturally as players explore and re-encounter the same locations, characters, and situations.

## Review Questions

Before moving on, test your understanding:

1. What symbol encloses all alternative content, and what symbol separates elements within an alternative?
2. How does a sequence behave when it reaches its last element?
3. What symbol starts a cycle, and how does cycling differ from a sequence?
4. When would you use a once-only alternative instead of a sequence?
5. What happens when you use a shuffle—how does it decide which element to show?
6. What keyword do you use for a multi-line sequence alternative?
7. What's the difference between `shuffle once` and `shuffle stopping`?
8. How can blank elements in alternatives be used to create timed reveals?

## Try It

This chapter's examples demonstrate the different kinds of alternatives available within ink. Alternatives allow you to create very complex stories with looping content, randomization, and sophisticated variation. Learning how alternatives work can be challenging, but practicing with them will help you understand how each type functions and how they can be combined to build advanced ink stories.

Here's a starter project to extend:

```ink
You enter the mysterious shop.

-> Browse

== Browse ==
The shopkeeper looks up. "{Hello there!|Back again?|Still browsing, I see.|You again!}"

+ [Browse weapons]
    You see swords and bows on the wall.
    -> Browse
+ [Browse potions]
    Colorful vials line the shelves.
    -> Browse
+ [Leave]
    You exit the shop.
    -> END
```

As practice, complete the following objectives:

**Objective 1:** Replace the weapon description ("You see swords and bows on the wall.") with a **sequence** that provides increasingly detailed descriptions each time the player browses weapons. Include at least three different descriptions that get progressively more detailed.

**Objective 2:** Replace the potion description with a **cycle** that rotates through different potion colors or effects each time the player browses them. Use at least four different cycle elements.

**Objective 3:** Add a new choice to examine a mysterious artifact. Use a **once-only** alternative with blank elements to create suspense—make the player examine it three times before something happens on the fourth examination. On the fourth time, reveal something significant about the artifact.

**Objective 4:** Add a **nested alternative** somewhere in your story. For example, you could create a random encounter when leaving the shop that shuffles between different creature types, each with its own shuffled behavior (similar to the vampire/zombie example from this chapter).

Once you've completed these objectives, test your story multiple times to see how the alternatives behave. Pay attention to:
- Does your sequence stop at the last element and repeat it?
- Does your cycle loop back to the beginning?
- Do your blank elements create the intended timing?
- Does your nested alternative produce varied, interesting results?

Have someone else play through your story several times to verify that the alternatives create a dynamic, engaging experience!
