import RandomCharacter

NUMBER_OF_CHARS=175
CHARS_PRE_LINE=25

for i in range(NUMBER_OF_CHARS):
    print(RandomCharacter.getRandomDigitCharacter(),end=' |')
    if(i+1)%CHARS_PRE_LINE==0:
        print()