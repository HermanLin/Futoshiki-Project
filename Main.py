from CSP import CSP
from Backtracking import BacktrackingSearch
import copy

def processFile(filename):
    # read and process an input file for the initial game board and constraints
    f = open(filename, 'r')
    # read 6 lines and remove trailing newlines for initial game board
    initialBoard = [next(f).rstrip().split(' ') for line in range(6)]
    for i in range(6):
        for j in range(6):
            initialBoard[i][j] = int(initialBoard[i][j])
    next(f) # skip blank line
    # read 6 lines and remove trailing newlines for horizontal constraints
    horzConstraint = [next(f).rstrip().split(' ') for line in range(6)]
    next(f) # skip blank line
    # read 6 lines and remove trailing newlines for ivertical contraints
    vertConstraint = [next(f).rstrip().split(' ') for line in range(5)]
    f.close()

    # process constraints
    #domains = setDomain(initialBoard)

    return initialBoard, horzConstraint, vertConstraint 

def outputFile(filename, outputFileName, board):
    #copyfile(filename, outputFileName)

    f = open(outputFileName, 'a')
    for row in board:
        for cell in row:
            f.write(str(cell) + " ")
        f.write("\n")
    f.close()

def processConstraints(arr):
    resultConstraint = []
    for r in arr:
        row = r.split(' ')
        for j in range(len(row)):
            if row[j] == '<' or row[j] == '^':
                row[j] = 1
            elif row[j] == '>' or row[j] == 'v':
                row[j] = 2
            else:
                row[j] = int(row[j]) # convert '0' to int
        resultConstraint.append(row)
    return resultConstraint

def main():
    initial_board, h_constraints, v_constraints = processFile("Input2.txt")
    problem = CSP(initial_board, h_constraints, v_constraints)
    
    '''
    print("\n=======================================")
    problem.printBoard()
    print("\n=======================================")
    #problem.printDomain()
    row, col = problem.heuristic()
    print(row, col)
    
    result = problem.isConsistent(3, 5)
    print(result)
    
    '''
    '''
    '''
    BTS = BacktrackingSearch(problem)
    solution = BTS.backtrack(problem)
    if solution:
        #outputFile("Input1.txt", "Output1.txt", solution)
        print("=== SOLUTION ===")
        BTS.csp.printBoard()
    else: print("=== NO SOLUTION FOUND ===")

if __name__ == "__main__":
    main()