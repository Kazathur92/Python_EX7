# Examples of comprehensions
nums = range(10)
small_numbers = [num for num in nums if num < 6]
# print(small_numbers)
# Only add numbers to the new list if the value is less than 6

words = ['big', 'red', 'dog', 'ate', 'his', 'food']
three_letters_words = [ word.title() for word in words if len(word) == 3 ]
# print(three_letters_words)
# len(stringVariable) is equivalent to stringVariable.length in JavaScript


# 1 Define a set that contains tuples. Each tuple should contain two strings:

# The name of an artist
# A song by that artist
# Make sure that some of the songs are from the band Nickelback. You can see a list of their greatest hits on Amazon.

# # Example set
# songs = {
#     ('Nickelback', 'How You Remind Me'),
#     ('Will.i.am', 'That Power'),
#     ('Miles Davis', 'Stella by Starlight'),
#     ('Nickelback', 'Animals')
# }
# 2 Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

songs = {
    ('Nickelback', 'How You Remind Me'),
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
}

no_more_nickleback = [ song for song in songs if song[0] != "Nickelback" ]
set(no_more_nickleback)

print(no_more_nickleback)


