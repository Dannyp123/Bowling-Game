def new_main():
    total_throws = []
    frame_throws = []
    name = input("Player's name: ")
    for frame in range(1, 10):
        print_frame(frame)
        first_throw = input_first_throw(name)
        if first_throw == 10:
            print('AWESOME.... You got a strike!!')
            total_throws.append(total_throws[0])
            total_throws.append(first_throw)
            frame_throws.append('X')
            total = sum(total_throws)
            print(total)
            print(total_throws)
            print(frame_throws)
        else:
            second_throw = input_second_throw(first_throw)
            if first_throw + second_throw == 10:
                total_balls = first_throw + second_throw
                print('YAY, you got a SPARE')
                total_throws.append(second_throw)
                total_throws.append(total_balls)
                frame_throws.append('/')
                total = sum(total_throws)
                print(total)
                print(total_throws)
                print(frame_throws)
            else:
                print('\nYou are doing a great job!')
                bowling_total = first_throw + second_throw
                total_throws.append(bowling_total)
                frame_throws.append(second_throw)
                frame_throws.append(first_throw)
                total = sum(total_throws)
                print(frame_throws)
                print(total_throws)
                print(total)
    print('You have a total of', total)
    print('\nGoodbye', name)


def input_first_throw(name):
    while True:
        score = int(input('\nHow many pins did you knock down? '))

        if score > 10:
            print('There is only Ten Pins!!')
        else:
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
    print('Frame: ', frame)
    print('---------------------------------------------------------')


if __name__ == '__main__':
    new_main()
