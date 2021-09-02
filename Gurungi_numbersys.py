class NumberObject:
    def __init__(self, int_part: str or list = "", float_part: str or list = "", sign: str = "+") -> None:
        self.int_part = list(int_part)
        self.has_float_part = not not float_part
        self.float_part = list(float_part)
        self.sign = sign

    def __str__(self):
        return "{}.{}".format("".join(self.int_part), "".join(self.float_part)) if self.has_float_part \
            else "".join(self.int_part)

    @staticmethod
    def multiply(one, another):
        pass

    @staticmethod
    def divide(one, another):
        pass

def compare(_one: NumberObject, _another: NumberObject) -> int:
    one = NumberObject(_one.int_part, _one.float_part, _one.sign)
    another = NumberObject(_another.int_part, _another.float_part, _another.sign)

    if one.sign == "+" and another.sign == "-":
        return minus(one, another)
    elif one.sign == "-" and another.sign == "+":
        return minus(another, one)
    elif one.sign == "-" and another.sign == "-":
        sign = "-"
    else:
        sign = "+"

    # 자릿수를 비교 (누가 더 큰가?)
    max_cipher = max(len(one.int_part), len(another.int_part)) - 1
    int_result = ["0" for _ in range(max_cipher + 1)]


def plus(_one: NumberObject, _another: NumberObject) -> NumberObject:
    one = NumberObject(_one.int_part, _one.float_part, _one.sign)
    another = NumberObject(_another.int_part, _another.float_part, _another.sign)

    if one.sign == "+" and another.sign == "-":
        return minus(one, another)
    elif one.sign == "-" and another.sign == "+":
        return minus(another, one)
    elif one.sign == "-" and another.sign == "-":
        sign = "-"
    else:
        sign = "+"

    # 자릿수를 비교 (누가 더 큰가?)
    max_cipher = max(len(one.int_part), len(another.int_part)) - 1
    int_result = ["0" for _ in range(max_cipher + 1)]

    while not len(one.int_part) == len(another.int_part):
        if len(one.int_part) > len(another.int_part):
            another.int_part.insert(0, "0")
        else:
            one.int_part.insert(0, "0")

    for i in range(max_cipher, -1, -1):
        try:
            left = int(one.int_part[i])
        except IndexError:
            left = 0

        try:
            right = int(another.int_part[i])
        except IndexError:
            right = 0

        if int(int_result[i]) + left + right < 10:
            int_result[i] = str(int(int_result[i]) + left + right)
        else:
            if i == 0:
                int_result.insert(0, "0")
                i += 1

            int_result[i - 1] = str(int(int_result[i - 1]) + 1)
            int_result[i] = str(int(int_result[i]) + left + right - 10)

    return NumberObject(int_result, sign=sign)


def minus(_one: NumberObject, _another: NumberObject) -> str:

    one = NumberObject(_one.int_part, _one.float_part, _one.sign)
    another = NumberObject(_another.int_part, _another.float_part, _another.sign)

    # 자릿수를 비교 (누가 더 큰가?)
    max_cipher = max(len(one.int_part), len(another.int_part)) - 1
    int_result = ["0" for _ in range(max_cipher + 1)]

    while not len(one.int_part) == len(another.int_part):
        if len(one.int_part) > len(another.int_part):
            another.int_part.insert(0, "0")
        else:
            one.int_part.insert(0, "0")

    for i in range(max_cipher, -1, -1):
        try:
            left = int(one.int_part[i])
        except IndexError:
            left = 0

        try:
            right = int(another.int_part[i])
        except IndexError:
            right = 0

        if int(int_result[i]) + left + right < 10:
            int_result[i] = str(int(int_result[i]) + left + right)
        else:
            if i == 0:
                int_result.insert(0, "0")
                i += 1

            int_result[i - 1] = str(int(int_result[i - 1]) + 1)
            int_result[i] = str(int(int_result[i]) + left + right - 10)
    return "".join(int_result)


if __name__ == '__main__':
    import random
    import tqdm

    times = 10000000
    verbose = False
    succeed = 0
    fail = 0

    for i in tqdm.trange(times):
        a = random.randint(-1000, 1000000)
        b = random.randint(-1000, 10000)

        one = NumberObject(str(a)) if a > 0 else NumberObject(str(a)[1:], sign="-")
        another = NumberObject(str(b)) if b > 0 else NumberObject(str(b)[1:], sign="-")

        if verbose:
            print("Testing {}+{}...".format(a, b), end="\t")
        if int(plus(one, another)) == a + b:
            if verbose:
                print(True)
            succeed += 1
        else:
            if verbose:
                print(False)
            fail += 1

    print("\nRunning algorithm with {} testcases.".format(times))
    print("Succeed = {}\tFail = {}".format(succeed, fail))
    print("Test succeed" if not fail else "Test failed.")
