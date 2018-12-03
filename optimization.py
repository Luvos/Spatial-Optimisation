import numpy as np
import matplotlib.pyplot as plt

 
route = [0,1,2,3,4,5,0] #Initial root to be optimized
# time matrix representing the time it takes to travel between the cities 
time_matrix = np.array([[0,72,100,215,116,166],
                      [72,0,155,214,78,108],
                      [100,155,0,151,204,240],
                      [215,214,151,0,292,104],
                      [116,78,204,292,0,185],
                      [166,108,240,104,185,0]])

#function for calculating the total time/duration for a completed route
def path_time(time_matrix, route):
    time = 0
    for i in range(len(route)-1):
        time += time_matrix[route[i]][route[i+1]]
    return time
# 2 opt swap method to manipulate the given route/change the root
def Two_opt_swap(fields, i, k):
    start = fields[0:i]
    middle = fields[i:k]
    middle = middle[::-1]
    end = fields[k:]
    newFields = start + middle + end
    return newFields


n = len(route)
i = 1

Init_time = path_distance(time_matrix,route)#initial time for the initial route
best_route = route
best_time = Init_time

while i < n:
    for swap_first in range(1,len(route)): 
        for swap_last in range(swap_first+2,len(route)): 
            new_route = Two_opt_swap(route,swap_first,swap_last) 
            new_time = path_time(time_matrix,new_route)
            if new_time < best_time: # If the path yields an improved time,
                route = new_route # make this the accepted best route
                best_time = new_time # update the time/duration corresponding to the new route
            else:
                for swap_first in range(1,len(route)): 
                    for swap_last in range(swap_first+1,len(route)): 
                        new_route = Two_opt_swap(route,swap_first,swap_last) 
                        new_time = path_time(time_matrix,new_route)
                        if new_time < best_time: 
                            route = new_route 
                            best_time = new_time 
                        else:
                            i += 1
                
print("optimal time =", best_distance, "optimal route =", route)

