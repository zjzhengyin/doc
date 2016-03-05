import mxnet as mx
import numpy as np
data_dir = "/home/zhaixingzi/NustoreForCode/machine_learning/mxnet_practice/example/image-classification/mnist/"
val = mx.io.MNISTIter(
    image       = data_dir + "t10k-images-idx3-ubyte",
    label       = data_dir + "t10k-labels-idx1-ubyte",
#    label       = None,
    input_shape = (784,),
    flat        = True)
m = mx.model.FeedForward.load(prefix='my_mnist_model',epoch =18637959467,ctx = mx.cpu())
c = m.predict(X = val)
np.save('predict',c)
np.savetxt('predict.txt',c)
print 'done'
'''
success!
'''
