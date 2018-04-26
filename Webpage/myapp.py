from flask import Blueprint, render_template, flash, redirect, url_for, Flask
from flask_bootstrap import Bootstrap

from pyspark import SparkContext
from pyspark.sql import SQLContext
import pandas as pd

import findspark
findspark.init()

from pyspark.sql.session import SparkSession

sc =SparkContext.getOrCreate()
sqlContext = SQLContext(sc)
spark = SparkSession(sc)
books = sqlContext.read.load('books.csv', format = 'csv', header = True)

books.registerTempTable("df")

qry1 = sqlContext.sql("select title,authors,original_publication_year,language_code,average_rating from df order by average_rating DESC limit 10")
qr1 = qry1.toPandas()
qr1.columns = map(str.upper, qr1.columns)
qr1.index = qr1.index + 1

qry2 = sqlContext.sql("select title,authors,original_publication_year,language_code,average_rating from df order by ratings_count limit 10")
qr2 = qry2.toPandas()
qr2.columns = map(str.upper, qr2.columns)
qr2.index = qr2.index + 1

qry3 = sqlContext.sql("select title,authors,original_publication_year,language_code,average_rating from df where average_rating between 4 and 5 order by original_publication_year + 0 DESC limit 20")
qr3 = qry3.toPandas()
qr3.columns = map(str.upper, qr3.columns)
qr3.index = qr3.index + 1

qry4 = sqlContext.sql("select title,original_publication_year,language_code from df where authors = 'Suzanne Collins' order by original_publication_year + 0 DESC ")
qr4 = qry4.toPandas()
qr4.columns = map(str.upper, qr4.columns)
qr4.index = qr4.index + 1
	
app = Flask(__name__)
Bootstrap(app)
  
@app.route('/')
def index():
	
	q1= qr1.to_html()
	q2= qr2.to_html()
	q3= qr3.to_html()
	q4= qr4.to_html()
	return render_template('index.html', query1= q1, query2 = q2, query3 = q3, query4 = q4)
