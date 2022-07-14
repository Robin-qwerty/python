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
    print('\033[1m' + "menu" + '\033[0m' + " type 1, 2 or 3")
    print('\033[1m' + "1"  + '\033[0m' + " -> database")
    print('\033[1m' + "2"  + '\033[0m' + " -> add new product")
    print('\033[1m' + "3"  + '\033[0m' + " -> update product track")
    print('\033[1m' + "exit"  + '\033[0m' + " -> exit program")
    print(" ")
    menu = input()

    if menu == '1':
        database()
    elif menu == '2':
        url_input()
    elif menu == '3':
        updatetrack()
    elif menu == '3':
        quit()


def url_input():
    os.system('clear')

    def insertproductdatabase():
        mycursor = mydb.cursor()
        mycursor.execute("SELECT product.id, product.name, brand.brand_name FROM product INNER JOIN brand ON brand.id = product.brand")
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
                sql = "SELECT product.id, product.name, brand.brand_name FROM product INNER JOIN brand ON brand.id = product.brand WHERE product.id = %s"
                val = (productid)
                mycursor.execute(sql, (val,))
                myresult = mycursor.fetchall()

                for x in myresult:
                    if x == None:
                        error = "not a usable id"
                        print(error)
                        time.sleep(2)
                        insertproductdatabase()
                    else:
                        print("product word toegevoegt aan:", x)

                sql = "INSERT INTO product_info (website, url, product) VALUES (%s, %s, %s)"
                val = (website, url, productid)
                mycursor.execute(sql, val)
                mydb.commit()
                id = mycursor.lastrowid
                print(mycursor.rowcount, "record inserted with id:", id)

                sql = "INSERT INTO product_track (product_info, price, price_usd, price_pounds, stock, date) VALUES (%s, %s, %s, %s, %s, %s)"
                val = (id, input_price, price_usd, price_pounds, stock, date.strftime("%Y-%m-%d"))
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")

                time.sleep(2)
                menu()
            else:
                error = "not a usable input"
                print(error)
                time.sleep(2)
                insertproductdatabase()

        except ValueError:
            if productid == 'no' or productid == 'NO' or productid == 'n':
                mycursor = mydb.cursor()
                mycursor.execute("SELECT * FROM brand")
                myresult = mycursor.fetchall()

                for x in myresult:
                    print(x)

                print("Type the ID of an existing brand or type the name of a new brand: ", end="")
                brand = input()

                try:
                    val = int(brand)
                    val = 'number'

                    if val == 'number':
                        sql = "SELECT id, brand_name FROM brand WHERE id = %s"
                        val = (brand)
                        mycursor.execute(sql, (val,))
                        myresult = mycursor.fetchall()

                        for x in myresult:
                            if x == None:
                                error = "not a usable id"
                                print(error)
                                time.sleep(2)
                                insertproductdatabase()
                            else:
                                print("product word toegevoegt aan:", x)

                        sql = "INSERT INTO product (name, brand) VALUES (%s, %s)"
                        val = (name, brand)
                        mycursor.execute(sql, val)
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
                except ValueError:
                    sql = "INSERT INTO brand (brand_name) VALUES (%s)"
                    val = (brand)
                    mycursor.execute(sql, (val,))
                    mydb.commit()
                    id = mycursor.lastrowid
                    print(mycursor.rowcount, "record inserted with id:", id)

                    sql = "INSERT INTO product (name, brand) VALUES (%s, %s)"
                    val = (name, id)
                    mycursor.execute(sql, val)
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
                error = "not a usable input"
                print(error)
                time.sleep(2)
                insertproductdatabase()

    print('\033[1m' + "exit by typing 'exit'" + '\033[0m')
    print('\033[1m' + "paste a product url: ", end="" + '\033[0m')
    url = input()

    price_usd = None
    price_pounds = None

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
            error = "no usable link"
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

            price_usd = input_price
            input_price = float(input_price) * 0.993
            input_price = float(round(input_price, 2))
            print("price:", input_price)
            print("price in usd: ", price_usd)

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
            error = "no usable link"
            print(error)
            time.sleep(2)
            url_input()
    elif 'airjacker.com/products/' in url:
        try:
            website = '3'
            print(" ")
            result = requests.get(url)
            doc = BeautifulSoup(result.content, "html.parser")
            lists = doc.find('div', id="ProductInfo-template--14434326741090__main")

            name = lists.find('h1', class_="product__title").text.replace('\n','').replace('              ', '').replace('            ', '')
            input_price = lists.find('span', class_="price-item price-item--regular").text

            try:
                lists.find('button', name_="add")
                stock = 1
            except:
                stock = 0

            print("name:", name)

            special_characters = ['€','$','£',' ']
            for i in special_characters:
                input_price = input_price.replace(i,'')

            price_pounds = input_price
            input_price = float(input_price) * 1.18
            input_price = float(round(input_price, 2))
            print("price:", input_price)
            print("price in pounds: ", price_pounds)

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
            error = "no usable link"
            print(error)
            time.sleep(2)
            url_input()
    elif 'yourfpv.co.uk/product/' in url:
        try:
            website = '4'
            print(" ")
            result = requests.get(url)
            doc = BeautifulSoup(result.content, "html.parser")
            lists = doc.find('div', class_="product-info summary col-fit col entry-summary product-summary text-left form-minimal")

            name = lists.find('h1', class_="product-title product_title entry-title").text.replace('\n','').replace('', '').replace('', '')
            input_price = lists.find('bdi').text

            try:
                stock = lists.find('p', class_="stock in-stock").text
                stock = 1
            except:
                stock = 0

            print("name:", name)

            special_characters = ['€','$','£',' ']
            for i in special_characters:
                input_price = input_price.replace(i,'')

            price_pounds = input_price
            input_price = float(input_price) * 1.18
            input_price = float(round(input_price, 2))
            print("price:", input_price)
            print("price in pounds: ", price_pounds)

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
            error = "no usable link"
            print(error)
            time.sleep(2)
            url_input()
    elif 'unmannedtechshop.co.uk/product/' in url:
        try:
            website = '5'
            print(" ")
            result = requests.get(url)
            doc = BeautifulSoup(result.content, "html.parser")
            lists = doc.find('div', class_="product-info summary col-fit col entry-summary product-summary text-left form-minimal")

            name = lists.find('h1', class_="product-title product_title entry-title").text.replace('\n','').replace('', '').replace('', '')
            input_price = lists.find('bdi').text

            try:
                lists.find('p', class_="stock out-of-stock")
                stock = 0
            except:
                stock = 1

            print("name:", name)

            special_characters = ['€','$','£',' ']
            for i in special_characters:
                input_price = input_price.replace(i,'')

            price_pounds = input_price
            input_price = float(input_price) * 1.18
            input_price = float(round(input_price, 2))
            print("price:", input_price)
            print("price in pounds: ", price_pounds)

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
            error = "no usable link"
            print(error)
            time.sleep(2)
            url_input()
    elif 'hobbyrc.co.uk/' in url:
        try:
            website = '6'
            print(" ")
            result = requests.get(url)
            doc = BeautifulSoup(result.content, "html.parser")
            lists = doc.find('div', class_="overview")

            name = lists.find('div', class_="product-name").text.replace('\n','').replace('', '').replace('', '')
            input_price = lists.find('div', class_="product-price").text.replace(' inc VAT ','')
            stock = lists.find('button', type="button").text

            if 'Notify me when available' in stock:
                stock = 0
            else:
                stock = 1

            print("name:", name)

            special_characters = ['€','$','£',' ']
            for i in special_characters:
                input_price = input_price.replace(i,'')

            price_pounds = input_price
            input_price = float(input_price) * 1.18
            input_price = float(round(input_price, 2))
            print("price:", input_price)
            print("price in pounds: ", price_pounds)

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
            error = "no usable link"
            print(error)
            time.sleep(2)
            url_input()
    elif 'exit' in url:
        menu()
    elif 'x' in url:
        menu()
    else:
        error = "no usable link"
        print(error)
        time.sleep(2)
        url_input()

def database():
    os.system('clear')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT product.id, product.name, brand.brand_name FROM product INNER JOIN brand ON brand.id = product.brand")
    myresult = mycursor.fetchall()

    print('\033[1m' + "bestaande producten:" + '\033[0m')
    for x in myresult:
        print(x)

    print(" ")
    print("type an id to see more or 'exit' to exit: ", end="")
    input_id = input()

    if 'exit' in input_id:
        menu()
    elif 'x' in input_id:
        menu()
    else:
        try:
            val = int(input_id)
            val = 'number'

            if val == 'number':
                try:
                    print(" ")
                    sql = "SELECT product_info.id, product_info.url, website.website FROM product_info INNER JOIN website ON website.id = product_info.website WHERE product_info.product = %s"
                    val = (input_id)
                    mycursor.execute(sql, (val,))
                    myresult = mycursor.fetchall()

                    for x in myresult:
                        print(x)

                    print(" ")
                    print("type an id to see more or 'exit' to exit: ", end="")
                    input_id = input()

                    if 'exit' in input_id:
                        menu()
                    elif 'x' in input_id:
                        menu()
                    else:
                        try:
                            val = int(input_id)
                            val = 'number'

                            if val == 'number':
                                try:
                                    print(" ")
                                    sql = "SELECT product_track.id, product_track.price, product_track.stock, product_track.date FROM product_track INNER JOIN product_info ON product_info.id = product_track.product_info WHERE product_track.product_info = %s"
                                    val = (input_id)
                                    mycursor.execute(sql, (val,))
                                    myresult = mycursor.fetchall()

                                    for x in myresult:
                                        print(x)

                                    print(" ")
                                    print("type 'exit' to exit: ", end="")
                                    input_id = input()
                                    database()
                                except:
                                    error = "not a usable id"
                                    print(error)
                                    time.sleep(2)
                                    database()
                        except:
                            error = "not a usable id"
                            print(error)
                            time.sleep(2)
                            database()

                except:
                    error = "not a usable id"
                    print(error)
                    time.sleep(2)
                    database()

        except:
            database()

def updatetrack():
    os.system('clear')

    exit = input()

    if 'exit' in input_id:
        menu()
    elif 'x' in input_id:
        menu()
    else:
        menu()


menu()
