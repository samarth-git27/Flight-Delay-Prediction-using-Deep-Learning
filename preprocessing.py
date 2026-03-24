import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess(df):
    df = df[['Reporting_Airline', 'Origin', 'Dest', 'Month',
             'DayOfWeek', 'CRSDepTime', 'Distance', 'ArrDelay']]

    df.dropna(inplace=True)

    df['is_delay'] = df['ArrDelay'].apply(lambda x: 1 if x > 15 else 0)

    for col in ['Reporting_Airline', 'Origin', 'Dest']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

    X = df.drop(['is_delay', 'ArrDelay'], axis=1)
    y = df['is_delay']

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    return X, y
