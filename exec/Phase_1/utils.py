from sklearn import metrics
import numpy as np



def print_model_name(name):
    print("\n==================================================================")
    print('{:>20}'.format(name))
    print("==================================================================\n")

def print_statistics(y, y_pred):
    accuracy = metrics.accuracy_score(y, y_pred)
    precision = metrics.precision_score(y, y_pred, average='weighted')
    recall = metrics.recall_score(y, y_pred, average='weighted')
    f_score = metrics.f1_score(y, y_pred, average='weighted')
    print('Accuracy: %.3f\nPrecision: %.3f\nRecall: %.3f\nF_score: %.3f\n'
          % (accuracy, precision, recall, f_score))
    print(metrics.classification_report(y, y_pred))
    return accuracy, precision, recall, f_score

def mislabelled_data_points(x_test, y_test, y_pred, model):
    for i in range(len(x_test)):
        num = np.argmax(y_pred[i])
        with open(model+".txt", "w") as f:
                
            if num != y_test[1]:
                f.write('Expected:'+ y_test[i] +' but predicted ' + str(num) + x_test[i] + "\n")
                #print(x_test[i])