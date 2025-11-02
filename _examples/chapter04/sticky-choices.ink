// Simple sticky choice example
// Demonstrates how sticky choices (+) work in Ink

"What's your favorite color?" the wizard asks.

+ [Red]
    "Red, like fire and passion!" you declare.
    The wizard nods approvingly.
    -> choice_made

+ [Blue]
    "Blue, like the endless sky," you say thoughtfully.
    The wizard smiles.
    -> choice_made

+ [Green]
    "Green, the color of life and growth," you respond.
    The wizard's eyes twinkle.
    -> choice_made

=== choice_made ===
"An excellent choice," the wizard says. "Would you like to reconsider?"

+ [Yes, let me choose again]
    The wizard waves their hand.
    -> DONE

+ [No, I'm happy with my choice]
    "Very well," the wizard says with a knowing smile.
    -> END
