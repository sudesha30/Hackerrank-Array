There are 8 prison cells in a row and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
Note : that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0 if the ith cell is vacant, and you are given an integer n.

Return the state of the prison after n days (i.e., n such changes described above).

Input Format

The First line contains an integer N
The Second line contains 8 integers denoting the value of prison cells.
Constraints

cells.length == 8
cells[i] is either 0 or 1.
1 <= n <= 10^9

Solution:
def prisonAfterNDays(cells, N):
    # Create a dictionary to store cell patterns and their corresponding day
    seen = {}
    
    # Perform iterations to simulate state changes
    while N > 0:
        cell_pattern = tuple(cells)
        
        # If the current pattern is already seen, it means a cycle has started
        if cell_pattern in seen:
            cycle_length = seen[cell_pattern] - N
            N %= cycle_length
        
        # Update the seen dictionary with the current pattern and day
        seen[cell_pattern] = N
        
        # Perform one day of state change
        next_cells = [0] * 8
        for i in range(1, 7):
            next_cells[i] = 1 if cells[i - 1] == cells[i + 1] else 0
        
        cells = next_cells
        N -= 1
    
    return cells

# Input handling
n, N = map(int, input().split())
initial_cells = list(map(int, input().split()))

# Calculate and print the state of the prison after N days
result = prisonAfterNDays(initial_cells, N)
print(*result)
