#include<bits/stdc++.h>
using namespace std;
int main (){
	string start;
	string bud;
	
	cin >> start >> bud;
	int day = 0;
	
	int hour = 0, min = 0, second = 0;
	
	 second = (start[6] - '0') * 10 + start[7] - '0';
	 min = (start[3] - '0') * 10 + start[4] - '0';
	 hour = (start[0] - '0') * 10 + start[1] - '0';
	 
	 
	 second = second + (bud[6] - '0') * 10 + bud[7] - '0';
	 min =  min + (bud[3] - '0') * 10 + bud[4] - '0';
	 hour =  hour + (bud[0] - '0') * 10 + bud[1] - '0';
	 
	 
	 
	 while(second >= 60){
	 	second = second - 60;
	 	min++;
	 }
	 while(min >= 60){
	 	min = min - 60;
	 	hour++;
	 }
	 while(hour >= 24){
	 	hour = hour - 24;
	 	day++;
	 }
	 
	 


cout << day << ":" << hour << ":" << min << ":" << second;
return 0;
}
