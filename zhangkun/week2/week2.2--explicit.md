#week2.2--explicit
##c++中explicit关键字的使用
在看c++代码时经常会遇到explicit的使用，由于之前很少进行编程的训练，所以用到的c++关键字屈指可数。关于explicit关键字的使用，用一个小例子说明一下。如下：
```c++
#include<iostream>
#include<string>

using namespace std;

class Student{
public:
    Student(int age){
        this->age = age;
        cout<<this->age<<endl;
    }
private:
    int age;
};

class Teacher{
public:
    explicit Teacher(int age){
        this->age = age;
        cout<<this->age<<endl;
    }
private:
    int age;
};

int main(){
    Student zhang(23);
    Student wang = 43;  //right
    Teacher xue = Teacher(50);
//  Teacher zhao = 50;   //wrong
    return 0;
}

```
---
简要的说explicit关键字的用处就是类的实例化必须显示地调用构造函数完成。