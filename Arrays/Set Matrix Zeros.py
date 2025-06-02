class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        row_len = len(matrix)
        col_len = len(matrix[0])
        row = [0]*row_len
        col= [0]*col_len

        # functions starts here
        for i in range(row_len):
            for j in range(col_len):
                if (matrix[i][j] == 0):
                    row[i] = 1
                    col[j] = 1



        for  i in range(row_len):
            for j in range(col_len):
                if( row[i] == 1 or  col[j] == 1):
                    matrix[i][j] = 0

        return matrix

                


        
        
        

                
                
        