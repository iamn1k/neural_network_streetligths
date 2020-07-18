# neural_network_streetligths           
# The streetlight problem
• -> light on  
◯ -> light off  
This toy problem considers how a network learns entire datasets
Consider yourself approaching a street corner in a foreign country. 
As you approach, you look up and realize that the street light is unfamiliar. 
How can you know when it’s safe to cross the street? 

┌─┬─┬─┐        
│ •   │•  │•  │      
└─┴─┴─┘    
You can know when it’s safe to cross the street by interpreting the streetlight. 
But in this case, you don’t know how to interpret it. Which light combinations indicate when it’s time to walk? 
Which indicate when it’s time to stop? To solve this problem, you might sit at the street corner for a few minutes observing the correlation between each light combination and whether people around you choose to walk or stop. 
You take a seat and record the following pattern:

┌─┬─┬─┐          
│ •     │  ◯│    •   │          
└─┴─┴─┘      
STOP↑

OK, nobody walked at the first light. At this point you’re thinking, “Wow, this pattern could
be anything. The left light or the right light could be correlated with stopping, or the central
light could be correlated with walking.” There’s no way to know. Let’s take another datapoint:

┌─┬─┬──┐          
│ ◯      │ • │    •   │          
└─┴─┴──┘  
WALK↑

Now you’re getting somewhere. Only the middle light changed this time, and you got the
opposite pattern. The working hypothesis is that the middle light indicates when people feel
safe to walk. Over the next few minutes, you record the following six light patterns, noting
when people walk or stop. Do you notice a pattern overall?

┌─┬─┬─┐        
│ •   │ ◯│•  │      
└─┴─┴─┘  
STOP↑

┌─┬─┬──┐          
│ ◯      │ • │    •   │          
└─┴─┴──┘  
WALK↑

┌─┬─┬──┐          
│ ◯      │◯  │    •   │          
└─┴─┴──┘  
STOP↑

┌─┬─┬──┐          
│   •    │ • │    •   │          
└─┴─┴──┘  
WALK↑

┌─┬─┬──┐          
│ ◯      │ • │    •   │          
└─┴─┴──┘  
WALK↑

┌─┬─┬─┐          
│ •     │  ◯│    •   │          
└─┴─┴─┘      
STOP↑

As hypothesized, there is a perfect correlation between the middle (crisscross) light and
whether it’s safe to walk. You learned this pattern by observing all the individual datapoints
and searching for correlation. This is what you’re going do.
