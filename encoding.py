le_airline = LabelEncoder()
le_origin = LabelEncoder()
le_dest = LabelEncoder()

df['Reporting_Airline'] = le_airline.fit_transform(df['Reporting_Airline'])
df['Origin'] = le_origin.fit_transform(df['Origin'])
df['Dest'] = le_dest.fit_transform(df['Dest'])
