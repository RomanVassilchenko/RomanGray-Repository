#include<bits/stdc++.h>
using namespace std;

int main()
{
	srand(time(0));
	int A[10];
	int B[10];
	int C[100];
	for(int i = 0 ; i < 10; i++){
		A[i] = rand()%101;
		B[i] = rand()%101;
	}
	for(int i = 0; i < 10; i++){
	cout << A[i] << " ";	
	}
	cout << endl;
	for(int i = 0; i < 10; i++){
		cout << B[i] << " ";
	}
	cout << endl;
	for(int i = 0; i < 10; i++){
		C[i] = A[i];
	}
	for(int i = 0; i < 10; i++){
	C[i+10] = B[i];	
	}
	
	for(int i = 0; i < 20; i++){
		cout << C[i] << " ";
	}
	return 0;
}
