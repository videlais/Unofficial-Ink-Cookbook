// Example 4.15: Conditional Knot Testing
// Demonstrates using knot visit counts in conditional logic

VAR secretsFound = 0

-> CheckProgress

=== CheckProgress ===

# Your Exploration Progress

Secrets discovered: {secretsFound}

{SecretRoom:
    You remember the secret room you discovered earlier.
- else:
    There might be hidden areas you haven't found yet.
}

{SecretRoom > 1:
    You've been to the secret room {SecretRoom} times. You're quite familiar with it now.
}

{HiddenPassage:
    You know about the hidden passage behind the bookshelf.
- else:
    Perhaps there are hidden passages in these old walls?
}

{TreasureVault:
    The treasure vault! What a discovery that was.
}

{SecretRoom && HiddenPassage && TreasureVault:
    You've found all the secrets this place has to offer. You're a master explorer!
}

# What would you like to do?

+ {not SecretRoom} [Search for secrets in the main hall]
    You carefully examine the walls and furniture...
    You found a secret room!
    ~ secretsFound += 1
    -> SecretRoom

+ {SecretRoom && not HiddenPassage} [Look for hidden passages]
    You tap on the walls, listening for hollow sounds...
    Behind the bookshelf, you discover a hidden passage!
    ~ secretsFound += 1
    -> HiddenPassage

+ {HiddenPassage && not TreasureVault} [Follow the hidden passage]
    You navigate the dark passage carefully...
    It leads to a treasure vault!
    ~ secretsFound += 1
    -> TreasureVault

+ {SecretRoom} [Return to the secret room]
    -> SecretRoom

+ {HiddenPassage} [Explore the hidden passage again]
    -> HiddenPassage

+ {TreasureVault} [Visit the treasure vault]
    -> TreasureVault

+ {SecretRoom && HiddenPassage && TreasureVault} [Reflect on your discoveries]
    You've explored every secret this place has to offer. What an adventure!
    -> DONE

+ [Continue exploring]
    {not (SecretRoom && HiddenPassage && TreasureVault):
        There are still secrets to discover. Keep searching!
    - else:
        You've found everything there is to find.
    }
    -> CheckProgress

=== SecretRoom ===
{You enter the secret room.|You return to the secret room.}

{SecretRoom == 1:
    The room is filled with ancient artifacts and mysterious symbols on the walls. This is an incredible discovery!
}

{SecretRoom > 1:
    The familiar artifacts and symbols greet you once again.
}

-> CheckProgress

=== HiddenPassage ===
{You step into the hidden passage.|You enter the hidden passage once more.}

The passage is narrow and dark, but you can see light ahead.

-> CheckProgress

=== TreasureVault ===
{You discover the treasure vault!|You return to the treasure vault.}

{TreasureVault == 1:
    Gold and jewels sparkle in the torchlight. You've struck it rich!
}

{TreasureVault > 1:
    The treasure is still here, glittering magnificently.
}

-> CheckProgress
