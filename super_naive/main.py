import inspect
import pkgutil
import sys
from methods.base import BaseClass


def load_modules():
    methods = {}
    for i, pkg_name, _ in pkgutil.iter_modules(['methods/']):
        full_name = '{}.{}'.format('methods', pkg_name)
        if full_name not in sys.modules:
            module = i.find_module(pkg_name).load_module(full_name)
            for cl_name, cl in inspect.getmembers(module, inspect.isclass):
                # Only checking the name because I am far too lazy to actually
                # package this properly.
                if issubclass(cl, BaseClass) and cl_name != 'BaseClass':
                    methods[cl_name] = cl()
    return methods

def load_and_manually_class_find():
    methods = load_modules()
    for method, obj in methods.items():
        print'{}: {}'.format(obj.name, obj.help_string)

load_and_manually_class_find()
