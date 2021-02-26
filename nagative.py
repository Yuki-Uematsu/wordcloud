import pandas as pd
import re

from PIL import Image
import numpy as np



df = pd.read_csv("---.csv")
#print("first_data_sides_is {}".format(df.info()))
de = pd.read_csv("---.csv")
#print("second_data_sides_is {}".format(de.info()))
da = pd.read_csv("---.csv")
#print("third_data_sides_is {}".format(da.info()))

show = {}
show.update(df)
show.update(de)
show.update(da)
print(show)

data = pd.concat(show,axis=0)
t = str(df) + str(de) + str(da)
#print(hash(t))
try :
    P = re.compile(t)
    final = re.sub("\d","",P)
except re.error:
    pass
"""
print("first_data",df)
print("second_data",de)
print("third_data",da)
"""
show_one = pd.DataFrame(show)
#print(len(show_one))
"""
show_one.drop(type(show)=="int")
show.append(de)
"""

"""
print("first_data",df)
print("second_data",de)
print("third_data",da)
"""
"""
show.drop(type(show)=="int")
show.append(da)
show.drop(type(show)=="int")
"""

from wordcloud import WordCloud

mask = np.array(Image.open('mask.png'))
wordcloud = WordCloud(background_color='white',mask=mask,font_path="./ipagp.ttf",max_words=3000000000000000000000000000000,contour_color='black')

wordcloud.generate('\n'.join(show_one))
wordcloud.to_file('wordcloud_after.png')
