from shutil import copyfile


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
    horzConstraint = [next(f).rstrip() for line in range(6)]
    next(f) # skip blank line
    # read 6 lines and remove trailing newlines for ivertical contraints
    vertConstraint = [next(f).rstrip() for line in range(5)]
    f.close()

    # process constraints
    horzConstraint = processConstraints(horzConstraint)
    vertConstraint = processConstraints(vertConstraint)
    domains = setDomain(initialBoard)

    # fill constraintDict
    constraintDict = {}
    for i in range(len(domains)):
        for j in range(domains[i]):
            

    return initialBoard, horzConstraint, vertConstraint

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

def setDomain(board):
    domains = []
    for row in board:
        row_domain = []
        for cell in row:
            if cell == 0:
                row_domain.append([1,2,3,4,5,6])
            else:
                row_domain.append([cell])
        domains.append(row_domain)

# ['0 0 > 0 0', '0 0 0 0 0', '0 0 0 0 0', '0 0 0 < 0', '0 > 0 0 >', '> 0 0 0 0']
# '0 0 > 0 0' -> [0, 0, >, 0, 0]
'''    
i, h, v = processFile("Input1.txt")
print(i)
print(h)
print(v)

X = {x_1....x_36} - final variables
ConstraintDict = { [i][j]: {domain:[], hc:int, vc:int} }
## D = {d_1....d_36}
d = [1...6]
HC = 0 (none), 1 (<), 2 (>)
VC = 0 (none), 1 (^) , 2 (v)
'''
