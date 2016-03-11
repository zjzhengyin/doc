#week2.1 -- protobuf
##protobuf的简单使
protobuf在caffe中有很重要的运用，所以简单了解一下还是有点用处的，我对protobuf的认识现在只停留在最初级的阶段，感觉就是一个生成类的工具，提供了统一的接口，下面是一个简单的例子。	

---
1. student.proto 
```proto
package test;
message Student{
      required string name = 1;
      required int32  age  = 2;
      optional float  gard = 3;
	  }
```
2. 生成目标头文件及cC文件,命令如下
```shell
protoc --cpp_out=<directory> student.proto
```
3. test.cpp 进行测试
```c++
#include"student.pb.h"
#include <string>
#include <iostream>
using namespace std;
int main(){
      test::Student zhangkun;
      zhangkun.set_name("zhangkun");
      zhangkun.set_age(24);
      zhangkun.set_gard(100);
      cout<<zhangkun.name()<<endl;
      cout<<zhangkun.age()<<endl;
      cout<<zhangkun.gard()<<endl;
      cout<<"succeed!"<<endl;
      return 0;
}
```
4. 编译
```c++
g++ -std=c++11 test.cpp student.pb.cc `pkg-config --cflags --libs protobuf` -o <binary>
```
5. 结果
```c++
zhangkun
24
100
succeed!
```

done!





