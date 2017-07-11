import abc
import sys
import pkgutil


class BaseClass(object):

    __metaclass__ = abc.ABCMeta

    class __metaclass__(type):
        def __init__(cls, name, base, attrs):
            if not hasattr(cls, 'registry'):
                cls.registry = {}
            else:
                cls.registry[name] = cls()

    @classmethod
    def load(cls, path):
        cls.registry = {}
        for i, pkg_name, _ in pkgutil.iter_modules([path]):
            full_name = '{}.{}'.format(path, pkg_name)
            if full_name not in sys.modules:
                try:
                    i.find_module(pkg_name).load_module(full_name)
                except Exception as e:
                    print 'Could not load module : {}'.format(full_name)
                    print str(e)

    @classmethod
    def get_full_help(cls):
        for k, v in cls.registry.items():
            print '{}: {}'.format(v.name, v.help_string)

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
