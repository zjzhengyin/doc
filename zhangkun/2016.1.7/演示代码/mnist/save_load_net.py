import mxnet as mx
def get_mlp0():
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
    
def get_mlp1():
    
    data = mx.symbol.Variable('bigData')
    mlp  = mx.symbol.SoftmaxOutput(data = data, name = 'softmax')
    return mlp
    
mlp=get_mlp0()
mlp.save('my_symbol')
'''
    how to save a Symbol
    ----mlp.save('pname')
    ----mxnet.symbol.Symbol.save()
......................................................................................
    how to load a Symbol
    ----mxnet.symbol.load('pname')
'''
    
