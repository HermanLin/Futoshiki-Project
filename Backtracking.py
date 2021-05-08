from CSP import CSP
import copy
import time

class BacktrackingSearch:

    def __init__(self, csp):
        self.csp = csp #board, domains, hc, vc
        #self.initialAssignment = copy.deepcopy(csp.board)
    
    def backtrack(self, csp):
        if csp.isComplete():
            return csp.board
        # select an unassigned variable to update
        #row, col = csp.heuristic()
        sorted_min_pos = csp.heuristic()

        for pos in sorted_min_pos:
            row, col = pos[0], pos[1]

            # get the domain associated with the (row, col)

            domain = csp.domains[row][col]
            # in order to perform inferencing, save old state
            oldDomains = copy.deepcopy(csp.domains)

            for value in domain:
                # update board with value and check consistency
                print("VALUE", value)
                csp.board[row][col] = value
                print("====ADDED VALUE TO BOARD=============================================")
                csp.printBoard()
                print("==================================================")
                csp.printDomains()
                print("===================================================")
                if csp.isConsistent(row, col):
                    # perform forward check
                    if csp.forwardCheck():
                        print("======================")
                        csp.printBoard()
                        print("===========")
                        csp.printDomains()
                        print("===========")
                        
                        input()
                        #time.sleep(1)
                    
                        result = self.backtrack(csp)
                        if result != None:
                            return csp.board
                    
                    # if the assignment is not consistent or fails, reset
                    csp.board[row][col] = 0
                # reset domains
                csp.domains = oldDomains
            return None
        return None   
    