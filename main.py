from bs4 import BeautifulSoup
import mysql.connector
import datetime
import requests
import json
import time
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
    print('\033[1m' + "1"  + '\033[0m' + " -> database")
    print('\033[1m' + "2"  + '\033[0m' + " -> add new product")
    print('\033[1m' + "3"  + '\033[0m' + " -> update product track")
    print(" ")
    menu = input()

    if menu == '1':
        database()
    elif menu == '2':
        url_input()
    elif menu == '3':
        updatetrack()


def url_input():
    os.system('clear')

    def insertproductdatabase():
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM product")
        myresult = mycursor.fetchall()

        print(" ")
        print('\033[1m' + "bestaande producten:" + '\033[0m')
        for x in myresult:
            print(x)

        print(" ")
        print('\033[1m' + "Wil je dit product aan een bestaand product koppelen?" + '\033[0m')
        print('\033[1m' + "Zo ja type het id van het product of type 'no' als je een nieuwe wilt aanamken: ", end="" + '\033[0m')
        productid = input()

        try:
            val = int(productid)
            val = 'number'

            if val == 'number':
                try:
                    sql = "SELECT * FROM product WHERE id = %s"
                    val = (productid)
                    mycursor.execute(sql, (val,))
                    myresult = mycursor.fetchall()

                    for x in myresult:
                        print("product word toegevoegt aan:", x)
                except:
                    error = "Geen geldige id"
                    print(error)
                    time.sleep(2)
                    insertproductdatabase()

                sql = "INSERT INTO product_info (website, url, product) VALUES (%s, %s, %s)"
                val = (website, url, productid)
                mycursor.execute(sql, val)
                mydb.commit()
                id = mycursor.lastrowid
                print(mycursor.rowcount, "record inserted with id:", id)

                sql = "INSERT INTO product_track (product_info, price, stock, date) VALUES (%s, %s, %s, %s)"
                val = (id, input_price, stock, date.strftime("%Y-%m-%d"))
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")

                time.sleep(2)
                menu()
            else:
                error = "Geen geldige input"
                print(error)
                time.sleep(2)
                insertproductdatabase()

        except ValueError:
            if productid == 'no' or productid == 'NO' or productid == 'n':
                sql = "INSERT INTO product (name) VALUES (%s)"
                val = (name)
                mycursor.execute(sql, (val,))
                mydb.commit()
                id = mycursor.lastrowid
                print(mycursor.rowcount, "record inserted with id:", id)

                sql = "INSERT INTO product_info (website, url, product) VALUES (%s, %s, %s)"
                val = (website, url, id)
                mycursor.execute(sql, val)
                mydb.commit()
                id = mycursor.lastrowid
                print(mycursor.rowcount, "record inserted with id:", id)

                sql = "INSERT INTO product_track (product_info, price, stock, date) VALUES (%s, %s, %s, %s)"
                val = (id, input_price, stock, date.strftime("%Y-%m-%d"))
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")

                time.sleep(2)
                menu()
            else:
                error = "Geen geldige input"
                print(error)
                time.sleep(2)
                insertproductdatabase()

    print('\033[1m' + "exit by typing 'exit'" + '\033[0m')
    print('\033[1m' + "paste a product url: ", end="" + '\033[0m')
    url = input()

    if 'droneshop.nl/' in url:
        try:
            website = '1'
            print(" ")
            result = requests.get(url)
            doc = BeautifulSoup(result.content, "html.parser")
            lists = doc.find('div', class_="product-info-main col-sm-6 col-md-6 col-lg-6 col-xl-6")

            name = lists.find('span', class_="base").text
            input_price = lists.find('span', class_="price").text.replace(',', '.').replace(' ', '')
            stock = lists.find('div', title="Beschikbaarheid").text

            if 'Beschikbaarheid: Niet op voorraad' in stock:
                stock = 0
            else:
                stock = 1

            print("name: ", name)

            special_characters = ['€','$',' ']
            print("price:", input_price)
            for i in special_characters:
                input_price = input_price.replace(i,'')

            if stock == 0:
                print("stock: out of stock")
            else:
                print("stock: in stock")

            print(" ")
            print('\033[1m' + "you sure you want to add the", name, "to the database" + '\033[0m')
            print("yes/no: " , end="")
            yesorno = input()

            if yesorno == 'yes' or yesorno == 'YES' or yesorno == 'y':
                insertproductdatabase()
        except:
            error = "geen bruikbare link"
            print(error)
            time.sleep(2)
            url_input()
    elif 'getfpv.com/' in url:
        try:
            website = '2'
            print(" ")
            result = requests.get(url)
            doc = BeautifulSoup(result.content, "html.parser")
            lists = doc.find('div', class_="order-2 w-full mb-6 md:w-7/12 md:pl-5 lg:pl-10 md:py-6 lg:w-1/2 md:mb-0")

            name = lists.find('h1', class_="mb-3 text-3xl font-medium text-gray-900 title-font").text.replace('\n','').replace('        ', '').replace('     ', '')
            script = doc.find_all('script')[15].text.strip()[153:-2991]
            data = json.loads(script)
            input_price = data["Price"]
            stock = lists.find('p', class_="flex items-center align-middle available gap-x-2 stock").text.replace('\n','')
            if stock == 'Out of Stock':
                stock = 0
            else:
                stock = 1

            print("name:", name)

            special_characters = ['€','$',' ']
            print("price:", input_price)
            for i in special_characters:
                input_price = input_price.replace(i,'')

            if stock == 0:
                print("stock: out of stock")
            else:
                print("stock: in stock")

            print(" ")
            print('\033[1m' + "you sure you want to add the", name, "to the database" + '\033[0m')
            print("yes/no: " , end="")
            yesorno = input()

            if yesorno == 'yes' or yesorno == 'YES' or yesorno == 'y':
                insertproductdatabase()
            else:
                url_input()
        except:
            error = "geen bruikbare link"
            print(error)
            time.sleep(2)
            url_input()
    elif 'exit' in url:
        menu()
    else:
        error = "geen bruikbare link"
        print(error)
        time.sleep(2)
        url_input()

def database():
    os.system('clear')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM product")
    myresult = mycursor.fetchall()

    print(" ")
    print('\033[1m' + "bestaande producten:" + '\033[0m')
    for x in myresult:
        print(x)

    exit = input()

    if 'exit' in exit:
        menu()
    else:
        menu()

def updatetrack():
    exit = input()

    if 'exit' in exit:
        menu()
    else:
        menu()


menu()
