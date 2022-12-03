import json
import pandas as pd 
from pandas import DataFrame, Series

def simple_baseline():
    data = pd.read_csv('530finalprojectdata/clean_test_data.csv')

    f = open("530finalprojectdata/gendered_words.json")
    gender_dict = json.load(f)
    gender_dict = pd.DataFrame(gender_dict).set_index('word').to_dict()['gender']

    data['words'] = data.Lyrics.apply(lambda x: len([y for y in x.split() if y in gender_dict]))
    data['male'] = data.Lyrics.apply(lambda x: len([y for y in x.split() if y in gender_dict and gender_dict[y] == 'm']))
    data['female'] = data.Lyrics.apply(lambda x: len([y for y in x.split() if y in gender_dict and gender_dict[y] == 'f']))

    data['male_pct'] = data.apply(lambda x: x['male'] / x['words'] if x['words'] > 0 else 0,axis=1)
    data['female_pct'] = data.apply(lambda x: x['female'] / x['words'] if x['words'] > 0 else 0,axis=1)
    data['sexist'] = data.apply(lambda x: (abs(x['male_pct'] - x['female_pct']) > 0.1) + 0, axis=1)
    return list(data['sexist'])

def main():
    y_preds = simple_baseline()
    print(y_preds)
    return y_preds

if __name__ == "__main__":
    main()