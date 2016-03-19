#include <iostream>
#include "caffe/caffe.hpp"
#include <string>

bool make_choice(std::string &filename){
    if(filename.rfind(".solverstate")!=std::string::npos){
        caffe::SolverState state;
        caffe::ReadProtoFromBinaryFile(filename, &state);
        caffe::WriteProtoToTextFile(state,filename+"txt"); 
        return 1;
    }
    if(filename.rfind(".caffemodel")!=std::string::npos){
        caffe::NetParameter param;
        caffe::ReadProtoFromBinaryFile(filename, &param);
        caffe::WriteProtoToTextFile(param,filename+"txt");
        return 1;
    }
    return 0;
}
        

int main(){
    std::string infilename;
    std::cout<<"请输入需读取文件名"<<std::endl;
    std::cin>>infilename;
    
    if(make_choice(infilename))
        std::cout<<"done"<<std::endl;
    else
        std::cout<<"something wrong!"<<std::endl;
    return 0;   
}

