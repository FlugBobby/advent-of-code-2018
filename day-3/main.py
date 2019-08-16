#!/usr/bin/python3.6


def parse_input():
    print("parse input")
    with open('inputs/input_easy.txt') as input_file:
        for line in input_file:
            _inputs = []
            split = line.split()
            print(split[2].split(',')[0])
            print(split[2].split(',')[1].split(':')[0])
            _x: int(split[2].split(',')[0])
            _y: int(split[2].split(',')[1].split(':')[0])
            _sizeX: int(split[3].split('x')[0])
            _sizeY: int(split[3].split('x')[1])

            _input = {
                'x': _x
                'y': _y
                'sizeX': _sizeX
                'sizeY': _sizeY
            }
#            _input.y = split[2].split(',')[1].split(':')[0]
            print(_input)
            
            # print(split[3].split(','))
    return _input

#def init_map

def main():
    _input = parse_input()
    print(_input)

main()
