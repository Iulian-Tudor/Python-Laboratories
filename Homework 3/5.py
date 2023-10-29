def validate_dict(rules, dict_to_validate):
    for rule in rules:
        key, prefix, middle, suffix = rule
        if key not in dict_to_validate:
            return False
        value = dict_to_validate[key]
        if not (value.startswith(prefix) and middle in value and value.endswith(suffix)):
            return False
    return True


def main():
    rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    dict_to_validate = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
    result = validate_dict(rules, dict_to_validate)
    print(result)

if __name__ == "__main__":
    main()