# Make an empty list for storing aliens.
<<<<<<< HEAD
# Modified by Debdatta Porya

=======
>>>>>>> 3690082cad0aad58cedb4face741aa025d6e8d73
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
<<<<<<< HEAD
print(f"Total number of aliens: {len(aliens)}")
print(aliens)
=======
print(f"Total number of aliens: {len(aliens)}")
>>>>>>> 3690082cad0aad58cedb4face741aa025d6e8d73
