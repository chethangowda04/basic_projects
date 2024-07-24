ids = ['Chethan', 'Acchu']
psw = ['911', '613']
bal = [2000000, 70000]

idx_id = 0


# login
def acc():
    print('')

    accid = input('Enter your account id : ')
    print('')

    if (accid in ids):
        idx_id = (ids.index(accid))

        password = input('Enter your password : ')
        if (password in psw and password == psw[idx_id]):

            print('')
            print('Welcome!!')

            activity(idx_id)
        else:
            print('wrong password')
            acc()
    else:
        print('wrong id......')

        print('')

        print('This id does not exist! ')
        create_acc()

# activities to do
def activity(idx_id):
    print('')
    print('Your bank balance amount =', bal[idx_id])

    opt = int(input('Do you want to withdraw money (1)/deposit money (2)/log out (3) : '))

    while (opt != 3):

        if (opt == 1):

            print('')

            x = int(input('Enter the amount of money you want to withdraw : '))
            total = bal[idx_id] - x

            bal[idx_id] = total

            print('')

            print('You have recieved rupees', x)

            print('')

            print('1.Your bank balance amount =', bal[idx_id])




        elif (opt == 2):

            print('')

            x = int(input('Enter the amount of money you want to deposit : '))
            total = bal[idx_id] + x

            bal[idx_id] = total

            print('')

            print('You have deposited rupees', x)

            print('')

            print('2.Your bank balance amount =', bal[idx_id])

        else:
            print('ERROR')
            activity(idx_id)

        opt = int(input('Do you want to withdraw money (1)/deposit money (2)/log out (3) : '))

    print('logging out...')
    print('Thank You!')


acc()