import time
import random
import matplotlib.pyplot as plt
from sorting_algorithms import selection_sort, insertion_sort, merge_sort, shellsort

def generate_array(num: int, length) -> list:
    '''
    Generate random array, return array.
    Range of numbers in the array: from -10.000 to 10.000.

    parameters:
        legth:
            number of elements in the generated array
        num:
            number of the array type
            1 - random array
            2 - ascending array
            3 - descending array
            4 - array out of {1, 2, 3} with finitely many repetitions
    '''
    arr = []

    if num == 1:
        for _ in range(length):
            arr.append(random.randint(-10000, 10000))

    elif num == 2:
        minimum = -10000
        for _ in range(length):
            arr.append(random.randint(minimum, minimum + 100))
            minimum = arr[-1]

    elif num == 3:
        maximum = 10000
        for _ in range(length):
            arr.append(random.randint(maximum - 100, maximum))
            maximum = arr[-1]

    elif num == 4:
        for _ in range(length):
            arr.append(random.choice([1, 2, 3]))

    return arr


def compare_algorithms() -> list:
    '''
    Run all 4 algoritms with the following inputs:
        - size from 2^7 to 2^15
        - type of array from 1 to 4
    Return list of tuples, where each tuple contains algorithm name,
    type of array, size of array, number of comparisons and work time.
    '''
    result = []

    for num in range(1, 5):
        for size in range(7, 16):
            actual_size = 2 ** size

            for alg_type in (selection_sort, insertion_sort, merge_sort, shellsort):
                arr = generate_array(num, actual_size)
                start = time.time()
                result_of_sort = alg_type(arr)

                work_time = time.time() - start
                comparisons = result_of_sort[1]

                result.append((alg_type.__name__, num, actual_size, comparisons, work_time))

    return result


def list_to_dict(lst: list) -> dict:
    '''
    Convert list of results into dictionary. Return dictionary.
    '''
    dct = {'selection_sort': [], 'insertion_sort': [], 'merge_sort': [],\
           'shellsort': []}

    for elem in lst:
        if elem[0] == 'selection_sort':
            dct['selection_sort'].append(elem[1:])
        elif elem[0] == 'insertion_sort':
            dct['insertion_sort'].append(elem[1:])
        elif elem[0] == 'merge_sort':
            dct['merge_sort'].append(elem[1:])
        elif elem[0] == 'shellsort':
            dct['shellsort'].append(elem[1:])

    return dct


def plot_graphs(data, num, param, title):
    '''
    Plot (size - param) graph for num-th type of array.
    Param defines which dependency to plot:
        - 2: size - number of comparisons
        - 3: size - work time
    '''
    labels = []

    for algorithm in data.keys():
        x_arr, y_arr = [], []

        for elem in dct[algorithm]:
            if elem[0] == num:
                x_arr.append(elem[1]) #actual size
                y_arr.append(elem[param]) #comp (2) or time (3)

        labels.append(algorithm)
        plt.plot(x_arr, y_arr)

    if param == 2:
        plt.ylabel('number of comparisons')
        plt.yscale('log')
    else:
        plt.ylabel('work time')

    plt.title(title)
    plt.xlabel('size of array')
    plt.legend(labels = (labels), loc = 'upper left')
    plt.show()


def visualize(data):
    '''
    Visualize data in graphs.
    '''
    plot_graphs(data, 1, 2, 'Dependency of number of comparisons on the size of the array.\nRandomized array.')
    plot_graphs(data, 2, 2, 'Dependency of number of comparisons on the size of the array.\nAscending order.')
    plot_graphs(data, 3, 2, 'Dependency of number of comparisons on the size of the array.\nDescending order.')
    plot_graphs(data, 4, 2, 'Dependency of number of comparisons on the size of the array.\n{1, 2, 3} set.')

    plot_graphs(data, 1, 3, 'Dependency of work time on the size of the array.\nRandomized array.')
    plot_graphs(data, 2, 3, 'Dependency of work time on the size of the array.\nAscending order.')
    plot_graphs(data, 3, 3, 'Dependency of work time on the size of the array.\nDescending order.')
    plot_graphs(data, 4, 3, 'Dependency of work time on the size of the array.\n{1, 2, 3} set.')


res = compare_algorithms()
dct = list_to_dict(res)
visualize(dct)
