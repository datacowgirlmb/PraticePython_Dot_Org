# Ex 22: Read from File

# Read in a file with a list of names,
# & count the number of times each name occurs.
# Also, read in a file of image names,
# & parse the name to get the category.
# Then count images in each category.

name_count = {}

with open('NamesList.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line in name_count:
            name_count[line] += 1
        else:
            name_count[line] = 1

        line = f.readline()

print(name_count)

image_category_count = {}

with open('ImagesList.txt') as g:
    line = g.readline()
    while line:
        image = line.split('/')
        category = image[2]

        if category in image_category_count:
            image_category_count[category] += 1
        else:
            image_category_count[category] = 1

        line = g.readline()

print(image_category_count)
