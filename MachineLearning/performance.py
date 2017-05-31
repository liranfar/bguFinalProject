from sklearn import metrics


def print_accuracy(y_train , nb_predict_train,):
    print("Accuracy: {0:.4f}".format(metrics.accuracy_score(y_train, nb_predict_train)))


def print_confusion_matrix(y_test, nb_predict_test):
    print ("Confusion Matrix")
    print("{0}".format(metrics.confusion_matrix(y_test, nb_predict_test, labels=['malware', 'benign'])))
    print("")
    print("Classification Report")
    print(metrics.classification_report(y_test, nb_predict_test, labels=['malware', 'benign']))


