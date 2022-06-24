import os
import pandas as pd

data = [dict(name='file1', filepath='S:/Raj_Old_SDrive/A73517468 1.pdf'),
    dict(name='file2', filepath='doc/1907012019I95414092.pdf')]

df = pd.DataFrame(data)

def make_clickable(url):
    name= os.path.basename(url)
    return '<a href="{}">{}</a>'.format(url,name)

df.style.format({'filepath': make_clickable})