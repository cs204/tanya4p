while True:
    v = input("Дробь: ")
    try:
        num, den = v.split('/')
        num = int(num)
        den = int(den)
        res = num / den * 100
        break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
res = round(res)
if res<=1:
    print("E")
elif res >=99:
    print("F")
else:
    print(str(round(res))+"%")