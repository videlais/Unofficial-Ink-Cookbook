VAR gold = 100
VAR itemPrice = 25

You have {gold} gold coins.

-> Shop

== Shop ==
+ [Buy a sword ({itemPrice} gold)]
    ~ gold = gold - itemPrice
    You buy the sword. Gold remaining: {gold}
    -> Shop
+ [Sell an item (+15 gold)]
    ~ gold = gold + 15
    You sell an old item. Gold now: {gold}
    -> Shop
+ [Leave shop]
    You leave with {gold} gold.
    -> END
