# 猜數字遊戲 (Number Guessing Game)

這是一個簡單的命令列猜數字遊戲，玩家需要在有限的次數內猜出電腦所想的數字。

## 🎮 遊戲規則

- 電腦會隨機產生一個 1-100 之間的數字
- 玩家有 10 次機會猜測這個數字
- 每次猜測後，系統會提示數字是太大還是太小
- 猜對或用完次數後遊戲結束

## 📋 系統需求

- Python 3.6 或更高版本

## 🚀 開始遊戲

1. 複製專案到本地：
```bash
git clone [repository-url]
cd number-guessing
```

2. 執行遊戲：
```bash
python src/game.py
```

## 📁 專案結構

```
number-guessing/
├── src/
│   ├── game.py      # 主遊戲程式
│   ├── logic.py     # 遊戲邏輯
│   └── utils.py     # 工具函式
└── README.md        # 說明文件
```

## 🎯 遊戲功能

- ✨ 使用者輸入驗證
- 📊 顯示剩餘猜測次數
- 🎮 可重新開始遊戲
- 🌏 完整的中文介面
- 😊 友善的使用者提示

## 🤝 貢獻

歡迎提交 Issue 或 Pull Request 來協助改進遊戲！

## 📜 授權條款

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 檔案。