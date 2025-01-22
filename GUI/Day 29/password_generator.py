from random import choice, randint, shuffle
from string import ascii_letters, punctuation, digits

password_list = (
        [choice(ascii_letters) for _ in range(randint(8, 10))] +
        [choice(punctuation) for _ in range(randint(2, 4))] +
        [choice(digits) for _ in range(randint(2, 4))]
)

shuffle(password_list)
password = "".join(password_list)
