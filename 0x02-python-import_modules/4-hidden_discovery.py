#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    show = dir(hidden_4)
    l = len(show)
    for item in range(l):
        if show[item][:2] == '__':
            continue
        else:
            print(show[item])
