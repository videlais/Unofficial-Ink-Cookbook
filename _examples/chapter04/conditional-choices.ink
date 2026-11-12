// Example 4.16: Conditional Choices
// Demonstrates choices that appear based on conditions

VAR hasKey = false
VAR knowsPassword = false
VAR gold = 30
VAR hasMap = false
VAR strength = 50

-> Castle

=== Castle ===
You stand before the imposing castle gate. The stone walls tower above you, and a guard watches from the battlements.

{Inside:
    Having already gained entry once, you know several ways to get inside.
}

Your resources:
- Gold: {gold}
- Strength: {strength}
{hasKey: - A mysterious key}
{knowsPassword: - Knowledge of the password}
{hasMap: - A map of the castle}

How will you try to enter?

+ {hasKey} [Use the key to unlock the gate]
    You approach the gate quietly and insert the key into the lock. It turns smoothly!
    The gate swings open with barely a sound.
    -> Inside

+ {knowsPassword} [Speak the password to the guard]
    You call up to the guard and speak the ancient password: "Illuminus Noctis"
    The guard nods in recognition and signals for the gate to be opened.
    -> Inside

+ {gold >= 50} [Bribe the guard (50 gold)]
    ~ gold -= 50
    You discreetly offer the guard a pouch of gold coins.
    The guard pockets the coins and looks the other way as you slip inside.
    -> Inside

+ {strength >= 75} [Force the gate open]
    ~ strength -= 25
    Using all your might, you force the rusted gate open!
    The guard is too surprised to react in time.
    -> Inside

+ {hasMap && strength >= 40} [Use the map to find a secret entrance]
    ~ strength -= 20
    You consult the map and discover a hidden passage through the old well.
    It's a tight squeeze, but you make it through.
    -> Inside

+ {not hasKey && gold >= 25} [Buy information about a key (25 gold)]
    ~ gold -= 25
    You find a local merchant willing to share information...
    "There's an old key buried under the oak tree near the crossroads," they whisper.
    -> FindKey

+ {not knowsPassword && gold >= 20} [Learn the password (20 gold)]
    ~ gold -= 20
    You pay a former servant who knows the castle's secrets.
    They teach you the password: "Illuminus Noctis"
    ~ knowsPassword = true
    -> Castle

+ {not hasMap && gold >= 15} [Purchase a castle map (15 gold)]
    ~ gold -= 15
    You buy an old map from a traveling cartographer.
    ~ hasMap = true
    It shows hidden passages you never knew existed!
    -> Castle

+ {strength < 60} [Train to increase strength (10 gold)]
    {gold >= 10:
        ~ gold -= 10
        ~ strength += 15
        You spend time training with the local militia. Your strength increases!
    - else:
        You don't have enough gold for training.
    }
    -> Castle

+ [Try to sneak in]
    You attempt to sneak past the guard...
    {strength > 60:
        Your athleticism allows you to climb the wall unseen!
        -> Inside
    - else:
        The guards spot you immediately! You're forced to retreat.
        "Try a different approach," one guard laughs.
    }
    -> Castle

+ [Work to earn gold]
    You spend some time working at the local tavern.
    ~ gold += 15
    You earned 15 gold coins!
    -> Castle

+ [Give up]
    Perhaps this castle isn't meant to be entered today...
    -> DONE

=== FindKey ===
You travel to the crossroads and find the old oak tree. Sure enough, partially buried beneath its roots is an ornate key!

~ hasKey = true

You now have the key to the castle gate.

+ [Return to the castle]
    -> Castle

=== Inside ===
{You've made it inside the castle!|You enter the castle once again.}

{Inside == 1:
    The grand hall stretches before you, lit by flickering torches. Ancient tapestries line the walls, and a grand staircase leads to the upper floors.
    
    Your resourcefulness has paid off!
}

{Inside > 1:
    The familiar grand hall welcomes you back.
}

+ [Explore further]
    Your adventure in the castle continues...
    -> DONE

+ [Return to the gate]
    -> Castle
