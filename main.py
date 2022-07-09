from bs4 import BeautifulSoup
import mysql.connector
import datetime
import requests
import os
import re

os.system('clear')

date = datetime.datetime.now()

mydb = mysql.connector.connect(
  host="localhost",
  user="pythonDB",
  password="qwerty",
  database="pythonDB"
)

def url_input():
    print("paste a product url: " , end="")
    url = input()

    if 'droneshop.nl/' in url:
        print(" ")
        result = requests.get(url)
        doc = BeautifulSoup(result.content, "html.parser")
        lists = doc.find('div', class_="product-info-main col-sm-6 col-md-6 col-lg-6 col-xl-6")

        name = lists.find('span', class_="base").text
        input_price = lists.find('span', class_="price").text.replace(',', '.').replace(' ', '')
        try:
            lists.find('div', class_="stock available").text
            stock = 1
        except:
            stock = 0

        print("name: ", name)

        special_characters = ['€','$',' ']
        print("price:", input_price)
        for i in special_characters:
            input_price = input_price.replace(i,'')

        if stock == '0':
            print("stock: out of stock")
        else:
            print("stock: in stock")

        print(" ")
        print("you sure you want to at the", name, "to the database")
        print("yes/no: " , end="")
        yesorno = input()

        if yesorno == 'yes' or yesorno == 'YES' or yesorno == 'y':
            mycursor = mydb.cursor()
            sql = "INSERT INTO product (url, name, stock) VALUES (%s, %s, %s)"
            val = (url, name, stock)
            mycursor.execute(sql, val)
            mydb.commit()

            id = mycursor.lastrowid
            print(mycursor.rowcount, "record inserted with id:", id)

            mycursor = mydb.cursor()
            sql = "INSERT INTO product_track (product, date, price) VALUES (%s, %s, %s)"
            val = (id, date.strftime("%Y-%m-%d"), input_price)
            mycursor.execute(sql, val)
            mydb.commit()

            print(mycursor.rowcount, "record inserted.")
        else:
            url_input()
    else:
        error = "geen geldige link"
        print(error)
        url_input()

url_input()
