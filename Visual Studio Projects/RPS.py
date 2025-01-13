import random
choice = ['scissors','rock','paper']
computer_choice = random.choice(choice)
user_win = 0
computer_win=0
user_choice = input('do you want rock, paper, or scissors\n')
while(user_choice !='done'):
    if computer_choice == user_choice:
        print('TIE')
    elif user_choice == 'rock' and computer_choice == 'scissors':
        user_win=user_win+1
        print('WIN')
    elif user_choice =='scissor' and computer_choice == 'paper':
        user_win=user_win+1
        print('WIN')
    elif user_choice =='paper' and computer_choice == 'rock':
        user_win=user_win+1
        print('WIN')
    else: 
        computer_win=computer_win+1
        print('YOU LOSE')
    print('computer picked ' ,computer_choice)
    print('the score is ', user_win,' to ',computer_win)
    computer_choice = random.choice(choice)
    user_choice = input('Pick to go again\n\n')