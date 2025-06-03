import sys
import logging
import config
config.setup_logging()
from runs import run_read, run_descriptive, run_display, run_print

def main():
    """
    Entry point for the command-line interface.
    Accepts one argument to determine which operation to execute.
    """
    if len(sys.argv) < 2:
        logging.error("No command provided. Please use one of: run_read, run_descriptive, run_display, run_print")
        return

    command = sys.argv[1].lower()

    if command == "run_read":
        run_read()
    elif command == "run_descriptive":
        run_descriptive()
    elif command == "run_display":
        run_display()
    elif command == "run_print":
        run_print()
    else:
        logging.error(f"Unknown command: '{command}'. Available commands are: run_read, run_descriptive, run_display, run_print")

if __name__ == "__main__":
    main()