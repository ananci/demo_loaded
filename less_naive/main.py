import base
import methods

base.BaseClass.load(methods.__path__)
print(base.BaseClass.registry)
print(base.BaseClass.get_full_help())
