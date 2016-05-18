'''
usage:
    python my_align_face.py inputDir outPutdir --gray 0(gray) or 1(rgb)
    create originally for outputing 144*144 
    the eye_center locates at row:47
    the mouth_center locates at row:95  
    
    if you'd like to use this program ,please dowload shape_predictor_68_face_landmarks.dat from http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 
    
    changed by zhangkun based on https://github.com/tornadomeet/mxnet-face/blob/master/util/align_face.py .
    thanks for your reading.
'''

import cv2
import dlib
import numpy as np
import os,errno
import argparse

def mkdirP(path):
    assert path is not None
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
            
class Image:
    def __init__(self,path):
        assert path is not None
        self.path = path

    def getBGR(self):
        try:
            bgr = cv2.imread(self.path)
        except:
            bgr = None
        return bgr

    def getRGB(self):
        bgr = self.getBGR()
        if bgr is not None:
            rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
        else:
            rgb = None
        return rgb
    def getGRAY(self):
        gray = cv2.imread(self.path,cv2.IMREAD_GRAYSCALE)
        return gray

    def __repr__(self):
        return '({})'.format(self.path)
        
class AlignDlib:
    def __init__(self):
        facePredictor = './shape_predictor_68_face_landmarks.dat'
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(facePredictor)
        
    def getAllFaceBoundingBoxes(self, rgbImg):
        assert rgbImg is not None
        try:
            return self.detector(rgbImg, 1)
        except Exception as e:
            print("Warning: {}".format(e))
            return []
    def getLargestFaceBoundingBox(self, rgbImg):
        assert rgbImg is not None
        faces = self.getAllFaceBoundingBoxes(rgbImg)
        if len(faces) > 0:
            return max(faces, key=lambda rect: rect.width() * rect.height())
        else:
            return None

    def findLandmarks(self, rgbImg, bb):
        assert rgbImg is not None
        assert bb is not None
        points = self.predictor(rgbImg, bb)
        return list(map(lambda p: (p.x, p.y), points.parts()))

    def align(self, imgDim, rgbImg):
        assert imgDim is not None
        assert rgbImg is not None
        bb = None
        opencv_model="./cascade.xml"
        face_cascade = cv2.CascadeClassifier(opencv_model)
        faces = face_cascade.detectMultiScale(rgbImg, 1.1, 2, minSize=(30, 30))
        dlib_rects = []
        for (x,y,w,h) in faces:
            dlib_rects.append(dlib.rectangle(int(x),
                              int(y), int(x+w), int(y+h)))
            if len(faces) > 0:
                bb = max(dlib_rects, 
                    key=lambda rect: rect.width() * rect.height())
            else:
                bb = None
        if bb is None:
            bb = self.getLargestFaceBoundingBox(rgbImg)
        if bb is None:
            return None
        assert bb is not None
        landmarks = self.findLandmarks(rgbImg, bb)
        npLandmarks = np.float32(landmarks)
        leftInerEye = npLandmarks[39]
        rightInerEye = npLandmarks[42]
        leftMouth = npLandmarks[48]
        rightMouth = npLandmarks[54]
        eyec = (leftInerEye+rightInerEye)/2
        mouthc = (leftMouth+rightMouth)/2
        disEyecToMouthc = np.linalg.norm(eyec-mouthc)
        disLefteyeToCenter = np.linalg.norm(leftInerEye-rightInerEye)/2
        disLefemouthToCenter = np.linalg.norm(leftMouth-rightMouth)/2
        alpha = 48.0/disEyecToMouthc
        srcPoints = np.float32([eyec,mouthc,rightInerEye])
        dstEyec = np.float32([(71.5,47)])
        dstMouthc = np.float32([(71.5,95)])
        dstRightInerEye = np.float32([(71.45+alpha*disLefteyeToCenter,47)])
        dstPoints = np.float32([dstEyec,dstMouthc,dstRightInerEye])
        H = cv2.getAffineTransform(srcPoints,dstPoints)
        thumbnail = cv2.warpAffine(rgbImg, H, (imgDim, imgDim))
        return thumbnail

def alignMain(args):
    mkdirP(args.outputDir)
    imgs = list(iterImgs(args.inputDir))
    align = AlignDlib()
    for imgObject in imgs:
        print("=== {} ===".format(imgObject.path))
        outDir = os.path.dirname(os.path.join(args.outputDir,
                        os.path.relpath(imgObject.path,args.inputDir))) 
        mkdirP(outDir)
        rgb = imgObject.getRGB()
        outPath = os.path.join(outDir, os.path.basename(imgObject.path))
        assert rgb is not None
        outRgb = align.align(args.size, rgb)
        if outRgb is not None:
            if args.gray :
                outImg = cv2.cvtColor(outRgb, cv2.COLOR_RGB2GRAY)
            else:
                outImg = cv2.cvtColor(outRgb, cv2.COLOR_RGB2BGR)
        else:
            if args.gray :
                outImg = cv2.resize(imgObject.getGRAY(),(args.size,args.size))
            else :
                outImg = cv2.resize(imgObject.getBGR(),(args.size,args.size))
        
        cv2.imwrite(outPath,outImg)
        
def iterImgs(directory):
    assert directory is not None
    exts = [".jpg", ".png"]
    for dirPath,dirNames,fileNames in os.walk(directory):
        for fileName in fileNames:
            ext = os.path.splitext(fileName)[1]
            if ext in exts:
                yield Image(os.path.join(dirPath,fileName))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="a simple program for face align")
    parser.add_argument('inputDir', type=str, help="Input image directory.")
    parser.add_argument(
        'outputDir', type=str, help="Output directory of aligned images.")
    parser.add_argument('--size', type=int, help="Default image size 128.",
                                 default=144)
    parser.add_argument('--gray',type = int,help="default false(0), output 3-chanels' image",default =0)
    args = parser.parse_args()
    alignMain(args)
