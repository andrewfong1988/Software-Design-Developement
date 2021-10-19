def TowerOfHanoi(n , source, aux, destination):           
    if n == 1:
        print("Move disc 1 from pole",source,"to pole",destination)
        return
    TowerOfHanoi(n-1, source, aux, destination)
    print("Move disc",n,"from pole",source,"to pole",destination)
    TowerOfHanoi(n-1, aux, destination, source)
 
n = 3
TowerOfHanoi(n, 'A', 'B', 'C')
# A, C, B are the name of poles