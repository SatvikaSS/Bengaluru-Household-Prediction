import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv('bengaluru_house_data.csv')
df = df.drop(['area_type', 'society', 'balcony', 'availability'], axis=1)
df.dropna(inplace=True)
df['bhk'] = df['size'].apply(lambda x: int(x.split(' ')[0]))

def convert_sqft(x):
    try:
        return float(x)
    except:
        if '-' in x:
            tokens = x.split('-')
            return (float(tokens[0]) + float(tokens[1])) / 2
        return None

df['total_sqft'] = df['total_sqft'].apply(convert_sqft)
df.dropna(inplace=True)
df = df[df['total_sqft'] / df['bhk'] >= 300]
df = df[df['bath'] < df['bhk'] + 2]

df['location'] = df['location'].apply(lambda x: x.strip())
location_counts = df['location'].value_counts()
df['location'] = df['location'].apply(lambda x: 'other' if location_counts[x] <= 10 else x)

dummies = pd.get_dummies(df['location'])
df = pd.concat([df, dummies.drop('other', axis=1)], axis=1)
df.drop(['location', 'size'], axis=1, inplace=True)

X = df.drop('price', axis=1)
y = df['price']

model = LinearRegression()
model.fit(X, y)

# Save model and columns
pickle.dump(model, open('bangalore_model.pkl', 'wb'))
pickle.dump(X.columns, open('model_columns.pkl', 'wb'))
