#include<iostream>
using namespace std;
int main()
{
    int arr[] = {1,0,2,3,2,0,0,4,5,1};
    int first = 0; 
    int second = first + 1;
    int n = sizeof(arr)/sizeof(arr[0]);
    while(second != n)
    {
        if (arr[first] == 0)
        {
            while(arr[second] == 0)
            {
                second += 1;
            }
            arr[first] = arr[second];
            arr[second] = 0;
            second += 1;
        }
        first += 1;
    }
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}
//Time Complexity -> O(n)
//Space Complxity -> O(1)