#small_numbers = [num for num in nums if num < 6]
#three_letters_words = [ word.title() for word in words if len(word) == 3 ]

# Example set
songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals'),
    ('The Beatles', 'Nowhere Man'),
    ('The Rolling Stones', 'Brown Sugar'),
    ('Bob Marley', 'No Woman No Cry'),
    ('Nickelback', 'Song on Fire'),
    ('Nickelback', 'Talbot is the man')
}

better_songs = [song for song in songs if song[0] != 'Nickelback']
print(better_songs)