import re
import json

dataTypes = r'void|int|double|float|char|string|long'


def parse_cpp_file():
    scheme = {'blocks': [], 'arrows': [], 'x0': 0, 'y0': 100}
    x = 1000
    y = 100

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
                funcName = commands[i][commands[i].find(' ') + 1:]
                scheme['blocks'].append(
                    {
                        'x': x, 
                        'y': y,
                        'text': funcName,
                        'width': 100,
                        'height': 30,
                        'type': 'Начало / конец',
                        'isMenuBlock': False,
                        'fontSize': 14,
                        'textHeight': 14,
                        'isBold': False,
                        'isItalic': False,
                        'textAlign': 'center',
                        'labelsPosition': 1
                    })
                with open('some.json', 'w') as jsfile:
                    json.dump(scheme, jsfile)



def main():
    parse_cpp_file()


if __name__ == '__main__':
    main()