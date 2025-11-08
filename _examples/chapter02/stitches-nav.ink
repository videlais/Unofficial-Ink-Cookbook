You stand in the town square.
-> Town

== Town ==
= square
The fountain bubbles in the center of the square. Where do you want to go?

+ [Visit the market]
    -> market
+ [Visit the tavern]
    -> tavern
+ [Leave town]
    -> END

= market
The market is bustling with activity. Vendors call out their wares.

* [Buy some supplies]
    You purchase bread and water for your journey.
    -> square
* [Return to square]
    -> square

= tavern
The tavern is warm and inviting. A bard plays in the corner.

* [Order a drink]
    The innkeeper pours you a mug of ale.
    -> square
* [Return to square]
    -> square
