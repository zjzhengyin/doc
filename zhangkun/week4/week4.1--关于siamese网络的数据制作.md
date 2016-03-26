#关于siamese网络所用数据的制作

本周的实验由于用到了siamese,所以简单学习了一下caffe下数据转换的流程。
由于siamese网络本身的特点，其所需的数据是成对出现的，所以caffe自带的convert_imageset程序并不能直接拿来使用。需要做一些修改，关键部分如下;
```c++
bool nReadImageToDatum(const string& filename1,const string& filename2, const int label,const int height, const int width, const bool is_color, Datum* datum) {
  cv::Mat cv_img1 = ReadImageToCVMat(filename1, height, width, is_color);
  cv::Mat cv_img2 = ReadImageToCVMat(filename2, height, width, is_color);
  if (cv_img1.data && cv_img2.data) {
      vector<cv::Mat> chanels;
      chanels.push_back(cv_img1);
      chanels.push_back(cv_img2);
      cv::Mat cv_img;
      cv::merge(chanels, cv_img);
      CVMatToDatum(cv_img, datum);
      datum->set_label(label);
      return true;
  }
  else{
    std::cout<<"something wrong!"<<std::endl;
    return false;
  }
}
```

ps:
非常感谢尹奕博师兄提供的帮助。