from morse_code import morse_dict, alphabet_dict

while True:
    user_choice = input('What would you like to translate? Text, Morse or Quit: ').lower()

    if user_choice == 'text':
        text_input = input('Please enter Text to convert to Morse code: ').lower()

        text_item_list = []
        for word in text_input:
            text_item_list.append(word)

        text_item_list = ''.join(text_item_list)

        text_to_morse_trans = []
        for char in text_item_list:

            if char in morse_dict:
                text_to_morse_trans.append(morse_dict[char])

            elif char == ' ':
                char = ' / '
                text_to_morse_trans.append(char)

            else:
                print('Please enter a valid text input.')

        plain_morse_code = " ".join(text_to_morse_trans)
        print(f'The converted Morse code is: {plain_morse_code}')
        break

    elif user_choice == 'morse':

        print('Please use a forward-slash (/) to distinguish between words.')
        morse_input = input('Please enter Morse to convert to Text: ')
        morse_to_text_trans = []

        words = morse_input.split(' / ')
        for word in words:
            characters = word.split()
            translated_word = []

            for key in characters:
                if key in alphabet_dict:
                    translated_word.append(alphabet_dict[key])

                else:
                    print(f'Please enter a valid Morse code entry. {key} is not a recognised '
                          f'morse character.')

            morse_to_text_trans.append(''.join(translated_word))

        plain_text = ' '.join(morse_to_text_trans)
        print(f'The converted Text is: {plain_text}')
        break

    elif user_choice == 'quit':
        print('Quitting program')
        break

    else:
        print('Please input a valid selection. Text, Morse or Quit')
