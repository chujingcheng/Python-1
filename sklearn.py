from sklearn.linear_model import SGDClassifier

from preprocess import get_dataset_XY

def get_acc(predictlist,truelist):
    right = 0
    total = 0
    for pre, tru in zip(predictlist, truelist):
        total += 1
        if pre == tru:
            right += 1
    acc = right / 1.0 / total

trainX, trainY, testX, testY, validX, validY = get_dataset_XY
print traintX[0]

print len(trainX), len(trainY), len(testX), len(testY), len(validX), len(validY)



def build_model():
    clf = NearestCentroid()
    clf.fit(trainX,trainY)
    joblib.dump(clf,"models/nearst.model")
    predictY = clf.predict(testX)
    acc = get_acc(predictY, testY)
    print acc
    return 0






