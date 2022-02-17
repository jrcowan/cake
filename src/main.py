from src.frontend.console.menu import start_console
from src.backend.sqlite.setup import create_table

if __name__ == '__main__':
    start_console(create_table())
