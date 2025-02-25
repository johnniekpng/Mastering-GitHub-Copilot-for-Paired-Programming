import random

def generate_number(min_num=1, max_num=100):
    """產生一個指定範圍內的隨機數字"""
    return random.randint(min_num, max_num)

def check_guess(target, guess):
    """檢查猜測的數字是否正確"""
    if guess == target:
        return "correct"
    elif guess > target:
        return "high"
    else:
        return "low"