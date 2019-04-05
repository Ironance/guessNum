import random

range_ok = False

while range_ok == False:
    limit_low = input('Please input the lower limit of the range:')
    limit_up = input('Please input the upper limit of the range:')
    if limit_low < limit_up:
        range_ok = True
    else:
        print('Something wrong in range setting! Please set again.')

limit_low = int(limit_low)
limit_up = int(limit_up)
ans = random.randint(limit_low,limit_up)
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
            limit_low = user_ans + 1
            print('Range of the remained numbers is', limit_low, 'to', limit_up)
        else:
            print('The answer is less than', user_ans)
            limit_up = user_ans - 1
            print('Range of the remained numbers is', limit_low, 'to', limit_up)
