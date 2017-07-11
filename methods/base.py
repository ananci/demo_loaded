import abc


class BaseClass(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def entry(self, input):
        """Required common entry point for all implemented methods."""
        return

    @property
    def help_string(self):
        return self.__doc__

    @property
    def name(self):
        return self.__class__.__name__
