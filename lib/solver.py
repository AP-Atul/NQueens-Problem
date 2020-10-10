"""
Solver class to solve the Queen board using some algorithm
"""

from lib.problem.board import Board


class Solver:
    """
    Solving the Queen board by using algorithms defined

    Attributes
    ----------
    __board : Board
        initial board
    __stepsClimbed : int
        number of steps taken in the solution
    __currentHeuristics : int
        initial heuristic of the board
    __newHeuristics : int
        heuristic generated from the neighbour
    __verbose : bool
        True to print the neighbours chosen
    """
    def __init__(self, n=4, verbose=False):
        self.__board = Board(n=n)
        self.__stepsClimbed = 0
        self.__currentHeuristics = 0
        self.__newHeuristics = 0
        self.__verbose = verbose

    def runHillClimbing(self):
        """
        Run the hill climbing on the board
        Returns
        -------
        list
            final board state
        """
        currentState = self.__board.generateBoard()
        print("Starting Board :: ")
        self.__board.printBoard(currentState)

        while True:
            self.__currentHeuristics = self.__board.calculateHeuristic(currentState)
            neighbours = self.__board.getNeighbours(currentState)
            if not neighbours:
                break

            # min heuristic in selected
            neighbour = min(neighbours, key=lambda state: self.__board.calculateHeuristic(state))
            if self.__board.calculateHeuristic(neighbour) >= self.__board.calculateHeuristic(currentState):
                break

            if self.__verbose:
                print("Neighbour Board :: ")
                self.__board.printBoard(currentState)

            # updating the current state
            currentState = neighbour
            self.__stepsClimbed += 1
            self.__newHeuristics = self.__board.calculateHeuristic(currentState)

        print("Final Board :: ")
        self.__board.printBoard(currentState)
        return currentState

    def getStepsClimbed(self):
        """
        Returns the no of steps taken

        Returns
        -------
        int
            steps taken
        """
        return self.__stepsClimbed

    def getHeuristics(self):
        """
        Returns heuristics of initial and final states

        Returns
        -------
        tuple
            both heuristics
        """
        return self.__currentHeuristics, self.__newHeuristics