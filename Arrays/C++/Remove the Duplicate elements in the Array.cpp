#include<iostream>
using namespace std;
int main()
{
    int arr[] = {1,1,2,2,2,2,3,3};
    int first = 0 ;
    int second =1;
    while(second != sizeof(arr)/sizeof(arr[0]))
    {
        if (arr[second] != arr[first])
        {
            arr[first+1] = arr[second];
            first = first + 1;
        }
        second += 1;
    }
    cout<<first+1<<endl;
}
//Time Complexity -> O(n)