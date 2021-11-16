import sys
from src import ClassA
from src import shared_classb_instance

def main() -> int:
    """Simple main function

    Returns:
        int: system exit code
    """
    print("Hello World")

    classa_instance = ClassA()
    classa_instance.print_name()

    shared_classb_instance.log_caller(main.__name__)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())