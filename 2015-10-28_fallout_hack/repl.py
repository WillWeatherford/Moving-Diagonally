import re
QUIT_RE = re.compile(r'^[qQ]uit?$')


# decorator repl
# take a function
# see if it returns...?
# use while loop?


def repl(prompt, options={}):
    result = None
    while not result:
        u_in = raw_input(prompt)
        for match, func in options:
            if isinstance(re, tuple) and u_in in match:
                result = func(u_in)
    return result





def main():
    if repl():
        return




if __name__ == '__main__':
    main()
