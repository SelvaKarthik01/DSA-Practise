#include<iostream>
using namespace std;
int main()
{
    int arr[] = {1,2,4,5};
    int n = 5;
    int N = sizeof(arr)/sizeof(arr[0]);
    int sum_n = n*(n+1)/2;
    int s = 0;
    for(int i =0;i<N;i++)
    {
        s += arr[i];
    }
    cout<<sum_n - s<<endl;
}
// Time Complexity -> O(n)
// Space Complexity -> O(1)