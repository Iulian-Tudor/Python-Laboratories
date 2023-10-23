def loop(mapping):
    visited = set()
    final = []
    current_key = "start"

    while current_key not in visited:
        visited.add(current_key)
        final.append(mapping[current_key])
        current_key = mapping[current_key]
        

    return final


def main():
    mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
    print(loop(mapping))


main()