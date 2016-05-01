#include <string>
#include <vector>
#include <fstream>
#include <iostream>

#include "boost/algorithm/string.hpp"
#include "google/protobuf/text_format.h"

#include "caffe/blob.hpp"
#include "caffe/common.hpp"
#include "caffe/net.hpp"
#include "caffe/proto/caffe.pb.h"
#include "caffe/util/db.hpp"
#include "caffe/util/format.hpp"
#include "caffe/util/io.hpp"

using caffe::Blob;
using caffe::Caffe;
using caffe::Datum;
using caffe::Net;
using std::string;
using std::fstream;
using std::ios;

template<typename Dtype>
int feature_extraction_pipeline(int argc, char** argv);

int main(int argc, char** argv) {
  return feature_extraction_pipeline<float>(argc, argv);
//  return feature_extraction_pipeline<double>(argc, argv);
}

template<typename Dtype>
int feature_extraction_pipeline(int argc, char** argv) {
  const int num_required_args = 7;
  if (argc < num_required_args) {
    LOG(ERROR)<<
    "This program takes in a trained network and an input data layer, and then"
    " extract features of the input data produced by the net.\n"
    "Usage: extract_features  pretrained_net_param"
    "  feature_extraction_proto_file  extract_feature_blob_name1"
    "  num_mini_batches GPU(CPU)"
    "  save_feature_binary_name\n";
    return 1;
  }
  if (strcmp(argv[6], "GPU") == 0) {
    LOG(ERROR)<< "Using GPU";
    int device_id = 0;
    LOG(ERROR) << "Using Device_id=" << device_id;
    Caffe::SetDevice(device_id);
    Caffe::set_mode(Caffe::GPU);
  } else {
    LOG(ERROR) << "Using CPU";
    Caffe::set_mode(Caffe::CPU);
  }

  std::string pretrained_binary_proto(argv[1]);
  std::string feature_extraction_proto(argv[2]);
  boost::shared_ptr<Net<Dtype> > feature_extraction_net(
      new Net<Dtype>(feature_extraction_proto, caffe::TEST));
  feature_extraction_net->CopyTrainedLayersFrom(pretrained_binary_proto);
  std::string extract_feature_blob_name(argv[3]);
  std::string save_feature_binary_name(argv[6]);
  fstream feature_file(save_feature_binary_name.c_str(), ios::out|ios::binary);
  int num_mini_batches = atoi(argv[4]);
  LOG(ERROR)<< "Extacting Features";
  std::vector<Blob<float>*> input_vec;
  for (int batch_index = 0; batch_index < num_mini_batches; ++batch_index) {
      feature_extraction_net->Forward(input_vec);
      const boost::shared_ptr<Blob<Dtype> > feature_blob =
          feature_extraction_net->blob_by_name(extract_feature_blob_name);
      int batch_size = feature_blob->num();
      int dim_features = feature_blob->count() / batch_size;
      const Dtype* feature_blob_data;
      for (int n = 0; n < batch_size; ++n) {
          feature_blob_data = feature_blob->cpu_data() +
            feature_blob->offset(n);
          for (int d = 0; d < dim_features; ++d) {
            feature_file.write((char *)(&feature_blob_data[d]),sizeof(float));
          }
        }
    }  // for (int n = 0; n < batch_size; ++n)
    LOG(ERROR)<< "Successfully extracted the features!";
  return 0;
}
