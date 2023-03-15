import random
  
def read_file():  #파일로부터 데이터를 읽음
    try :
        with open('./lunch.txt', 'rt', encoding="UTF-8") as f: #자동으로 파일 읽기
            lunch = f.readlines()  # 다른 곳에선 사용x  지역변수            
            print(lunch)
            return lunch   #지역변수 이면서 밖에서도 사용가능
    except FileNotFoundError:
        print("파일이 없습니다")
        return    #아무 행동 안하고 통과    

def input_lunch():   #점심메뉴 입력 (메인에서 선택되었을 때 구동된다)       
    while True:
        mymenu = input("원하는 메뉴를 입력하세요")       
        try:
            if mymenu == "#":
                if len(lunch) == 0: raise IndexError
                print("다시입력하세요")
                continue                 
            elif mymenu.isnumeric() : 
                raise ValueError
                print("숫자ㄴㄴ")
                continue
            else:
                lunch.append(mymenu)
                continue       
        except(IndexError,ValueError):
            print("메뉴를 입력하세요")
        
        
def output_lunch():  #메뉴 2번  
    with open('./lunch.txt', 'rt', encoding="UTF-8") as f:
        lunch = f.readlines()
        print(lunch)
    if lunch.isalpha() : 
        print("메뉴를 입력하세요")        

def choice_lunch():  #메뉴 3번    
    lunch = read_file()
    mychoice = random.choice(lunch)
    print(mychoice)

def delete_lunch():   #메뉴 4번
    print(random.choice(lunch))
    deleteFood = input("삭제할 음식을 입력해주세요")   
    lunch.remove(deleteFood)
   
    

def write_lunch():    #메뉴 0 선택시 ==> 파일에 저장
    f = open('./lunch.txt','r',encoding='UTF-8')
    for i in lunch:
        data = "%s\n" % i
        f.write(data)
        
#main부분
lunch = read_file()

while True :    
    select = input("1)점심 메뉴 추가 2) 메뉴 확인 3) 점심메뉴선택 4) 메뉴 삭제 0) 종료")
    if select == "1":
        input_lunch()
    elif select == "2":    
        output_lunch()
    elif select == "3":
        choice_lunch()
    elif select == "4":
        delete_lunch()
    elif select == "0":
        write_lunch()
    else:
        print("숫자만 입력하세요")
        
 
 # try:
#     mychoice = random.choice(input_lunch())
#     print("점심메뉴는 : ", mychoice)
# except(IndexError, ValueError):
#     print("메뉴를 입력해주세요")

