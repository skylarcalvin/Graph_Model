# Author Skylar Calvin
# Date 07/07/2024
#
# This will test the graph model defined by the networkGraph class.

# First import the networkGraph class into this script from the graphGen script.
from graphGen import networkGraph

# Main program execution...
if __name__ == "__main__":

    # Initialize a class instance with seven nodes.
    g = networkGraph(7)

    # Create various hops between notes, creating a network.
    g.addHop(0, 1)
    g.addHop(1, 2)
    g.addHop(1, 3)
    g.addHop(2, 3)
    g.addHop(3, 5)
    g.addHop(2, 4)
    g.addHop(4, 5)
    g.addHop(3, 4)
    g.addHop(2, 6)
    g.addHop(4, 6)

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

    # Finally find the longest routes.
    g.findLongestRoute()

    # Lastly, print the longestRoutes class attribute to the console.
    print(g.longestRoutes)

