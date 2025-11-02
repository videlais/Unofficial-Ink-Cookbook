// Basic variable example
// Demonstrates using variables to track state

VAR coins = 0

You find yourself in a mysterious cave. You have {coins} coins.

+ [Search the ground]
    You search carefully and find a gold coin!
    ~ coins = coins + 1
    -> cave_loop

+ [Check behind the rocks]
    Behind the rocks, you discover 3 silver coins!
    ~ coins = coins + 3
    -> cave_loop

+ [Leave the cave]
    You leave with {coins} coins. Not bad!
    -> END

=== cave_loop ===
You now have {coins} coins.

{coins >= 5:
    Wow, you're getting rich! Maybe it's time to leave?
}

+ [Search the ground]
    You find another coin!
    ~ coins = coins + 1
    -> cave_loop

+ [Check behind the rocks]
    You find 2 more coins!
    ~ coins = coins + 2
    -> cave_loop

+ [Leave the cave]
    You leave with {coins} coins. {coins >= 5: Excellent haul!|Not bad!}
    -> END
