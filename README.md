image-search
===========

###介绍

image-search是一个由兴趣而产生的基于opencv的python图片搜索引擎。

###功能

* face_search:是一个脸部图片搜索引擎。
* book_covers:是一个物品图片匹配引擎。

###使用

* face_search:$ python index.py --dataset dataset --index index.csv，生成index.csv文件，接着python search.py --index index.csv --query queries/108100.png --result-path dataset从index.csv获取与之对应的png文件根据相似度由大到小进行排序，输出图片。
* book_covers:$ python search.py --db books.csv --covers covers --query queries/query01.png即可从covers文件夹中匹配出相应的商品。
