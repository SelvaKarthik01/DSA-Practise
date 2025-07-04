#include<iostream>
using namespace std;
int main()
{
    int arr[] = {1,2,3,4,5,6,7};
    int d = 8;
    d = d % (sizeof(arr)/sizeof(arr[0]));
    int temp[d];
    for(int i=0;i<d;i++)
    {
        temp[i] = arr[i];
    }
    for(int i=d;i<sizeof(arr)/sizeof(arr[0]);i++)
    {
        arr[i-d]=arr[i];
    };
    int n = sizeof(arr)/sizeof(arr[0]) - sizeof(temp)/sizeof(temp[0]);
    int j = 0;
    for(int i=n;i< sizeof(arr)/sizeof(arr[0]);i++)
    
    {
        arr[i] = temp[j];
        j += 1;
    }
    for(int i=0;i<sizeof(arr)/sizeof(arr[0]);i++)
    {
        cout<<arr[i]<<" ";
    }
}

