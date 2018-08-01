def main():
    score_times = []
    score_totals = []
    name = input("Player's name: ")

    for frames in range(1, 10):
        print('\nFrame', frames)
        while True:
            quitting = input(
                '\nDo you wanna quit, if so type quit to do so if not hit enter to continue!! '
            )
            if quitting == 'quit':
                print(name, "is finished!")
                print(name, "'s", 'Total: ', total2)
                exit()
            score = int(input('\nHow many pins did you knock down? '))

            if score > 10:
                print('There is only Ten Pins!!')
            else:
                print(
                    '\nKeep Bowling, its still your turn',
                    name,
                )
                score_times.append(score)
                break

        while True:
            score_2 = int(
                input('\nHow many pins did you knock down this time? '))
            total = score + score_2
            if score > 10:
                print('There is only Ten Pins!!\n')
            else:
                score_times.append(score_2)
                break
        score_times.append(score_2)

        score_totals.append(total)

        total2 = sum(score_totals)
        print(score_totals)
        print(total2)


if __name__ == '__main__':
    main()
