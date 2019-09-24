import random
directions = ['N', 'S', 'E', 'W']
answer = 'You are in the magic maze. Which way to go?' + random.choice(directions)
secret_escape_combi = ['S', 'S', 'N', 'W', 'E', 'S']
moves = 1
lives = 3
if moves == [11, 21 , 31]:
    lives = lives - 1
    print('You have just lost a life. You are now left with ' + str(lives) + ' lives')

for i in secret_escape_combi:
    while answer == secret_escape_combi[secret_escape_combi.index(i)] is False:
        print('Start again')
        x = x + 1
        if lives == 0:
            print('You are dead.')
            break
        if answer == secret_escape_combi[i]:
            i = i + 1
            if i < len(secret_escape_combi):
                print('Next, which way to go?')
            else:
                print('Congratualations! You have successfully escaped the maze.')
                break