// Simple knot and stitch example
// Demonstrates basic navigation with knots and stitches

You wake up in an unfamiliar room.

* [Look around]
    -> look_around
* [Try the door]
    -> try_door

=== look_around ===
The room is small and dusty. There's a window and a door.

* [Examine the window]
    -> look_around.window
* [Go to the door]
    -> try_door

= window
The window is locked, but you can see a garden outside.

* [Return to examining the room]
    -> look_around
* [Try the door instead]
    -> try_door

=== try_door ===
You try the door handle.

* [Push]
    The door swings open! You're free!
    -> END
    
* [Pull]
    The door doesn't budge.
    * * [Try pushing instead]
        The door swings open! You're free!
        -> END
    * * [Give up]
        You sit down, defeated.
        -> END
