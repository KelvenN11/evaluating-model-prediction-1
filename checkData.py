import getData
import matplotlib.pyplot as plt

data_US_train, data_US_test, data_global_train, data_global_test = getData.getData()

diff_train = [i for i in range(0, len(data_US_train))
        if (data_US_train.iloc[i] !=
        data_global_train.iloc[i]).any()]

diff_test = [i for i in range(0, len(data_US_test))
        if (data_US_test.iloc[i] !=
        data_global_test.iloc[i]).any()]

print(f"diff train: {len(diff_train) / len(data_global_train) * 100}%")
print(f"diff test: {len(diff_test) / len(data_global_test) * 100}%")
