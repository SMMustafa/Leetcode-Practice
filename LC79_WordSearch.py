class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        N = len(board)
        M = len(board[0])
        P = len(word)


        def helper(r,c,pos):
            if pos >=P:
                return True
            elif 0 <= r < N and 0 <= c < M and board[r][c] == word[pos]:
                temp = board[r][c]
                board[r][c] = None
                if helper(r+1,c,pos+1) or helper(r,c+1,pos+1) or helper(r-1,c,pos+1) or helper(r,c-1,pos+1):
                    return True
                board[r][c] = temp
            return False



        for r in range(N):
            for c in range(M):
                if helper(r,c,0):
                    return True
        return False
