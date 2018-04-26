# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 11:51:43 2018

@author: blrni
"""
from pyspark import SparkContext
from pyspark.sql import SQLContext

import findspark
findspark.init()

from pyspark.sql.session import SparkSession
sc =SparkContext.getOrCreate()
sqlContext = SQLContext(sc)
spark = SparkSession(sc)
books = sqlContext.read.load('books.csv', format = 'csv', header = True)

books.registerTempTable("df")


qry1 = sqlContext.sql("select * from df where book_id = 3")
qry1.show()

qry2 = sqlContext.sql("select authors,original_publication_year,title,language_code,average_rating from df order by average_rating DESC limit 10")
qry2.show()

qry3 = sqlContext.sql("select authors,original_publication_year,title,language_code,average_rating from df order by average_rating limit 10")
qry3.show()

qry4 = sqlContext.sql("select title,original_publication_year,language_code,authors from df where authors = 'Suzanne Collins' order by original_publication_year + 0 DESC ")
qry4.show()

qry5 = sqlContext.sql("select title,original_publication_year,language_code,authors,average_rating from df order by ratings_count limit 10")
qry5.show()

qry6 = sqlContext.sql("select title,original_publication_year,language_code,authors,average_rating from df where average_rating between 4 and 5 order by original_publication_year + 0 DESC ")
qry6.show()

qry7 = sqlContext.sql("select title,original_publication_year,language_code,authors,work_text_reviews_count from df order by work_text_reviews_count + 0 DESC limit 10")
qry7.show()
