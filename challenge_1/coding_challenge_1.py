def get_value(nested_dict, key_path):
    print(f"Path: '{key_path}'")
    current = nested_dict
    for key in key_path.split('/'):
        print(f"Key: '{key}' in {current}")
        if not isinstance(current, dict) or key not in current:
            raise KeyError(f"Invalid path at '{key}'")
        current = current[key]
        print(f"Current value after '{key}': {current}")
    print(f"Final value for '{key_path}': {current}\n")
    return current


def main():
    test_cases = [ 
        # 1 & # 2: simple case string
        ({"a": {"b": {"c": "d"}}}, "a/b/c", "d"),
        ({"x": {"y": {"z": "a"}}}, "x/y/z", "a"),
        # 3. check integer number
        ({"number": {"first": {"second": 3}}}, "number/first/second", 3),
        # 4. list
        ({"letters": {"vowels": ["a", "e", "i"]}}, "letters/vowels", ["a", "e", "i"]),
        # 5. boolean check
        ({"config": {"feature": {"enabled": True}}}, "config/feature/enabled", True),
        # 6. empty dictionary check
        ({"outer": {"inner": {}}}, "outer/inner", {}),
        # 7. single key check
        ({"root": "value"}, "root", "value"),
        # 8. deep nesting
        ({"lvl1": {"lvl2": {"lvl3": {"lvl4": "deep_lvl"}}}}, "lvl1/lvl2/lvl3/lvl4", "deep_lvl"),
    ]

    print("===== Running tests step by step: =====\n")
    for i, (obj, path, expected) in enumerate(test_cases, 1):
        print(f"--- Test {i} ---")
        try:
            result = get_value(obj, path)
            assert result == expected
            print(f"Test {i} passed.\n")
        except Exception as e:
            print(f"Test {i} failed: {e}\n")


if __name__ == "__main__":
    main()
