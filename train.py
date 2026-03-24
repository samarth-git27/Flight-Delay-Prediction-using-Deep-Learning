import pandas as pd
from preprocessing import preprocess
from model import build_model
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/sample_data.csv')

X, y = preprocess(df)

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = build_model(X_train.shape[1])

model.fit(X_train, y_train, epochs=10)

model.save('models/model.h5')
