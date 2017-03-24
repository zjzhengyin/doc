# windows下编译调试caffe
杨力 2017.2.22 

## 1. 下载源码
https://github.com/BVLC/caffe
branch选择windows， 下载源码

## 2. 打开工程
CommonSettings.props.example 复制一份，命名为CommonSettings.props，用文本编辑器打开（如notepad++），修改其中选项。

打开windows目录，用vs2013打开sln解决方案文件。


## 3. 编译运行
直接build即可。

此解决方案中自带的多个可执行工程，可直接运行，例如compute_image_mean，extract_features等。
