def find_by_appearances(x, *lists):
    counter = {}

    for lst in lists:
        for item in lst:
            if item in counter:
                counter[item] += 1
            else:
                counter[item] = 1

    result = [item for item, count in counter.items() if count == x]

    return result


def main():
    list1 = [1, 2, 3]
    list2 = [2, 3, 4]
    list3 = [3, 4, 5]
    list4 = [4, 1, "test"]
    x = 2

    print(find_by_appearances(x, list1, list2, list3, list4))


main()
