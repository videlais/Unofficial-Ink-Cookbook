# Chapter 10: Tunnels and Threads

- [Chapter 10: Tunnels and Threads](#chapter-10-tunnels-and-threads)
  - [Tunnels](#tunnels)
    - [Tunnel Code Example](#tunnel-code-example)
  - [Threads](#threads)

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

In the above example, the first divert `-> Show-Day` moves to the know **Show_Day**.

Inside this knot, a shuffle alternative is used to select a random day from the existing elements.

Next, a tunnel is returned to via the double-divert, `->->`.

Back to the original place in the code, the next divert, `-> Show_Time` is run. This moves to the knot **Show_Time**.

This uses two shuffles to first time a number between 1 and 12 and then to pick either "am" or "pm".

Next, the tunnel is returned to using another double-divert `->->`.

In order, the above code runs the knot **Show_Day**, returns, runs the **Show_Time**, and then returns again before the story ends with `-> DONE`.

## Threads

At the same time, threads provide a way to "collapse" a weave and "pull together" knots and diverts.

In some ways, threads are the opposite of tunnels and using diverts. Instead of "going out," threads "pull together" knots and stitches as part of a flow. To use threading, the arrow changes and points in, "<-".

Using threads helps separate knots into logical sections of code for the author and developer and then "thread" them all together again.
