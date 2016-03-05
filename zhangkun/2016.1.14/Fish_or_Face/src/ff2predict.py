import mxnet as mx
import numpy

root_dir = '../data/test100face/'
rec_path = root_dir + 'test100.rec'
label_lst = root_dir + 'test100.lst'
testlabel_lst = root_dir + 'test100l.lst'

model = mx.model.FeedForward.load(prefix = 'ff2',epoch = 20,ctx = mx.gpu(0))
val = mx.io.ImageRecordIter(
    path_imgrec = rec_path,
    data_shape  = (3,28,28),
    batch_size  = 1,)

result = model.predict(X = val)

a = result.shape[0]
ff_val = open(label_lst,'r')
ff_val1 = open(testlabel_lst,'w')
correct_num = 0


for b in range(a):
    line=ff_val.readline()
    if result[b][0] > result[b][1] :
        predict = '0\tfish'
    else :
        predict = '1\tface'
    print b
    new_line = line.strip('\n') + '\t'+predict+'\n'
    ff_val1.writelines(new_line)

ff_val1.close()
ff_val1 = open(testlabel_lst,'r')

for line in ff_val1.readlines():
    print line
    for_count_line = line.strip('\n').split('\t')
    if for_count_line[1].strip() ==  for_count_line[-2] :
        correct_num = correct_num + 1

    
ff_val.close()
ff_val1.close()
print "example..............",a
print "correct_num..........",correct_num
