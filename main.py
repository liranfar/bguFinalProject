from performance import *
from training import *
from df_handler import *
from mongo_reader import *

def start_process():
    db_mal_cursor = read_mongo(collection='analysis', db='cuckoo')
    mal_list = convert_to_json_list(db_mal_cursor)
    db_benign_cursor = read_mongo(collection='analysis', db='cuckooBenignDB')
    benign_list = convert_to_json_list(db_benign_cursor)
    df = merge_lists_and_normalize(mal_list, benign_list)
    df = fill_missing_values_to_zero(df)
    #df.head()
    #df.to_csv('out_csv.csv', sep=',', encoding='utf-8')
    x_train, x_test, y_train, y_test = split_data_frame(df)

    #nb_model = build_naive_bayes_model(x_train, y_train)
    #predict_and_print_results(nb_model, x_test, x_train, y_test, y_train)

    rf_model = build_random_forest_model(x_train, y_train)
    predict_and_print_results(rf_model, x_test, x_train, y_test, y_train)

    #lr_model = build_logistic_Regression(x_train, y_train)
    #predict_and_print_results(lr_model, x_test, x_train, y_test, y_train)

    #lr_cv_model = build_logistic_RegressionCV(x_train, y_train)
    #predict_and_print_results(lr_cv_model, x_test, x_train, y_test, y_train)


def predict_and_print_results(model, x_test, x_train, y_test, y_train):
    print("---------------------------- Model is: --------------------------")
    print(type(model))
    nb_predict_train = model.predict(x_train)
    print_accuracy(nb_predict_train, y_train)  # Train Accuracy
    nb_predict_test = model.predict(x_test)
    print_accuracy(y_test, nb_predict_test)  # Test Accuracy
    print_confusion_matrix(y_test, nb_predict_test)


if __name__ == "__main__":
    start_process()





