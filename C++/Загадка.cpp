#include<bits/stdc++.h>
using namespace std;
int main (){
 	int P,S;
 	double x,y;
 	cin >> P >> S;
 	y = (P + sqrt(P*P - 4 * S)) / 2;
 	x = P - y;
 	cout << x << " " << y;
return 0;
}
