# for model class
# abstract class

from abc import ABC, abstractmethod
from typing_extensions import override
import numpy as np
from sklearn.linear_model import LinearRegression

class Model:
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def pred(self, train, test) -> int:
        pass

# Just previous result = now
class Model1(Model):
    def pred(self, train, test):
        return train[-1]

# linear regression
class Model2(Model):
    def __init__(self) -> None:
        super().__init__()
        self.cur = LinearRegression()
    
    def pred(self, X_train, X_test):
        
        self.cur.fit(X_train[:-1].reshape(-1, 1), X_train[1:])
        return self.cur.predict(X_test.reshape(-1, 1))
