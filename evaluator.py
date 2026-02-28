import numpy as np
from sklearn.metrics import mean_squared_error

def evaluate(y_pred, y):
    # Will take MAE, MSE, and Directional
    
    y_pred = np.array(y_pred)
    y = np.array(y)
    
    MSE = mean_squared_error(y, y_pred)
    Directional = np.mean(((y_pred >= 0) == (y >= 0)).astype(int))
    
    positions = 2 * (y_pred >= 0).astype(int) - 1
    positions = positions.reshape(-1)
    
    actual_return = np.exp(y) - 1
    actual_return = actual_return.reshape(-1)

    strategy_return = positions * actual_return
    
    cumulative_return = np.cumprod(1 + strategy_return)
    
    mean_ret = np.mean(strategy_return)
    std_ret = np.std(strategy_return)
    
    sharpe = mean_ret / std_ret * np.sqrt(252)
    
    sr = np.asarray(strategy_return, dtype=float).reshape(-1)

    print("strategy_return shape:", sr.shape)
    print("min/max:", np.min(sr), np.max(sr))
    print("mean/std:", np.mean(sr), np.std(sr, ddof=1))
    print("any <= -1?:", np.any(sr <= -1))
    print("min(1+sr):", np.min(1 + sr))
    print("final wealth:", np.prod(1 + sr))
        
    return MSE, Directional, cumulative_return, sharpe

# test
# print(evaluate(np.array([1]), np.array([3])))