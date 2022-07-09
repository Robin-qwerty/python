from bs4 import BeautifulSoup
import mysql.connector
import datetime
import requests
import os
import re

date = datetime.datetime.now()

mydb = mysql.connector.connect(
  host="localhost",
  user="pythonDB",
  password="qwerty",
  database="pythonDB"
)

def menu():
    os.system('clear')
    print('\033[1m' + "menu" + '\033[0m')
    print('\033[1m' + "1"  + '\033[0m' + " -> add new product")
    print('\033[1m' + "2"  + '\033[0m' + " -> add new product")
    print('\033[1m' + "3"  + '\033[0m' + " -> add new product")
    print('\033[1m' + "4"  + '\033[0m' + " -> add new product")
    print(" ")
    menu = input()

    if menu == '1':
        url_input()
    elif menu == '2':
        url_input()
    elif menu == '3':
        url_input()
    elif menu == '4':
        url_input()
    else:
        menu()

def url_input():
    os.system('clear')
    print('\033[1m' + "paste a product url: " , end="" + '\033[0m')
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
        print('\033[1m' + "you sure you want to add the", name, "to the database" + '\033[0m')
        print("yes/no: " , end="")
        yesorno = input()

        if yesorno == 'yes' or yesorno == 'YES' or yesorno == 'y':
            mycursor = mydb.cursor()
            sql = "INSERT INTO product (name) VALUES (%s)"
            val = (name)
            mycursor.execute(sql, (val,))
            mydb.commit()

            id = mycursor.lastrowid
            print(mycursor.rowcount, "record inserted with id:", id)

            mycursor = mydb.cursor()
            sql = "INSERT INTO product_track (shop, url, product, stock, date, price) VALUES (%s, %s, %s, %s, %s, %s)"
            val = ('droneshop', url, id, stock, date.strftime("%Y-%m-%d"), input_price)
            mycursor.execute(sql, val)
            mydb.commit()

            print(mycursor.rowcount, "record inserted.")
        else:
            url_input()
    else:
        error = "geen geldige link"
        print(error)
        url_input()

menu()
