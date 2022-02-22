# 编写递归函数时，必须告诉它何时停止递归，正因为如此，每个递归函数都有两部分
# 基线条件和递归条件，递归条件指的是函数调用自己，而基线条件则指的是函数不在调用自己，从而避免形成无限循环。


def countdown(i):
    print(i)
    # 基线条件
    if i <= 1:
        return
    # 递归条件
    else:
        countdown(i - 1)

if __name__ == '__main__':
    countdown(100)