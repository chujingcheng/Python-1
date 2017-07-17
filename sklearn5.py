import joblib
from sklearn.linear_model import SGDClassifier

from preprocess import get_dataset_XY


def get_acc(predictList, trueList):
    right = 0
    total = 0
    for pre, tru in zip(predictList, trueList):
        total += 1
        if pre == tru:
            right += 1
    acc = right / 1.0 / total
    return acc


trainX, trainY, testX, testY, validX, validY = get_dataset_XY()
print trainX[0], trainY[0]

print len(trainX), len(trainY), len(testX), len(testY)


def build_model():
    clf = SGDClassifier(loss="hinge", penalty="l2", n_iter=200)
    clf.fit(trainX, trainY)
    joblib.dump(clf, 'models/sgd.model')
    predictY = clf.predict(testX)
    acc = get_acc(predictY, testY)
    print acc
    return 0


def main():
    build_model()
    return 0


if __name__ == '__main__':
    main()