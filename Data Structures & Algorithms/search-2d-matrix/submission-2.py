class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix)-1
        while low <= high:
            mid = (low+high)//2
            if((matrix[mid][0])<=target and matrix[mid][len(matrix[0])-1]>=target) or len(matrix) == 1:
                row = (low+high)//2
                high = len(matrix[row])-1
                low = 0
                while low <= high:
                    mid = (low+high)//2
                    if(matrix[row][mid])==target:
                        return True
                    if target > matrix[row][mid]:
                        low = mid+1
                    elif target < matrix[row][mid]:
                        high = mid-1
                break
            if target > matrix[mid][0]:
                low = mid+1
            elif target < matrix[mid][0]:
                high = mid-1
        
        
        return False
'''
        row = (low+high)//2
        high = len(matrix[row])-1
        low = 0

        while low <= high:
            mid = (low+high)//2
            if(matrix[row][mid])==target:
                return True
            if target > matrix[row][mid]:
                low = mid
            elif target < matrix[row][mid]:
                high = mid
        return False
'''


'''
        def x_search(point, target):
            if matrix[point[0],0]<=target and matrix[point[0],len(matrix[0])]>=target:
                return y_search()

            if matrix[point[0],point[1]]>target:
                return x_search()
            
            if matrix[point[0],point[1]]<target:
                return x_search()
            
            return []

        def y_search(point, target):
            if matrix[point[0],]>target:
                return x_search()
            
            if matrix[point[0],point[1]]<target:
                return x_search()

        
        
        x_search([len(matrix)//2,len(matrix[0])//2])
'''               
        
        