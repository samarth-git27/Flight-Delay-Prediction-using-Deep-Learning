df['is_delay'] = df['ArrDelay'].apply(lambda x: 1 if x > 15 else 0)
