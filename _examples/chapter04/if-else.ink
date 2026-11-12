// Example 4.13: If-Else Statements
// Demonstrates if-else conditional logic in multiple formats

VAR health = 75
VAR stamina = 60
VAR mood = "neutral"

-> CheckStatus

=== CheckStatus ===
You take stock of your condition.

# Health Assessment

{health > 80:
    You're feeling healthy and strong. Nothing can stop you!
    ~ mood = "confident"
- else:
    {health >= 50:
        Your health is good. You can handle most challenges.
        ~ mood = "ready"
    - else:
        {health >= 25:
            Your health is low. Be careful!
            ~ mood = "cautious"
        - else:
            You're critically injured! Seek help immediately!
            ~ mood = "desperate"
        }
    }
}

# Stamina Assessment

{stamina > 75:
    You're full of energy and ready for action.
- else:
    {stamina >= 40:
        You have enough stamina to continue.
    - else:
        You're exhausted and need to rest.
    }
}

# Current Mood

Your current mood: {mood}

# What will you do?

+ [Fight a monster]
    {health > 50 && stamina > 30:
        You engage in battle!
        ~ health -= 20
        ~ stamina -= 30
        You defeated the monster but took some damage.
    - else:
        You're too weak to fight. You retreat.
    }
    -> CheckStatus

+ [Rest]
    ~ health += 15
    ~ stamina += 40
    {health > 100:
        ~ health = 100
    }
    {stamina > 100:
        ~ stamina = 100
    }
    You rest and recover some health and stamina.
    -> CheckStatus

+ [Drink a potion]
    ~ health += 30
    {health > 100:
        ~ health = 100
    }
    You drink a healing potion!
    -> CheckStatus

+ [Continue]
    -> DONE
