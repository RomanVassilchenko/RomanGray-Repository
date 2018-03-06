#include<bits/stdc++.h> 
using namespace std;
 int k = 0;
int b;
int C[100];
int B[100]; 
int desat = 0;
int Chi = 2 ,  
a = 5; string s = " ";  
void fun (int Chi, int a) 
{ if (a == 0){     
return; } if(a!=0){       
b = a;      
B[k] = a % Chi;     
fun(Chi , a % Chi);     
k++;    
for(int i = 0; i < k; i++){     
C[i] = B[k - 1 - i]; }  
for(int i = 0 ; i < k; i++){     
if(C[i] == 10){         
s = s + "A";            
}     if(C[i] == 11){          
s = s + "B";             }
     if(C[i] == 12){          
	 s = s + "C";           
	 }     if(C[i] == 13){          
	 s = s + "D";             
	 }     if(C[i] == 14){          
	 s = s + "E";        
	 }     if(C[i] == 15){         
	 s = s + "F";            
	 }     if(C[i] < 10)     
	 {         
	 char tmp = C[i] + '0';         
	 s = s + tmp;         
	 }     
	 }     
	 cout <<"¬ведите " << b << " ??????????? ? " <<Chi <<" ??????? ? ????? = " <<s << endl;     
	 } }       
	 int main()
	 { setlocale(LC_ALL, "rus");
	  cout <<" ??????? ???????????" << endl;
	    cin >> Chi; 
		 cout <<" ??????? ???? ?????" << endl; 
		 cin >> a; 
		 cout << endl;  
		 fun ( Chi, a); 
		 cout << endl; 
		 cout <<" ?????" << s << " ??????????? ? ?????????? ? ????? = "<< a << endl;    
		 }
