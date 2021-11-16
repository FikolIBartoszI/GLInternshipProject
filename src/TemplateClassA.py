from .TemplateClassB import shared_classb_instance

class ClassA():
    def __init__(self) -> None:
        """Simple ClassA contructor"""
        pass

    def print_name(self) -> None:
        """Function that prints class name"""
        print("Hello World from", self.__class__.__name__)
        shared_classb_instance.log_caller(self.__class__.__name__)
