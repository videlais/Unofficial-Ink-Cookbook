# Chapter 7: Gather Points

- [Chapter 7: Gather Points](#chapter-7-gather-points)
  - [Gather Points](#gather-points)
    - [Explaining Gather Points](#explaining-gather-points)
    - [Chaining Gathering Points](#chaining-gathering-points)
  - [Labelled Options](#labelled-options)
    - [Label Scopes](#label-scopes)
    - [Diverting to Labels](#diverting-to-labels)
    - [Labels and Gathering Point Levels](#labels-and-gathering-point-levels)

**Summary:** In this chapter, you will learn about *gather points*, how they are used, and the shorthand they provide for larger and more complex projects.

---

## Gather Points

Through presenting a series of choices, an author can create a complex path through a story.

```ink
* Choice 1
  ** Choice 1.1
  ** Choice 1.2
* Choice 2
  ** Choice 2.1
  ** Choice 2.2
* Choice 3
  ** Choice 3.1
  ** Choice 3.2
```

One choice can lead to another that connects to a third. These can be both in the same file or across files using the `INCLUDE` keyword.

However, there is often a need to show some output after a choice is made or regardless of how a choice was made. The existing structures for doing such a thing do not work well or are potentially wasteful.

Consider the following example:

```ink
He leaned against the wall and waited. I could tell he was tense and the wrong thing could drive him away.

* "We can make it, just give me a second chance!"
* "I know I messed up, babe, but we can work it out!"
* "Are you really going to give up on five years of a relationship!"
```

In the above code, there are three choices. Each could, potentially, lead to other places using diverts or show more output. However, what if the outcome of all the choices needed to be the same?

One solution might be put the same text under each choice.

```ink
He leaned against the wall and waited. I could tell he was tense and the wrong thing could drive him away.

* "We can make it, just give me a second chance!"
  He paused and shook his head. "We are done. Please leave."
* "I know I messed up, babe, but we can work it out!"
  He paused and shook his head. "We are done. Please leave."
* "Are you really going to give up on five years of a relationship!"
  He paused and shook his head. "We are done. Please leave."
```

However, that's repetitive. There should not be a need to have the exact same text in multiple places!

Another solution might also be to simply have all the choices divert to the same knot:

```ink
He leaned against the wall and waited. I could tell he was tense and the wrong thing could drive him away.

* "We can make it, just give me a second chance!"
  -> Outcome
* "I know I messed up, babe, but we can work it out!"
  -> Outcome
* "Are you really going to give up on five years of a relationship!"
  -> Outcome

=== Outcome ==
He paused and shook his head. "We are done. Please leave."

-> DONE
 ```

While less wasteful than the previous solution, the outcome is still the same: the choices are using the result. While cleaner, in that the code is not as wasteful, there is a far better way to solve this issue.

### Explaining Gather Points

In previous code in the above examples, each choice could potentially branch the code or have used diverts. There needed to be a way to "gather" all the branches together!

In Ink, *gather points* use the minus sign, `-`, and serve as their name suggests, they *gather*.

```ink
He leaned against the wall and waited. I could tell he was tense and the wrong thing could drive him away.

* "We can make it, just give me a second chance!"
* "I know I messed up, babe, but we can work it out!"
* "Are you really going to give up on five years of a relationship!"
-  He paused and shook his head. "We are done. Please leave."
```

Using a *gather point* with a set of choices *gathers* the outcomes together. The result of all of the options would be the same: the gather point! No matter what was picked, all of the choices would "collapse" to the use of the `-` minus sign at the end of the set of choices.

However, this need not always be the case. The use of gather points *gather* all of the *eventual* output together. One usage of gather points is to make choices that all *gather* to a single output. A second usage could be to have output per choice that *eventually gathers* at a single outcome.

```ink
He leaned against the wall and waited. I could tell he was tense and the wrong thing could drive him away.

* "We can make it, just give me a second chance!"
  I took a step forward.
* "I know I messed up, babe, but we can work it out!"
  I tried not to look at his eyes.
* "Are you really going to give up on five years of a relationship!"
  I was trying not to scream at him.
-  He paused and shook his head. "We are done. Please leave."
```

In the above adjusted example, each choice has its own output that make it different than the others. However, the use of the gather point at the end of the set of choices *gathers* all of the eventual output together at the end.

With a gather point in a set of choices, and assuming no diverts are used, the outcome will always arrive at the gather point. After all, its purpose is to *gather* branches in a story.

### Chaining Gathering Points

Gathering points work well when "chained" together. When used with multiple sets of choices (and assuming no diverts are used), each gathering point will always be reached.

A quick way to create conversations where only one choice in a set has a consequence is through using gathering points. For the choice with the consequence, a line of code or additional output could be added, knowing the gathering point will move the story toward the next "chain" of dialogue.

```ink
VAR relationship = 50

"Can you reach that for me?" she asked, motioning up to the mixing bowls at the top of the shelf. Even stretching, and I tried not to look at her as she tried a couple times to reach it, she could not quite get a grip on them.
"Sure," I replied, getting up and walking over. As I reached for the shelf, I thought she would move, but she just stood there. "You gonna step back?"
"Do you want me to?" she asked, her eyes seemingly blinking at me innocently, but the question was more emotionally loaded than simply asking about the bowls.

* "I thought we were over this, J."
  ~ relationship -= 20
* I stood there silently waiting.
- "Fine," she said, a note of frustration in her voice as she finally moved out of my space.

* I considered reminding her that we had broken up two weeks ago and I would be moving away soon.
* Could I turn my back on months together for a new job? Was it more important than our life together?
  ~ relationship += 20
- My hand found the bowls. I pulled them down and handed them over.

She didn't look at me as she answered. "Thanks, Dee," she replied, moving the bowls, and herself, across the room from me.
```

In the above example, there are two sets of choices. However, only one of each set has a consequence for the story. For these choices, the value of *relationship* is changed. Otherwise, the story proceeds to the gathering point.

---

## Labelled Options

Like knots, choices can also be labelled. If a name is put into parentheses before the output of the option, it becomes the *label* for the option.

```ink
As I paused at the door, I heard a noise in the kitchen.

* (investigate) Might as well go see what it is.
* (ignore) "It's nothing, I'm sure," I said.

```

Knots, stitches, and labels all have values. Like what was done with conditional choices, labelled options work the same way. The use of curly brackets can check to see if an option has been chosen and react accordingly.

> **Note:** Labels, like with the name of knots, can be used as if they were variables. When included in curly brackets, the value of the variable is used as if it was a conditional statement. In these cases, 0 is `false` and other values are `true`.

```ink
As I paused at the door, I heard a noise in the kitchen.

* (investigate) Might as well go see what it is.
* (ignore) "It's nothing, I'm sure," I said.
-

* {investigate} I walked to the kitchen.
* {ignore} I walked back to my bedroom.
```

In the above code, if the player picks the option to investigate, the label *investigate* gains the value of 1 (and is thus `true`). If, instead, they pick the option to ignore, choosing the label *ignore*, its value is increased to 1.

A gathering point is then used to *gather* the output together with the minus sign, `-`, at the end of the set of choices.

> **Note:** The use of the gathering point is important in the above example. It serves to *gather* the otherwise potentially branching paths back together before the next set of choices. Without it, the story ends after the first set of choices!

For the next set of choices, the values of the labels are tested. If the player chose to investigate earlier, the label *investigate* will be `true` and a new option will be shown. If the label *ignore* was picked, its option would appear, instead.

When combined with gathering points, labelled options can optimize writing structures where different paths can be picked, gathered, and then tested without needing to use diverts or knots for the same task.

### Label Scopes

In programming terminology, a *scope* is a way of describing access to a variable. If something has a *local* scope, it can only be accessed within its block of code. If it has a *higher* scope, it can be accessed in its block of code and in another. If a variable has a *global* scope, it can be accessed anywhere in the code.

Labels have a *local* scope to the weave block in which they were created. However, like with stitches, they can be accessed through the name of the knots and stitch in which they were created.

For example, to access a stitch, *StitchExample*, inside of a knot, *KnotExample*, it would use the address of `KnotExample.StitchExample`. Both the knot and stitch names are needed, with a period, `.`, between them.

```ink
-> KnotExample.StitchExample

=== KnotExample ===

= StitchExample
Show this!
-> DONE
```

This is also true of labels. They can be accessed through their knot and stitch names.

```ink

-> KnotExample.StitchExample

=== KnotExample ===

= StitchExample
* (LabelExample) This is a label
-
-> DifferentKnot

=== DifferentKnot ===

{KnotExample.StitchExample.LabelExample: You picked the label option! Great job!}

-> DONE
```

In the above code, in order to test the label *LabelExample* (which is in a stitch inside of another knot), its full address is needed. This is `KnotExample.StitchExample.LabelExample`.

In the second knot, **DifferentKnot**, this address is used and the example, once the option "This is a label" is picked by the player, would show the output of "You picked the label option! Great job!".

### Diverting to Labels

All content in Ink is a weave. This means that labels, like knots and stitches, can also be diverted to as well.

For example, it is possible to divert directly to a choice if it has a label.

```ink

-> KnotExample.StitchExample.LabelExample

=== KnotExample ===

= StitchExample
- (LabelExample) Go here!
-> DONE
```

In the above example, the divert address of `KnotExample.StitchExample.LabelExample` is used. This moves directly to the label option of **LabelExample** (which is inside of **KnotExample** and **StitchExample**).

> **Note:** The combination of the words *labelled options* is important. Labels are part of options and thus must use choice syntax. This means that they must use choices, `*`, sticky choices, `+`, or gathering point, `-`, symbols in from of them. The labels are fo the *options*.

While labels are used with choices, when treated as addresses for diverts, they are no longer "choices." After all, if the story has diverted to that exact point, the choice has already been made!

For example, in the following code, the divert `-> LabelExample` is used.

```ink
-> LabelExample

* (LabelExample) This is a label using a gathering point!
  -> DONE
```

The output of the above code, however, would not be a choice *This is a label using a gathering point!*, but the output of "This is a label using a gathering point!". The choice was "made" when the divert happened.

### Labels and Gathering Point Levels

Labels work with any choice syntax. Gathering points *gather* the output of choices and collapse branches to a single point. Through adding a label at any point in a set of choices, it can be diverted to and used as if it was the output.

```ink
He leaned against the wall and waited. I could tell he was tense and the wrong thing could drive him away.

* "We can make it, just give me a second chance!"
  - - (ending) He paused and shook his head. "We are done. Please leave."
* "I know I messed up, babe, but we can work it out!"
  -> ending
* "Are you really going to give up on five years of a relationship!"
  -> ending
-
```

In a revision of earlier code in this chapter, it could be re-written to use a label under the first choice. All other choices, then, could then divert to this label, showing the same output every time.

However, using this more advanced pattern requires two things:

- Using a gathering point at the end of the choices to avoid running out of content.
- Using *second level* gathering point for the label.

Without the second gathering point, the choices would be gathered after the first one. The story would show the first choice *"We can make it, just give me a second chance!"* and then gather before moving to the second set of choices that would then begin with *"I know I messed up, babe, but we can work it out!"*.

With a second level gathering point, it works with the gathering *two levels out.* In other words, instead of gathering at the end of first choice, it works wih the larger set of choices, two levels up from itself.

In the new code, all options divert to the inner label, which is a second level gathering point. As this works with the gathering point of the set of choices, it serves as the output for all of the choices before they are ultimately gathered at the end of the set of choices.
