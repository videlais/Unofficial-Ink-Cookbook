// Example 4.17: Variables with Alternatives
// Demonstrates combining variables and alternatives for dynamic content

VAR currentWeather = ""
VAR mood = "neutral"
VAR encounterType = ""
VAR npcGreeting = ""

-> Start

=== Start ===
You wake up and begin a new day of adventure.

// Assign random weather using an alternative
~ currentWeather = "{~sunny|rainy|cloudy|snowy|foggy}"

The day is {currentWeather}.

// Mood changes based on weather
{currentWeather == "sunny":
    ~ mood = "happy"
    The sunshine lifts your spirits!
}

{currentWeather == "rainy":
    ~ mood = "gloomy"
    The rain dampens your mood.
}

{currentWeather == "cloudy":
    ~ mood = "thoughtful"
    The overcast sky makes you contemplative.
}

{currentWeather == "snowy":
    ~ mood = "excited"
    The snow fills you with childlike wonder!
}

{currentWeather == "foggy":
    ~ mood = "cautious"
    The thick fog makes you wary.
}

Your current mood: {mood}

+ [Begin your journey]
    -> Travel

=== Travel ===
You set out on the road.

// Random encounter type
~ encounterType = "{~merchant|traveler|guard|hermit|bard}"

You encounter a {encounterType} on the road.

// Different greeting based on encounter type
{encounterType == "merchant":
    ~ npcGreeting = "{~Hello, traveler! Care to see my wares?|Good day! I have the finest goods in the land!|Welcome, friend! What can I sell you today?}"
}

{encounterType == "traveler":
    ~ npcGreeting = "{~Greetings, fellow wanderer!|Safe travels to you!|Well met on this road!}"
}

{encounterType == "guard":
    ~ npcGreeting = "{~Halt! State your business!|Keep moving, citizen.|Papers, please.}"
}

{encounterType == "hermit":
    ~ npcGreeting = "{~Hmm? Oh, a visitor...|Strange to see someone out here.|What brings you to these parts?}"
}

{encounterType == "bard":
    ~ npcGreeting = "{~Hail, friend! Care for a song?|Well met! I have tales to share!|Greetings! Music for a coin?}"
}

"{npcGreeting}" they say.

// Weather affects the encounter
{currentWeather == "rainy":
    They huddle under their cloak, trying to stay dry.
}

{currentWeather == "sunny":
    They seem to be in good spirits, enjoying the weather.
}

{currentWeather == "snowy":
    They stamp their feet to keep warm.
}

// Your mood affects your response options
{mood == "happy":
    You feel friendly and open to conversation.
}

{mood == "gloomy":
    You're not really in the mood for small talk.
}

{mood == "cautious":
    You remain alert and guarded.
}

+ [Chat with them]
    You engage in pleasant conversation.
    
    // Random outcome
    ~ temp outcome = "{~They share useful information|They tell an entertaining story|They offer you a small gift|The conversation is brief but pleasant}"
    
    {outcome}
    
    -> Continue

+ [Trade with them] {encounterType == "merchant"}
    You browse their wares...
    
    ~ temp item = "{~a healing potion|a detailed map|a sturdy rope|a warm cloak|a sharp knife}"
    
    You purchase {item}.
    
    -> Continue

+ [Continue on your way]
    You nod politely and continue down the road.
    -> Continue

=== Continue ===

+ [Keep traveling]
    -> Travel

+ [Stop for the day]
    You decide to make camp for the night.
    -> DONE
