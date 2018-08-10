# 1. Grab the number 6 from this nested list and set it equal to the number six variable
nested_list = [1, [2, [4, [5, [6]], 3]]]
number_six = nested_list[1][1][1][1][0]
print number_six

# 2. Sort the cats list in alphabetical order
cats = ['Maine Coon', 'Tabby', 'Siamese', 'Garfield', 'Sylvester']
cats.sort()
print cats

# 4. Create a new list cat_jrs by appending 'Jr.' to each of the cats names
cats = ['Maine Coon', 'Tabby', 'Siamese', 'Garfield', 'Sylvester']

cat_1 = cats[0] + ' Jr.'
cat_2 = cats[1] + ' Jr.'
cat_3 = cats[2] + ' Jr.'
cat_4 = cats[3] + ' Jr.'
cat_5 = cats[4] + ' Jr.'
cat_jrs = [cat_1, cat_2, cat_3, cat_4, cat_5]
print cat_jrs

# 5. create a pets array that contains the elements of the cats and dogs lists 

cats = ['Maine Coon', 'Tabby', 'Siamese', 'Garfield', 'Sylvester']
dogs = ['Scooby', 'Scrappy', 'Clifford', 'Pickles', 'Floyd']
animal = [cats, dogs]
print animal

# 6. add the cats in more_cats to the original list of cats

cats = ['Maine Coon', 'Tabby', 'Siamese', 'Garfield', 'Sylvester']
more_cats = ['Horatio', 'Whiskers', 'Chesire']
cats.append(more_cats[0])
cats.append(more_cats[1])
cats.append(more_cats[2])
print cats


# BONUS: Sorts the cats list in alphabetical order by third character of each element

cats = ['Maine Coon', 'Tabby', 'Siamese', 'Garfield', 'Sylvester']
char1 = cats[0][2]
char2 = cats[1][2]
char3 = cats[2][2]
char4 = cats[3][2]
char5 = cats[4][2]
print char1, char2, char3, char4, char5

char_ls = [char1, char2, char3, char4, char5]
char_ls.sort()
print char_ls