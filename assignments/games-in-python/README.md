

# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

通过本次作业，你将用 Python 实现经典的单词猜测游戏 Hangman，锻炼字符串处理、循环、条件判断和随机选择等编程技能。

## 📝 Tasks

### 🛠️ 任务一：单词与界面初始化

#### Description
编写代码，随机从预设单词列表中选择一个单词，并以 `_ _ _` 形式显示给玩家。

#### Requirements
Completed program should:

- 包含一个不少于5个单词的列表
- 随机选择一个单词作为本轮游戏目标
- 用下划线显示未猜中的字母

### 🛠️ 任务二：实现猜字母与游戏主循环

#### Description
实现玩家输入字母、判断是否正确、更新显示和剩余机会，并在游戏结束时给出胜负提示。

#### Requirements
Completed program should:

- 接收玩家输入的字母并判断是否在单词中
- 正确更新已猜中的字母显示
- 跟踪并显示剩余猜测次数
- 在玩家猜中全部字母或用尽机会时，显示胜利或失败信息
