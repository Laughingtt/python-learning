from abc import ABCMeta, abstractmethod, ABC


class AbstractProductA(metaclass=ABCMeta):
    """
    Abstract products that may have multiple implementations
    """

    @staticmethod
    @abstractmethod
    def create():
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def params_space():
        raise NotImplementedError()


class LogisticRegression(AbstractProductA):
    @staticmethod
    def create():
        from model.lr.api import train
        return train

    def params_space(self):
        from model.lr.api import search_space
        return search_space()


class Xgboost(AbstractProductA):
    @staticmethod
    def create():
        from model.xgb.api import train
        return train

    def params_space(self):
        from model.xgb.api import search_space
        return search_space()


class RandomForest(AbstractProductA, ABC):
    @staticmethod
    def create():
        from model.rf.api import train
        return train

    def params_space(self):
        from model.rf.api import search_space
        return search_space()


class FCNN(AbstractProductA, ABC):
    @staticmethod
    def create():
        from model.torch.fcnn.api import trainable
        return trainable

    def params_space(self):
        from model.torch.fcnn.api import search_space
        return search_space()


class Resnet18(AbstractProductA, ABC):
    @staticmethod
    def create():
        from model.torch.resnet.api import train_resnet18
        return train_resnet18

    def params_space(self):
        from model.torch.resnet.api import search_space
        return search_space()


class Resnet34(Resnet18):
    @staticmethod
    def create():
        from model.torch.resnet.api import train_resnet34
        return train_resnet34


class ModelStateConf(object):
    def __init__(self):
        self.logisticregression = "LogisticRegression"
        self.xgboost = "Xgboost"
        self.randomforest = "RandomForest"
        self.fcnn = "FCNN"
        self.resnet18 = "Resnet18"
        self.resnet34 = "Resnet34"
