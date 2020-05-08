import pandas as pd
import string

def convert_dollars(dollar):
    return int(dollar.replace("$", "").replace(",", ""))


def to_date(df,col):
    df[col] = pd.to_datetime(df[col])
    return df

def remove_punctuations(text):
    for punctuation in string.punctuation:
            text = text.lower().replace(punctuation, "")
    return text

