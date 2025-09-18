def get_value(nested_dict, key_path):
    current = nested_dict
    for key in key_path.split('/'):
        if not isinstance(current, dict) or key not in current:
            raise KeyError(f"Invalid path at '{key}'")
        current = current[key]
    return current


def main():
    test_cases = [ 
        # 1 & # 2: simple case string
        ({"a": {"b": {"c": "d"}}}, "a/b/c", "d"),
        ({"x": {"y": {"z": "a"}}}, "x/y/z", "a")
    ]

    print("=====Running tests: =====\n")
    for i, (obj, path, expected) in enumerate(test_cases, 1):
        try:
            result = get_value(obj, path)
            assert result == expected
            print(f"Test {i} passed.")
        except Exception as e:
            print(f"Test {i} failed: {e}")


if __name__ == "__main__":
    main()
