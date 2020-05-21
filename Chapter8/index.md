# Chapter 8: It's All Variable

- [Chapter 8: It's All Variable](#chapter-8-its-all-variable)
  - [Working with Code](#working-with-code)
  - [Single Line](#single-line)
  - [Multiple lines](#multiple-lines)
  - [Variables](#variables)
    - [Types of Data](#types-of-data)
      - [Numbers](#numbers)
      - [Strings](#strings)
      - [Booleans](#booleans)
      - [Text of Diverts](#text-of-diverts)
      - [Knots](#knots)
    - [Types of Variables](#types-of-variables)
      - [Global Variables](#global-variables)
      - [Temporary Variables](#temporary-variables)
      - [Constant Variables](#constant-variables)
  - [Conditional Logic](#conditional-logic)
    - [Chaining Testing (Switch Statements)](#chaining-testing-switch-statements)
    - [Testing Knot Values](#testing-knot-values)
    - [Multiple Conditionals](#multiple-conditionals)
    - [Advanced Choices](#advanced-choices)
    - [Working with Alternatives](#working-with-alternatives)
  - [Try It](#try-it)

**Summary:** In this chapter, you will learn about global, temporary, and constant variables in Ink and how to use them for different purposes.

---

## Working with Code

Like many other scripting languages, Ink also has the concepts of variables. Used to store and react to values during a program, variables in Ink can take different forms and be used for various uses.

When using variables in Ink, more direct coding is required. While variables can be created using their keywords, as covered later in this chapter, changing their values requires knowing more about how Ink handles its own programming.

Previously, programming in Ink consisted of using Knots, Diverts, and Alternatives. These were used to move around in a story or cycle through a collection of values. When working with variables and manipulating their values in Ink, this changes and takes on two different forms: single line or multiple lines.

---

## Single Line

A single line of programming in Ink starts with the tilde character, ~. It signifies that something will happen only on that single line and Ink should show or otherwise parse the next line as it normally work outside of programming.

```ink
~ health = health - 1
```

---

## Multiple lines

For programming that may take multiple lines, opening and closing curly brackets can be used to mark it off within other Ink code. Such usage is for multiple conditional testing (which is covered in this chapter) and extended uses of alternatives. However, it is important to be aware of how it used before it is explained in greater detail later.

```ink
{- health > 0:
    health = health - 1
 else health <= 0:
    You die.
    -> DEATH
}
```

---

## Variables

In programming terminology, a variable is something that can change. Often, the metaphor used is one of a bucket. The variable represents a value when the program is running. The two commons actions are to "look into" the bucket to see its value or to "change" the value that is in the bucket through replacing it or adding more into it.

The values of variables can be shown through using opening and closing curly brackets around them. This allows an easy way to include different values such as statistics for players to see before they make decisions.

```ink
You have {health}.
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

Like testing if a player has visited a knot or stitch a certain number of times, conditional logic can be used to test the values of variables and react accordingly.

The symbols used to compare values are called operators and include the following symbols and testing:

- `<:` Less than
- `>:` Greater than
- `<=:` Less than OR equal to
- `>=` Greater than OR equal to
- `!=:` Not equal
- `==:` Equal
- `&&:` And
- `||:` Or
- `Not:` same as not equal

Conditional logic can be part of multiple lines of code usage in Ink. In these cases, the first conditional logic test must follow the first opening curly bracket.

```ink
VAR drink = 10

-> DrinkMore

=== DrinkMore ===
 + [Drink more?]
    {- drink > 1:
          ~ drink = drink - 1
    }
    -> DrinkMore
```

Conditional logic follows the form of if testing. The use of "if" logic test if that which follows it is true or not. If it is, any code that follows it is also run. If the logic is not true, its instructions are ignored.

```ink
VAR drink = 4

-> DrinkMore

=== DrinkMore ===

The amount of drink left is {drink}.

 + {drink > 0} [Drink more?]
    ~ drink = drink - 1
    -> DrinkMore

 + {drink < 1} [Stop drinking]
    You decide to stop drinking.
    -> DONE
```

Along with the "if" testing is also an alternative, "else." The use of the `else` keyword uses hyphens within a multiple-line block of code. It establishes what should happen if the first conditional logic is not true. If that first test is not true, it then does something. What it can do is either provide some alternative code or additional tests.

**Example:**

```ink
VAR drink = 4
VAR stopDrinking = false

-> DrinkMore

=== DrinkMore ===

The amount of drink left is {drink}.

{drink > 0:
    ~ drink = drink - 1
 - else:
    ~ stopDrinking = true
}

 + {not stopDrinking} [Drink more?]
    -> DrinkMore

 + {stopDrinking} [Stop Drinking]
    -> DONE
```

### Chaining Testing (Switch Statements)

It is possible to "chain" multiple conditional logic tests together, one after another. In these cases, each testing will be run in order from top to bottom and any code associated with the test will be run if any of the tests are true.

In other scripting languages, such usages are sometimes called "switch statements." In Ink, it is possible to use a variable as the initial conditional and have the logic be possible values. In this case, each hyphen is a possible value from the variable with the else keyword as the "default" code to run if the other values are not available.

```ink
VAR drink = 4
VAR stopDrinking = false

-> DrinkMore

=== DrinkMore ===

The amount of drink left is {drink}.

{drink:
    - 0:
        ~ stopDrinking = true
    - 2:
        The drink is almost gone!
         ~ drink = drink - 1
    - else:
        ~ drink = drink - 1
}

 + {not stopDrinking} [Drink more?]
    -> DrinkMore

 + {stopDrinking} [Stop Drinking]
    -> DONE
```

### Testing Knot Values

The value of a knot (0 or 1) can be used to *conditionally* show content.

the choice will show the text or not based on the name of the knot.

Combining diverts and knots, choices can also be conditionally shown. Because Knots have unique names, code can check if they have been visited or not.

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

### Working with Alternatives

It is possible to save the result of an alternative in Ink. However, it cannot be the initial value of a variable. The reason for this is that alternatives collapse their possibilities when played; before the story starts, each alternative is all of its possible values!

Setting an initial default value is a good approach for working with alternatives, though. This value can be then be overridden by a single line of code that changes the value of the variable.

```ink
VAR day = ""

~ day = "{~Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday}"
```

The variable *day* would then retain whatever element was chosen by the shuffle until it was changed again by another line of code or the shuffle was used again in the same way.

---

## Try It

This chapter’s examples show off the power of variables, a concept used in many other scripting languages. Working with variables in Ink will allow you to create content that could be difficult (or even impossible!) to make otherwise. Using variables in your stories will also help you practice for other kinds of programming work.

If you are already familiar with how variables in other coding languages work, it is worth practicing with Ink’s variables to understand the similarities and differences between how Ink handles them in comparison to other languages.

To practice with Ink’s variables, we offer the following exercises:

First, create an Ink story that uses at least two numerical variables.  Display the starting value of both of the variables to your player. Change both of those variables at least once throughout the story and show the new values to your player. Make sure to use other kinds of Ink content, such as choices, knots, and diverts (Chapter 4) as well to create a story that makes sense and is fun to read through!

Next, revise your story and add at least one string to it. Display the starting value of the string to your player at some point in the story. Then, at some point in the story, offer your player a branching set of choices that can change the value of the string to one of at least two different options.  Once the string’s value has been changed, show it to your player again.

Finally, revise your story and add at least one boolean to it. Create at least one place in the story where the value of that boolean can be changed based on your player’s choices. Then, at some point in the story, use conditional logic that tests whether the value of the boolean is true or false and does something based on the value of the variable.
