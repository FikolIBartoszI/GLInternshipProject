import sys
from src import ClassA

def main() -> int:
    """Simple main function

    Returns:
        int: system exit code
    """
    print("Hello World")

    classa_instance = ClassA()
    classa_instance.print_name()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())