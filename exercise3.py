import random
import util
'''
'' Given an array of positive integers A with N numbers and another positive integer S, write a function that 
'' finds slices of A with consecutive indices such that the sum of this slice is S and outputs the number of such possible slices
'''

a_10 = random.sample(range(1, 11), 10)
a_100 = random.sample(range(1, 1000), 100)
a_1000 = random.sample(range(1, 10000), 1000)

def create_slices(A, N): 
    
    slices = []

    for i_idx, i  in enumerate(A):
        total = i
        slice = [i]

        # If the number is equal to N then we found the slice and index
        if total == N: 
            slices.append(slice)
            continue

        for j_idx, j in enumerate(A):    
            '''
            '' Skill all previouse elements
            '''
            if j_idx <= i_idx: 
                continue

            total = total + j
            slice.append(j)

            '''
            '' Break loop if total is greater then required
            '''
            if total > N:
                slice = []
                break

            if total == N:
                break

        if slice:
            total = sum(slice)
            '''
            '' To make sure only valid slices are added
            '''
            if total == N:
                slices.append(slice)

    return slices
    
start_time = util.get_start_time()
print(create_slices(a_10, 7))
util.print_end_time(start_time)


start_time = util.get_start_time()
print(create_slices(a_100, 200))
util.print_end_time(start_time)

start_time = util.get_start_time()
print(create_slices(a_1000, 250))
util.print_end_time(start_time)


'''
Output
[[4, 3], [6, 1], [7], [5, 2]]
0.127 milliseconds
[]
1.085 milliseconds
[[250]]
97.22200000000001 milliseconds
'''


    