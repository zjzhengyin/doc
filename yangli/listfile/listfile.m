
% 列出fileFolder目录下所有文件和子文件夹 的文件名，不加标号， 采用相对或绝对路径
%fileFolder='F:/data/face/lfw/lfw';
%fileFolder='G:/data/lfw/lfw';
%fileFolder='H:/data/face/casia/CASIA-WebFace';
%fileFolder='G:/data/face/facelib/target';
%fileFolder='G:/data/face/facelibc';
%fileFolder='D:/data/CASIA-WebFace';
%fileFolder='D:/data/CASIA-WebFacec-80x96';
%fileFolder='D:/data/CASIA-WebFacec-60x72-check';
%fileFolder='D:/proj/face/caffe/caffe-windows-git/buildVS2013/FaceTrace/bin/facelib';
%fileFolder='G:/data/face/FDDB/originalPics';
%fileFolder='G:/data/face/casia/CASIA-WebFacec';
%fileFolder='F:/data/face/facedet/negdata';
%fileFolder='G:/data/face/gs/ok';
fileFolder='F:/data/face/casia-maxpy/CASIA-maxpy-cleancc';
%fileFolder='F:/data/face/smallface/dinggonglu';
%fileFolder='G:/data/face/gs/okc';

fid = fopen('list_rec.txt', 'w');
dirOutput=dir(fullfile(fileFolder,'*'));
%filePrefix = strcat(fileFolder, '/'); %采用绝对路径
filePrefix = ''; % 采用相对路径
for i = 3:size(dirOutput, 1)
   if (dirOutput(i).isdir)%
        dir2 = dir(fullfile(fileFolder, dirOutput(i).name));
        for j = 3:size(dir2, 1)
            name = strcat(filePrefix, dirOutput(i).name, '/', dir2(j).name);
            fprintf(fid, '%s\n', name);
        end
   else
        name = strcat(fileFolder, '/', dirOutput(i).name);
        fprintf(fid, '%s\n', name);
   end
end
fclose(fid);