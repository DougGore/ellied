import importlib
import pkgutil
import inspect
from itertools import cycle

class PixletManager:
    """ Load and manage pixlet effects
    """
    def __init__(self, path="pixlets"):
        """ Initial pixel

        Args:
            path (str, optional): [description]. Defaults to "pixlets".
        """
        self.pixlet_list = {}
        py_path = path.replace("/", ".")

        for (a, module, c) in pkgutil.iter_modules([path]):
            if c is False:
                pixlet_class = self.import_pixlet("{}.{}".format(py_path, module))
                self.pixlet_list[module] = pixlet_class

        self.pixlet_iter = cycle(self.pixlet_list.values())

    def import_pixlet(self, reference):
        pixlet_module = importlib.import_module(reference)

        pixlet_classlist = inspect.getmembers(pixlet_module, inspect.isclass)

        # Get first class
        return pixlet_classlist[0][1]

    def next_pixlet(self):
        return next(self.pixlet_iter)

    def get_pixlet(self, name):
        if name in self.pixlet_list:
            return self.pixlet_list[name]
        
        return None
