#include <iostream>
using namespace std;
int main(){
	int numlist[]= {2,3,8,0,5,76,964,534,5,2,8};
	int summation= 0;
	for(int index=0; index<sizeof(numlist)/sizeof(int);index++){
		int e= numlist[index];
		if(e%2==0 or e%3==0){
			summation+=e;
        }			
	}
	cout<<summation<<endl;
}
