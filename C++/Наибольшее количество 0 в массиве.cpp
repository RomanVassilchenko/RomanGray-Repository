#include<bits/stdc++.h>
using namespace std;

int main()
{
	int A[10];
	for(int i = 0; i < 10; i++){
		A[i] = 0 + rand() % -2 ;
	}
	for(int i = 0; i < 10; i ++){
		cout << A[i];
	}
	int a = 0 , bufer = 0;
	for(int i = 0; i < 10; i++){
		if(A[i] == 0){
			a++;
			if(a>=bufer){
				bufer = a;
			}
		}
		else{
			a = 0;
		}
	}
	cout<<endl;
	cout << bufer ;
}
