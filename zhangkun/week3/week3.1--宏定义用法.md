#关于宏定义的三种常见用法
直接看代码
```c++
#include <iostream>
#define mult(x,y)    x*y
#define str(x) #x
#define add(x,y) x##y

using namespace std;

int main()
{

	int  mult = mult(1,0);
	cout<<mult<<endl;
    auto temp = str(zhangkun);
    cout<<temp<<endl;
	int  ten  = add(1,0);
	cout<<ten<<endl;

    return 0;
}
```
执行结果：
```c++
0
zhangkun
10

```
done!

March 15, 2016 7:30 PM
by zhangkun
