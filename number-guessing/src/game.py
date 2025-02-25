from logic import generate_number, check_guess
from utils import get_user_guess, display_result

def main():
    """主遊戲循環"""
    print("\n歡迎來到猜數字遊戲！")
    print("我想了一個 1-100 之間的數字。")
    print("你有 10 次機會猜出這個數字。\n")
    
    target = generate_number()
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        attempts += 1
        print(f"\n第 {attempts}/{max_attempts} 次嘗試")
        
        guess = get_user_guess()
        result = check_guess(target, guess)
        display_result(result, attempts)
        
        if result == "correct":
            break
    
    if attempts == max_attempts and result != "correct":
        print(f"\n😔 遊戲結束！正確答案是 {target}。")
    
    play_again = input("\n要再玩一次嗎？(yes/no): ").strip().lower()
    if play_again == "yes":
        main()
    else:
        print("\n感謝遊玩！再見！👋")

if __name__ == "__main__":
    main()