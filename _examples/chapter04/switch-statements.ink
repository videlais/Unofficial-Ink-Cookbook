// Example 4.14: Switch Statements
// Demonstrates switch-style conditional testing

VAR currentRoom = "kitchen"
VAR suspicion = 3
VAR timeOfDay = 2

-> ExploreHouse

=== ExploreHouse ===

# Current Location

{currentRoom:
    - "kitchen":
        You're in the kitchen. The smell of fresh bread fills the air. A large table dominates the center of the room.
    - "bedroom":
        You're in the bedroom. A soft bed beckons, and moonlight streams through the window.
    - "cellar":
        You're in the dark cellar. It's damp and cold. Strange sounds echo from the corners.
    - "library":
        You're in the library. Towering bookshelves line the walls, filled with ancient tomes.
    - "attic":
        You're in the dusty attic. Old furniture and forgotten treasures are scattered about.
    - else:
        You're somewhere else entirely. How did you get here?
}

# Guard's Attitude

{suspicion:
    - 0:
        The guard trusts you completely and waves you through.
    - 1:
        The guard is slightly wary of you but lets you pass.
    - 2:
        The guard is slightly wary of you but lets you pass.
    - 3:
        The guard is suspicious of your motives and watches you carefully.
    - 4:
        The guard is suspicious of your motives and watches you carefully.
    - 5:
        The guard considers you a threat and keeps their hand on their weapon.
    - 6:
        The guard considers you a threat and keeps their hand on their weapon.
    - else:
        The guard treats you as an enemy!
}

# Time of Day

{timeOfDay:
    - 0:
        It's the dead of night. Everything is quiet.
    - 1:
        Dawn is breaking. Early light filters in.
    - 2:
        It's mid-morning. The house is bright and active.
    - 3:
        Afternoon shadows grow long.
    - 4:
        Evening approaches. Lights are being lit.
    - else:
        Time has lost all meaning here.
}

# Where to next?

+ [Go to the kitchen]
    ~ currentRoom = "kitchen"
    -> ExploreHouse

+ [Go to the bedroom]
    ~ currentRoom = "bedroom"
    -> ExploreHouse

+ [Go to the cellar]
    ~ currentRoom = "cellar"
    ~ suspicion += 1
    Descending to the cellar makes the guard more suspicious...
    -> ExploreHouse

+ [Go to the library]
    ~ currentRoom = "library"
    -> ExploreHouse

+ [Go to the attic]
    ~ currentRoom = "attic"
    ~ suspicion += 1
    Heading to the attic raises the guard's suspicion...
    -> ExploreHouse

+ [Wait (advance time)]
    ~ timeOfDay += 1
    Time passes...
    -> ExploreHouse

+ [Be friendly to the guard]
    {suspicion > 0:
        ~ suspicion -= 1
        Your friendly demeanor reduces the guard's suspicion.
    - else:
        The guard already trusts you completely.
    }
    -> ExploreHouse

+ [Leave the house]
    You exit the house.
    -> DONE
