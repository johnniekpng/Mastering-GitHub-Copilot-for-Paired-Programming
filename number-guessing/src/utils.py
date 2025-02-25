def get_user_guess(min_num=1, max_num=100):
    """獲取並驗證使用者輸入"""
    while True:
        try:
            guess = int(input(f"請輸入一個 {min_num}-{max_num} 之間的數字: "))
            if min_num <= guess <= max_num:
                return guess
            print(f"請輸入 {min_num}-{max_num} 之間的數字。")
        except ValueError:
            print("無效的輸入，請輸入一個數字。")

def display_result(result, attempts):
    """顯示猜測結果"""
    if result == "correct":
        print(f"\n🎉 恭喜！你用了 {attempts} 次就猜對了！")
    elif result == "high":
        print("太高了！試試小一點的數字。")
    else:
        print("太低了！試試大一點的數字。")