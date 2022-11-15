# import sys
# import os
# from PIL import Image
#
# # grab first and second argument
# image_folder = sys.argv[1]
# output_folder = sys.argv[2]
#
# print(image_folder, output_folder)
#
# # check if folder/ exists, else create it
#
# #
# # if not os.path.exists(output_folder):
# #     os.makedirs(output_folder)
# #
# # # loop through Poker
# # # convert images to png
# # # save to folder
# #
# # for filename in os.listdir(image_folder):
# #     clean_name = os.path.splitext(filename)[0]
# #     img = Image.open(f'{image_folder}{filename}')
# #     # added the / in case user doesn't enter it. You may want to check for this and add or remover it.
# #     img.save(f'{output_folder}/{clean_name}.png', 'png')
# #     print('all done!')
