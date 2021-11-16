class ClassB:
    def __init__(self) -> None:
        """Simple constructor of class B"""
        pass

    def log_caller(self, caller_name: str) -> None:
        """Function that prints caller name

        Args:
            caller_name (str): name of the calling function/class
        """
        print(self.__class__.__name__, "used by", caller_name)

shared_classb_instance = ClassB()