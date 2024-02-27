import sys

from src.ui.TaskManagerConsoleUI import TaskManagerConsoleUI


def main():
    path = "tasks.json"
    if len(sys.argv) > 1:
        path = TaskManagerConsoleUI(sys.argv[1])

    ui = TaskManagerConsoleUI(path)
    ui.main()


if __name__ == '__main__':
    main()
