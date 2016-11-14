#include <iostream>
#include <string>
using namespace std;

void sayHello();

int main () {
    int i = 0,j = 0;
    float f = 0.9;
    double d = 0.999;
    char c = 's';
    string str = "Hello", str1 = "World";
	int stringList[] = {10, 15, 20, 40, 56};
    cout<<"stringList:"<<stringList<<endl;
	cout<<"size of stringList:"<<sizeof(stringList)<<endl;
	cout<<"length of stringlist:"<<sizeof(stringList)/sizeof(int)<<endl;
    for (int index = 0; index < sizeof(stringList)/sizeof(int); index++) {
    	cout<<stringList[index]<<endl;
    }
	sayHello();
	int *ptr1 = &stringList[1];
	cout<<ptr1<<endl;
	cout<<&stringList[0]<<endl;
	int *ptr2=ptr1 + 1;
	cout<<ptr1<<endl;
	cout<<ptr2<<endl;
	cout<<*ptr2<<endl;
}

void sayHello() {
  cout<<"Hello World"<<endl;
}
