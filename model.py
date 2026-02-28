# for model class
# abstract class

from abc import ABC, abstractmethod
from typing_extensions import override
import numpy as np

class Model:
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def pred(self, train, test) -> int:
        pass
    
class Model1(Model):
    def pred(self, train, test):
        y_pred = np.append(train[-1], test[:-1])
        return y_pred