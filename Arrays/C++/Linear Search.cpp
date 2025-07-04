#include<iostream>
using namespace std;
int main()
{
    int arr[] = {1,2,3,4,5};
    int el = 3;
    int flag = -1;
    int n = sizeof(arr)/sizeof(arr[0]);
    for(int i=0;i<n;i++)
    {
        if (arr[i] == el)
        {
            flag = i;
            break;
        }
    }
    cout<<flag<<endl;
}
// Time Complexity -> O(n)
// Space Complexity -> O(1)