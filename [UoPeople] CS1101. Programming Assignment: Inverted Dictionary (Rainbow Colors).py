# Creating an Artistic Inverted Dictionary
RainbowColors = {'C1': ['Red', 'Rose', 'Sangria', 'Scarlet', 'Warm Colours'],
                 'C2': ['Orange', 'Carrot', 'Sandstone', 'Warm Colours'],
                 'C3': ['Yellow', 'Bumble Bee', 'Dandelion', 'Warm Colours'],
                 'C4': ['Green', 'Chartreuse', 'Olive', 'Calming Effects'],
                 'C5': ['Blue', 'Navy', 'Ocean', 'Denim', 'Cerulean', 'Cool Colours', 'Calming Effects'],
                 'C6': ['Indigo', 'Purple', 'berry', 'Cool Colours', 'Calming Effects'],
                 'C7': ['Violet', 'Purple', 'Lavender', 'Cool Colours', 'Calming Effects']}

print('Original dictionary contains', RainbowColors)
print('\n')


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        for sub_key in val:
            if sub_key not in inverse:
                inverse[sub_key] = [key]
        else:
            inverse[sub_key].append(key)
    return inverse


inverted_Rainbow = invert_dict(RainbowColors)
print('Inverted colorful dictionary now contains', inverted_Rainbow)

# My dictionary describes the 7 colors of a rainbow and lists examples of its shade.
# My inverted dictionary helps to tell an artist which color is 'warm' or 'cool' colors especially if the palette name
# is new and obscure to them. This can potentially teach and help them to organize hundreds to thousands of
# color codings in design software.
