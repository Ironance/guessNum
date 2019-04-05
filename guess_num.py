import random

ans = random.randint(1,100)
guess_count = 0

while True:
    user_ans = input('Please input your answer: ')
    user_ans = int(user_ans)
    guess_count = guess_count + 1
    if ans == user_ans:
        print('BINGO! The answer is', ans)
        print('You have guessed', guess_count, 'time(s)')
        break
    else:
        if ans > user_ans:
            print('The answer is greater than', user_ans)
        else:
            print('The answer is less than', user_ans)