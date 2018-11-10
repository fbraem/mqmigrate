import abc

class Migrator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def defineQL(self, name):
        pass
