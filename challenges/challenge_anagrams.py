# Dividir lista!!!!!
# Ordenar as strings ORDEM NUMÉRICA
# Comparar strings ORDENADAS

def sorting_list(str_list):

    swap = True
    iterations = 0

    while swap:
        swap = False
        for i in range(len(str_list) - iterations - 1):
            if str_list[i] > str_list[i + 1]:
                str_list[i], str_list[i + 1] = str_list[i + 1], str_list[i]
            swap = True
        iterations += 1
    return ''.join(str_list)


def is_anagram(first_string, second_string):
    lista = list(first_string.lower())
    lista2 = list(second_string.lower())

    sorted_list = sorting_list(lista)
    sorted_list2 = sorting_list(lista2)

    if sorted_list == '' or sorted_list2 == '':
        print("False")
        return (sorted_list, sorted_list2, False)

    for i in range(len(sorted_list)):
        if sorted_list == sorted_list2:
            print(sorted_list, sorted_list2, True)
            return (sorted_list, sorted_list2, True)
        else:
            print(sorted_list, sorted_list2, False)
            return (sorted_list, sorted_list2, False)


lista = 'Roma'
lista2 = 'amor'
is_anagram(lista, lista2)
