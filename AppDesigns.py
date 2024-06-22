import random
import sys
import time

from rich.console import Console
from rich.markdown import Markdown

MARKDOWN = """
# PRIYANKA'S POS

"""

console = Console()


def progress_bar(count_value, total, suffix=''):
    bar_length = 100
    filled_up_length = int(round(bar_length * count_value / float(total)))
    percentage = round(100.0 * count_value / float(total), 1)
    bar = '=' * filled_up_length + '-' * (bar_length - filled_up_length)
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percentage, '%', suffix))
    sys.stdout.flush()


def inject_progress_bar():
    print("")
    for i in range(11):
        time.sleep(random.random())
        progress_bar(i, 10)

    print("")
    print("")


def print_heading():
    md = Markdown(MARKDOWN)
    console.print(md)
    print("")


def print_welcome_message(name):
    console.print("Welcome " + name + "!", style="bold green")
    print("")


def print_special(message):
    console.print(message, style="bold cyan")
