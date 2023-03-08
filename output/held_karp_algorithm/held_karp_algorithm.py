from timeit import default_timer as timer
import collections
import numpy as np
import itertools
import sys
import os
import memory_profiler

input_file = ''
output_file = ''
number_of_reapeats = 10 #defeult
matrix = []
n = 6 #default

def main():

    set_globals()

    with open('outputdata.csv', 'a') as file:
        for i in range(number_of_reapeats):
            start = timer()
            x = tsp_distance()
            end = timer()
            y = round(end - start, 8)
            file.write(f'{n}; {y}; {x[0]}; [ ')
            for i in x[1]:
                file.write(f'{i} ')
            file.write(']\n')
    file.close()

def set_globals():
    global input_file
    global number_of_reapeats
    global n
    global matrix
    
    with open('config.ini') as file:
        line = file.readline()
        list = line.split()
        input_file = list[0]
        number_of_reapeats = int(list[1])
    file.close()

    with open(input_file) as file:
        file_extension = os.path.splitext(input_file)[1]
        lines = file.readlines()
        n = int(lines[0])
        matrix = np.zeros((n, n))

        if file_extension == '.txt':
            for i, line in enumerate(lines[1:]):
                for j, value in enumerate(line.split()):
                    matrix[i][j] = int(value)
        elif file_extension == '.atsp':
            counter = 0
            list = collections.deque([])
            for line in lines[1:]:
                for value in line.split():
                    list.append(int(value))
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = list.popleft()
        elif file_extension == '.tsp':
            list = collections.deque([])
            for line in lines[1:]:
                for value in line.split():
                    list.append(int(value))
            counter = 1
            for i in range(n):
                for j in range(counter):
                    matrix[i][j] = list.popleft()
                    matrix[j][i] = matrix[i][j]
                counter = counter + 1
    file.close()

def tsp_distance():
    cost_dictionary = {}
    for next_vertex in range(1, n):
        cost_dictionary[(1 << next_vertex, next_vertex)] = (matrix[0][next_vertex], 0)
    
    cost_list = []
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            subset_binary = 0
            for element in subset: 
                subset_binary = subset_binary + (1 << element)
            for next_vertex in subset:
                for vertex in subset:
                    if vertex != next_vertex:
                        cost_list.append((cost_dictionary[subset_binary & ~ (1 << next_vertex), vertex][0] 
                        + matrix[vertex][next_vertex], vertex))

                min_tuple = (sys.maxsize, 0)
                for tuple in cost_list:
                    if tuple[0] < min_tuple[0]:
                        min_tuple = tuple

                cost_dictionary[subset_binary, next_vertex] = min_tuple
                cost_list.clear()

    min_cost = (sys.maxsize, )

    for last_stop in range(1, n):
        distance = cost_dictionary[(1 << n) - 2, last_stop][0] + matrix[last_stop][0]
        if distance < min_cost[0]:
            min_cost = (distance, last_stop)

    min_path = collections.deque([0])

    set_binary = (1 << n) - 2
    vertex = min_cost[1]
    min_path.appendleft(vertex)
    prev_vertex = cost_dictionary[set_binary, vertex][1]
    set_binary = (1 << vertex) ^ set_binary

    for i in range(n - 3):
        vertex = prev_vertex
        min_path.appendleft(vertex)
        prev_vertex = cost_dictionary[set_binary, vertex][1]
        set_binary = (1 << vertex) ^ set_binary

    min_path.appendleft(prev_vertex)
    min_path.appendleft(0)
    
    return (min_cost[0], min_path)

if __name__ == "__main__":
    main()

    