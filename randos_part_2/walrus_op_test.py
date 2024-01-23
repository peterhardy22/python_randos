
def func(x: int) -> int:
    return x - 1

results: list = [result for number in range(10) if (result := func(number) > 3)]
print(results)