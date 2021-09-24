import datetime
import util

"""
Sieve method to generate the prime numbers 
Reference https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""
def sieve(numbers, n):
    i = 2
    while i*i <= n:
        if numbers[i] == 0:
            i += 1
            continue
        j = 2*i
        while j < n:
            numbers[j] = 0
            j += i
        i += 1
    return numbers

def print_prime_numbers(number):
    numbers = []
    n = number
    numbers = [1]*n
    numbers[0] = 0
    numbers[1] = 0
    numbers = sieve(numbers, n)
    for i in range(1, n):
        if numbers[i] == 1:
            numbers.append(i)
            print (i, end=', ')
        
start_time = util.get_start_time()
print_prime_numbers(100)
util.print_end_time(start_time)

start_time = util.get_start_time()
print_prime_numbers(500)
util.print_end_time(start_time)

start_time = util.get_start_time()
print_prime_numbers(1000)
util.print_end_time(start_time)

'''
    100 - 0.367 milliseconds
    500 - 0.7699999999999999  milliseconds
    1000 - 1.537 milliseconds
'''

'''
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 0.367 milliseconds
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 0.7699999999999999 milliseconds
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1.537 milliseconds
'''