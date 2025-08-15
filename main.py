import numpy as np
import joblib
from keras.models import Sequential
from keras.layers import Dense

# Load the pre-trained model and scaler
model = Sequential([
    Dense(64, input_dim=50, activation='relu'),
    Dense(64, activation='relu'),
    Dense(1)
])
model.load_weights('S-ANN-340K_model.weights.h5')

scaler = joblib.load('scaler_S.pkl')   # raises FileNotFoundError if missing


def predict_S(raw_features):
    x = np.asarray(raw_features, dtype=float).reshape(1, -1)
    if x.shape[1] != 50:
        raise ValueError(f'Expected 50 features, got {x.shape[1]}')

    x_scaled = scaler.transform(x)          
    log_S    = model.predict(x_scaled, verbose=0).squeeze()  
    S_pred   = float(np.exp(log_S))         
    return S_pred

if __name__ == '__main__':

    # EXAMPLE: read a comma-separated line of 50 numbers from 'input_IL.txt'. 
    # Note: the current numbers in 'input_IL.txt' correspond to the sigma profiles of [EMIM][PF6] ionic liquid. Replace with your own values.
    with open('input_IL.txt') as f:
        vals = list(map(float, f.readline().split('\t')))
    print('Predicted S_R32:', predict_S(vals))
