#include"student.pb.h"
#include <string>
#include <iostream>
#include <fstream>

int main(){
      test::Student zhangkun;
      zhangkun.set_name("zhangkun");
      zhangkun.set_age(24);
      zhangkun.set_gard(100);
      fstream out("test_zk",ios::out | ios::trunc | ios::binary);
      zhangkun.SerializeToOstream(&out);
      return 0;
}

/*
2016年03月17日 星期四 23时49分31秒 
*/

