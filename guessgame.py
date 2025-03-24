import random

answer_number = random.randrange(1,101)
guess_count = 0
is_guessing = True
print("즐거운 숫자 맞추기~~")
#print(answer_number)

while is_guessing:

    guess_count += 1
    if guess_count == 7:
        print("정답을 맞추지 못햇습니다.")
        break
    guess_number = int(input(f"{7 - guess_count}번의 기회가 남았습니다. 숫자를 입력: "))
    if guess_number > answer_number:
        print("입력한 숫자 보다 작습니다.\n")
    if guess_number < answer_number:
        print("입력한 숫자 보다 큽니다.\n")
    if guess_number == answer_number:
        print(f"와! 정답{guess_count}번만에 맞췄어요!")
        is_guessing = False