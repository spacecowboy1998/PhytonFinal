def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


while True:
    turn = int(input("მიმდევრობის მერამდენე რიცხვის ხილვა გსურთ? :"))
    if turn < 0:
        print("შემოიტანეთ ნატურალური რიცხვი")
    elif turn == 1:
        print(1)
        break
    elif turn == 0:
        print(0)
        break
    else:
        print(fibonacci(turn))
        break
