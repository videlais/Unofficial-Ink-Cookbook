You enter the mysterious room.

The value of SecretRoom is {SecretRoom} (not visited yet).

-> SecretRoom

== SecretRoom ==
You're now in the secret room!
The value of SecretRoom is {SecretRoom} (visited once).

+ [Visit again]
    -> SecretRoom
+ [Check the value]
    -> CheckValue

== CheckValue ==
After visiting SecretRoom, its value is {SecretRoom}.

{SecretRoom > 1: You've been to the secret room {SecretRoom} times! }
{SecretRoom == 1: You've been to the secret room once. }
-> END
