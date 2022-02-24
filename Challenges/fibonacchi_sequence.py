# fibonacchi sequence
# 0, 1, 1, 2, 3, 5, 8, 13

def fibonnachi(terms, n, n_plus_one):
    for i in range(1,terms+1):
        fib = n + n_plus_one
        print(fib)
        n = n_plus_one
        n_plus_one = fib        
        

terms = 1000
n = 0
n_plus_one = 1

fibonnachi(terms, n, n_plus_one)
