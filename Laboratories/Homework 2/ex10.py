def split_lists(*lists):
    max_len = max([len(lst) for lst in lists])
    final = []

    for i in range(max_len):
        tupla = ()
        for lst in lists:
            if i < len(lst):
                tupla += (lst[i],)
            else:
                tupla += (None,)
        final.append(tupla)

    return final


def main():
    list1 = [1, 2, 3]
    list2 = [5, 6, 7]
    list3 = ["a", "b", "c", "d"]

    print(split_lists(list1, list2, list3))


main()
