// Example 4.12: Basic Conditionals
// Demonstrates comparison operators and simple conditional tests

VAR gold = 50
VAR hasKey = false
VAR health = 75

-> Start

=== Start ===
You check your inventory and assess your situation.

You have {gold} gold coins.

{hasKey: You also have a key in your pocket.}
{not hasKey: You don't have a key yet.}

{health > 80: You're feeling strong and healthy!}
{health >= 50 && health <= 80: Your health is decent.}
{health < 50: You're injured and need to rest.}

{gold >= 100: You're quite wealthy!}
{gold >= 50 && gold < 100: You have a modest amount of gold.}
{gold < 20: You're running low on funds.}

{gold > 30 && not hasKey: You have enough gold to buy a key.}

+ [Find a key]
    ~ hasKey = true
    You found a key on the ground!
    -> Start
    
+ {gold >= 30} [Buy supplies (-30 gold)]
    ~ gold -= 30
    You purchase some supplies.
    -> Start
    
+ [Search for treasure]
    ~ gold += 25
    You found a small treasure! +25 gold
    -> Start
    
+ [Rest and recover]
    ~ health = 100
    You rest and regain your strength.
    -> Start
    
+ {gold < 10 && health < 30} [This situation looks dire...]
    With little gold and poor health, your adventure may be ending.
    -> DONE
    
+ [Continue your journey]
    -> DONE
