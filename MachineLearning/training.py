import numpy as np
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegressionCV
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def split_data_frame(df):
    x = df.drop(['class'],axis=1).values
    y = df['class'].values
    split_test_size = 0.20
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=split_test_size,random_state=42)
    _print_pre_training_data(df, x_test, x_train, y_test, y_train)

    return x_train, x_test, y_train, y_test
    #print(len(x_train))
    #print(len(df.index))


def _print_pre_training_data(df, x_test, x_train, y_test, y_train):
    print("{0:0.2f}% in training set".format(float((len(x_train)) / float(len(df.index))) * 100))
    print("{0:0.2f}% in test set".format(float(len(x_test)) / float(len(df.index)) * 100))
    print("Original malware : {0} ({1:0.2f}%)".format(len(df.loc[df['class'] == 'malware']),
                                                      float(len(df.loc[df['class'] == 'malware'])) / float(
                                                          len(df.index)) * 100.0))
    print("Original benign : {0} ({1:0.2f}%)".format(len(df.loc[df['class'] == 'benign']),
                                                     float(len(df.loc[df['class'] == 'benign'])) / float(
                                                         len(df.index)) * 100.0))
    print("")
    print("Training malware : {0} ({1:0.2f}%)".format(len(y_train[y_train[:] == 'malware']),
                                                   float(len(y_train[y_train[:] == 'malware'])) / float(
                                                       len(y_train)) * 100.0))
    print("Training benign : {0} ({1:0.2f}%)".format(len(y_train[y_train[:] == 'benign']),
                                                    float(len(y_train[y_train[:] == 'benign'])) / float(
                                                        len(y_train) * 100.0)))
    print("")
    print("Test malware : {0} ({1:0.2f}%)".format(len(y_test[y_test[:] == 'malware']),
                                               float(len(y_test[y_test[:] == 'malware'])) / float(len(y_test)) * 100.0))
    print("Test benign     : {0} ({1:0.2f}%)".format(len(y_test[y_test[:] == 'benign']),
                                                    float(len(y_test[y_test[:] == 'benign'])) / float(
                                                        len(y_test)) * 100.0))


def build_naive_bayes_model(x_train, y_train):

    nb_model = GaussianNB()
    nb_model.fit(x_train,y_train.ravel())
    return nb_model

def build_random_forest_model(x_train, y_train):

    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(x_train, y_train.ravel())
    return rf_model

def build_random_forest_model(x_train, y_train):

    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(x_train, y_train.ravel())
    print "10-fold Cross validation score is :"
    print np.mean(cross_val_score(rf_model, x_train, y_train, cv=10))
    return rf_model

def build_logistic_Regression(x_train, y_train):

    lr_model = LogisticRegression(C=0.7, random_state=42)
    lr_model.fit(x_train, y_train)
    return lr_model

def build_logistic_RegressionCV(x_train, y_train):

    lr_cv_model = LogisticRegressionCV(n_jobs=-1, random_state=42,Cs=3, cv=10, refit=True, class_weight="balanced")
    lr_cv_model.fit(x_train, y_train)
    return lr_cv_model