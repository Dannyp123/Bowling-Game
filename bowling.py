def new_main():
    score_times = []
    name = input("Player's name: ")
    for frame in range(1, 10):
        print_frame(frame)
        first_throw = input_first_throw(name)
        if first_throw == 10:
            print('AWESOME.... You got a strike!!')
            score_times.append(first_throw)
            print(score_times)
        else:
            second_throw = input_second_throw(first_throw)
            if first_throw + second_throw == 10:
                print('YAY, you got a SPARE')
                score_times.append(second_throw)
                print(score_times)
            else:
                print('You bowled great!')
                bowling_total = first_throw + second_throw
                score_times.append(bowling_total)
                total = sum(score_times)
                print(score_times)
    print('You have a total of', total)
    print('\nGoodbye', name)


def input_first_throw(name):
    while True:
        score = int(input('\nHow many pins did you knock down? '))

        if score > 10:
            print('There is only Ten Pins!!')
        else:
            print(
                '\nKeep Bowling, its still your turn',
                name,
            )
            return score


def input_second_throw(first_throw):
    while True:
        second_throw = int(
            input('\nHow many pins did you knock down this time? '))

        pair_score = first_throw + second_throw

        if pair_score > 10:
            print('There is only Ten Pins!!\n')
        else:
            return second_throw


def print_frame(frame):
    print('---------------------------------------------------------')
    print('Frame: ', frame)
    print('---------------------------------------------------------')


if __name__ == '__main__':
    new_main()
