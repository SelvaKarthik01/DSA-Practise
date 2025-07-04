#include<iostream>
using namespace std;
int main()
{
    int arr[] = {1,2,3,4,5};
    int temp = arr[0];
    for(int i=1;i<sizeof(arr)/sizeof(arr[0]);i++)
    {
        arr[i-1] = arr[i];
    }
    arr[sizeof(arr)/sizeof(arr[0])-1] = temp;
    for(int i=0;i<sizeof(arr)/sizeof(arr[0]);i++)
    {
        cout<<arr[i]<<" ";
    }
}

// Time Complexity -> O(n)
//Space Complexity -> O(1)