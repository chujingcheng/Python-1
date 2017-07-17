from pydub import AudioSegment
import os
from pymir import AudioFile
import soundfile
from pydub import AudioSegment
from calcLPCC import calcLPCC
import numpy
def wavread(filename):
    x, fs = soundfile.read(filename)
    return x, fs

def wavwrite(filename, y, fs):
    soundfile.write(filename, y, fs)
    return 0

def format_2_wav(audioPath="audio.ogg"):
    song = AudioSegment.from_file(audioPath, audioPath[-3:])
    song = song.set_channels(1)
    song.export(audioPath.replace(audioPath[-3:], "wav"), "wav")
    return 0


def batach_format_2_wav(audioDir="dataset/"):
    print audioDir
    for root, dirs, names in os.walk(audioDir):
        print names
        for name in names:
            audioPath = os.path.join(root, name)
            if ".ogg" in audioPath or ".mp3" in audioPath:
                format_2_wav(audioPath)
                print audioPath, "........"

    return 0


def calcLPCC(wav_path, frame_size=1024, lpcc_order=12):
    wavData = AudioFile.open(wav_path)
    lpcc_feature = []
    # Decomposing into frames
    # Fixed frame size
    windowFunction = numpy.hamming
    fixedFrames = wavData.frames(frame_size, windowFunction)
    for frame_item in fixedFrames:
        frame_lpcc_feature = frame_item.lpcc(lpcc_order)
        drop_flag = False
        for number in frame_lpcc_feature:
            if math.isinf(number) or math.isnan(number):
                drop_flag = True
                break
        if not drop_flag:
            lpcc_feature.append(frame_lpcc_feature)
    # print lpcc_feature
    # print len(lpcc_feature)
    lpcc_feature = numpy.array(lpcc_feature)

    return lpcc_feature

def extract_lpcc_feat(audioPath):
    songXlpcc = []
    songYlabel = []
    audioData , fs = wavread(audioPath)
    if"train"in audioPath:
        lab_path = audioPath.replace("train","lab")[:-3] + "lab"
    elif "test" in audioPath:
        lab_path = audioPath.replace("test","lab")[:-3] + "lab"
    else:
        lab_path = audioPath.replace("valid", "lab")[:-3] + "lab"
    lab_file = open(lab_path, "r")
    lab_content = lab_file.readlines()
    lab_file.close()
    for segment in lab_content:
        list_segment = segment.split(" ")
        start = float(list_segment[0])
        end = float(list_segment[1])
        label = list_segment[2][:-1]
        segmentData = audioData[int(start * fs):int(end * fs)]
        temp_path = 'tempSegment.wav'
        wavwrite(temp_path, segmentData, fs)
        segmentLPCC = calcLPCC(temp_path)
        os.remove(temp_path)
        for lpcc_item in segmentLPCC:
            songXlpcc.append(lpcc_item)
            songYlabel.append(label)

    return songXlpcc, songYlabel


def batch_extract_lpcc_feat(audio_dir):
    finalX = []
    finalY = []
    for root, dirs, filenames in os.walk(audio_dir):
        for filename in filenames:
            audioPath = os.path.join(root,filename)
            if".wav" in audioPath:
                songLPCC,songLabel = extract_lpcc_feat(audioPath)
                finalX.extend(songLPCC)
                finalY.extend(songLabel)
    return finalX,finalY

def save_dataset_XY(trainX, trainY, testX, testY, validX, validY):
    file = h5py.File('D:\Python\music\dataset.h5', 'w')
    file.create_dataset('trainX', data=trainX)
    file.create_dataset('trainY', data=trainY)
    file.create_dataset('testX', data=testX)
    file.create_dataset('testY', data=testY)
    file.create_dataset('validX', data=validX)
    file.create_dataset('validY', data=validY)
    file.close()

    return 0


def get_dataset_XY(dataset_h5='D:\Python\music\dataset.h5'):
    file = h5py.File(dataset_h5, 'r')
    trainX = file['trainX'][:]
    trainY = file['trainY'][:]
    testX = file['testX'][:]
    testY = file['testY'][:]
    validX = file['validX'][:]
    validY = file['validX'][:]
    file.close()
    return trainX, trainY, testX, testY, validX, validY




def main():
    sep = os.sep
    audioDir = "D:\Python\music" + sep
    print audioDir
    # batach_format_2_wav(audioDir)
    trainx, trainy = batch_extract_lpcc_feat(audioDir + "train")
    testx, testy = batch_extract_lpcc_feat(audioDir + "test")
    validx, validy = batch_extract_lpcc_feat(audioDir + "valid")
    return 0

if __name__ == '__main__':
    main()