"""
Docstring for Binary Search.Minimize Max Distance to Gas Stations

import heapq
def Insert_Max_Heap(L,heap):
    for i in range(1,len(L)):
        heapq.heappush(heap,(-(L[i]-L[i-1]),i-1))
    
def Max_Gas_Station(L,heap,sector,k):
    while(k > 0):
        max_distance,index = heapq.heappop(heap)
        sector[index] += 1
        new_distance = (L[index+1]-L[index])/(sector[index]+1)
        k -=1 
        heapq.heappush(heap,((-new_distance),index))
        print(heap)
    
L= eval(input("Enter the Distances of Gas Statations : "))
k = int(input("Enter the Number of Stations to be Added : "))
sector = [0]*(len(L)-1)
heap = []
Insert_Max_Heap(L,heap)
Max_Gas_Station(L,heap,sector,k)
max_distance, index = heapq.heappop(heap)
print(max_distance*-1)


TC -> O((n-1)*log(n-1)) -> for inserting the distance into a max heap + O(klogk) for pushing after instering the gas station 
                  Total -> O(nlogn) + O(nlogn) -> 2O(nlogn) -> O(nlogn)
SC -> O(n-1) for sectors + O(n-1) for max heap -> O(2(n-1)) -> O(n)


Time Compleixty : O(logn) for Binary Search + O(n) for finding the max Distance
                  Total -> O(n)
Space Complexity : O(1)

"""
import math
def Max_Distance(L):
    maxi = 0 
    for i in range(len(L)-1):
        maxi = max(maxi,L[i+1]-L[i])
    return maxi 
def GasStation(L,dist):
    no_stations = 0 
    for i in range(len(L)-1):
        distance = L[i+1]-L[i]
        no_stations += math.floor(distance/dist)
        if distance % dist == 0:
            no_stations -= 1
    return no_stations
def Binary_Search(L,k):
    MAX = 10**(-6)
    low = 0 
    high = Max_Distance(L)
    while(high-low > MAX):
        mid = low + (high-low)/2
        if GasStation(L,mid) <= k:
            ans = mid
            high = mid - MAX
        elif GasStation(L,mid) > k:
            low = mid + MAX
    return ans 
L = eval(input("Enter the Gas Station Across X Axis: "))
k = int(input("Enter the No. of Gas Station to be Added: "))
print(Binary_Search(L,k))


