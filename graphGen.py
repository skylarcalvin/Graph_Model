# Author Skylar Calvin
# Date 07/07/2024

# For this I will be using three default dictionaries, which allow you to initialize at object as
#   a new key's value if unspecified.
from collections import defaultdict as dd

# Main class modelling the graph.
class networkGraph:
    '''
    Class models a network (or graph) of nodes or destinations.

    Naming convention used:
        network: the graph as a whole.
        node: a vertice in the graph.
        hop: an edge in the graph.
        route: all of the nodes along the way from the starting and destination nodes.
    
    Class attributes:
        nodes: the number of nodes in the dictionary.
        networkGraph: is a default dictionary containing nodes, and possible next hops.
        hops: a dictionary of capacity values per start and destination tuple.
        routes: is a default dictionary containing all possible graph routes for each starting and destination node.
        longestRoutes: A list of lists containing the longest routes in the network.
        widestRoutes: A default dictionary containing the widest route per start, destination pair.
    '''

    def __init__(self, nodes: int = 7):
        '''
        Constructor function sets the attibutes when the class initializes.
        '''

        self.nodes = nodes # Default to 7
        self.networkGraph = dd(list)
        self.caps = dict()
        self.routes = dd(list)
        self.longestRoutes = list()
        self.widestRoutes = dd(list)

    def addHop (self, x: int, y: int, cap: int = 0):
        '''
        Function adds a hop to the network.

        Let:
            x: defined as the current node where you are.
            y: defined as the node you are going to.
            cap: the capacity of the hop.
        '''

        # Add the destination to the list in the starting point's value.
        self.networkGraph[x].append(y)
        
        # add a capacity entry into the hops dictionary.
        self.caps[(x, y)] = cap

    def routeInit(self, x: int, y: int):
        '''
        Function initializes an empty route in the routes default dictionary
            for the given starting and destination nodes.

        Let:

            x: the starting node, and,
            y: the destination node.
        '''

        self.routes[(x, y)] = []

    def findAllRoutes(
            self, 
            x: int, 
            y: int, 
            visited: dict = dict(),
            route: list = list()
            ):
        '''
        Wrapping function recursively finds all possible routes for the node in the in the network. 
            We do this by saving the original starting point x to a local variable, and then defining 
            a new function to contain the recursive algorithm. By doing this, the original starting point 
            remains accessible through future iterations of recursion.

        Let:

            x: The starting node,
            y: The destination node,
            visited: A dictionary of all nodes, containing whether the node is being visited or not (True/False), and,
            route: be the list of all nodes visited along the way to the destination.
        '''

        # First, save the original starting point, so it survives recursion.
        old_x = x

        # Next, define a new function that the original X can be used in.
        def findRoutes(
            x: int, 
            y: int, 
            visited: dict = dict(),
            route: list = list()
            ):
            '''
            Function performs the recursion and runs the algorithm to define the routes.

            variables are the same as, and passed in from the wrapping function.
            '''

            # Set the currently visited node to True in the visited dictionarly
            visited[x] = True

            # Add the currently visited node to the route.
            route.append(x)
            
            # Find the next possible nodes and loop through them.
            for node in self.networkGraph[x]:
                
                # If the currently visited node is the same as the destination.
                if node == y:

                    # Create a list of all nodes contained in the current route (using a list comprehension)
                    #   and append that to the original starting point and destination's tuple in the
                    #   class's routes attribute.
                    self.routes[(old_x, y)].append([n for n in route])

                    # Finally, look in that newly created route in routes.
                    for r in self.routes[old_x, y]:
                        
                        # And if the destination is not there,
                        if node not in r:
                            
                            # Add it.
                            r.append(node)

                # Otherwise,
                else:
                    
                    # If the current node hasn't been visited,
                    if visited[node] == False:
                        
                        # Run another recusion iteration using the current node.
                        findRoutes(x = node, y = y, visited = visited, route = route)

            # Last but not least...

            # Remove the current node from the current route (Since it's now in there twice at the end...)
            route.pop()
            
            # And, leave the current node, by setting the node in visited back to False.
            visited[x] = False

        # Run the recursion function, passing the wrapping fuction's variables to it.
        findRoutes(x = x, y = y, visited = visited, route = route)


    def loadRoutes(self, x: int, y: int):
        '''
        Function to traverse networkGraph, and discover all possible routes, 
            using the findAllRoutes function.

        Let:

            x: The starting node, and,
            y: The destination node.
        '''

        # Itintialize an empty route for the starting and destination nodes.
        self.routeInit(x = x, y =y)

        # Create a dictionary for visiting the nodes, in which all nodes are set to False.
        visited = [False] * (self.nodes)

        # Discover all of the possible routes in the network.
        self.findAllRoutes(x = x, y = y, visited = visited)

        #### Clean up the list of routes by removing the empty routes. ####

        # Initialize a list for the empty routes.
        emptyRoutes = []

        # loop through the keys in the routes dictionary.
        for k in self.routes.keys():
            
            # Identify empty roots by checking if the current troute is empty or not.
            if self.routes[k] == []:
                
                # If it is, add it to the emptyRoutes list for removal.
                emptyRoutes.append(k)
        
        # Now, loop through the empty routes.
        for k in emptyRoutes:
            
            # And delete them from the routes dictionary.
            del(self.routes[k])

    def findLongestRoutes(self):
        '''
        Function finds and returns the longest routes in the network. In case of a tie for longest, the
            function's output is appended to the longestROutes class attribute, which is a list.
        '''

        # Initialize emplty lists for the routes, and the rout liengths.
        routes = []
        lengths = []

        # Loop through the keys in the routes class attribute.
        for k in self.routes.keys():
            
            # Add the list of routes for the current key to the routes list.
            routes.extend(self.routes[k])

        # Now, loop through the list of routes.
        for r in routes:

            # And, append the length of that route to the lengths list.
            #   (The number ops in the route is given by the numberof nodes minus one...)
            lengths.append(len(r) - 1)

        # Then, loop through the enumeration of the lengths, capturing the indesx and vlaue of the 
        #   current iteration.
        for i, v in  enumerate(lengths):
            
            # If the value is the same as the max length,
            if v == max(lengths):
                
                # Append it to the longestRoutes class attirbute.
                self.longestRoutes.append(routes[i])    

    def findWidestRoute (self, x: int, y: int):
        '''
        Function finds the widest route for a given starting and destination node in a network.

        Let:

            x: The starting node, and,
            y: The destination node.
        '''
        
        # Check if the starting and destination nodes exist in the routes.
        if (x, y) in self.routes:

            # If so, save the given route list to a local variable.
            routes = self.routes[(x, y)]
            
            # Initialize an empty dictionary for the hop capacities.
            caps = {}

            # Loop through the roots.
            for r in routes:

                # Initialize a dictionary per route for the hop capacities.
                routeCaps = {}

                # Loop through the indexes of the root list:
                for i in range(len(r)):

                    # And check if the index plus one is out of bounds of the list indexes.
                    if i + 1 <= len(r) - 1:

                        # Save the current and next nodes in the hop as a tuple.
                        tup = (r[i], r[i + 1])

                        # Add to the capacities for the route for the hop by looking the capacity up in the class attribute containing hop capacities.
                        routeCaps[tup] = self.caps[tup]

                # Identify the route's bottleneck by taking the minimum capacity from the values in the routeCap dictionary.
                routeBottleneck = min(routeCaps.values())

                # Now, convert the route list into a tuple so it can be added to the bottleneck dictionary for the start and destination points.
                caps[tuple(r)] = routeBottleneck

            # Get the widest route for the start and destination nodes by getting the key of the maximum value of the bottleneck dictionary.
            widestRoute = max(caps, key = caps.get)

            # Finally update the widestRoutes class attribute with the route that was found.
            self.widestRoutes[(x,y)] = list(widestRoute)

