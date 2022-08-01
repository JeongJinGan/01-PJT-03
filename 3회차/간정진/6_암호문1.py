# 명령어 = 명령어리스트[0]
# if 명령어 == "I":
#   x = 명령어리스트[0 + 1]
#   y = 명령어리스트[0 + 2]
#   숫자리스트 = 명령어리스트[0 + 3 : 0 + 3 + y]
#   for 숫자 in 숫자_리스트[::-1]:
#       암호문.inser(삽입_인덱스, 숫자) # 0 -> 1
#----------------------------------------------------#
import sys

sys.stdin = open("_암호문1.txt", "r")

T = 10
# ctrl + d 단축키 쉼표 표시하고 단추키 쓰면 쉼표만 표시 가능
# 원본암호문 = [449047, 855428, 425117, 532416, 358612, 929816, 313459, 311433, 472478, 589139, 568205]

for t in range(1, T+1):
    origin_len = int(input())
    origin_list = list(map(int, input().split()))

    command_len = int(input())
    command_list = input().split()

    # i의 초기화
    i = 0

    # while 문 
    while i < len(command_list):
        command = command_list[i]
        if command == "I":
            # x, y 숫자리스트 s 구해야한다.
            x = int(command_list[i+1])
            y = int(command_list[i+2])
            number_list = command_list[i + 3 : i + 3 + y]

            # insert 메서드를 써서 x의 위치에 숫자들을 삽입한다.
            # 역순으로 삽입한다.
            for number in number_list[::-1]:
                origin_list.insert(x, int(number))
        
        # 0 + 1 -> 1
        i = i + 1
    
    print(f'#{t}' ,*origin_list[:10])
