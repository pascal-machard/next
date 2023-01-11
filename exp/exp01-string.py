def main():
    message = "Hello World"

    message = 'hello' + ' ' + 'world'

    message = 'hello ' * 3

    message = 'hello'
    message += ' '
    message += 'world'

    message = 'hello' + ' ' + 'world'
    print(len(message))

    message = "HELLO WORLD"
    messagea = message.lower()
    print(messagea)

    message = "HELLO WORLD"
    messagea = message.replace("L", "pizza")
    print(messagea)

    message = "Hello World"
    messagea = message[1:8]
    print(messagea)

    startLoc = 2
    endLoc = 8
    messageb = message[startLoc: endLoc]
    print(messageb)

    message = "Hello World"
    print(message[:5].find("d"))

    message= "Rio de Janeiro"
    print(message.count(' '))

    my_phrase = "let's go to the beach"
    my_words = my_phrase.split(" ")
    for word in my_words:
        print(word)

    long_text = "This is a multiline, \n\n" \
    "a long string with lots of text \n\n" \
    "I'm using backlashes to make it work."
    print(long_text)

    regular_text = "   This is a regular text."
    no_space_begin_text = regular_text.lstrip()
    print(regular_text)
    #'   This is a regular text.'
    print(no_space_begin_text)
    #'This is a regular text.'

    regular_text = "$@G#This is a regular text."
    clean_begin_text = regular_text.lstrip("#$@G")
    print(regular_text)
    # $@G#This is a regular text.
    print(clean_begin_text)
    # This is a regular text.

    regular_text = "This is a regular text.   "
    no_space_end_text = regular_text.rstrip()
    print(regular_text)
    # 'This is a regular text.   '
    print(no_space_end_text)
    # 'This is a regular text.'

    regular_text = "  This is a regular text.   "
    no_space_text = regular_text.strip()
    print(regular_text)
    # '  This is a regular text.   '
    print(no_space_text)
    # 'This is a regular text.'

    regular_text = "AbC#This is a regular text.$@G#"
    clean_text = regular_text.strip("AbC#$@G")
    print(regular_text)
    # AbC#This is a regular text.$@G#
    print(clean_text)
    # This is a regular text.

    regular_text = "This is a regular text."
    title_case_text = regular_text.title()
    print(regular_text)
    # This is a regular text.
    print(title_case_text)
    # This Is A Regular Text.

    regular_text = "This IS a reguLar text."
    swapped_case_text = regular_text.swapcase()
    print(regular_text)
    # This IS a reguLar text.
    print(swapped_case_text)
    # tHIS is A REGUlAR TEXT.

    my_string = ''
    if not my_string:
      print("My string is empty!!!")

    word = 'beach'
    number_spaces = 32
    word_justified = word.rjust(number_spaces)
    print(word)
    # 'beach'
    print(word_justified)
    # '                           beach'

    word = 'beach'
    number_chars = 32
    char = '$'
    word_justified = word.rjust(number_chars, char)
    print(word)
    # beach
    print(word_justified)
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$beach

    word = 'beach'
    number_spaces = 32
    word_justified = word.ljust(number_spaces)
    print(word)
    # 'beach'
    print(word_justified)
    # 'beach                           '

    word = 'beach'
    print(word.isalnum())
    # output: True
    word = '32'
    print(word.isalnum())
    # output: True
    word = 'number32'  # notice there is no space
    print(word.isalnum())
    # output: True
    word = 'Favorite number is 32'  # notice the space between words
    print(word.isalnum())
    # output: False
    word = '@number32$'  # notice the special chars '@' and '$'
    print(word.isalnum())
    # output: False

    text = ''  # notice this is an empty string, there is no white space here
    print(text.isprintable())
    # output: True
    text = 'This is a regular text'
    print(text.isprintable())
    # output: True
    text = ' '  # one space
    print(text.isprintable())
    # output: True
    text = '                        '  # many spaces
    print(text.isprintable())
    # output: True
    text = '\f\n\r\t\v'
    print(text.isprintable())
    # output: False

    text = ' '
    print(text.isspace())
    # output: True
    text = ' \f\n\r\t\v'
    print(text.isspace())
    # output: True
    text = '                        '
    print(text.isspace())
    # output: True
    text = ''  # notice this is an empty string, there is no white space here
    print(text.isspace())
    # output: False
    text = 'This is a regular text'
    print(text.isspace())
    # output: False

    phrase = "This is a regular text"
    print(phrase.startswith('This is'))
    # output: True
    print(phrase.startswith('text'))
    # output: False

    phrase = "This is a regular text"

    print(phrase.startswith('regular', 10))  # the word regular starts at position 10 of the phrase
    # output: True
    print(phrase.startswith('regular', 10, 22))  # look for in 'regular text'
    # output: True
    print(phrase.startswith('regular', 10, 15))  ##look for in 'regul'
    # output: False

    text = 'This is a regular text'
    print(text.isupper())
    # output: False
    text = 'THIS IS A REGULAR TEXT'
    print(text.isupper())
    # output: True
    text = 'THIS $ 1S @ A R3GULAR TEXT!'
    print(text.isupper())
    # output: True

    my_string = 'beach'

    print('$'.join(my_string))
    # output: b$e$a$c$h
    my_list = ['bmw', 'ferrari', 'mclaren']
    print('$'.join(my_list))
    # output: bmw$ferrari$mclaren
    my_tuple = ('bmw', 'ferrari', 'mclaren')
    print('$'.join(my_tuple))
    # output: bmw$ferrari$mclaren

    my_set = {'bmw', 'ferrari', 'mclaren'}
    print('|'.join(my_set))
    # output: bmw|ferrari|mclaren

    my_dict = {'bmw': 'BMW I8', 'ferrari': 'Ferrari F8', 'mclaren': 'McLaren 720S'}
    print(','.join(my_dict))
    # output: bmw,ferrari,mclaren

    my_string = 'world \n cup'
    print(my_string.splitlines())
    # output: ['world ', ' cup']

    my_string = 'world \n cup'
    print(my_string.splitlines(True))
    # output: ['world \n', ' cup']

    word = '32'
    print(word.isdigit())
    # output: True
    print("\u2083".isdigit())  # unicode for subscript 3
    # output: True
    word = 'beach'
    print(word.isdigit())
    # output: False
    word = 'number32'
    print(word.isdigit())
    # output: False
    word = '1 2 3'  # notice the space between chars
    print(word.isdigit())
    # output: False
    word = '@32$'  # notice the special chars '@' and '$'
    print(word.isdigit())
    # output: False

    word = '32'
    print(word.isdecimal())
    # output: True

    word = '954'
    print(word.isdecimal())
    # output: True
    print("\u2083".isdecimal())  # unicode for subscript 3
    # output: False
    word = 'beach'
    print(word.isdecimal())
    # output: False
    word = 'number32'
    print(word.isdecimal())
    # output: False
    word = '1 2 3'  # notice the space between chars
    print(word.isdecimal())
    # output: False
    word = '@32$'  # notice the special chars '@' and '$'
    print(word.isdecimal())
    # output: False

    word = 'beach'
    print(word.isalpha())
    # output: True
    word = '32'
    print(word.isalpha())
    # output: False
    word = 'number32'
    print(word.isalpha())
    # output: False
    word = 'Favorite number is blue'  # notice the space between words
    print(word.isalpha())
    # output: False
    word = '@beach$'  # notice the special chars '@' and '$'
    print(word.isalpha())
    # output: False

    my_string = 'B\tR'
    print(my_string.expandtabs())
    # output: B       R
    my_string = 'WORL\tD\tCUP'
    print(my_string.expandtabs())
    # output: WORL    D       CUP

    word = 'beach'
    number_spaces = 32
    word_centered = word.center(number_spaces)
    print(word)
    # 'beach'
    print(word_centered)
    ##output: '              beach              '

    word = 'beach'
    number_chars = 33
    char = '$'
    word_centered = word.center(number_chars, char)
    print(word)
    # beach
    print(word_centered)
    # output: $$$$$$$$$$$$$$beach$$$$$$$$$$$$$$

    phrase = "This is a regular text"
    # look for in 'This is', the rest of the phrase is not included
    print(phrase.find('This', 0, 7))
    # look for in 'This is a regular'
    print(phrase.find('regular', 0, 17))
    # look for in 'This is a regul'
    print(phrase.find('a', 0, 15))

if __name__ == "__main__":
    main()
