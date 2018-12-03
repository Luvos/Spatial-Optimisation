import numpy as np
import matplotlib.pyplot as plt

#locations for the route to be optimized
location0 = "115 St Andrew’s Drive, Durban North, KwaZulu-Natal, South Africa"
location1 = "67 Boshoff Street, Pietermaritzburg, KwaZulu-Natal, South Africa"
location2 = "4 Paul Avenue, Fairview, Empangeni, KwaZulu-Natal, South Africa"
location3 = "166 Kerk Street, Vryheid, KwaZulu-Natal, South Africa"
location4 = "9 Margaret Street, Ixopo, KwaZulu-Natal, South Africa"
location5 = "16 Poort Road, Ladysmith, KwaZulu-Natal, South Africa"

# A list of all locations  
location = [location0,location1,location2,location3,location4,location5]
 
route = [0,1,2,3,4,5,0] #indexes for Initial route to be optimized
# the 0 index is added at the end of the list to complete the route

locations_route = dict(zip(location,route))# dictionary showing each location and its index

# time matrix reprenting the time it takes to travel between the cities 
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

best_route_dict = {i: location[i] for i in route}
route_addresses = best_route_dict.values()
best_path = list(route_addresses)
best_path.append(best_path[0]) # adding the initial location as the end point of the route
print("optimal time =", best_time,"minutes", "Or", best_time//60,"hrs",(best_time%60), "minutes")
print("optimal route =", best_path)
