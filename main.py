import sys
import os
import os
import re
from PIL import Image

if not 'pngs' in os.listdir('.'):
    os.makedirs('pngs')

for i in os.listdir('./Poker/'):
    name = re.findall('(.+)\.', i)
    print(name[0])
    img = Image.open('./Poker/' + i)
    img.save('./pngs/' + name[0] + '.png', 'png')

print('All done!')

# grab first and second argument
# image_folder = sys.argv[1]
# output_folder = sys.argv[2]

# check if folder/ exists, else create it
# print(output_folder)
#
#
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# loop through Poker
# convert images to png
# save to folder

# for filename in os.listdir(image_folder):
#     clean_name = os.path.splitext(filename)[0]
#     img = Image.open(f'{image_folder}{filename}')
#     # added the / in case user doesn't enter it. You may want to check for this and add or remover it.
#     img.save(f'{output_folder}/{clean_name}.png', 'png')
#     print('all done!')
