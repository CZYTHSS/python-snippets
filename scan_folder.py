# -*- coding: utf-8 -*- 
import os 
def Test2(rootDir): 
    fout = open('result.sql','w+')
    for lists in os.listdir(rootDir): 
        path = os.path.join(rootDir, lists) 
        print path 
        if path.split('.')[1] == 'sql':
            fin = open(path,'r+')
            file = fin.read()
            fout.write(file)
        if os.path.isdir(path): 
            Test2(path)
    fout.close()


Test2("/home/mark/Desktop/Tables_MusicBrainz")
