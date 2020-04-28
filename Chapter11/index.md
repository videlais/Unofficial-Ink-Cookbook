# Chapter 11: LIST-ing to a Side

- [Chapter 11: LIST-ing to a Side](#chapter-11-list-ing-to-a-side)
  - [LIST](#list)
  - [Automatically Set to False](#automatically-set-to-false)
  - [Enabling Values](#enabling-values)
  - [Built-in Functions](#built-in-functions)
    - [`LIST_COUNT()`](#listcount)
    - [`LIST_MIN()`](#listmin)
    - [`LIST_MAX()`](#listmax)
    - [`LIST_ALL()`](#listall)
    - [`LIST_VALUE()`](#listvalue)
    - [`LIST_INVERT()`](#listinvert)
    - [`LIST_RANDOM()`](#listrandom)
  - [Inclusion Testing](#inclusion-testing)
    - [Manipulating List Values](#manipulating-list-values)
      - [Addition](#addition)
      - [Subtraction](#subtraction)
  - [Conflicting Values and Variable Names](#conflicting-values-and-variable-names)
    - [Comparing LISTS](#comparing-lists)
      - [Less Than](#less-than)
      - [Greater Than](#greater-than)
      - [Greater Than Or Equal To](#greater-than-or-equal-to)
      - [Less Than Or Equal To](#less-than-or-equal-to)
  - [Multi-listed Lists](#multi-listed-lists)

**Summary:** In this chapter, you will learn how to work with LISTs, some of the basic functionality, and how they can be used within projects.

## LIST

Beyond using variables, Ink also provides a data type call a LIST. These store collections of values that can be accessed, changed, and manipulated in different ways in connection to each other.

Along with variables and their different types like temporary and constants, Ink also has a variable type called a LIST. It allows for storing a sequence of things where both the values and their order is important.

```ink
LIST moods = happy, angry, sad
```

Rules for Lists:

- Must contain unique variable names
- Ordering matters
- Positions start with 1 (unless overwritten)
- Will create variables if they do not already exist
- Created variables are set to false

Because lists will create new variables if included and not previous created, this allows for creating a list of possibilities and then having a new, separate variable with the current state.

These can also be used as part of the flow once set earlier, allowing for changing states throughout a story.

## Automatically Set to False

The values used in a `LIST` are automatically set to false. What this means in practice is that any values include in a `LIST` are in it, but do not count toward its total unless they are “enabled,” set to true.

The following code will show a value of 0.

```ink
LIST moods = happy, angry, sad

{ LIST_COUNT(moods) }
```

The function `LIST_COUNT()` returns the total number of enabled entries in a `LIST`. If they are not true, they are not counted toward its total.

## Enabling Values

Values in a `LIST` are considered true if they have opening and closing parentheses around them.

The same code which shown a total of zero will change to three when all of its values are now set to true.

```ink
LIST moods = (happy), (angry), (sad)

{ LIST_COUNT(moods) }
```

## Built-in Functions

For dealing directly with lists, Ink also has several specific functions. As a `LIST` can have both true and false values, each of these functions deals with and understands the entries in a `LIST` in different ways.

### `LIST_COUNT()`

The function `LIST_COUNT()` returns the number of values in the `LIST` that are set to true.

```ink
LIST moods = (happy), angry, (sad)

{ LIST_COUNT(moods) }
```

### `LIST_MIN()`

The function `LIST_MIN()` returns the first true entry in a `LIST` or nothing if there are no true entries in the `LIST`.

```ink
LIST moods = happy, angry, (sad)

{ LIST_MIN(moods) }
```

### `LIST_MAX()`

The function `LIST_MAX()` returns the last true entry in a `LIST` or nothing if there are no true entries in the `LIST`.

```ink
LIST moods = happy, angry, (sad)

{ LIST_MAX(moods) }
```

### `LIST_ALL()`

The function `LIST_ALL()` returns all entries regardless if true or not as comma-separated values.

```ink
LIST moods = happy, angry, (sad)

{ LIST_ALL(moods) }

LIST_RANGE(list_name, min_value, max_value)
```

The function `LIST_RANGE()` returns a selection from a `LIST` starting at the minimum value and extending to the maximum values of true values in the `LIST`. The minimum and maximum values are the numerical values, positions, starting at 1 (unless overwritten).

If the minimum or maximum value is outside the list of values, its nearest correct values is used.

```ink
LIST moods = happy, (angry), sad, melancholy

{ LIST_RANGE(moods, 2, 3) }
```

### `LIST_VALUE()`

The function `LIST_VALUE()` returns the numerical value of a `LIST` entry regardless of if it is true or not.

```ink
LIST moods = happy, angry, sad, melancholy

{ LIST_VALUE(sad) }
```

### `LIST_INVERT()`

The function `LIST_INVERT()` returns a new `LIST` with each entry’s value to its opposite, `true` to `false` and `false` to `true`.

```ink
LIST moods = happy, angry, sad, melancholy

{ LIST_COUNT(moods) }
~ moods = LIST_INVERT(moods)
{ LIST_COUNT(moods) }
```

### `LIST_RANDOM()`

The function `LIST_RANDOM()` returns a random true entry from a `LIST`. If there are no true entries, the function returns nothing.

```ink
LIST moods = (happy), (angry), (sad), (melancholy)

{ LIST_RANDOM(moods) }
```

## Inclusion Testing

Beyond functions to work with `LIST` values, Ink also has special symbols for working with testing for inclusion in a `LIST`. When comparing multiple values, they should be within an opening and closing parentheses.

- `?`: If multiple entries are part of the list and `true`.

```ink
LIST moods = (happy), (angry), (sad), (melancholy)

{ moods ? (happy, angry): Both happy and angry }
```

- `has`: If an entry is part of the list and is true

The keyword has works the same as using the question mark, `?`.

```ink
LIST moods = (happy), (angry), (sad), (melancholy)

{ moods has (happy, angry): Both happy and angry }
```

- `!?`: If multiple entries are not part of the list and not true

The exclamation mark works as a negation to the inclusion, question mark, `?`, symbol.

```ink
LIST moods = happy, angry, sad, melancholy

{ moods !? (happy, angry): Neither happy nor angry }
```

- `hasnt`: If an entry is not part of a list and not `true`

The keyword `hasnt` is the same as using the symbols, `!?`

```ink
LIST moods = happy, angry, sad, melancholy

{ moods hasnt (happy, angry): Neither happy nor angry }
```

### Manipulating List Values

Like other variable values, a `LIST` can also use some of the same mathematical symbols others can. However, a `LIST` can only use values associated with either itself or another `LIST` within the same project.

#### Addition

Adding a value to a `LIST`, `VAR`, or `CONST` using existing `LIST` values works through the `+=` symbol pairing. It means "set the current value to itself plus this new value." When used with `LIST` values, they can be "added" to the existing `LIST`.

```ink
LIST Items = (Dagger), (Lead_Pipe), (Spanner), (Candlestick), (Revolver), (Rope)

LIST clues = Main_Room

~ clues += (Dagger)

Current Clues: {clues}
```

#### Subtraction

Removing values from a `LIST` or using `LIST` values works similar to addition. It uses the `-=` symbols to mean "set the current value to itself minus this new value."

```ink
LIST Items = (Dagger), (Lead_Pipe), (Spanner), (Candlestick), (Revolver), (Rope)

LIST clues = Main_Room

~ Items -= (Dagger)
~ clues += (Dagger)

Current Clues: {clues}
```

## Conflicting Values and Variable Names

One of the rules of `LIST` is that must contain unique variable names. A value cannot exist in two separate `LIST`s. Therefore, when moving values from one `LIST` to another, it is recommended to remove first and then add to the new `LIST`.

```ink
LIST Items = (Dagger), (Lead_Pipe), (Spanner), (Candlestick), (Revolver), (Rope)

LIST clues = Main_Room

~ temp randomClue = LIST_RANDOM(Items)

The random clue is {randomClue}.

~ Items -= randomClue
~ clues += randomClue

Current Clues: {clues}
```

### Comparing LISTS

While Ink supplies the ability to compare two different `LIST`s and their entries, it is not as helpful as it may first seem. Comparing `LIST`s only work on the numerical values of entries. However, the operators `>`, `<`, `>=`, and `<=` all work.

#### Less Than

```ink
LIST_A < LIST_B
```

The smallest value in A is less than the smallest values in B.

#### Greater Than

```ink
LIST_A > LIST_B
```

The smallest value in A is bigger than the largest values in B.

#### Greater Than Or Equal To

```ink
LIST_A >= LIST_B
```

The smallest value in A is at least the smallest value in B, and the largest value in A is at least the largest value in B.

#### Less Than Or Equal To

```ink
LIST_A <= LIST_B
```

The smallest value is A is smaller than all values in B, and the largest value in A smaller than the largest value in B.

## Multi-listed Lists

Once a `LIST` value exists, it can be used by any `LIST` or by a `VAR`, or temp variable. Beyond moving values between `LIST`s, it is also possible to intermix values from `LIST`s once they are created.

In more complex projects, this can be a way to define all possible value in a `LIST` and then use them to define different states or descriptions during the running of a project.

```ink
LIST Items = (Dagger), (Lead_Pipe), (Spanner), (Candlestick), (Revolver), (Rope)
LIST Rooms = (Dining_Room), (Lounge), (Kitchen), (Study), (Hall), (Billiard_Room), (Conservatory), (Ballroom), (Library), (Cellar)

VAR CLUE = ()

~ temp item = LIST_RANDOM(Items)

You found {item}

~ temp room = LIST_RANDOM(Rooms)

You are in the {room}

~ CLUE += item
~ CLUE += room

Current clues are: {CLUE}
```

**Example:**

```ink
LIST allPeople = (Major_Mustard), (Lt_Lemon), (Sam_White)

~ temp randomPerson = LIST_RANDOM(allPeople)

VAR clues = ()
~ clues += randomPerson

Who do you accuse?
* [Major Mustard]
    {checkClues(Major_Mustard):
    - 1:
        It is her!
     -0:
        It is not her!
    }
    -> DONE
* [Lt. Lemon]
    {checkClues(Major_Mustard):
    - 1:
        It is him!
     -0:
        It is not him!
    }
    -> DONE
* [Sam White]
    { checkClues(Sam_White):
    - 1:
        It is them!
     -0:
        It is not them!
    }
    -> DONE

=== function checkClues(x) ===
~ return clues ? x
```
