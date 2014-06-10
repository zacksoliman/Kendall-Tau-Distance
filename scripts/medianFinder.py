import ast
import math

#holds the solution set (medians)
solutions = []
#holds the permutation set for which we want to find it's median(s)
permSet = []
#hold the min kendall tau distance found thus far
dist_KT = float('inf')
#Holds the size of the permutations
permSize = 0
#Holds element we can add to the rigth or to the left of the integer i
elem_right
elem_left

class MedianFinder:

    def inversePermutation(permutation):
        inverse = list(range(len(permutation)))

        for i in range(0,len(permutation)):
            inverse[((permutation[i])-1)] = i

        return inverse

    def KendallTauDistance(permutation, permSet):
        distance = 0
        totalDist = 0
        permA =inversePermutation(permutation)
        for p in permSet:
            permB = inversePermutation(p)

            # COMPUTE DISTANCE
            for i in range(0,len(p)-1):
                for j in range(i+1, len(permB)):
                    if(((permA[i]<permA[j])and(permB[i]>permB[j])) or
                    ((permA[i]>permA[j]) and (permB[i]<permB[j]))):
                        distance+=1

            totalDist += distance
            distance = 0
        return totalDist

    #builds initial constraints from the given permutation set
    def buildConstraints(permSet):

        #counts the number of times the int i is before j in all permutations in permSet
        counterMatrix = [[0 for x in range(len(permSize)+1)] for x in range(len(permSize)+1)]

        elem_right = [set() for x in range(len(permSize)+1)]
        elem_left = [set() for x in range(len(permSize)+1)]
        #TODO: init elem_{right, left}[0] to all

        #Start by counting
        for perm in permSet:
            for i in range(len(permSize)-1):
                for j in range(i+1, len(permSize)):
                    counterMatrix[perm[i]][perm[j]]+=1

        majority = math.ceil(len(permSize)/2)

        for i in range(len(counterMatrix)):
            for j in range(len(counterMatrix)):

                if counterMatrix[i][j] >= majority:
                    #Then we have j to the right of i in a majority of cases
                    elem_right[i].add[j]
                    #and i to the left of j
                    elem_left[j].add[i]
        return elem_left, elem_right

    #Builds and returns the initial instances from which we start building our
    #solution
    def buildInitialInstances(left):

        size = len(left)
        partialSol = []
        initialInstances=[]

        #Find (if it exists) the element that will be the first element of a median
        for i in range(1,size):

            if len(left[i]) == 0:
                #We found the first element of a median
                partialSol.append(i)

                #We start constructing this initial instance

                #Continue adding elements to the partial solution until its no longer possible
                done = False
                while(!done):
                    lastElementAdded = partialSol[len(partialSol)-1]
                    done = True

                    for s in left:
                        if (len(s) == 1) and (lastElementAdded in s):
                            partialSol.append(left.index(s))
                            done=False
                            break

                initialInstances.append(partialSol[:])
                del partialSol[:]

        return initialInstances

    #Finds the median by starting from the given initial solution set
    def findMedBT(potentialSolution):

        #CASE 1: We have a potential solution if it is the correct size
        if len(potentialSolution) == permSize
            currentDist = KendallTauDistance(potentialSolution)

            #Check if it's a better solution
            if currentDist < dist_KT:
                dist_KT = currentDist
                solutions[:] = []
                solutions.append(potentialSolution)
                return
            #Check if it is as good as the solutions we found
            elif currentDist == dist_KT:
                solutions.append(potentialSolution)
                return
            #If we reach here then the potential solution is not an optimal one
            else:
                return

        lastElement = 0
        #CASE 2: Check if the current partial solution is valid
        elif not isValid(potentialSolution):
            return
        #Find the elements that we can add to the current solution and recurse
        if len(potentialSolution) != 0:
            lastElement = potentialSolution[len(potentialSolution)-1]

        else:
            lastElement = 0

        for elem in


    def findMedian():

        """Loops through all the inital solutions and calls findMedBT"""

        startingInstances = getInitialInstances()
        for potentialSolution in startingInstances:
            findMedBT(potentialSolution)

                ########
                # MAIN #
                ########

if __name__ == '__main__'

    #TODO: testing
