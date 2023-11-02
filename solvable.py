# Python3 program to check if a given
# instance of 8 puzzle is solvable or not

# A utility function to count
# inversions in given array 'arr[]'
def getInvCount(arr):
	inv_count = 0
	empty_value = None
	for i in range(0, 9):
		for j in range(i + 1, 9):
			if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
				inv_count += 1
	return inv_count

	
# This function returns true
# if given 8 puzzle is solvable.
def isSolvable(matrix) :

	# Count inversions in given 8 puzzle
	inv_count = getInvCount([j for sub in matrix for j in sub])

	# return true if inversion count is even.
	return (inv_count % 2 == 0)
	
if __name__ == '__main__':
    # Driver code
    puzzle = [[8, 1, 2],[None, 4, 3],[7, 6, 5]]
    if(isSolvable(puzzle)) :
        print("Solvable")
    else:
        print("Not Solvable")
        
        # This code is contributed by vitorhugooli
        # Fala meu povo desse Brasil varonil 
