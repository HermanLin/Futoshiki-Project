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
    horzConstraint = [next(f).rstrip().split(' ') for line in range(6)]
    next(f) # skip blank line
    # read 6 lines and remove trailing newlines for ivertical contraints
    vertConstraint = [next(f).rstrip().split(' ') for line in range(5)]
    f.close()

    # process constraints
    domains = setDomain(initialBoard)

    return initialBoard, horzConstraint, vertConstraint, domains

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
    return domains

def forwardCheck(board, domains, hc, vc):
    #printDomain(domains)
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != 0: 
                updateDomain(board, domains, hc, vc, row, col)
    #print("=====================")
    #printDomain(domains)

def updateDomain(board, domains, hc, vc, row, col):
    val = domains[row][col] #[]

    # update row
    for i in range(6):
        if domains[row][i] != val:
            try:
                domains[row][i].remove(val[0])
            except ValueError:
                pass
    # update column
    for i in range(6):
        if domains[i][col] != val:
            try:
                domains[i][col].remove(val[0])
            except ValueError:
                pass

    # update according to horizontal inequality constraints
    # check if cell has horizontal constraints (row, col - 1) and (row, col)
    if col - 1 < 0: # we are in first column
        arg = [col+1]
    elif col == 5: # we are in last column
        arg = [col-1]
    else:
        arg = [col-1, col]
    for i in arg:
        if hc[row][i] == '<': # less than
            domains[row][i] = [x for x in domains[row][i] if x < val[0]]
        elif hc[row][i] == '>': # greater than
            domains[row][i] = [x for x in domains[row][i] if x > val[0]]
    # update according to vertical inequality constraints
    # check if cell has vertical constraints (row - 1, col) and (row, col)
    if row - 1 < 0: # we are in first row
        arg = [row+1]
    elif row == 5: # we are in last row
        arg = [row-1]
    else:
        arg = [row-1, row]
    for i in arg:
        if vc[i][col] == '^': # less than
            domains[i][col] = [x for x in domains[i][col] if x < val[0]]
        elif vc[i][col] == 'v': # greater than
            domains[i][col] = [x for x in domains[i][col] if x > val[0]]


def printDomain(domains):
    for i in range(len(domains)):
        print(domains[i])
    
def MRV(board, domains, row):
    domain_lens = [len(d) for d in domains[row]]
    new_lens = []
    for col in range(6):
        if domain_lens[col] == 1:
            if board[row][col] != 0:
                new_lens.append(7)
            else:
                new_lens.append(domain_lens[col])
        else:
            new_lens.append(domain_lens[col])

    num = min(new_lens)
    return [d for d, i in enumerate(new_lens) if num == i]

# degree heuristic returns number of unassigned neighbors
def degreeHeuristic(board, hc, vc, row, col):
    remainingNeighbors = 0
    for c in range(6):
        if board[row][c] == 0:
            remainingNeighbors += 1
    for r in range(6):
        if board[r][col] == 0:
            remainingNeighbors += 1
    return remainingNeighbors-2 # remove duplicate count

def main():
    a, b, c, d = processFile("Input1.txt")
    #print(d)
    forwardCheck(a, d, b, c)
    #print(d)
    
    for r in range(6):
        mrv = MRV(a, d, r)
        if len(mrv) > 1:
            degrees = []
            for i in mrv:
                degrees.append((i, degreeHeuristic(a, b, c, r, i)))
            print(degrees)
        else:
            print(mrv[0])
    

main()
'''   
X = {x_1....x_36} - final variables
ConstraintDict = { [i][j]: {domain:[], hc:int, vc:int} }
## D = {d_1....d_36}
d = [1...6]
HC = 0 (none), 1 (<), 2 (>)
VC = 0 (none), 1 (^) , 2 (v)
'''

