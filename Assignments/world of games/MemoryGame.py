def Memory_Game(diff):
    import random
    def generate_sequence():
        import random
        seq = []
        for i in range(diff):
            seq.append(random.randint(1, 101))
        return seq

    def user_sequence():
        userseq = []
        for i in range(diff):

            number = int(input('please enter a number between 1 -101:\n'))
            if 0 < number < 101:
                userseq.append(number)
            else:
                print('error number out of range')
                break
        return userseq

    def is_list_equal(generated, user):
        user.sort()
        generated.sort()
        print(user == generated)

    def play():
        if is_list_equal(generate_sequence(), user_sequence()):
            print('congratulations !! you have won :)')
        else:
            print('You have lost, try again :(')
    play()