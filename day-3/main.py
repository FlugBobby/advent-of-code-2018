#!/usr/bin/python3

import numpy
from operator import itemgetter


def has_intersection(rect1, rect2):
    if rect1['x2'] < rect2['x1']:
        return(False)
    elif rect2['y2'] < rect1['y1'] and rect2['y1'] < rect1['y1']:
        return(False)
    elif rect1['y2'] < rect2['y1'] and rect1['y1'] < rect2['y1']:
         return(False)
    else:
        return(True)

# def optmimize_rectangles(rect1, rect2):
#     if rect1["x2"] >= rect2['x2']:

def set_intersections(results, rect1, rect2):
    intersectX1 = max(rect1['x1'], rect2['x1'])
    intersectX2 = min(rect1['x2'], rect2['x2'])
    intersectY1 = max(rect1['y1'], rect2['y1'])
    intersectY2 = min(rect1['y2'], rect2['y2'])

    set_intersection = False
    for x in range(intersectX1, intersectX2 + 1):
        for y in range(intersectY1, intersectY2 + 1):
            results[x][y] = results[x][y] + 1
            set_intersection = True

    if set_intersection:
        rect1["has_intersect"] = True
        rect2["has_intersect"] = True


#    if rect1["x2"] >= rect2['x2']:
    #     print("Hum")
    #     print(rect1)
    # #     print(rect2)
    #     if (rect2['y2'] > intersectY2):
    #         rect2['y2'] = intersectY2 + 1



    # if rect1["x2"] >= rect2['x2']:
    #     print("Hum")
    #     print(rect1)
    #     print(rect2)

def find_intersections(inputs, maxX, maxY):
    i = 0
    results = numpy.zeros((maxX + 1, maxY + 1))
    for rect1 in inputs:
        i = i + 1
        for j in range (i, len(inputs)):
            rect2 = inputs[j]
            if (rect1['x2'] < rect2['x1']):
                break
            if has_intersection(rect1, rect2):
                set_intersections(results, rect1, rect2)
    return (results)

def order_inputs(inputs):
    inputs.sort(key=lambda x: x['coord'][1])
    inputs.sort(key=lambda x: x['coord'][0])

def parse_input():
    inputs = []
    with open('inputs/input.txt') as input_file:
        maxX = 0
        maxY = 0
        for line in input_file:
            split = line.split()
            _x =  int(split[2].split(',')[0])
            _y = int(split[2].split(',')[1].split(':')[0])
            _sizeX = int(split[3].split('x')[0])
            _sizeY = int(split[3].split('x')[1])

            _input = {
                'id': split[0],
                'coord': (_x, _y),
                'x1': _x,
                'y1': _y,
                'x2': _x + _sizeX - 1,
                'y2': _y + _sizeY - 1,
                'has_intersect': False
            }
            inputs.append(_input)
            if maxX < _input['x2']:
                maxX = _input['x2']
            if maxY < _input['y2']:
                maxY = _input['y2']

    order_inputs(inputs)
    results = find_intersections(inputs, maxX, maxY)
    print_answer_part1(results)
    print_answer_part2(inputs)

def print_answer_part2(inputs):
    for _input in inputs:
        if _input['has_intersect'] == False:
            print(_input['id'])

def print_answer_part1(results):
    _sum = 0
    answer = 0
    for i in range(0, len(results)):
        for j in results[i]:
            _sum = _sum + j
            if j > 0:
                answer = answer + 1
    print(_sum)
    print(answer)

def main():
    parse_input()

main()
