VAR hasKey = false
VAR doorLocked = true

You stand before a locked door.

-> CheckDoor

== CheckDoor ==
{hasKey: You have the key. }
{not hasKey: You don't have a key yet. }
{doorLocked: The door is locked. }
{not doorLocked: The door is unlocked! }

+ {not hasKey} [Search for the key]
    You search the area and find a rusty key!
    ~ hasKey = true
    -> CheckDoor
+ {hasKey and doorLocked} [Unlock the door]
    You use the key to unlock the door.
    ~ doorLocked = false
    -> CheckDoor
+ {not doorLocked} [Open the door]
    You open the door and step through.
    -> END
