#include"student.pb.h"
#include <fcntl.h>
#include <unistd.h>
#include <iostream>
#include <google/protobuf/text_format.h>
#include <google/protobuf/io/zero_copy_stream_impl.h>

using google::protobuf::io::FileInputStream;

int main(){
    test::Student zhangkun;
    int fd = open("test.txt", O_RDONLY);
    FileInputStream* input = new FileInputStream(fd);
    google::protobuf::TextFormat::Parse(input, &zhangkun);
    delete input;
    close(fd);

    std::cout<<zhangkun.name()<<"\n"
             <<zhangkun.age()<<"\n"
             <<zhangkun.gard()<<std::endl;
    return 0;
}



