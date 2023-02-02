import os

a = 'images'  #  r 的意思是  raw  string  原始字符串
img_list_name = os.listdir(a)
print(img_list_name)

for i in range(len(img_list_name)):
    old = os.path.join(a, img_list_name[i])
    new = os.path.join(a, '风景{:03}.jpg'.format(i+1))
    os.rename(old, new)
