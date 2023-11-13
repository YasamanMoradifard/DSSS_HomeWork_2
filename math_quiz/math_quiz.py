import random

""" Modifications:
    1- Arguments name (Done)
    2- functions name (Done)
    3- add comment (Done)
    4- Docstring (Done)
    5- Error handling 
    6- use 'zip'
    7- Modular (Done)
"""
def Random_number(min, max):
    """Return an inteter between min & max randomly

    Args:
        min (int): the minimum number
        max (int): the maximum number

    Returns:
        int: random number between min & max
    """
    if not isinstance(min, int) or not isinstance(max, int):
        raise TypeError("Arguments 'min' and 'max' must be integers.")
    return random.randint(min, max)


def Operation():
    """Choose an operation randomly

    Returns:
        str: one of mathematical operations (+, -, *)
    """
    return random.choice(['+', '-', '*'])


def Operation_on_numbers(num1, num2, operation):
    """Apply mathematical operation on two numbers

    Args:
        num1 (int): number 1
        num2 (int): number 2
        operation (str): mathematical operation 

    Returns:
        problem (str): The problem definition
        Answer (int): the result of the mathematical operation
    """
    promblem = f"{num1} {operation} {num2}"
    if operation == '+': Answer = num1 + num2 # add
    elif operation == '-': Answer = num1 - num2 # subtract
    else: Answer = num1 * num2 # multiplication

    return promblem, Answer


def math_quiz():
    """Math quiz: 
    1st" generates the mathematical problem
    2nd: ask user for the answer
    3rd: correct answer will gain 1 point
    4th: the game plays in 3 round
    """

    score = 0
    TotlaRound = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(TotlaRound):
        num1 = Random_number(1, 10); num2 = Random_number(1, 5); random_opearation = Operation() # numbers and operation generation

        PROBLEM, ANSWER = Operation_on_numbers(num1, num2, random_opearation) # problem generation
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ") # user's answer
        #useranswer = int(useranswer)

        if int(useranswer) == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score} out of {TotlaRound}")

if __name__ == "__main__":
    math_quiz()
