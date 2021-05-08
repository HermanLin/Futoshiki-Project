from CSP import CSP
from Backtracking import BacktrackingSearch

def processFile(filename, outputFilename):
    f = open(filename, 'r')
    # read 6 lines and remove trailing newlines for initial game board
    initialBoard = [next(f).rstrip().split(' ') for line in range(6)]
    for i in range(6):
        for j in range(6):
            initialBoard[i][j] = int(initialBoard[i][j])
    next(f) # skip blank line
    # read 6 lines and remove trailing newlines for horizontal constraints
    horzConstraints = [next(f).rstrip().split(' ') for line in range(6)]
    next(f) # skip blank line
    # read 6 lines and remove trailing newlines for vertical contraints
    vertConstraints = [next(f).rstrip().split(' ') for line in range(5)]
    f.close()

    problem = CSP(initialBoard, horzConstraints, vertConstraints)
    print("===== Initial Board =====")
    problem.printBoard()
    
    BTS = BacktrackingSearch(problem)
    solution = BTS.backtrack(problem)

    if solution:
        print("======= SOLUTION ========")
        for row in solution: print(row)
        print()
    else: print("NO SOLUTION FOUND\n")
    outputFile(outputFilename, solution)

def outputFile(outputFilename, board):
    file = open(outputFilename, 'w')
    for row in board:
        for cell in row:
            file.write(str(cell) + " ")
        file.write("\n")
    file.close()

def main():
    processFile("Input1.txt", "Output1.txt")
    processFile("Input2.txt", "Output2.txt")
    processFile("Input3.txt", "Output3.txt")

if __name__ == "__main__":
    main()