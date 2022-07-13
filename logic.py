from random import randint, choice

from constants import DifficultyOption, Operation


def generate_expression(difficulty: DifficultyOption) -> tuple[str, int]:
    if difficulty == DifficultyOption.EASY:
        operation = choice([Operation.ADD, Operation.SUB])
    else:
        operation = choice(list(Operation))

    first_number = randint(2, 1000)

    if operation == Operation.DIV:
        second_number = choice(_get_divisors(first_number))
    elif operation == Operation.MUL and difficulty == DifficultyOption.MEDIUM:
        second_number = randint(2, 9)
    elif operation == Operation.MUL and difficulty == DifficultyOption.HARD:
        second_number = randint(2, 50)
    elif difficulty == DifficultyOption.EASY:
        second_number = randint(2, 100)
    else:
        second_number = randint(2, 1000)

    expression = f'{first_number} {operation} {second_number}'
    answer = operation.function(first_number, second_number)

    return expression, answer


def _get_divisors(divided: int) -> list[int]:
    divisors = []
    divisor = 2

    while divided > 1:
        if divided % divisor == 0:
            divisors.append(divisor)
            divided = divided / divisor
        else:
            divisor = divisor + 1

    return divisors
