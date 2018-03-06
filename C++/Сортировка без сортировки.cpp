#include<bits/stdc++.h>
using namespace std;

int a[5];
int b[7];
int c[100];

int main ()
{
	srand(time(0));
	
	for(int i = 0; i < 5; i++){
		a[i] = rand()%101;
	}
	
	for(int i = 0; i < 7; i++){
		b[i] = rand()%101;
	}
	sort(a + 0, a + 5);
	sort(b + 0, b + 7);
	
	for(int i = 0; i < 5; i++){
		cout << a[i] << " ";
	}
	cout << endl;
	
	
	for(int i = 0; i < 7; i++){
		cout << b[i] << " ";
	}
	cout << endl;
	
	
	
	int i = 0, j = 0, k = 0;
	
	
	while(i!=5 && j!=7){
		if(a[i] < b[j]){
				c[k] = a[i];
				i++;
				k++;
			}
			else if(a[i] > b[j]){
				c[k] = b[j];
				j++;
				k++;
			}
			else{
				c[k] = b[j];
				c[k+1] = a[i];
				i++;
				j++;
				k++;
			}
			
			
			if(i == 5 && j != 7){
				c[k] = b[j];
				j++;
				k++;
				
			}
			else if( i != 5 && j == 7) {
				c[k] = b[j];
				i++;
				k++;
			}
	}
		while(i!=5){
			c[k] = a[i];
			k++;
			i++;
		}
		while(j!=7){
			c[k] = b[j];
			k++;
			j++;
		}
		
	
	for(int i = 0 ; i < 12; i ++) {
		cout << c[i] << " ";
	}
}
