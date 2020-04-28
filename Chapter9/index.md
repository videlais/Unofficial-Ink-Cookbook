# Chapter 9: Knot and Function Parameters

- [Chapter 9: Knot and Function Parameters](#chapter-9-knot-and-function-parameters)
  - [Functions](#functions)
  - [Knot Parameters](#knot-parameters)
  - [Ink Functions](#ink-functions)
  - [Passing By Reference](#passing-by-reference)
  - [Variable Naming Issues](#variable-naming-issues)
  - [Built-in Functions](#built-in-functions)
    - [`POW(number, to-the-power-of)`](#pownumber-to-the-power-of)
    - [`RANDOM(min, max)`](#randommin-max)
    - [`FLOOR()`](#floor)
    - [`INT()`](#int)
    - [`FLOAT()`](#float)
    - [`CHOICE_COUNT()`](#choicecount)
    - [`TURNS()`](#turns)
    - [`SEED_RANDOM(seed)`](#seedrandomseed)

**Summary:** In this chapter, you will learn about knot parameters, functions, and the differences between the two.

## Functions

To help with process data, Ink provides ways to pass information between knots and functions. When working with variables, these provide a way to process or test data in different ways.

In programming terminology, a function is some section of code designed around some task. It borrows the term for mathematical functions in which data is changed through applying some known set of rules.

In Ink, the concept of functions come in two ways. The first is in Knot Parameters and then second is in Functions themselves. For Ink, these divisions help authors to think through how to divide up their code and calculations in ways that may be more narrative or mechanically focused depending on their needs.

## Knot Parameters

When working with functions and their related concepts, the most commonly associated term is parameters. In programming terminology, a parameter is some data passed to a function or other function-like programming concept. In Ink, this means that data can be passed to a knot that can then act on it in some way.

Data is passed as a parameter to a knot through including its name and opening and closing parentheses. Within these, a value or the name of an existing variable can be placed. Multiple parameters are separated by commas.

Within the knot itself, the new names for the values passed it as parameters are defined through open and closing parentheses. These new named variables exist within the context of the knot and act like temporary variables -- they can only be used within the knot itself.

```ink
-> Food_Choices("")

=== Food_Choices(previousChoice) ===

{previousChoice != "": (We've already talked about having {previousChoice}.) }

* [Pizza?] He shook his head. "I don't like pizza."
    -> Food_Choices("pizza")

* [Salad?] "Not a salad."
    -> Food_Choices("salad")

* [Nothing?] {"We have to eat something!"|"Stop being silly!"}
    -> Food_Choices("nothing")

* [Sushi?] "Sushi sounds good!"
    We walked to the local sushi place.

-> END
```

## Ink Functions

Functions in Ink act like knots with parameters. They can define the name of variables and those act as temporarily variables within their context. They can also perform small tasks and make calculations using code. However, knots with parameters and function has a small very key difference: function can return data.

Functions are a special type of knot but use the keyword "function." This also enables them to use additional functionality not available to regular knots and stitches: returning data using the "return" keyword.

Similar to many other scripting languages, functions in Ink can be called, perform some task, and then return the result of the task.

```ink
Today is {getRandomDay()}.

=== function getRandomDay() ===
~ return "{~Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday}"
```

However, while functions enable the useful feature of being able to react and respond with a return value, they also have some limitations.

Functions cannot:

- contain stitches
- use diverts or offer choices

Functions can:

- call other functions
- include printed content
- return a value of any type
- recurse safely

## Passing By Reference

Functions in Ink are also capable of another common programming concept called passing by reference. Normally, values are copied when a function is used. Within the function, some action is taken and maybe a value is returned. The values passed to the function, however, do not change inside of the function itself.

Using a concept called passing by reference, values passed to a function can be changed. The term “by reference” takes is meaning from an early programming term of where the location of a variable in computer memory was its reference. By knowing a variable's reference, it was possible to change its value directly.

In Ink, this terminology means that using the keyword "ref", a variable is available to be changed inside of the function. Instead of copying its value, its reference is passed to the function.

```ink
VAR name = "Dan"

The current name is {name}.

The new name is {changeName(name)} {name}.

=== function changeName(ref newName) ===
~ newName = "Fred"
```

## Variable Naming Issues

As was mentioned in the chapter called "It’s All Variable", variables created using the keyword `VAR` are global. This means they can be accessed anywhere in the Flow. This also means that their names are reserved. Two variables cannot have the same name.

In the earlier section explaining how parameters are temporary variables within a knot or function, this means they cannot share names with other, existing variables in a project. Naming variables and parameters, then, becomes a matter of trying to use the most descriptive names for their purpose.

## Built-in Functions

To help with common mathematical operations, Ink has several built-in functions that can be called anywhere in a project. They include the following:

### `POW(number, to-the-power-of)`

The function pow() computes and returns a number multiplied by itself the number of times supplied by the second parameter. It is the to-the-power-of function.

```ink
{ POW(4, 2) }
```

### `RANDOM(min, max)`

The `RANDOM()` function returns a random number between ranges of the minimum and maximum numbers passed to it.

```ink
{ RANDOM(1, 6) }
```

### `FLOOR()`

The `FLOOR()` function rounds down a decimal number to the nearest whole number.

```ink
{ FLOOR(3.14159) }
```

### `INT()`

The `INT()` function converts a decimal number into a whole number by removing its decimal value.

```ink
{ INT(3.01) }
```

### `FLOAT()`

The `FLOAT()` function converts a whole number into a decimal number, adding a decimal value to it.

### `CHOICE_COUNT()`

The `CHOICE_COUNT()` function returns the number of options within the recent section of project.

```ink
* {false} Option A
*  {true} Option B
*  {CHOICE_COUNT() == 1} Option C
```

### `TURNS()`

The `TURNS()` function returns the number of "turns" (user actions).

```ink
{ TURNS() } // 0

* Option 1

{ TURNS() } // 1
```

### `SEED_RANDOM(seed)`

The function `SEED_RANDOM()` accepts a value to "seed" the `RANDOM()` function. This function can be used to "lock" the randomness of a flow from a single value.

```ink
~ SEED_RANDOM(255)
```
