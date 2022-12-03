import sys
import sklearn
import sklearn.metrics as metrics
import pandas as pd

from strong_baseline import run_strong_baseline
from simple_baseline import simple_baseline

def score(y_pred, y_test):
    return metrics.f1_score(y_test, y_pred,average='binary')

def main():
    args = sys.argv
    test_data = pd.read_csv('530finalprojectdata/clean_test_data.csv')
    print(args)
    if (args[1] == 'manual'):
        y_pred = args[1].split(',')
        y_pred = [int(x) for x in y_pred]
        y_test = args[2].split(',')
        y_test = [int(x) for x in y_test]
        print(y_pred)
        s = score(y_pred, y_test)
        print("Score is", s)
    elif (args[1] == 'simple'):
        y_pred = simple_baseline()
        y_test = li
    elif (args[1] == 'strong'):
        y_pred = run_strong_baseline()

if __name__ == "__main__":
    main()