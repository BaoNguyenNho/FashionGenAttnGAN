import h5py
import pickle
# Đọc đối tượng từ file pickle
# with open('D:\Download\FashionGenAttnGAN\FashionGenAttnGAN\data\captions2_attngan.pickle', 'rb') as file:
#     data = pickle.load(file)

# print(len(data))
# train_file_h5 = h5py.File("D:\Download\FashionGenAttnGAN\FashionGenAttnGAN\data\\fashiongen_256_256_train.h5", mode='r')

# print(train_file_h5['image'][2])
from PIL import ImageFont, ImageDraw
import os
current_dir = os.path.dirname(__file__)
fnt = ImageFont.truetype("FreeMono.ttf", 50)
# print the current path of os


# print (os.path.join(current_dir, "code", "FreeMono.ttf"))