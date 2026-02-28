import getData
import evaluator
import model
import printResult

data_US_train, data_US_test, data_global_train, data_global_test = getData.getData()
name_data = ["US", "Global"]
printResult.printResult(model.Model1(), 1, name_data, ([data_US_train, data_global_train]),
            ([data_global_train, data_global_test]))


