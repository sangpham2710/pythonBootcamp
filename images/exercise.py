from PIL import Image

mask = Image.open('mask.png')
word_matrix = Image.open('word_matrix.png')

# mask.show()
mask = mask.resize(word_matrix.size)
# mask.show()
# word_matrix.show()
# print(mask.size)
# print(word_matrix.size)

mask.putalpha(100)
word_matrix.paste(im=mask, box=(0, 0), mask=mask)
word_matrix.show()
