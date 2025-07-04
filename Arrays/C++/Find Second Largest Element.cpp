#include<iostream>
using namespace std;
int main()
{
    int arr[] = {1,2,4,7,7,5};
    int largest = arr[0];
    int slargest = -1;
    for(int i=0;i<sizeof(arr)/sizeof(arr[0]);i++)
    {
        if (arr[i] > largest)
        {
            slargest = largest;
            largest = arr[i];
            
        }
        if (arr[i] < largest && arr[i] > slargest)
        {
            slargest = arr[i];
        }
    }
    cout<<slargest<<endl;
}