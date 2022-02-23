# 散列表
def dictMap():
    book = dict()
    book["apple"] = 0.67
    book["milk"] = 1.49
    book["avocado"] = 1.49
    book["banana"] = 0.69
    print(book)
    print(book["avocado"])

voted = {}
def check_voter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")

if __name__ == '__main__':
    dictMap()

    check_voter("tom")
    check_voter("mike")
    check_voter("mike")

