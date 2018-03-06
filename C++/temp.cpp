#include<bits/stdc++.h>
using namespace std;

string A;
string B;
string C;
int L = 0;
int N;
int S;
int bufer = 0;

int main()
{
   
    cin >> N;
	for(int i = 0 ; i < N; i++){
	    cin >> A[i];
	}
	for(int i = 0 ; i < N; i++){
	    cin >> B[i];
	}
	for(int i = N - 1; i >= -1; i--){
	    bufer = A[i] + B[i] + C[i];
	    C[i] = bufer%2;
	    C[i - 1] = C[i - 1] + bufer/2;
	   
	}
	for(int i = -1 ; i < N; i++){
	    cout << C[i] << " ";
	}
	

	
}
