import evaluator
import model
import matplotlib.pyplot as plt
import numpy as np

def printResult(model_used: model.Model, cur_number, name_data, train, test):
    for i in range(0, len(train)):
        y_pred = []
        for k in range(0, len(train[i])):
            y_pred.append(model_used.pred(train[i][k], test[i][k]))
        
        MSE, Directional, cumulative_return, sharpe = evaluator.evaluate(
            y_pred, test[i])
        
        print(
            f"MSE for Model {cur_number} in data {name_data[i]}: "
            f"{MSE}"
            )
        
        print(
            f"Directional for Model {cur_number} in data {name_data[i]}: "
            f"{Directional}"
            )

        print(
            f"Sharpe for Model {cur_number} in data {name_data[i]}: "
            f"{sharpe}"
            )

        print(np.shape(cumulative_return))
        plt.plot(cumulative_return)
        plt.show()