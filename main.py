def to_upper(name):
    return name.upper()


def say_hello(name):
    print(f'Hello, {name}')  # Press ⌘F8 to toggle the breakpoint.



if __name__ == '__main__':
    name = 'Swaleha'
    say_hello(name)
    up = to_upper(name)
    print(up)