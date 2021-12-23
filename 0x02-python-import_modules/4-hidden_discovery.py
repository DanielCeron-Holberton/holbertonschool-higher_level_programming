#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    new_array = dir(hidden_4)

    for element in new_array:
        if element[:2] != "__":
            print(element)
