# Author Skylar Calvin
# Date 07/07/2024
#
# This will test the graph model defined by the networkGraph class.

# First import the networkGraph class into this script from the graphGen script.
from graphGen import networkGraph
from random import randint

# Main program execution...
if __name__ == "__main__":

    # Initialize a class instance with seven nodes.
    g = networkGraph(7)

    # Create various hops between notes, creating a wighted network.
    g.addHop(0, 1, 50)
    g.addHop(1, 2, 35)
    g.addHop(1, 3, 42)
    g.addHop(2, 3, 53)
    g.addHop(3, 5, 40)
    g.addHop(2, 4, 24)
    g.addHop(4, 5, 35)
    g.addHop(3, 4, 15)
    g.addHop(2, 6, 23)
    g.addHop(4, 6, 15)

    ################################################################
    #### At this point we have a working network structure.     ####
    ####    We can now find all possible routes in the network. ####
    ################################################################

    # Define ranges for all starting points and destinations.
    startingPoints = range(g.nodes)
    destinations = range(g.nodes)

    # For each starting point and destination combination, we will discover all routes
    #   between the two, saving then to the routes class attribute. Then, we'll find the
    # longest routes in the network, and print them out.

    # Loop through the starting points.
    for s in startingPoints:

        # Loop through the destinations.
        for d in destinations:

            # For each combination, load the routes.
            g.loadRoutes(s, d)

    # Find the longest routes.
    g.findLongestRoutes()

    # Now, let's find the widest routes.
    
    # Loop through the starting points.
    for s in startingPoints:

        # Loop through the destinations.
        for d in destinations:

            # And find all of the widest routes.ß
            g.findWidestRoute(s, d)

    # Print the longestRoutes class attribute to the console.
    print(g.longestRoutes)
    
    # Pick an arbitrary source and destination node, and find the widest route between the two.
    
    # Variable to break infinite loop.
    terminator = True
    
    # Try random conbinations until one is found that exists in the routes:
    while terminator == True:

        # Pick two random numbers between 0 and 6...
        X = randint(0, 6)
        Y = randint(0, 6)
        
        print(f'Trying {X}, and {Y}...')

        # Check if the associated starting and destination point tuple is in the routes, stored in the class attribute.
        if (X, Y) in g.routes:

            print(f'{X}, and {Y} were found!')

            # If it is, look up the widest route for it in the dictionary of widest routes, stored in the class attribute.
            widestForXY = g.widestRoutes[(X, Y)]

            print(f'The widest route between {X} and {Y} is {widestForXY}.')

            # Break the infinite loop.
            terminator = False

        # If not...
        else:

            print(f'{X}, and {Y} were not found. Trying again...')

