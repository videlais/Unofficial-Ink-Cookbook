VAR health = 100
VAR playerName = "Adventurer"

Welcome, {playerName}! Health: {health}

-> Battle

== Battle ==
+ [Attack]
    You attack the enemy! They counter-attack.
    ~ health = health - 20
    Your health: {health}
    {health <= 0: You've been defeated! -> GameOver }
    -> Battle
+ {health > 50} [Run away]
    You flee to safety with {health} health remaining.
    -> END

== GameOver ==
Game Over. Final health: {health}
-> END
