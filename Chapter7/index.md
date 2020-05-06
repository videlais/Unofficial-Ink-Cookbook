# Chapter 7: Gather Points

- [Chapter 7: Gather Points](#chapter-7-gather-points)
  - [Gather Points](#gather-points)
    - [Explaining Gather Points](#explaining-gather-points)
    - [Chaining Gathering Points](#chaining-gathering-points)
  - [Labelled Options](#labelled-options)

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

## Labelled Options

Like knots, options can also be labelled. Like what was done with conditional choices, labelled options can work the same way. Code can check to see if an option has been chosen and react accordingly.

While knots and stitches can be used to divert into new story sections, using a weave, with gather points and labelled options, code can be reduced in complexity.
