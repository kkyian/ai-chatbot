what_to_say = {'hello':'hello', 'bye':'bye'}
while True:
    input1 = input('What do you want to say:')
    if input1 in what_to_say:
        print(what_to_say[input1])
        stay = input('do you want to quit:')
    else:
        say = input(f'What would you say to reply {input1}:')
        what_to_say[input1] = say
        print(what_to_say[input1])
        stay = input('do you want to quit:')
    if stay == 'yes':
        break