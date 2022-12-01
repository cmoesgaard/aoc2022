
def get_input():
    with open("input") as f:
        return f.read().strip()

def get_sums():
    input_string = get_input()
    split_input = [inner.split("\n") for inner in input_string.split("\n\n")]
    parsed_input = [list(map(int, inner)) for inner in split_input]

    return list(map(sum, parsed_input))

def day1A():
    sums = get_sums()

    print(max(sums))


def day1B():
    sums = get_sums()
    sorted_sums = sorted(sums, reverse=True)

    print(sum(sorted_sums[0:3]))


day1A()
day1B()
