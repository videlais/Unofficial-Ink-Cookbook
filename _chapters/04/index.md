---
title: "It's All Variable"
order: 4
chapter_number: 4
layout: chapter
---

## Chapter Summary

In this chapter, you will learn about variables in ink—how to store and manipulate data to create dynamic, stat-based narratives. You'll discover how to use global, temporary, and constant variables to track player statistics, story state, and make decisions based on conditional logic. Variables transform ink from a simple branching narrative tool into a full programming language capable of complex game mechanics.

## Learning Objectives

By the end of this chapter, you will be able to:

- Differentiate between global, temporary, and constant variables
- Manipulate numerical, string, and boolean data types
- Implement conditional logic using comparison operators
- Construct switch statements for multi-condition testing
- Evaluate knot values to create conditional story branches
- Display variable values within your narrative

## Table of Contents

- [Chapter Summary](#chapter-summary)
- [Learning Objectives](#learning-objectives)
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Working with Code](#working-with-code)
  - [Single Line Code](#single-line-code)
  - [Code Example 4.1: Single Line Operations](#code-example-41-single-line-operations)
  - [Multiple Line Code](#multiple-line-code)
  - [Code Example 4.2: Multiple Line Operations](#code-example-42-multiple-line-operations)
- [Variables](#variables)
  - [Displaying Variable Values](#displaying-variable-values)
  - [Code Example 4.3: Displaying Variables](#code-example-43-displaying-variables)
  - [Types of Data](#types-of-data)
    - [Numbers](#numbers)
    - [Code Example 4.4: Working with Numbers](#code-example-44-working-with-numbers)
    - [Interactive Example 4.4: Numeric Variables](#interactive-example-44-numeric-variables)
    - [Strings](#strings)
    - [Code Example 4.5: Working with Strings](#code-example-45-working-with-strings)
    - [Booleans](#booleans)
    - [Code Example 4.6: Working with Booleans](#code-example-46-working-with-booleans)
    - [Interactive Example 4.6: Boolean Variables](#interactive-example-46-boolean-variables)
    - [Text of Diverts](#text-of-diverts)
    - [Code Example 4.7: Divert Variables](#code-example-47-divert-variables)
    - [Knots as Values](#knots-as-values)
    - [Code Example 4.8: Knot Values](#code-example-48-knot-values)
    - [Interactive Example 4.8: Knot Values](#interactive-example-48-knot-values)
  - [Types of Variables](#types-of-variables)
    - [Global Variables](#global-variables)
    - [Code Example 4.9: Global Variables](#code-example-49-global-variables)
    - [Interactive Example 4.9: Global Variables](#interactive-example-49-global-variables)
    - [Temporary Variables](#temporary-variables)
    - [Code Example 4.10: Temporary Variables](#code-example-410-temporary-variables)
    - [Constant Variables](#constant-variables)
    - [Code Example 4.11: Constant Variables](#code-example-411-constant-variables)
    - [Interactive Example 4.11: Constant Variables](#interactive-example-411-constant-variables)
- [Conditional Logic](#conditional-logic)
  - [Comparison Operators](#comparison-operators)
  - [Code Example 4.12: Basic Conditionals](#code-example-412-basic-conditionals)
  - [Interactive Example 4.12: Basic Conditionals](#interactive-example-412-basic-conditionals)
  - [If-Else Logic](#if-else-logic)
  - [Code Example 4.13: If-Else Statements](#code-example-413-if-else-statements)
  - [Interactive Example 4.13: If-Else Logic](#interactive-example-413-if-else-logic)
  - [Switch Statements](#switch-statements)
  - [Code Example 4.14: Switch Statements](#code-example-414-switch-statements)
  - [Interactive Example 4.14: Switch Statements](#interactive-example-414-switch-statements)
  - [Testing Knot Values](#testing-knot-values)
  - [Code Example 4.15: Conditional Knot Testing](#code-example-415-conditional-knot-testing)
  - [Interactive Example 4.15: Knot-Based Conditionals](#interactive-example-415-knot-based-conditionals)
  - [Advanced Conditional Choices](#advanced-conditional-choices)
  - [Code Example 4.16: Conditional Choices](#code-example-416-conditional-choices)
  - [Working with Alternatives and Variables](#working-with-alternatives-and-variables)
  - [Code Example 4.17: Alternatives in Variables](#code-example-417-alternatives-in-variables)
- [Summary](#summary)
- [Review Questions](#review-questions)
- [Try It](#try-it)

---

## Introduction

In Chapters 1 through 3, you learned how to create dynamic narratives using choices, knots, diverts, and alternatives. These tools allow you to build branching stories with variety and replayability.

However, you may have noticed a limitation: there's no way to track player decisions over time, accumulate statistics, or make story branches depend on accumulated choices rather than individual moments. For example, how would you create a health system, track a player's relationship with different characters, or unlock content based on collecting items?

**Variables** solve these problems by giving ink the power to remember and track information throughout your story. A variable is a named container that holds a value—like a health score, a character's name, or whether the player has found a key. Variables allow you to create RPG-style stats, inventory systems, relationship trackers, and sophisticated game mechanics within your narratives.

In this chapter, you'll learn about three types of variables (**global**, **temporary**, and **constant**), different kinds of data they can store (**numbers**, **strings**, **booleans**), and how to use **conditional logic** to make story decisions based on variable values. You'll also discover how to combine variables with the ink features you've already learned to create truly interactive, stat-driven narratives.

> **Note** If an interactive example does not load, you can view the [source code]({{ site.baseurl }}/_examples/chapter04/) directly. Use Tab and Enter keys to navigate choices in the interactive examples.

---

## Working with Code

Like many other scripting languages, ink provides the concept of **variables**—containers that store and track values during your story. Variables in ink can take different forms and serve various purposes, from tracking health points to remembering a character's name.

When using variables in ink, you'll write more direct code than you have with choices and diverts. While variables are declared using keywords (covered later in this chapter), changing their values requires understanding how ink handles programming operations.

> **Important** Previously, your ink "programming" consisted of knots, diverts, and alternatives—structural elements for navigation and variation. Variables introduce true computational programming: math, logic, and state tracking.

Ink code that manipulates variables takes two forms: **single line** or **multiple line** operations.

### Single Line Code

A single line of programming in ink starts with the tilde character, `~`. It signifies that an operation happens only on that line, and ink should process the next line normally.

> **Tip** Think of the tilde (`~`) as ink's way of saying "this line is code, not story text." It's how you tell ink to perform calculations or change variable values without displaying anything to the player.

### Code Example 4.1: Single Line Operations

```ink
VAR health = 10

You take damage!
~ health = health - 1

Your current health is {health}.
```

The tilde line subtracts 1 from health without displaying anything. Only the narrative text and the health value appear to the player.

### Multiple Line Code

For programming that spans multiple lines, opening and closing curly brackets `{}` create a code block. This is used for conditional testing (covered later) and complex logic.

> **Note** Multi-line code blocks are especially useful for if-else logic, where you need to test conditions and execute different code based on the results.

### Code Example 4.2: Multiple Line Operations

```ink
VAR health = 5

You take a devastating hit!

{health > 0:
    ~ health = health - 1
    You're hurt but still standing. Health: {health}
- else:
    You collapse, defeated.
    -> DEATH
}

== DEATH ==
Game Over.
-> END
```

---

## Variables

In programming terminology, a variable is something that can change. Often, the metaphor used is one of a bucket. The variable represents a value when the program is running. The two commons actions are to "look into" the bucket to see its value or to "change" the value that is in the bucket through replacing it or adding more into it.

The values of variables can be shown through using opening and closing curly brackets around them. This allows an easy way to include different values such as statistics for players to see before they make decisions.

```ink
---

## Variables

In programming terminology, a **variable** is something that can change. A common metaphor is a bucket or container: the variable represents a value while the program runs. You can "look into" the bucket to see its value or "change" what's inside by replacing it or adding to it.

> **Note** The term "variable" comes from "varies"—these containers hold values that can vary (change) as your story progresses.

### Displaying Variable Values

Variable values can be displayed by placing the variable name within curly brackets, `{}`. This allows you to show statistics, scores, or other tracked information to players.

### Code Example 4.3: Displaying Variables

```ink
VAR health = 100
VAR name = "Hero"
VAR hasKey = false

{name} stands ready for adventure.
Current health: {health}
Carrying a key: {hasKey}
```

When this runs, the player sees:
```
Hero stands ready for adventure.
Current health: 100
Carrying a key: false
```

### Types of Data

Ink supports several different types of data that variables can store. Understanding these **data types** is crucial for using variables effectively.

#### Numbers

Variables can hold any numeric value, including both whole numbers (integers) and decimal numbers (floats).

> **Tip** Ink handles both integers (1, 5, 100) and decimals (4.5, 0.25, 99.9) seamlessly. Use decimals when you need precision, like for damage multipliers or percentage calculations.

Numbers support mathematical operations:
- **Addition:** `+`
- **Subtraction:** `-`
- **Multiplication:** `*`
- **Division:** `/`
- **Modulo (remainder):** `%`

### Code Example 4.4: Working with Numbers

```ink
VAR gold = 100
VAR price = 25
VAR discount = 0.5

You have {gold} gold coins.

~ gold = gold - price
After buying the sword: {gold} gold

~ gold = gold * discount
After the mysterious curse halves your gold: {gold} gold

VAR remainder = 10 % 3
Ten divided by three leaves a remainder of {remainder}.
```

> **Important** The modulo operator (`%`) returns the remainder after division. For example, `10 % 3 = 1` because 10 divided by 3 is 3 with a remainder of 1. This is useful for cycling through values or checking if numbers are even/odd.

### Interactive Example 4.4: Numeric Variables

{% include ink-player.html
   story="chapter04/numbers"
   title="Example: Numeric Variables"
   height="450px"
%}

#### Strings

In programming terminology, a **string** is a collection of characters (letters, numbers, spaces, punctuation) enclosed in double quotation marks.

> **Warning** In ink, string manipulation is limited. You cannot concatenate (join) strings or perform complex operations. Strings are primarily for storage and comparison.

### Code Example 4.5: Working with Strings

```ink
VAR playerName = "Alice"
VAR npcResponse = "Welcome to my shop"

{npcResponse}, {playerName}!

// String comparisons:
{playerName == "Alice": You are Alice! }
{playerName != "Bob": You are not Bob. }
{"Welcome" ? npcResponse: The NPC said welcome. }
```

String operations:
- **Equality:** `==` (tests if strings are identical)
- **Inequality:** `!=` (tests if strings are different)
- **Substring:** `?` (tests if right string appears in left string)

#### Booleans

**Boolean** values are named after George Boole, who created boolean algebra. In programming, boolean values represent binary states: `true` or `false`, `1` or `0`, yes or no.

> **Note** Booleans are the result of all conditional tests. When you check `health > 0`, the result is a boolean: either true (health is greater than 0) or false (it isn't).

### Code Example 4.6: Working with Booleans

```ink
VAR hasKey = false
VAR doorUnlocked = false

{hasKey: You have the key. }
{not hasKey: You don't have the key. }

~ hasKey = true
~ doorUnlocked = hasKey

{doorUnlocked: The door is now unlocked! }
```

### Interactive Example 4.6: Boolean Variables

{% include ink-player.html
   story="chapter04/booleans"
   title="Example: Boolean Variables"
   height="400px"
%}

#### Text of Diverts

Because variables can hold strings, they can also store the "target" of a divert. While limited in application, this can be useful for saving navigation paths in complex projects.

> **Tip** Divert variables are advanced features. They're most useful in procedurally generated stories or when you need to dynamically choose destinations based on game state.

### Code Example 4.7: Divert Variables

```ink
VAR nextLocation = -> Market

You decide where to go next.

* [Head to the market]
    ~ nextLocation = -> Market
    -> nextLocation
* [Head to the tavern]
    ~ nextLocation = -> Tavern
    -> nextLocation

== Market ==
You arrive at the bustling market.
-> DONE

== Tavern ==
You enter the cozy tavern.
-> DONE
```

#### Knots as Values

When you place a knot name in curly brackets `{}`, you access its **value**—a number representing how many times it's been visited.

> **Important** Knot values start at 0 (not visited) and increment each time the knot is encountered. A knot visited once has value 1, twice has value 2, and so on.

### Code Example 4.8: Knot Values

```ink
// Example_Knot hasn't been visited yet, so its value is 0
The knot Example_Knot has value {Example_Knot} (not visited).

-> Example_Knot

== Example_Knot ==
// Now we're IN the knot, so it's been visited
This knot's value is now {Example_Knot} (visited once).

-> Example_Knot_Again

== Example_Knot_Again ==
Going back to check...
-> Example_Knot_Check

== Example_Knot_Check ==
After visiting Example_Knot, its value is {Example_Knot}.
-> DONE
```

### Interactive Example 4.8: Knot Values

{% include ink-player.html
   story="chapter04/knot-values"
   story="chapter04/knot-values"
   title="Example: Knot Values"
   height="400px"
%}

---

### Types of Variables

Ink provides three different categories of variables: **global**, **temporary**, and **constant**. Each serves a different purpose and has different scope and mutability.

> **Note** "Scope" refers to where a variable can be accessed in your code. "Mutability" refers to whether a variable's value can change after it's created.

#### Global Variables

**Global variables** are defined using the keyword `VAR` and can be accessed from anywhere in your ink project. They persist throughout the entire story and are perfect for tracking player stats, inventory, or story state.

> **Important** Global variables must be declared at the top of your ink file, before any knots or story content. This is a requirement of ink's structure.

### Code Example 4.9: Global Variables

```ink
VAR health = 100
VAR playerName = "Adventurer"

Welcome, {playerName}! Health: {health}

-> FIGHT

== FIGHT ==
+ [Attack]
    You attack! The enemy strikes back.
    ~ health = health - 20
    Your health: {health}
    {health <= 0: -> GameOver }
    -> FIGHT
+ {health > 50} [Run away]
    You flee to safety.
    -> DONE

== GameOver ==
You've been defeated!
-> DONE
```

### Interactive Example 4.9: Global Variables

{% include ink-player.html
   story="chapter04/global-vars"
   title="Example: Global Variables"
   height="450px"
%}

#### Temporary Variables

**Temporary variables** are created using the tilde `~` followed by the keyword `temp`. They only exist within the knot or stitch where they're created and are deleted when that knot/stitch ends.

> **Tip** Use temporary variables for calculations you only need momentarily, like random values, intermediate math results, or loop counters. They don't clutter your global namespace.

### Code Example 4.10: Temporary Variables

```ink
VAR health = 50

-> Potion

== Potion ==
+ [Drink a potion]
    ~ temp healAmount = RANDOM(1, 10)
    The potion glows warmly. You heal {healAmount} health!
    ~ health = health + healAmount
    Your health is now {health}.
    -> Potion
+ [Stop drinking potions]
    You've had enough potions.
    -> DONE
```

**Note:** The `RANDOM(1, 10)` function generates a random number between 1 and 10 (inclusive). `healAmount` only exists within the Potion knot.

#### Constant Variables

**Constants** are created using the keyword `CONST`. Like global variables, they can be accessed throughout your project, but unlike globals, their values cannot be changed once set.

> **Warning** Constants are truly constant—attempting to change a constant's value will cause an ink error. Use them for values that should never change, like maximum stats, damage values, or game rules.

### Code Example 4.11: Constant Variables

```ink
VAR enemyHealth = 50
CONST SWORD_DAMAGE = 10
CONST CRIT_DAMAGE = 20

Enemy health: {enemyHealth}

-> FIGHT

== FIGHT ==
+ [Normal attack]
    ~ enemyHealth = enemyHealth - SWORD_DAMAGE
    You deal {SWORD_DAMAGE} damage! Enemy: {enemyHealth}
    {enemyHealth <= 0: -> Victory }
    -> FIGHT
+ [Critical strike]
    ~ enemyHealth = enemyHealth - CRIT_DAMAGE
    Critical! {CRIT_DAMAGE} damage! Enemy: {enemyHealth}
    {enemyHealth <= 0: -> Victory }
    -> FIGHT

== Victory ==
Victory! The enemy is defeated!
-> DONE
```

### Interactive Example 4.11: Constant Variables

{% include ink-player.html
   story="chapter04/constants"
   title="Example: Constant Variables"
   height="450px"
%}
```

### Types of Data

Ink supports saving and using many different types of data. These include numbers, strings, Booleans, and even the text of diverts.

#### Numbers

The value of any variable can be any number, including both whole and decimal.

```ink
VAR test = 4.5
```

Numbers can be added, subtracted, and divided from each other using the addition (+), subtraction (-), and forward-slash (/) symbols.

```ink
VAR test = 4.5
~ test = test + 10
~ test = test - 9
~ test = test / 3
```

Numbers also have an additional operation called modulo or mod. A modulus operation returns the remainder after division. For example, 9 % 3 would be 0, as there is not a remainder. However, 10 % 3 would be 1, as there is a single 1 remaining after the nearest division.

The mod operator uses the percentage symbol, `%`.

```ink
VAR test = 10
~ test = test % 3
```

#### Strings

In programming terminology, a string is a collection of letters, numbers, spaces, and other special characters enclosed in double quotation marks.

```ink
VAR name = “John”
```

In Ink, there is limited support for working with strings. However, there are three operations that can take place between strings: equality, inequality, and substring.

To test if one string is exactly the same as another string, the equality symbol, ==, can be used.

```ink
{ "Yes, exactly." == "Yes, exactly." }
```

For comparing strings that are not exactly the same, the inequality, not equal, symbol, `!=`, can be used.

```ink
{ "Not exact." != "Nope. Not at all." }
```

The last operation is the substring operation. It tests if the string to the right can be found in the string to the left of the operator. It uses the question mark, ?.

```ink
{ "Not exact." ? "exact" }
```

#### Booleans

Boolean values are named after George Boole, the inventor of what is now called boolean algebra. In his work, he created a representation of complex systems using simple rules where the outcome was either true or false.

In computer programming, these values, the keywords `true` and `false`, are called Boolean values because they represent either 1 or 0. These are the outcomes of any conditional testing (covered later in this chapter) and can also be stored in variables as well.

```ink
VAR proof = true
VAR example = false
```

#### Text of Diverts

Because variables can hold strings, the "target" of a divert can also be stored in a variable. While limited in application, such values can be used to save a longer divert name and use the variable in its place in more complicated or larger projects.

```ink
VAR someDivert = -> Next

* What was next?
    -> someDivert

=== Next ==
This was!
-> DONE
```

#### Knots

When the name of a knot is placed in curly brackets, `{}`, its *value* can be used. In Ink, the value of a knot is a Boolean value. If it has not been visited, its value is 0 (`false`). If it has, its value is 1 (`true`).

```ink
// Value of Example_Knot will be 0 to start.
The knot Example_Knot has not been visited. Its value is {Example_Knot}.

-> Example_Knot

=== Example_Knot ===
// Knot has been visited.
// Its value will now be 1.
This knot has been visited! Its value is now {Example_Knot}.
-> DONE

```

### Types of Variables

Ink provides three different types of variables: global, temporary, and constant.

#### Global Variables

Like many other scripting languages, Ink also understands *scope*. In programming terminology, a variable’s scope is where it can be accessed in a program. Depending on which “level” (scope) a variable has, it can or can not be accessed by other parts of the program.

```ink
VAR health = 0
VAR name = "Dan"
VAR divertExample = ->Example
```

Global variables are defined using the keyword `VAR` in Ink. Because they are global, they can be accessed in any part of a project. Once they are created, they are a part of everything. They can be used, updated, and accessed across the entire Flow. They can contain numbers, strings, and even diverts.

```ink
Example:

VAR health = 0

-> FIGHT

=== FIGHT ===
+ [Do you fight?]
    You try to fight, but are attacked.
    ~ health = health - 1
    -> FIGHT
```

#### Temporary Variables

When a global might be too much, or a number of calculations need to be carried out through creating new values per step, temporary variables can be used.

Temporary variables are created through using the tilde and the keyword "temp". Once created, they last during the life of the knot or stitch in which they were created.

**Example:**

```ink
VAR health = 0

-> Potion

=== Potion ===
+ [Drink a Potion]
     ~ temp additionalHealth = RANDOM(1,5)
    You gain some additional health. +{additionalHealth}
    ~ health = health + additionalHealth
    -> Potion
```

#### Constant Variables

Like global variables, constants are set and can be accessed throughout a Flow. However, unlike global variables, they cannot be changed once set. Their values are constant.

Constants are created using the keyword `CONST`.

**Example:**

```ink
VAR enemyHealth = 20
CONST swordDamage = 4

-> FIGHT

=== FIGHT ===
+ [Swing Sword]
    ~ enemyHealth = enemyHealth - swordDamage
    You swing your sword at the enemy! They take {swordDamage} damage!
    Their current health is {enemyHealth}.
    -> FIGHT
```

---

## Conditional Logic

Variables become truly powerful when combined with conditional logic—the ability to test values and make decisions based on those tests. This allows your stories to respond dynamically to player choices and story state.

> **Note:** Conditional logic is fundamental to interactive storytelling. Mastering these techniques will allow you to create sophisticated branching narratives that remember and respond to player actions.

### Comparison Operators

Ink uses comparison operators to test relationships between values. These operators work with numbers, strings, and booleans:

- `<` Less than
- `>` Greater than
- `<=` Less than or equal to
- `>=` Greater than or equal to
- `!=` Not equal
- `==` Equal
- `&&` And (both conditions must be true)
- `||` Or (at least one condition must be true)
- `not` Negation (opposite of the value)

> **Tip:** Comparison operators return boolean values (`true` or `false`), which makes them perfect for controlling story flow.

#### Code Example 4.12: Basic Conditionals

```ink
VAR gold = 50
VAR hasKey = false

You have {gold} gold coins.
{hasKey: You also have a key.}
{not hasKey: You don't have a key yet.}
{gold >= 100: You're quite wealthy!}
{gold < 20: You're running low on funds.}
```

#### Interactive Example 4.12

{% include ink-player.html storyPath="chapter04/basic-conditionals.json" %}

### If-Else Logic

The most common conditional pattern is if-else logic: if a condition is true, do one thing; otherwise (else), do another.

> **Important:** In multi-line conditional blocks, the first test must immediately follow the opening curly bracket `{`, then alternatives use `- else:`.

#### Code Example 4.13: If-Else Statements

```ink
VAR health = 75

{health > 50:
    You're feeling healthy and strong.
- else:
    You're wounded and weakened.
}

{health >= 100:
    Your health is at maximum!
- health >= 50:
    Your health is good.
- health >= 25:
    Your health is low. Be careful!
- else:
    You're critically injured!
}
```

#### Interactive Example 4.13

{% include ink-player.html storyPath="chapter04/if-else.json" %}

> **Warning:** Ink evaluates conditionals from top to bottom. Place more specific conditions before general ones to ensure correct logic flow.

### Switch Statements

Ink supports switch-style logic where you test a variable against multiple specific values. This is particularly useful for state machines or menu systems.

> **Note:** In switch statements, each case uses a single hyphen `-`, and `- else:` serves as the default case when no other values match.

#### Code Example 4.14: Switch Statements

```ink
VAR currentRoom = "kitchen"

{currentRoom:
    - "kitchen":
        You're in the kitchen. The smell of fresh bread fills the air.
    - "bedroom":
        You're in the bedroom. A soft bed beckons.
    - "cellar":
        You're in the dark cellar. It's damp and cold.
    - else:
        You're somewhere else entirely.
}
```

You can also use switch statements with numbers:

```ink
VAR suspicion = 3

{suspicion:
    - 0:
        They trust you completely.
    - 1:
        They're slightly wary of you.
    - 2:
        They're slightly wary of you.
    - 3:
        They're suspicious of your motives.
    - 4:
        They're suspicious of your motives.
    - else:
        They consider you an enemy!
}
```

#### Interactive Example 4.14

{% include ink-player.html storyPath="chapter04/switch-statements.json" height="400px" %}

### Testing Knot Values

As mentioned earlier, knots have numeric values that track how many times they've been visited. You can use these values in conditional logic to create sophisticated control flow.

> **Important:** Unvisited knots have a value of `0` (which is equivalent to `false`). Each visit increments the count, so `{KnotName}` checks if it's been visited at least once, while `{KnotName > 2}` checks if it's been visited more than twice.

#### Code Example 4.15: Conditional Knot Testing

```ink
-> CheckProgress

=== CheckProgress ===
{SecretRoom:
    You remember the secret room you discovered.
- else:
    There might be hidden areas you haven't found yet.
}

{SecretRoom > 1:
    You've been to the secret room multiple times.
}

+ {not SecretRoom} [Search for secrets]
    -> SecretRoom
+ {SecretRoom} [Return to the secret room]
    -> SecretRoom
+ [Continue exploring]
    -> DONE

=== SecretRoom ===
You found the secret room!
-> CheckProgress
```

#### Interactive Example 4.15

{% include ink-player.html storyPath="chapter04/knot-conditionals.json" height="400px" %}

### Conditional Choices

Conditionals can control which choices appear to the player. This creates dynamic choice menus that respond to story state.

> **Tip:** Conditional choices are perfect for creating progression systems where new options unlock based on player actions or variable values.

#### Code Example 4.16: Conditional Choices

```ink
VAR hasKey = false
VAR knowsPassword = false
VAR gold = 30

-> Castle

=== Castle ===
You stand before the castle gate.

+ {hasKey} [Use the key to unlock the gate]
    You unlock the gate with the key.
    -> Inside
+ {knowsPassword} [Speak the password]
    The guard nods and opens the gate.
    -> Inside
+ {gold >= 50} [Bribe the guard (50 gold)]
    ~ gold -= 50
    The guard pockets the coins and looks away.
    -> Inside
+ [Try to sneak in]
    The guards catch you. Try a different approach!
    -> Castle

=== Inside ===
You've made it inside the castle!
-> DONE
```

#### Interactive Example 4.16

{% include ink-player.html storyPath="chapter04/conditional-choices.json" height="450px" %}

> **Warning:** Make sure players always have at least one choice available. If all choices are conditional, include a fallback option that's always accessible.

### Combining Variables and Alternatives

Variables and alternatives can work together to create dynamic, varied content that remembers state.

> **Important:** You cannot assign an alternative directly as a variable's initial value (e.g., `VAR day = {~Mon|Tue}` won't work). Instead, declare the variable first, then assign the alternative result using a line of code.

#### Code Example 4.17: Variables with Alternatives

```ink
VAR currentWeather = ""
VAR mood = "neutral"

// Assign a random weather condition
~ currentWeather = "{~sunny|rainy|cloudy|snowy}"

The day is {currentWeather}.

{currentWeather == "sunny":
    ~ mood = "happy"
    The sunshine lifts your spirits!
}

{currentWeather == "rainy":
    ~ mood = "gloomy"
    The rain dampens your mood.
}

Your current mood: {mood}
```

#### Interactive Example 4.17

{% include ink-player.html storyPath="chapter04/alternatives-vars.json" height="350px" %}

> **Tip:** This technique is excellent for creating dynamic descriptions, random events, or procedurally generated content that still maintains consistency throughout your story.

---

## Summary

This chapter introduced you to variables and conditional logic in Ink—essential tools for creating dynamic, responsive interactive narratives.

**Variables** allow you to store and manipulate data throughout your story. Ink provides three types:

- **Global variables** (`VAR`) are accessible throughout your entire story and persist across knots and stitches. They're perfect for tracking player stats, inventory, relationships, or any story-wide state.
- **Temporary variables** (`temp`) exist only within the knot or stitch where they're created. They're ideal for calculations, intermediate values, or local state that doesn't need to persist.
- **Constants** (`CONST`) are global values that cannot be changed once set. They're useful for game rules, difficulty settings, or any value that should remain fixed throughout the story.

**Data types** in Ink include:

- **Numbers** for counting, calculations, and tracking quantities
- **Strings** for storing text like names, locations, or descriptions
- **Booleans** for true/false flags and yes/no decisions
- **Diverts** for storing story destinations
- **Knot values** which track how many times each knot has been visited

**Conditional logic** enables your story to make decisions based on variable values and story state:

- **Comparison operators** (`<`, `>`, `<=`, `>=`, `==`, `!=`, `&&`, `||`, `not`) test relationships between values
- **If-else statements** create branching logic that responds to conditions
- **Switch statements** efficiently test a variable against multiple specific values
- **Knot value testing** allows your story to remember and respond to which paths the player has taken
- **Conditional choices** show or hide options based on story state, creating dynamic menus that evolve with the narrative
- **Variables with alternatives** combine randomness with persistence for varied yet consistent content

Together, these techniques form the foundation of sophisticated interactive storytelling. They enable you to create stories that remember player actions, respond to choices with nuanced consequences, and maintain complex narrative state across branching paths.

---

## Review Questions

1. **What is the difference between global variables (`VAR`), temporary variables (`temp`), and constants (`CONST`)? When would you use each type?**

2. **What are the five data types that variables can store in Ink? Give an example of when you might use each type in a story.**

3. **How do you display the value of a variable in your story text? What symbol is used?**

4. **What value does an unvisited knot have? How does this value change when the player visits the knot?**

5. **Explain the difference between `==` and `=` in Ink. What does each symbol do?**

6. **In an if-else conditional block, what happens if the first condition is false? How do you specify alternative code to run?**

7. **What is a switch statement and how does it differ from a series of if-else conditionals? When might a switch statement be more appropriate?**

8. **Why can't you assign an alternative (like `{~A|B|C}`) as the initial value of a variable? How should you work with alternatives and variables together?**

---

## Try It

Variables and conditional logic are fundamental programming concepts that appear in nearly every programming language. Mastering them in Ink will not only improve your interactive storytelling but also help you develop skills transferable to other coding contexts.

> **Tip:** Start simple and build complexity gradually. Test your code frequently to catch errors early.

### Starter Code

Use this basic story structure as a starting point for your exercises:

```ink
// Variables
VAR playerName = "Adventurer"
VAR gold = 100
VAR health = 100
VAR hasMap = false

-> Introduction

=== Introduction ===
Welcome, {playerName}!

You begin your journey with {gold} gold coins and {health} health.

-> MainHub

=== MainHub ===
What would you like to do?

+ [Check inventory]
    -> CheckInventory
+ [Explore the area]
    -> Explore
+ [Rest]
    -> Rest
+ [End journey]
    -> DONE

=== CheckInventory ===
Your current status:
- Gold: {gold}
- Health: {health}
- Map: {hasMap: You have it!|You don't have one.}

-> MainHub

=== Explore ===
You explore the surrounding area...
-> MainHub

=== Rest ===
You rest for a while...
-> MainHub
```

### Objectives

#### Objective 1: Work with Numeric Variables

Expand the `Explore` knot to create encounters that change your gold and health values. Create at least three different encounters:

- One that increases gold (finding treasure)
- One that decreases gold (paying a toll or buying something)
- One that decreases health (combat or an accident)

Display the updated values to the player after each encounter and use conditional logic to check if gold or health reach critical thresholds (like gold < 10 or health < 25).

#### Objective 2: Add String Variables and Choices

Add a `VAR location = "forest"` string variable at the top of your story. In the `Explore` knot, offer the player branching choices that change the location to different values (like "mountain", "village", or "cave"). Display the current location in the `MainHub` knot so players know where they are. Make the encounters in Objective 1 vary based on the current location using conditional logic.

#### Objective 3: Implement Boolean Logic

Expand the story to include at least two boolean variables (like `hasMap`, `hasWeapon`, or `knowsSecret`). Create encounters in the `Explore` knot where these booleans can be set to `true` based on player choices. Then, use conditional choices in `MainHub` or `Explore` to show different options based on these boolean values—for example, a choice to "Use the map" only appears if `hasMap` is true.

#### Objective 4: Track Progress with Knot Values

Create a new knot called `SecretArea`. In your `Explore` knot, add a conditional choice that only appears after the player has explored a certain number of times—use the `Explore` knot's visit count to determine this (for example, `{Explore > 3}`). When the player visits `SecretArea`, display different text based on whether it's their first visit or a repeat visit using knot value conditionals.

### Testing Your Story

As you build your story, test it regularly:

- Verify that all variable changes work as expected
- Check that conditional choices appear and disappear correctly
- Ensure you can't get stuck with no choices available
- Confirm that knot visit counters work properly
- Test edge cases like running out of gold or health

> **Important:** Good interactive fiction always gives players meaningful choices. Make sure your conditionals enhance the story rather than restrict it unnecessarily.
