X = df.drop(['is_delay', 'ArrDelay'], axis=1)
y = df['is_delay']

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
