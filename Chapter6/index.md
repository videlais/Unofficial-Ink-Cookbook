# Chapter 6: Alternatives

- [Chapter 6: Alternatives](#chapter-6-alternatives)
  - [Alternatives](#alternatives)
  - [Cycles](#cycles)
  - [Once-Only](#once-only)
  - [Shuffles](#shuffles)
  - [Multi-block Alternatives](#multi-block-alternatives)
    - [Sequences](#sequences)
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

## Alternatives

Along with writing text, Ink also provides a way to create alternatives, a programmable way to provide sequences of text, different cycling, and shuffled, or random text from a collection.

In Ink, Alternatives are usually text within curly brackets, `{}`. They have already been introduced as part of determining if a knot (or stitch) has been visited. When used with text strings, they can be used to introduce "alternative" text.
Sequences

```ink
-> Freaking_Out

== Freaking_Out ===
+ [Think more about it]
    {What should I do? | What if I didn't say anything? | Should I ask him out?}
    -> Freaking_Out
```

By default, the values within the curly brackets will move in sequence from one to another until it reaches the end. It will then stop at the last value and repeat it.

## Cycles

```ink
-> New_Day

== New_Day
+ [It's a new day!]
    It was {&Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday}.
    -> New_Day
```

To have the text strings repeat, create a "cycle" of values using the `&` symbol within the curly brackets.

## Once-Only

Instead of cycling text, Ink also provides a "once-only" alternative that runs through its entries and then stops at the end showing nothing. It only runs through its entries "once."

```ink
{!"I don't want you around"|"You need to leave"|"Get out"}, I said.
```

## Shuffles

```ink
It was {~Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday}.
```

Within alternatives, entries can also be selected at random. This is called a shuffle. It uses the tilde, `~`.

**Example:**

```ink
It was {~Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday}.

I was unsure about asking him out on a date.

CHAPTER 1: ASKING HIM OUT

-> Chapter_1

=== Chapter_1 ===

{&What should I do? | What if I didn't say anything? | Should I ask him out?}

+ {Chapter_1} [Did he even like guys?]
    -> Chapter_1

* {Chapter_1} I should just do it!
    I let it go for weeks. Finally, I asked him out.
    -> Chapter_2

=== Chapter_2 ===
CHAPTER 2: GETTING READY

Why hadn't I thought about what I was going to wear?

Here I am, 30 minutes before the date and I haven't picked out my clothes!
```

## Multi-block Alternatives

Alternatives are often used as part of bracket entries. However, they also have an extended, multiline as well.

### Sequences

The keyword stopping is used as part of a multiline sequence alternative.

```ink
{stopping:
  -  I entered the ancient passage.
  -  I walked into the ancient passage again.
  -  "Hello, ancient passage! We are old friends now."
}
```

### Multiline Cycles

Multiline cycles use the cycle keyword.

```ink
{cycle:
  - I waited.
  - I looked around for a moment.
  - I continued to wait.
}
```

### Multiline Once-Only

The once-only alternative used the keyword once for multiline usage.

```ink
{once:
  - Could I really win?
  - Dare I continue?
}
```

### Multi-line Shuffles

Mult-line shuffles use the shuffle keyword.

```ink
{shuffle:
  - King of Diamonds.
  - King of Spades.
  - King of Hearts
  - King of Clubs
}
```

## Advanced Shuffles

The keyword shuffle can be paired with the keywords once and stopping.

### Shuffle Once

When paired with the keyword once, the shuffle will pick a random entry and then show nothing when used additional times.

```ink
{shuffle once:
  - King of Diamonds.
  - King of Spades.
  - King of Hearts
  - King of Clubs
}
```

### Shuffle Stopping

Using the keywords shuffle and stopping together shows a random entry excluding the last one and then only the last one in additional attempts.

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

Previously, alternatives were shown as part of single usage or as containing merely text. The usage of alternatives extend much more than what has been shown so far.

#### Blank Elements

Alternatives can contain blank elements.

A single element, for example, can be held until the user interacts with a section or knot a certain number of times before showing, using the alternative itself to track the number of interactions.

```ink
I walked through each room, looking everything over. My uncle had told me this house was haunted, but I never believed it.

-> Check

== Check ==
+ [Check everything]
    {!||A light suddenly came on by itself!}
    -> Check
```

#### Nested Alternatives

Alternatives can be nested into other alternatives.

```ink
The {~ vampire {~runs|flies} | zombie {~scrambles|crawls} } toward you.
```

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

### Choice Text and Alternatives

Alternatives can be used as part of the choice text of an option. However, to avoid the alternative appearing as a conditional, it is recommended to have some text before the alternative.

```ink
-> GreetShoppers

== GreetShoppers ==
+ Hello. {& Hey there!|Welcome!|Have a good time!}
    -> GreetShoppers
```

## Try It

This chapter’s examples demonstrate the different kinds of alternatives available within Ink. Alternatives allow you to create very complex stories with looping content, randomization, and lots of other advanced features. Learning how alternatives work can be challenging, but practicing with them will help you figure out how each one works and how they can be combined together to build advanced Ink stories.

We recommend the following practice exercises:

First, create a simple Ink story that uses a sequence. You need a loop (Chapter 4) of some kind so that your player will visit your sequence at least twice, which means you will probably need to use choices, diverts, and knots (Chapter 4) as well. Remember that a sequence will stop at the last value and repeat it once the end of the sequence is reached: you might want to take advantage of that feature in your story’s narrative. As usual, don’t worry about writing a lengthy story, but try to create one that makes sense.

Next, revise your story to include a cycle and a once-only. Remember that a cycle will repeat the values inside it, while a once-only will show nothing once the last entry is reached, so try to revise your story’s narrative so that the new content will make sense.

After that, revise the story again: this time, find a way to include a shuffle in the story. Remember that a shuffle will randomize the values inside it, so you might want to think of something in your story’s narrative that could have a randomized outcome. As a tip, remember that you can nest alternatives within another: doing so is a common way to use shuffles and allows you to create heavily randomized content.
