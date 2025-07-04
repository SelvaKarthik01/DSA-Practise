#include<iostream>
using namespace std;
int main()
{
    int arr[] = {1,1,2,2,3,3,4,4,5,5,6};
    int x = 0;
    int n = sizeof(arr)/sizeof(arr[0]);
    for(int i=0;i<n;i++)
    {
        x = x ^ arr[i];
    }
    cout<<x<<endl;
    return 0;
}
// Time Complexity -> O(n)
// Space Complexity -> O(1)