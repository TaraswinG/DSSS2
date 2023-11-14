import random


def operand_fetch(min, max):
    """
    gives a random integer in the range of min and max
    Args:
        min (int): minimum value of the range
        max (int): maximum value of the range

    Returns:
        int: output is a random integer in the given range
    """    
    
    return random.randint(min, max)


def operator_fetch():
    """
    To generate an operator randomly among '+' '-' '*'

    Returns:
        string: outputs a the operator randomly
    """    
    return random.choice(['+', '-', '*'])


def res_calc(data1, data2, operator):
    """
    defines the problem and calculates the result

    Args:
        data1 (int): from operand_fetch
        data2 (int): from operand_fetch
        operator (string): from operator_fetch

    Returns:
        string, int: The question is in form of string and answer is calculated
    """    
    problem = f"{data1} {operator} {data2}"
    if operator == '+': res = data1 + data2
    elif operator == '-': res = data1 - data2
    else: operator = data1 * data2
    return problem, res

def math_quiz():
    score_sum = 0
    n_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    #start the loop through the number of questions
    for _ in range(n_questions):
        
        data1 = operand_fetch(1, 10)
        data2 = operand_fetch(1, 5.5)
        operator = operator_fetch()

        PROBLEM, ANSWER = res_calc(data1, data2, operator)
        print(f"\nQuestion: {PROBLEM}")
        #to check the validity of user given answer
        while True:
            useranswer = input("Your answer: ")
            try:
                useranswer = int(useranswer)
                break
            except ValueError:
                print("Given input value is invalid. Try again!")
        #score update
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score_sum}/{n_questions}")

if __name__ == "__main__":
    math_quiz()
