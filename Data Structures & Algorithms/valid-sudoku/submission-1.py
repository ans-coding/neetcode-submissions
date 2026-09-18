class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checkerR = set()
        checkerC = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
        checkerB = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
        for row in range(0,9):
            for col in range(0,9):
                if (board[row][col].isdigit() and (1<=int(board[row][col]) and int(board[row][col])<=9)):
                    if(board[row][col] in checkerR) or (board[row][col] in checkerC[col]) or (board[row][col] in checkerB[(row//3)+((col//3)*3)]):
                        return False
                    checkerR.add(board[row][col])
                    checkerC[col].add(board[row][col])
                    checkerB[(row//3)+((col//3)*3)].add(board[row][col])
                elif(board[row][col]=="."):
                    checkerR.add(board[row][col])
                    checkerC[col].add(board[row][col])
                    checkerB[(row//3)+((col//3)*3)].add(board[row][col])
            checkerR = set()
        return True
