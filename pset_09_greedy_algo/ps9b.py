###########################
# Problem Set 9b: Space Cows 
# Name:
# Collaborators:
# Time:

from ps9b_partition import getPartitions
import time

#================================
# Part 2: Transporting Space Cows
#================================

# Problem 5
def loadCows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name, weight pairs
    """
    txtFile = open(filename)

    #parse file
    cowDict = {}
    
    for line in txtFile:
        each = line.split(',')
        cow = each[0]
        weight = each[1].strip('\n')

        cowDict[cow] = float(weight)
    
    return cowDict

# Problem 6
def greedyTransport(cows,limit):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via a greedy heuristic (always choose the heaviest cow to fill the
    remaining space).
    
    Parameters:
    cows - a dictionary of name (string), weight (float) pairs
    limit - weight limit of the spaceship
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    def solveTripsByWeight():
        """solve problem with just float values from cow weights"""
        
        #sorted list of cow weights
        cowWeight = sorted(cows.values())
        cowWeight.reverse()

        #copy list to avoid side effects
        copyWeight = cowWeight[:]
        results = []

        #overall loop to hold all the trips
        while len(copyWeight) > 0:

            #variable resets after each trip
            trip = []
            weight = 0
            cowWeight = copyWeight[:]

            #inner loop for each trip
            for i in range(len(cowWeight)):
                if weight + cowWeight[i] <= limit:
                    weight += cowWeight[i]
                    trip.append(cowWeight[i])
                    copyWeight.remove(cowWeight[i])
                    
            #final results         
            results.append(trip)
            
        return results

    def findValue(dic, val):
        """Used this code from StackOverflow to search dict value"""
        return [k for k, v in dic.iteritems() if v == val][0]

    def replaceNumWithName():
        """replaces float with dictionary cow name"""
        
        results = solveTripsByWeight()

        #create a dict copy to remove cows that already went on trip
        cows2 = cows.copy()
        while len(cows2) > 0:
            for i in range(len(results)):
                for j in range(len(results[i])):
                    #since cow name doesn't matter
                    #just search dictionary for correct weight
                    #replace weight with first found cow name
                    #delete that cow
                    replace = findValue(cows2, results[i][j])
                    cows2.pop(replace)
                    results[i][j] = replace

        return results

    return replaceNumWithName()
    
# Problem 7
def bruteForceTransport(cows,limit):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.
    
    Parameters:
    cows - a dictionary of name (string), weight (float) pairs
    limit - weight limit of the spaceship
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cowWeight = sorted(cows.values())
    cowWeight.reverse()

    print cowWeight
    
    allPart = []
    lenPart = []
    usePart = []
    
    for part in getPartitions(cowWeight):
        allPart.append(part)

    for part in allPart:
        numList = [item for sublist in part for item in sublist]
        
        if len(numList) == len(cowWeight):
            print numList
            lenPart.append(part)


    assert False
    
    for part in lenPart:
        test = []
        for trip in part:
            if sum(trip) < limit:
                test.append(trip)
        if len(test) == len(part):
            usePart.append(test)

    lenIndex = []
    for part in usePart:
        lenIndex.append(len(part))

    find = min(lenIndex)

    for part in usePart:
        if len(part) == find:
            return part
        
        

# Problem 8
if __name__ == "__main__":

    """
    Using the data from ps9b_data.txt and the specified weight limit, run your
    greedyTransport and bruteForceTransport functions here. Print out the
    number of trips returned by each method, and how long each method takes
    to run in seconds.
    """
    #print greedyTransport(loadCows("ps9b_data.txt"), 0.7)
    print bruteForceTransport(loadCows("ps9b_data.txt"), 1.0)


