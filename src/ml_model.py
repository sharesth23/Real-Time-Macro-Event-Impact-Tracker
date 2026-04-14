import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor

class ImpactModel:

    def __init__(self):
        self.model = RandomForestRegressor()

    def train(self):
        X = np.random.rand(100, 3)
        y = np.random.rand(100)
        self.model.fit(X, y)
        joblib.dump(self.model, "models/model.pkl")

    def load(self):
        self.model = joblib.load("models/model.pkl")

    def predict(self, features):
        return float(self.model.predict([features])[0])