//jagged array is a 2d matrix with  variable size of column
#include<iostream>
using namespace std;
int main()
{
  
  int r,c;
  r=3;
  int s[]={4,3,2};
    int**arr=new int*[r];//declearing heap
    for(int i=0;i<r;i++)
    {
        arr[i]=new int[s[i]];
        // or *(arr+i)
    }
    cout<<"enter the element of matrix"<<endl;
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<s[i];j++)
        {
            cin>>arr[i][j];

        }
         cout<<endl;
    }

    for(int i=0;i<r;i++)
    {
        for(int j=0;j<s[i];j++)
        {
            cout<<arr[i][j];
        }
        cout<<endl;
    }
    //releasing the memory
     for(int i=0;i<r;i++)
    {
        delete [] arr[i];
    }
    //deleting the whole array
    delete [] arr;

 return 0;
}
