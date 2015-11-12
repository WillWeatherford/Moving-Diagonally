
# repl
# each loop has a menu list, mapping a regex to a function called if the regex matches
# that function runs until it is resolved, returning True
# pass

from repl import repl
import re

QUIT_RE = re.compile(r'^[qQ]uit?$')


def main():
    if repl():
        return

if __name__ == '__main__':
    main()
