from urllib import request
import os
img_dir = "./images"
if not os.path.exists(img_dir):
    os.mkdir(img_dir)
    
url="https://dullyshin.github.io/2018/08/30/HTML-imgLink/#lg=1&slide=0"
request.urlretrieve(url, img_dir+'images/test.jpg')