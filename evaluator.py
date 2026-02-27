import numpy as np

def evaluate(y_pred, y):
    # Will take MAE, MSE, and Directional
    
    MAE = np.mean(np.abs(y_pred - y))
    MSE = np.mean(np.square(y_pred - y))
    Directional = np.mean(((y_pred >= 0) == (y >= 0)).astype(int))
    
    return MAE, MSE, Directional

# test
print(evaluate(np.array([1]), np.array([3])))