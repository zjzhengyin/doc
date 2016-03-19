##读写.solverstate和.caffemodel文件
.solverstate和.caffemodel是在caffe的使用过程中常会遇到的两种文件，由于它们都是二进制文件所以不能直接查看。如果我们想知道这里面到底写的是什么东西，可以通过调用io.cpp里的函数进行读取再格式化输出到文件中进行查看。

在` 读写.solverstate和.caffemodel文件`目录下，我写了一个简单的程序来进行读写这两种文件，大家看一下就会明白的。

###tips:
大家在编译此程序的时候，我建议把它放到`yourcaffe/tools`目录下，然后执行make命令，编译链接成功后会在`yourcaffe/build/tools`目录下生成相应的可执行文件。

March 19, 2016 8:36 PM