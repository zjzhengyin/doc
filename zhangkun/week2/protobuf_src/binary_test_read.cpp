#include"student.pb.h"
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

int main(){
      test::Student zhangkun;
      fstream in("./test_zk",ios::in | ios::binary);
      zhangkun.ParseFromIstream(&in);
      
      cout<<zhangkun.name()<<"\n"
          <<zhangkun.age()<<"\n"
          <<zhangkun.gard()<<endl;
      return 0;
}

/*
2016年03月17日 23时49分58秒 
*/
