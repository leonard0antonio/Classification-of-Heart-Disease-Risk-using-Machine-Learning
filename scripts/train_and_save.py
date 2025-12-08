import pandas as pandas
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import os

def train_and_save(csv_path="./heart.xls", path="app_backend/model/heart.pkl"):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    df = pandas.read_csv(csv_path)

    X = df.drop('nome_da_coluna_alvo', axis=1) 
    y = df['nome_da_coluna_alvo']


    # Modelo utilizado: Random Forest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    # Salva no formato pickle
    with open(path, "wb") as f:
        pickle.dump(model, f)
    print(f"Modelo treinado e salvo em: {path}")

if name == "main":
    train_and_save()