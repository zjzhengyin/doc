#include"student.pb.h"
#include <fcntl.h>
#include <unistd.h>
#include <google/protobuf/text_format.h>
#include <google/protobuf/io/zero_copy_stream_impl.h>

using google::protobuf::io::FileOutputStream;

int main(){
    test::Student zhangkun;//student.pb.h
    zhangkun.set_name("zhangkun");
    zhangkun.set_age(24);
    zhangkun.set_gard(100);

    int fd = open("test.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);//fcntl.h
    FileOutputStream* output = new FileOutputStream(fd);//zero_copy_stream_impl.h
    google::protobuf::TextFormat::Print(zhangkun, output);//text_format.h
    delete output;
    close(fd);//unistd.h
    return 0;
}
