import re

dataTypes = r'void|int|double|float|char|string|long'

def parse_cpp_file():
    scheme = {'blocks': [], 'arrows': [], 'x0': 0, 'y0': 100}
    with open('solve.cpp', 'r') as f:
        commands = list(map(lambda x: x.rstrip().strip(r'[{} ]'), f.readlines()))
        commands = list(map(lambda x: x.lstrip(' ').replace('endl', '').replace('<<', '').replace('>>', '').replace('rand()', 'рандом'), commands))
        for i in range(len(commands)):
            if '#' in commands[i] or 'using' in commands[i]:
                continue
            if re.match(dataTypes, commands[i]) and '(' in commands[i] and ');' in commands[i] and not '=' in commands[i]:
                continue
            if re.match(dataTypes, commands[i]) and '(' in commands[i] and ')' in commands[i] \
                and not ';' in commands[i] and not '=' in commands[i]:
                print(commands[i])



def main():
    parse_cpp_file()


if __name__ == "__main__":
    main()