def main():
    print("hello world1234")

def ex1():
    a=[1,2,3,4,5]
    print(a[0],a[1],a[2],a[3],a[4])

def ex2():
    a="현재가:50000"
    b=a[4:9]
    print(a)
    print(b)

# '50000'+'50000' = '5000050000'
# c='50000'
# d='50000'
# e=int(c)+int(d)
# print(e)



a={"이름":"홍길동", "국어":100, "영어":88, "수학":95}
print("수학점수:", a["수학"])
print("이름:",a["이름"])


def ex3():
    s1='hello 123 world'
    num=s1[6:9]
    print(num)

    r = len(s1)
    print(r)

def ex4():
    s1='    hello 123 world     \n'
    r1 = len(s1)
    r2 = len(s1.strip())
    print(r1)
    print(r2)

def ex5():
    rec="홍길동, 100,95,88"    
    item=rec.split(",")
    print(item)


def ex6():
    name = '홍길동'
    age = 32
    s = f"{name}님의 나이는 {age}입니다."
    print(s)


class Stock:
    종목코드 = None
    회사명 = None
    현재가 = None
    거래량 = None
    예측 =  None

    def evaluate(self):
        ret = f"종목코드: {self.종목코드}, 회사명: {self.회사명}, 현재가: {self.현재가}, 거래량: {self.거래량}, 예측:{self.예측}"
        print(ret)

def ex7():
    a = 5
    b = 'hello'
    c = Stock()
    c.종목코드 = '005930'
    c.회사명 = '삼성전자'
    c.현재가 = 70000
    c.거래량 = 10000000
    c.예측 = 1
    d = Stock()
    d.종목코드 = '000660'
    d.회사명 = 'SK하이닉스'
    d.현재가 = 130000
    d.거래량 = 5000000
    d.예측 = 0
    c.evaluate()
    d.evaluate()    
       
def getstocks():
    f = open("stock.csv", 'rt', encoding='utf-8')

    ret = []

    for i, stock in enumerate(f.readlines()):
        if i == 0:
            continue

        r1 = stock.strip()
        r2 = r1.split(',')

        s = Stock()
        s.종목코드 = r2[0]
        s.회사명 = r2[1]
        s.현재가 = r2[2]
        s.거래량 = r2[3]
        s.예측 = r2[4]
        
        s.evaluate()
        ret.append(s)

    return ret

if __name__  == "__main__":
    r = getstocks()
    print(r)



# if __name__  == "__main__":
    #main()
    #ex1()
    #ex2()
    # ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex7()

