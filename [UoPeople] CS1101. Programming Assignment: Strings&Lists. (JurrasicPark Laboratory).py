# CS1101. Chapter 11: String & Lists. Week 6. By Avy Artemis.
# Theme: Jurassic Park (The Laboratory)


# List 5 words in a string separated by spaces (Be Original, They Said)
dinosaurs_string = 'Tyrannosaurus Triceratops Velociraptor Spinosaurus Allosaurus'

# Splitting string into List of words using 'split'
dinosaurs_split = dinosaurs_string.split(' ')

# Deleting 3 words from List using different Python Operation
del dinosaurs_split[1:4]

# Sorting the List
dinosaurs_split.sort()

# Add >= 3 words to the List using different Python Operation
dinosaurs_split[2:] = ['IndominusRex']
new_species = ['BlueRaptor']
new_collection = new_species + dinosaurs_split
new_collection.append('TRex')
lab_reptile = ['Chameleon']
new_collection.extend(lab_reptile)
new_collection.sort()

# Turn List of words back to single string using 'join'
x = ' '
new_dinosaur_string_collection = x.join(new_collection)
print(new_dinosaur_string_collection)


