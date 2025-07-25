from random import randint

# Random CPU number
rand_num = randint(1, 100)

step_count = []

while True:
    try:
        user_input = int(input('🎯 Guess a number between 1 and 100: '))
        step_count.append(user_input)
        if 1 <= user_input <= 100:
            if user_input == rand_num:
                print("\n✅ Your guess is correct! 🎉🎉🎉\n")
                print(f"🎯 Your Number: {user_input}")
                print(f"🖥️  CPU Number : {rand_num}")
                break
            elif user_input < rand_num:
                print('📉 Your number is too low!\n')
            elif user_input > rand_num:
                print('📈 Your number is too high!\n')
        else:
            print('\n🚫 Number out of range (1-100).')
            print('🙏 Thank you for playing!')
            break
    except ValueError:
        # This catches non-integer input (like letters or symbols)
        print('⚠️ Please enter an integer number.')

# Show how many attempts were made
print(f"\n🔢 Total guesses: {len(step_count)}")
print('👋 Thank you for playing!\n')
