import random
import string


def name_generator(letters):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                  'n', 'o', 'p', 'q', 'r', 's', 'y', 'v', 'w', 'x', 'y', 'z']
    v = []
    c = []
    names = []
    for letter in letters:
        if letter.lower() in vowels:
            v.append(letter)
        elif letter.lower() in consonants:
            c.append(letter)
    if len(letters) < 3:
        raise Exception(
            'There should be more than {} letters in the letters'.format(len(letters)))
    if len(v) == 0:
        raise Exception('There is no vowel in the letters')
    if len(c) == 0:
        raise Exception('There is no consonant in the letters')
    for i in range(5):
        first_name_len = random.randint(2, len(letters))
        last_name_len = random.randint(2, len(letters))

        first_name = random.choice(
            v) + "".join(random.sample(letters, first_name_len))
        last_name = random.choice(
            c) + "".join(random.sample(letters, last_name_len))
        full_name = first_name + " " + last_name

        user = {
            "first_name": first_name.title(),
            "last_name": last_name.title(),
            "full_name": full_name.title()
        }

        names.append(user)
    return names

print(name_generator(['v', 'w', 'A', 'I', 'T']))
