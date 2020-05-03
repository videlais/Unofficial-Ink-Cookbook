# Chapter 6: Alternatives

- [Chapter 6: Alternatives](#chapter-6-alternatives)
  - [Alternatives](#alternatives)
  - [Sequences](#sequences)
  - [Cycles](#cycles)
  - [Once-Only](#once-only)
  - [Shuffles](#shuffles)
  - [Multi-Line Alternatives](#multi-line-alternatives)
    - [Multi-Line Sequences](#multi-line-sequences)
    - [Multiline Cycles](#multiline-cycles)
    - [Multiline Once-Only](#multiline-once-only)
    - [Multi-line Shuffles](#multi-line-shuffles)
  - [Advanced Shuffles](#advanced-shuffles)
    - [Shuffle Once](#shuffle-once)
    - [Shuffle Stopping](#shuffle-stopping)
    - [Advanced Alternatives](#advanced-alternatives)
      - [Blank Elements](#blank-elements)
      - [Nested Alternatives](#nested-alternatives)
      - [Alternatives and Diverts](#alternatives-and-diverts)
    - [Choice Text and Alternatives](#choice-text-and-alternatives)
  - [Try It](#try-it)

**Summary:** In this chapter, you will learn about alternatives and how to use sequences, cycles, and shuffles.

---

## Alternatives

Along with writing text, Ink also provides a way to create *alternatives*, a programmable way to provide sequences of text, different cycling, and shuffled, or random text from a collection.

In Ink, alternatives are usually text within curly brackets, `{}`. When used with text strings, they can be used to introduce "alternative" text.

Each element in an alternative is separated by the pipe character, `|`. Some alternative forms also use special characters at the start to differentiate their forms from others.

## Sequences

A *sequence* is a series of values. Ink will move from one to another *in sequence* until there are no more to show.

```ink
{What should I do? | What if I didn't say anything? | Should I ask him out?}
```

In the above code, the first element "What should I do?" would be shown. If the alternative is encountered a second time, the element "What if I didn't say anything?" would be shown. If encountered a third time, finally "Should I ask him out?" would be shown.

Using diverts and knots to loop, it is possible to view all entries in a sequence through re-encountering it. Ink will show each element until there are no more.

```ink
-> Freaking_Out

== Freaking_Out ===
+ [Think more about it]
    {What should I do? | What if I didn't say anything? | Should I ask him out?}
    -> Freaking_Out
```

## Cycles

A *cycle* is an alternative that repeats. It "cycles" all of entries in order and them starts back at the first element again.

Cycles start with the ampersand, `&`.

```ink
{&Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday}
```

If a cycle is encountered again, it will move to the next element in order. Using diverts and knots to loop, the entries in the cycle can be shown and then repeated.

```ink
-> New_Day

== New_Day
+ [It's a new day!]
    It was {&Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday}.
    -> New_Day
```

## Once-Only

Instead of cycling text, Ink also provides a "once-only" alternative that runs through its entries and then stops at the end showing nothing. It only runs through its entries "once."

Cycles start with the exclamation point, `!`.

```ink
{!"I don't want you around"|"You need to leave"|"Get out"}, I said.
```

## Shuffles

A *shuffle* is a special type of alternative. Instead of using entries in sequence, it uses them *randomly*. It will pick a new, random element from the entries each time it is encountered.

Shuffles start with a tilde, `~`.

```ink
It was {~Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday}.
```

## Multi-Line Alternatives

Alternatives are often written using curly bracket with entries separated by the pipe character. However, they also have an extended, multiline form as well.

When written in the multi-line format, each element in the alternative is separated by a newline and then a hyphen, `-`. Everything on the line following the hyphen is considered part of the element.

### Multi-Line Sequences

The keyword `stopping` is used as part of a multiline sequence alternative.

```ink
{stopping:
  -  I entered the ancient passage.
  -  I walked into the ancient passage again.
  -  "Hello, ancient passage! We are old friends now."
}
```

### Multiline Cycles

Multiline cycles use the `cycle` keyword.

```ink
{cycle:
  - I waited.
  - I looked around for a moment.
  - I continued to wait.
}
```

### Multiline Once-Only

The once-only alternative used the keyword `once` for multiline usage.

```ink
{once:
  - Could I really win?
  - Dare I continue?
}
```

### Multi-line Shuffles

Multi-line shuffles use the `shuffle` keyword.

```ink
{shuffle:
  - King of Diamonds.
  - King of Spades.
  - King of Hearts
  - King of Clubs
}
```

## Advanced Shuffles

The keyword `shuffle` can be paired with the keywords `once` and `stopping`.

### Shuffle Once

When paired with the keyword `once`, the `shuffle` keyword will pick a random element and then show nothing when used additional times.

```ink
{shuffle once:
  - King of Diamonds.
  - King of Spades.
  - King of Hearts
  - King of Clubs
}
```

### Shuffle Stopping

Using the keywords `shuffle` and `stopping` together shows a random element excluding the last one and then only the last one in additional attempts.

```ink
{shuffle stopping:
  - King of Diamonds.
  - King of Spades.
  - King of Hearts
  - King of Clubs
  - (No more kings.)
}
```

### Advanced Alternatives

Previously, alternatives were shown as part of single usage or as containing merely text. The usage of alternatives extend much more than what has been shown so far!

#### Blank Elements

Alternatives can contain blank elements.

A single element, for example, can be held until the user interacts with a knot a certain number of times before showing it, using the alternative itself to track the number of interactions.

```ink
I walked through each room, looking everything over. My uncle had told me this house was haunted, but I never believed it.

-> Check

== Check ==
+ [Check everything]
    {!||A light suddenly came on by itself!}
    -> Check
```

In the above code, only the selective output "Check everything" will appear until a user makes a choice three times. At the start of the fourth, the text "A light suddenly came on by itself!" will be shown.

The use of the once-only (starting with `!`) also means the text will continue to be shown as the alternative has been run once.

#### Nested Alternatives

Alternatives can also be nested into other alternatives.

```ink
The {~ vampire {~runs|flies} | zombie {~scrambles|crawls} } toward you.
```

There are two shuffles in the above example:

**First Verb Shuffle:**

```ink
{~runs|flies}
```

**Second Verb Shuffle:**

```ink
{~scrambles|crawls}
```

Both of these are inside a larger shuffle:

```ink
{~ vampire | zombie }
```

When encountered, a random element from the larger shuffle will be picked. Then, using one of the inner shuffles, a second element will be picked.

#### Alternatives and Diverts

As alternatives contain text, they can also contain diverts as well.

```ink
I awake on the shore. I am attacked by a <>

{~ ->Shark| ->Crab}

== Shark ==
shark!
-> DONE

== Crab ==
crab!
-> DONE
```

**Reminder:** In the above example, the use of `<>` is glue. It makes the next line run together with the previous.

### Choice Text and Alternatives

Alternatives can be used as part of the choice text of an option. However, to avoid the alternative appearing as a conditional, it is recommended to have some text before the alternative.

```ink
-> GreetShoppers

== GreetShoppers ==
+ Hello. {& Hey there!|Welcome!|Have a good time!}
    -> GreetShoppers
```

## Try It

This chapter’s examples demonstrate the different kinds of alternatives available within Ink.

Alternatives allow you to create very complex stories with looping content, randomization, and lots of other advanced features. Learning how alternatives work can be challenging, but practicing with them will help you figure out how each one works and how they can be combined together to build advanced Ink stories!

We recommend the following practice exercises:

First, create a simple Ink story that uses a sequence. You need a loop of some kind so that your player will visit your sequence at least twice, which means you will probably need to use choices, diverts, and knots as well. (Remember that a sequence will stop at the last value and repeat it once the end of the sequence is reached: you might want to take advantage of that feature in your story’s narrative.) As usual, don’t worry about writing a lengthy story, but try to create one that makes sense.

Next, revise your story to include a cycle and a once-only. Remember that a cycle will repeat the values inside it, while a once-only will show nothing once the last element is reached, so try to revise your story’s narrative so that the new content will make sense.

After that, revise the story again: this time, find a way to include a shuffle in the story. Remember that a shuffle will randomize the values inside it, so you might want to think of something in your story’s narrative that could have a randomized outcome.

As a tip, remember that you can nest alternatives within another: doing so is a common way to use shuffles and allows you to create heavily randomized content!
