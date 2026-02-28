import evaluator
import model

def printResult(model_used: model.Model, cur_number, name_data, train, test):
    for i in range(0, len(train)):
        MAE, MSE, Directional = evaluator.evaluate(model_used.pred(train[i], test[i]), test[i])
        
        print(
            f"MAE for Model {cur_number} in data {name_data[i]}: "
            f"{MAE}"
            )
        
        print(
            f"MSE for Model {cur_number} in data {name_data[i]}: "
            f"{MSE}"
            )
        
        print(
            f"Directional for Model {cur_number} in data {name_data[i]}: "
            f"{Directional}"
            )