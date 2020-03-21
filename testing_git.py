def printing_hello():
    print("Привет GitHub!")

# удалил

def fact(max_nym):
    res = 1
    for num_next in range (1, max_nym+1):
        res *= num_next
    return res

def input_name():
    name = input("Введите Ваше имя: ")
    return name

if __name__ == '__main__':
    printing_hello()
    input_name()
    print(fact(5))