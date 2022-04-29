import random

from matplotlib import pyplot as plt


def generate_table():
    matrix = [[1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 1, 1, 1, 1, 1]]

    for lala in range(random.randint(2, 6)):
        x = random.randint(1, 4)
        y = random.randint(1, 4)
        matrix[x][y] = 2

    return matrix


def plot(matrix):
    matrix = update_vacuum_cleaner(matrix, 1, 4)
    scroll_panel(matrix)


def scroll_panel(matrix):
    colum = search_index(matrix, -1)[0]._getitem_(0)
    line = search_index(matrix, -1)[0]._getitem_(1)

    validate_attributes(matrix, colum, line)


def validate_attributes(matrix, colum, line):
    index_dust = search_index(matrix, 2)

    for dust in index_dust:

        colum_dust = dust[0]
        line_dust = dust[1]

        while validate_if_attribute_is_in_place_to_aspire(colum, line, colum_dust, line_dust):

            if colum_dust > colum:
                matrix = clean_index(matrix, colum, line)
                colum += 1
                update_vacuum_cleaner(matrix, colum, line)

            if line_dust > line:
                matrix = clean_index(matrix, colum, line)
                line += 1
                update_vacuum_cleaner(matrix, colum, line)

            if colum_dust < colum:
                matrix = clean_index(matrix, colum, line)
                colum -= 1
                update_vacuum_cleaner(matrix, colum, line)

            if line_dust < line:
                matrix = clean_index(matrix, colum, line)
                line -= 1
                update_vacuum_cleaner(matrix, colum, line)


def validate_if_attribute_is_in_place_to_aspire(colum, line, colum_dust, line_dust):
    if colum_dust > colum or line_dust > line:
        return True

    if colum_dust < colum or line_dust < line:
        return True

    return False


def clean_index(matrix, colum, line):
    matrix[colum][line] = 0
    return matrix


def search_index(matrix, val):
    values = []
    for i, j in enumerate(matrix):
        for k, li in enumerate(j):
            if li == val:
                values = values + [(i, k)]
    return values


def update_vacuum_cleaner(matrix, colum, line):
    matrix = set_index_vacuum_cleaner(matrix, -1, colum, line)
    print(matrix)
    plt.imshow(matrix, 'Blues')
    plt.show(block=False)
    plt.pause(0.5)
    plt.clf()
    return matrix


def set_index_vacuum_cleaner(matrix, value, colum, line):
    matrix[colum][line] = value
    return matrix


def main():
    plt.show()
    matrix = generate_table()
    plot(matrix)


main()