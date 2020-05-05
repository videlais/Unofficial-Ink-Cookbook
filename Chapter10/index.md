# Chapter 10: Tunnels and Threads

- [Chapter 10: Tunnels and Threads](#chapter-10-tunnels-and-threads)
  - [Tunnels](#tunnels)
    - [Tunnel Code Example](#tunnel-code-example)
    - [Tunnels to Tunnels](#tunnels-to-tunnels)
  - [Threads](#threads)
    - [Thread Code Example](#thread-code-example)
    - [Combining Knots](#combining-knots)

**Summary:** In this chapter, you will learn about Tunnels, Threads, and how they can be used in larger projects.

---

## Tunnels

Because of the complex nature of connections between knows and diverts, sometimes a way to move "through" a complex weave is needed. Tunnels provide that.

In Ink, it can often be useful to create a knot that is returned to multiple times throughout a flow. Instead of a complex series of diverts and knots, Ink has functionality to quickly go to a knot and then return called a tunnel.

As it names implies, tunnels are connections between sections where the flow is diverted to a knot or stitch and then returns again. The player passes through the "tunnel" and out the other side back to the same or different place in the story.

```ink
-> Show_Day -> Show_Time -> DONE
```

Tunnels are created using the divert (arrow) to "go to" a knot or stitch and then a second divert after the name of the knot or stitch.

```ink
=== Show_Day ===
Today is {~Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday}
->->
```

To return from the tunnel, use two divert symbols in a row. This will "twice divert" back to the original location.

### Tunnel Code Example

```ink
-> Show_Day -> Show_Time -> DONE

=== Show_Day ===
Today is {~Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday}
->->

=== Show_Time ===
It is {~1|2|3|4|5|6|7|8|9|10|11|12} {~am|pm}
->->
```

In the above example, the first divert `-> Show-Day` moves to the knot **Show_Day**.

Inside this knot, a shuffle alternative is used to select a random day from the existing elements.

Next, a tunnel is returned to via the double-divert, `->->`.

Back to the original place in the code, the next divert, `-> Show_Time` is run. This moves to the knot **Show_Time**.

This uses two shuffles to first time a number between 1 and 12 and then to pick either "am" or "pm".

Next, the tunnel is returned to using another double-divert `->->`.

In order, the above code runs the knot **Show_Day**, returns, runs the **Show_Time**, and then returns again before the story ends with `-> DONE`.

### Tunnels to Tunnels

As tunnels use diverts and knots, it is also possible to include tunnels inside other tunnels. This is completely safe!

```ink
-> One -> Two -> Three -> Four -> Five -> Six -> DONE

=== One ===
It <>
->->

=== Two ===
starts <>
->->

=== Three ===
with <>
->->

=== Four ===
one <>
->->

=== Five ===
thing.
->->

=== Six ===

-> SixOne -> SixTwo -> SixThree -> SixFour ->->

= SixOne
I <>
->->

= SixTwo
don't <>
->->

= SixThree
know <>
->->

= SixFour
why.
->->
```

In the above, complicate example, the story starts with one tunnel as a series of diverts: `-> One -> Two -> Three -> Four -> Five -> Six -> DONE`.

Each numbered knot adds a single word (using glue) and then returns to the tunnel. Finally, the tunnel reaches knot **Six**.

Inside **Six** are four stitches. These are used as part of an internal tunnel. All of these add their own words.

Finally, the inner **Six** tunnel returns back to the original and the story content ends.

Combined together, it creates the following out:

```ink
It starts with one thing.

I don't know why.
```

**Reminder:** The use of `<>` is *glue*. It runs the next line into the current, *gluing* them together. It can be used across knots and stitches to combine output on one line.

## Threads

*Threads* provide a way to "collapse" a weave and "pull together" knots and diverts.

In some ways, threads are the opposite of tunnels and using diverts. Instead of "going out," threads "pull together" content as part of a flow.

To use threading, the divert arrow changes and points in, `<-`.

```ink
<- FirstChoice
<- SecondChoice
<- ThirdChoice
```

Using threads helps separate knots into logical sections of code for the author and developer and then "thread" them all together again.

### Thread Code Example

```ink
This is a thread example:
<- FirstChoice
<- SecondChoice
<- ThirdChoice

=== FirstChoice ===
* Pick me!
-> CollectChoices

=== SecondChoice ===
* No, pick me!
-> CollectChoices

=== ThirdChoice ===
* No, this one! Me!
-> CollectChoices

=== CollectChoices ===
All of the above knots are collected (threaded together) and end up here!
-> DONE
```

In the above example, the story starts and three threads are used: `<- FirstChoice`, `<- SecondChoice`, and `<- ThirdChoice`.

All three of these point to same knot **CollectChoices**, and thus are all "threaded" to that center point.

### Combining Knots

While a common example might use choices, this need not be the case. Threads can also be used for text content.

```ink
This is a thread example:
<- FirstChoice
<- SecondChoice
<- ThirdChoice

=== FirstChoice ===
Show this thing!
-> CollectChoices

=== SecondChoice ===
Show this!
-> CollectChoices

=== ThirdChoice ===
Now show me!
-> CollectChoices

=== CollectChoices ===
-> DONE
```

In fact, the earlier tunnel example could be re-written as example using threads instead:

```ink
<- Show_Day
<- Show_Time

=== Show_Day ===
Today is {~Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday}
-> Update

=== Show_Time ===
It is {~1|2|3|4|5|6|7|8|9|10|11|12} {~am|pm}
-> Update

=== Update ===
-> DONE
```
