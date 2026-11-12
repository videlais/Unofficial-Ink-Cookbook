VAR enemyHealth = 50
CONST SWORD_DAMAGE = 10
CONST CRIT_DAMAGE = 20

Enemy health: {enemyHealth}

-> Fight

== Fight ==
+ [Normal attack ({SWORD_DAMAGE} damage)]
    ~ enemyHealth = enemyHealth - SWORD_DAMAGE
    You deal {SWORD_DAMAGE} damage! Enemy health: {enemyHealth}
    {enemyHealth <= 0: -> Victory }
    -> Fight
+ [Critical strike ({CRIT_DAMAGE} damage)]
    ~ enemyHealth = enemyHealth - CRIT_DAMAGE
    Critical hit for {CRIT_DAMAGE} damage! Enemy health: {enemyHealth}
    {enemyHealth <= 0: -> Victory }
    -> Fight

== Victory ==
Victory! The enemy is defeated!
-> END
