import mxnet as mx
def get_mlp():
    """
    multi-layer perceptron
    """
    data = mx.symbol.Variable('data')
    fc1  = mx.symbol.FullyConnected(data = data, name='fc1', num_hidden=128)
    act1 = mx.symbol.Activation(data = fc1, name='relu1', act_type="relu")
    fc2  = mx.symbol.FullyConnected(data = act1, name = 'fc2', num_hidden = 64)
    act2 = mx.symbol.Activation(data = fc2, name='relu2', act_type="relu")
    fc3  = mx.symbol.FullyConnected(data = act2, name='fc3', num_hidden=10)
    mlp  = mx.symbol.SoftmaxOutput(data = fc3, name = 'softmax')
    return mlp
    
def get_iterator():
    data_dir = "/home/zhaixingzi/NutstoreForMaterials/知识分享/2016.1.7/演示代码/mnist/mnist/"

    train           = mx.io.MNISTIter(
        image       = data_dir + "train-images-idx3-ubyte",
        label       = data_dir + "train-labels-idx1-ubyte",
        input_shape = (784,),
        batch_size  = 128,
        shuffle     = True,
        flat        = True,
        num_parts   = 1,
        part_index  = 0)

    val = mx.io.MNISTIter(
        image       = data_dir + "t10k-images-idx3-ubyte",
        label       = data_dir + "t10k-labels-idx1-ubyte",
        input_shape = (784,),
        batch_size  = 128,
        flat        = True,
        num_parts   = 1,
        part_index  = 0)

    return (train, val)
    
def fit(data_loader):
    (train,val)=data_loader()
    model = mx.model.FeedForward(
        ctx                = mx.cpu(),
        symbol             = get_mlp(),
        num_epoch          = 10,
        learning_rate      = .1,
        momentum           = 0.9,
        wd                 = 0.00001,
        initializer        = mx.init.Xavier(factor_type="in", magnitude=2.34),
        )

    model.fit(
        X                  = train,
        eval_data          = val,
        kvstore            = mx.kvstore.create('local'),
        batch_end_callback = mx.callback.Speedometer(128, 50),
        epoch_end_callback = None)
        
    return model

#*************************************************************************************
#*************************************************************************************
model=fit(get_iterator)
model.save('my-mnist-module', 1234)
print "done!"
