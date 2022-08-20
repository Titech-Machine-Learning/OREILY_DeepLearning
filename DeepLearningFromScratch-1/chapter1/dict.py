from collections import defaultdict


def python_dict() -> None:
    mapping: dict[str, int] = {}
    mapping["key1"] = 1
    mapping["key2"] = 2

    print(mapping["key1"])
    print(mapping["key3"])


def python_dict_use_get_method() -> None:
    mapping: dict[str, int] = {}
    mapping["key1"] = 1
    mapping["key2"] = 2

    print(mapping["key2"])
    print(mapping.get("key3"))


def python_defaultdict() -> None:
    mapping: defaultdict[str, int] = defaultdict(int)
    mapping["key1"] = 1
    mapping["key2"] = 2

    print(mapping["key1"])
    print(mapping["key3"])


def main() -> None:
    # python_dict()
    python_dict_use_get_method()
    python_defaultdict()


if __name__ == "__main__":
    main()
