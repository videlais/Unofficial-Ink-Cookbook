---
title: "LIST-ing to a Side"
order: 11
chapter_number: 11
layout: chapter
---

# Chapter 11: LIST-ing to a Side

**Learning Objectives:** By the end of this chapter, you will be able to:

- Create and manipulate LISTs for tracking collections of values
- Apply built-in LIST functions including LIST_COUNT(), LIST_MIN(), and LIST_MAX()
- Implement list operations for addition, subtraction, and intersection
- Design state machines using LISTs to model changing conditions
- Construct multi-listed lists for tracking object properties across categories
- Evaluate list containment and equality for conditional logic

- [Chapter 11: LIST-ing to a Side](#chapter-11-list-ing-to-a-side)
  - [LIST](#list)
  - [Automatically Set to `false`](#automatically-set-to-false)
  - [Enabling Values](#enabling-values)
  - [Built-in Functions](#built-in-functions)
    - [`LIST_COUNT()`](#list_count)
    - [`LIST_MIN()`](#list_min)
    - [`LIST_MAX()`](#list_max)
    - [`LIST_ALL()`](#list_all)
    - [`LIST_RANGE()`](#list_range)
    - [`LIST_VALUE()`](#list_value)
    - [`LIST_INVERT()`](#list_invert)
    - [`LIST_RANDOM()`](#list_random)
  - [Inclusion Testing](#inclusion-testing)
    - [Manipulating List Values](#manipulating-list-values)
      - [Addition](#addition)
      - [Subtraction](#subtraction)
      - [Setting Multiple Values](#setting-multiple-values)
  - [Conflicting Values and Variable Names](#conflicting-values-and-variable-names)
  - [Comparing LISTS](#comparing-lists)
    - [Equality Testing](#equality-testing)
    - [Containment vs Equality](#containment-vs-equality)
    - [Less Than](#less-than)
      - [Greater Than](#greater-than)
      - [Greater Than Or Equal To](#greater-than-or-equal-to)
      - [Less Than Or Equal To](#less-than-or-equal-to)
  - [List Intersection](#list-intersection)
  - [Using Lists as State Machines](#using-lists-as-state-machines)
  - [Using Lists for Flags and Tracking](#using-lists-for-flags-and-tracking)
  - [Multi-listed Lists](#multi-listed-lists)
    - [Tracking Objects with Lists](#tracking-objects-with-lists)
    - [Tracking Multiple Properties](#tracking-multiple-properties)
  - [Advanced: Custom List Values](#advanced-custom-list-values)
  - [Practical Example: Inventory and State Management](#practical-example-inventory-and-state-management)
  - [Try It](#try-it)

**Summary:** In this chapter, you will learn how to work with LISTs, some of the basic functionality, and how they can be used within projects.

---

## LIST

Beyond using variables, Ink also provides a data type call a `LIST`. These store collections of values that can be accessed, changed, and manipulated in different ways in connection to each other.

```ink
LIST moods = happy, angry, sad
```

Rules for Lists:

- Must contain unique variable names
- Ordering matters
- Positions start with 1 (unless overwritten)
- Will create variables if they do not already exist
- Created variables are set to `false`

Because lists will create new variables if included and not previous created, this allows for creating a list of possibilities and then having a new, separate variable.

These can also be used as part of the flow once set earlier, allowing for changing states throughout a story.

---

## Automatically Set to `false`

The values used in a `LIST` are automatically set to `false`. What this means in practice is that any values include in a `LIST` are in it, but do not count toward its total unless they are "enabled," set to true.

The following code will show a value of 0.

```ink
LIST moods = happy, angry, sad

{ LIST_COUNT(moods) }
```

> **Note:** function `LIST_COUNT()` returns the total number of enabled entries in a `LIST`. If they are not `true`, they are not counted toward its total.

## Enabling Values

Values in a `LIST` are considered `true` if they have opening and closing parentheses around them.

The same code which shown a total of zero will change to three when all of its values are now set to `true`.

```ink
LIST moods = (happy), (angry), (sad)

{ LIST_COUNT(moods) }
```

---

## Built-in Functions

For dealing directly with lists, Ink also has several specific functions. As a `LIST` can have both `true` and `false` values, each of these functions deals with and understands the entries in a `LIST` in different ways.

### `LIST_COUNT()`

The function `LIST_COUNT()` returns the number of values in the `LIST` that are set to `true` .

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
```

This is particularly useful when you want to access the complete set of possible values in a list, rather than just the currently enabled ones.

### `LIST_RANGE()`

The function `LIST_RANGE()` returns a selection from a `LIST` starting at the minimum value and extending to the maximum values. The minimum and maximum values are the numerical values, positions, starting at 1 (unless overwritten).

If the minimum or maximum value is outside the list of values, its nearest correct values is used.

```ink
LIST moods = happy, (angry), sad, melancholy

{ LIST_RANGE(moods, 2, 3) }
```

You can also use `LIST_RANGE` with `LIST_ALL()` to get a slice of all possible values:

```ink
LIST primeNumbers = two, three, five, seven, eleven, thirteen, seventeen, nineteen

{LIST_RANGE(LIST_ALL(primeNumbers), 3, 6)} // five, seven, eleven, thirteen
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

The function `LIST_RANDOM()` returns a random `true` entry from a `LIST`. If there are no `true` entries, the function returns nothing.

```ink
LIST moods = (happy), (angry), (sad), (melancholy)

{ LIST_RANDOM(moods) }
```

---

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

Trying to add an entry that's already in the list does nothing. Trying to remove an entry that's not there also does nothing. Neither produces an error, and a list can never contain duplicate entries.

#### Setting Multiple Values

You can assign multiple values to a list at once using parentheses:

```ink
LIST DoctorsInSurgery = Adams, Bernard, Cartwright, Denver, Eamonn

~ DoctorsInSurgery = (Adams, Bernard)  // Only Adams and Bernard are now true
```

You can also assign the empty list to clear a list out:

```ink
~ DoctorsInSurgery = ()  // Everyone has gone home
```

And you can add or remove multiple entries at once:

```ink
~ DoctorsInSurgery += (Eamonn, Denver)
~ DoctorsInSurgery -= (Adams, Bernard)
```

---

## Conflicting Values and Variable Names

One of the rules of `LIST` is that they must contain unique variable names. A value cannot exist in two separate `LIST`s! Therefore, when moving values from one `LIST` to another, it is recommended to remove first and then add to the new `LIST`.

```ink
LIST Items = (Dagger), (Lead_Pipe), (Spanner), (Candlestick), (Revolver), (Rope)

LIST clues = Main_Room

~ temp randomClue = LIST_RANDOM(Items)

The random clue is {randomClue}.

~ Items -= randomClue
~ clues += randomClue

Current Clues: {clues}
```

## Comparing LISTS

Ink provides several ways to compare lists. Some comparisons test for equality or containment, while others compare the numerical values of entries.

### Equality Testing

Testing multi-valued lists is slightly more complex than single-valued ones. Equality (`==`) means 'set equality' - that is, all entries are identical.

```ink
LIST DoctorsInSurgery = (Adams), (Bernard), Cartwright

{ DoctorsInSurgery == (Adams, Bernard):
    Dr Adams and Dr Bernard are having a loud argument in one corner.
}
```

If Dr Cartwright is also present, the two won't argue, as the lists being compared won't be equal - DoctorsInSurgery will have a Cartwright that the list (Adams, Bernard) doesn't have.

Not equals (`!=`) works as expected:

```ink
{ DoctorsInSurgery != (Adams, Bernard):
    At least Adams and Bernard aren't arguing.
}
```

### Containment vs Equality

The `?` (or `has`) operator tests for containment, not equality:

```ink
{ DoctorsInSurgery ? (Adams, Bernard):
    Dr Adams and Dr Bernard are present (and possibly others too).
}
```

This is different from equality because it only checks if Adams and Bernard are in the list, not whether they're the *only* ones in the list.

### Less Than

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

The smallest value in A is smaller than all values in B, and the largest value in A is smaller than the largest value in B.

> **Note:** These comparison operators work on the numerical values of list entries, not on containment. They're most useful when using lists as state machines where the order matters.

---

## List Intersection

The intersection operator (`^`) allows you to find the overlap between two lists. This returns a new list containing only the values that appear in both lists.

```ink
LIST CoreValues = strength, courage, compassion, greed, nepotism, self_belief, delusions_of_godhood
VAR desiredValues = (strength, courage, compassion, self_belief)
VAR actualValues = (greed, nepotism, self_belief, delusions_of_godhood)

{desiredValues ^ actualValues} // prints "self_belief"
```

The result is a new list, so you can test it:

```ink
{desiredValues ^ actualValues: 
    The new president has at least one desirable quality.
}

{LIST_COUNT(desiredValues ^ actualValues) == 1: 
    Correction, the new president has only one desirable quality. 
    {desiredValues ^ actualValues == self_belief: 
        It's the scary one.
    }
}
```

This is particularly useful for checking if there's "some overlap" between lists, which is different from the `?` operator that checks if one list entirely contains another.

---

## Using Lists as State Machines

One of the most powerful uses of lists is as state machines. Each list entry represents a state, and you can move between states using simple operations.

```ink
LIST KettleState = cold, boiling, recently_boiled

VAR kettleState = cold

* [Turn on kettle]
    The kettle begins to bubble and boil.
    ~ kettleState = boiling
    
* {kettleState == boiling} [Turn off kettle]
    You turn off the kettle.
    ~ kettleState = recently_boiled
    
* {kettleState == recently_boiled} [Make tea]
    Perfect timing for tea!
```

You can use `++` and `--` to step through states:

```ink
LIST VolumeLevel = off, quiet, medium, loud, deafening

VAR volume = quiet

* [Turn up volume]
    ~ volume++
    {volume == deafening:
        The sound is overwhelming!
    - else:
        The volume increases.
    }
```

When a list is used as a state machine, it typically contains only one value at a time, representing the current state.

---

## Using Lists for Flags and Tracking

Lists are excellent for tracking game flags - things that have happened or been discovered. Unlike using multiple boolean variables, a list keeps everything organized in one place.

```ink
LIST GameEvents = foundSword, openedCasket, metGorgon, solvedRiddle

VAR completedEvents = ()

* [Open the casket]
    You open the ancient casket with a creak.
    ~ completedEvents += openedCasket
    {completedEvents ? foundSword:
        You place the sword inside carefully.
    - else:
        It's empty. You'll need to find something to put in it.
    }

* {completedEvents ? openedCasket && not completedEvents ? foundSword}
    [Search for a sword]
    After searching, you find an ancient sword!
    ~ completedEvents += foundSword
```

You can test for multiple flags at once:

```ink
{completedEvents ? (foundSword, openedCasket, solvedRiddle):
    With the sword placed in the casket and the riddle solved, the door opens!
}
```

This pattern is much cleaner than having separate variables for each flag and manually checking them all.

---

## Multi-listed Lists

One of the most powerful features of lists is that a single variable can contain values from multiple different list families. This allows you to use lists for world modeling and object tracking.

### Tracking Objects with Lists

You can define lists for different types of things, then combine them to track what's where:

```ink
LIST Characters = Alfred, Batman, Robin
LIST Props = champagne_glass, newspaper

VAR BallroomContents = (Alfred, Batman, newspaper)
VAR HallwayContents = (Robin, champagne_glass)

=== function describe_room(roomState)
    {roomState ? Alfred: Alfred is here, standing quietly in a corner.}
    {roomState ? Batman: Batman's presence dominates all.}
    {roomState ? Robin: Robin is all but forgotten.}
    {roomState ? champagne_glass: A champagne glass lies discarded on the floor.}
    {roomState ? newspaper: A newspaper headline screams WHO IS THE BATMAN?}

{describe_room(BallroomContents)}
```

This produces:

```
Alfred is here, standing quietly in a corner.
Batman's presence dominates all.
A newspaper headline screams WHO IS THE BATMAN?
```

You can then move things between rooms:

```ink
* [Move to hallway]
    ~ BallroomContents -= Batman
    ~ HallwayContents += Batman
    Batman strides into the hallway.
```

### Tracking Multiple Properties

You can also use multi-valued lists to track different properties of the same object:

```ink
LIST OnOff = on, off
LIST HotCold = cold, warm, hot

VAR kettleState = (off, cold)

=== function turnOnKettle()
    {kettleState ? hot:
        You turn on the kettle, but it immediately flips off again.
    - else:
        The water in the kettle begins to heat up.
        ~ kettleState -= off
        ~ kettleState += on
    }

=== function can_make_tea()
    ~ return kettleState ? (hot, off)
```

Here, `kettleState` tracks both whether the kettle is on/off AND whether it's hot/cold simultaneously. This is much cleaner than having two separate variables.

To make changing states easier, you can create a helper function:

```ink
=== function changeStateTo(ref stateVariable, stateToReach)
    // Remove all states of this type
    ~ stateVariable -= LIST_ALL(stateToReach)
    // Put back the state we want
    ~ stateVariable += stateToReach

~ changeStateTo(kettleState, on)
~ changeStateTo(kettleState, warm)
```

---

## Advanced: Custom List Values

By default, list values start at 1 and increment by 1, but you can specify your own numerical values:

```ink
LIST PrimeNumbers = two = 2, three = 3, five = 5, seven = 7, eleven = 11

{LIST_VALUE(seven)}  // 7
```

If you specify a value but not the next one, Ink will assume an increment of 1:

```ink
LIST PrimeNumbers = two = 2, three, five = 5
// 'three' will automatically be 3
```

This is useful when the numerical values have meaning in your game, such as damage values, prices, or difficulty levels.

---

## Practical Example: Inventory and State Management

Here's a practical example showing how to use lists for a simple inventory and puzzle system:

```ink
LIST Inventory = (none), key, torch, rope, map
LIST RoomItems = (chest), (door), (window)
LIST DoorState = locked, unlocked, open

VAR playerInventory = ()
VAR currentRoom = (chest, door)
VAR doorState = locked

-> room

=== room ===
You are in a dark room.
{currentRoom ? chest: There is a wooden chest here.}
{currentRoom ? door: There is a locked door to the north.}
{currentRoom ? window: A window lets in some light.}

- (choices)
* {currentRoom ? chest && playerInventory !? key} [Search the chest]
    You search the chest and find a key!
    ~ playerInventory += key
    ~ currentRoom -= chest
    -> choices

* {currentRoom ? door && doorState == locked && playerInventory ? key}
    [Unlock the door]
    You use the key to unlock the door.
    ~ doorState = unlocked
    -> choices

* {currentRoom ? door && doorState == unlocked} [Open the door]
    You open the door and escape!
    ~ doorState = open
    -> escaped

* {playerInventory != ()} [Check inventory]
    You are carrying: {playerInventory}.
    -> choices

+ {choices > 2} [Wait]
    Time passes...
    -> choices

=== escaped ===
You have escaped! Congratulations!
-> END
```

This example demonstrates:
- Using lists for inventory tracking
- Using lists for room contents
- Using lists as state machines (door state)
- Testing list contents for conditional choices
- Adding and removing items from lists

---

## Try It

Lists are one of Ink's most powerful features, but they take practice to master. Here are some exercises to help you understand them better:

**Exercise 1: Basic List Operations**

Create a simple mood tracker:
- Define a LIST of different moods (happy, sad, angry, excited, calm)
- Start with one mood active
- Create choices that change the mood
- Display the current mood to the player
- Try using `++` and `--` to move between moods in order

**Exercise 2: Inventory System**

Build a basic inventory system:
- Create a LIST of items the player can find
- Create a VAR to hold the player's current inventory
- Add choices to pick up items (add them to inventory)
- Add choices to use or drop items (remove them from inventory)
- Display the inventory contents
- Create a conditional choice that only appears when the player has a specific item

**Exercise 3: Multi-Property Tracking**

Create an object with multiple states:
- Define two LISTs: one for on/off states, one for temperature states
- Create a variable that tracks both properties
- Write functions to change each property independently
- Create conditional text that reacts to different combinations of states

**Exercise 4: Flag Tracking**

Build a simple quest system:
- Create a LIST of quest events (talked_to_guard, found_key, opened_chest, etc.)
- Track which events have been completed
- Create choices that only appear after certain events are completed
- Use the `?` operator to check for multiple completed events before showing a final choice

**Exercise 5: Advanced Challenge**

Combine everything you've learned:
- Create a mystery game with suspects, locations, and clues as separate LISTs
- Track which clues have been found
- Track suspect locations
- Use list intersection to find overlaps (e.g., which suspects were in a certain location AND have a certain clue)
- Create a final accusation that checks if the player has gathered enough evidence

The key to mastering lists is understanding when to use them as state machines (one value at a time), flags (multiple values tracking what's happened), or properties (mixing values from different list families). Experiment with all three approaches!
