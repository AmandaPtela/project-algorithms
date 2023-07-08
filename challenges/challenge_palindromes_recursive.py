def is_palindrome_recursive(word, low_index, high_index):
    str = list(word)
    list_reverse = str.copy()

    if len(word) == 0:
        return False

    if low_index > high_index:
        return True

    list_reverse.reverse()

    # print(str)
    # print(list_reverse)
    if str[low_index] != list_reverse[low_index]:
        return False

    else:
        return is_palindrome_recursive(str, low_index + 1, high_index - 1)


# is_palindrome_recursive('AGUA', 0, len('AGUA') - 1)

# Função parâmetro
# caso base = parada
# Caso recursivo - chamada da função

    raise NotImplementedError
