# from pymongo import MongoClient
# import datetime
# client = MongoClient("mongodb+srv://Azashax:Azamat007sh@cluster0.b4qqa.mongodb.net/data?retryWrites=true&w=majority")
# db = client["data"]
# collection1 = db["test"]
# collection2 = db["test2"]
#
#
# class ATM:
#
#     def registration(self):
#
#         name = input("name:")
#         surname = input("surname:")
#         bank_card = int(input("bank_card:"))
#         pin_cod = int(input("pin_cod:"))
#         balance = int(input("balance:"))
#         a = [
#             {
#                "name": name,
#                "surname": surname,
#                "bank_card": bank_card,
#                "pin_cod": pin_cod,
#                "balance": balance
#             }
#             ]
#         if collection1.count_documents({"bank_card": bank_card}) == 0:
#             collection1.insert_many(a)
#
#     def balancec(self):
#         xxx = collection1.find_one({"bank_card": bank_kard1})["balance"]
#         print(xxx)
#
#     def deposit_money(self):
#         vnest = float(input("Введите сумму для депозита:"))
#         q = datetime.datetime.now()
#         t1 = [{
#             "name": collection1.find_one({"bank_card": bank_kard1})["name"],
#             "surname": collection1.find_one({"bank_card": bank_kard1})["surname"],
#             "карта": bank_kard1,
#             "Внесенная сумма:": vnest,
#             "время": q,
#         }]
#         collection2.insert_many(t1)
#         balance123 = collection1.find_one({"bank_card": bank_kard1})["balance"]
#         collection1.update_many({'bank_card': bank_kard1}, {"$set": {"balance": balance123 + vnest}})
#
#         print(f"Внесенная сумма:{vnest}")
#
#     def cash_withdrawal(self):
#         snyatt = float(input("Введите сумму вывода:"))
#         print("Комиссия 1%")
#
#         if collection1.find_one({"bank_card": bank_kard1})["balance"] >= snyatt*1.01:
#             q = datetime.datetime.now()
#             t2 = [{
#                      "name": collection1.find_one({"bank_card": bank_kard1})["name"],
#                      "surname": collection1.find_one({"bank_card": bank_kard1})["surname"],
#                      "карта": bank_kard1,
#                      "вы сняли:": snyatt,
#                      "время": q,
#                 }]
#             collection2.insert_many(t2)
#             balance123 = collection1.find_one({"bank_card": bank_kard1})["balance"]
#             collection1.update_many({'bank_card': bank_kard1}, {"$set": {"balance": balance123 - snyatt*1.01}})
#             print(f"Вы сняли:{snyatt*1.01}")
#
#         else:
#             print("Не хватает денег!!!")
#
#     def Send_money(self):
#         karta = int(input("Введите Банковский аккаунт получателя карты:"))
#         otpp = float(input("Введите сумму отправки:"))
#         print("Комиссия 1%")
#         if collection1.find_one({"bank_card": bank_kard1})["balance"] >= otpp * 1.01:
#             q = datetime.datetime.now()
#             t3 = [{
#                 "name": collection1.find_one({"bank_card": bank_kard1})["name"],
#                 "surname": collection1.find_one({"bank_card": bank_kard1})["surname"],
#                 "karta": bank_kard1,
#                 "карта получателя": karta,
#                 "время": q,
#                 "вы отправили :": otpp
#
#                 }]
#             collection2.insert_many(t3)
#             balance123 = collection1.find_one({"bank_card": bank_kard1})["balance"]
#             balance124 = collection1.find_one({"bank_card": karta})["balance"]
#             collection1.update_many({'bank_card': bank_kard1}, {"$set": {"balance": balance123 - otpp * 1.01}})
#             collection1.update_many({'bank_card': karta}, {"$set": {"balance": balance124 + otpp}})
#
#         else:
#             print("Не хватает денег!!!")
#
#     def delete(self):
#         collection1.delete_many({})
#         collection2.delete_many({})
#
#
# t = ATM()
#
#
# print("Добро пожаловать в банкомат Академии")
# print("выберите операцию который вы хотите сделать")
#
#
# while 1:
#     print("""1. регистрация
# 2. войти в акаунт
# 3. удалить всё
# """)
#     choose = int(input(":"))
#     if choose == 1:
#         t.registration()
#     elif choose == 2:
#         bank_kard1 = int(input("karta:"))
#         password = int(input("pin:"))
#         if collection1.count_documents({"bank_card": bank_kard1}) == 1 and collection1.count_documents({"pin_cod":  password}) == 1:
#             while 1:
#
#                 print("""1. просмотр баланса
# 2. внесение денег
# 3. снятие денег
# 4. отправка денег
# 5. Завершить оперaцию""")
#
#                 x = int(input("Введите:"))
#
#                 if x == 1:
#                     t.balancec()
#
#                 elif x == 2:
#                     t.deposit_money()
#
#                 elif x == 3:
#                     t.cash_withdrawal()
#
#                 elif x == 4:
#                     t.Send_money()
#
#                 elif x == 5:
#                     print("Спасибо за выбор банкомат Академии")
#                     break
#
#                 else:
#                     continue
#
#         else:
#             continue
#     elif choose == 3:
#         t.delete()

































# problem 2


# from pymongo import MongoClient
# import datetime
#
# client = MongoClient(
#     "mongodb+srv://Azashax:Azamat007sh@cluster0.b4qqa.mongodb.net/testdata?retryWrites=true&w=majority")
# db = client["testdata"]
# collection1 = db["chek"]
# collection3 = db["notforyou"]
# collection4 = db["products"]
# collection2 = db["users"]
#
# collection1.delete_many({})
# collection2.delete_many({})
# collection3.delete_many({})
# collection4.delete_many({})
# aa = [
#     {
#         "fullname": "Sh",
#         "name": "Azamat",
#         "Login": 1234,
#         "password": 1234,
#         "balance": 0,
#     }
# ]
# collection3.insert_many(aa)
#
#
# class OnlineShop:
#
#     def welcome(self):
#         print('Выберите операцию которую вы хотите сделать:')
#         print('1. Просмотр баланса')
#         print('2. Пополнить баланс')
#         print('3. Начать покупку')
#         print('4. Корзина')
#         print('5. Очистить корзину')
#         print('0. выход')
#
#     def registration(self):
#         fullname = str(input('Введите имя и фамилию:'))
#         login = str(input('Введите логин:'))
#         password = str(input('Введите пароль:'))
#         user = [
#             {
#                 'Fullname': fullname,
#                 'Login': login,
#                 'Password': password,
#                 'Balance': 0
#             }
#         ]
#         collection2.insert_many(user)
#         print('Запись успешно зарегестрированна!')
#
#     def sign_in(self):
#         Login1 = str(input('Введите логин:'))
#         Password1 = str(input('Введите пароль:'))
#         if collection2.count_documents({"Login": Login1}) == 1 and collection2.count_documents(
#                 {"Password": Password1}) == 1:
#             while True:
#                 t.welcome()
#                 opetarion = int(input(':'))
#                 xxx1 = collection2.find_one({"Login": Login1})["Balance"]
#                 if opetarion == 1:
#                     print('Ваш баланс', xxx1)
#                 elif opetarion == 2:
#                     deposit = int(input('Введите сумму пополнения:'))
#                     collection2.update_one({"Login": Login1}, {'$inc': {"Balance": deposit}})
#                     print('Баланс успешно пополнен!')
#                 elif opetarion == 3:
#                     print('Выберите товар:')
#                     while True:
#                         for x in collection4.find():
#                             print('id:', x['_id'], ',', 'Название:', x['Product'], ',', 'количество:', x['Quantity'],
#                                   ',', 'Цена:', x['Prise'])
#                         chose_product = int(input('Выберите id товара: '))
#                         if collection4.count_documents({'_id': chose_product}) == 0:
#                             print('Такого товара не существует!')
#                             break
#                         else:
#                             price = collection4.find_one({'_id': chose_product})['Prise']
#                             name_product = collection4.find_one({'_id': chose_product})['Product']
#                             quantity = int(input('Количество:'))
#                             over_all = quantity * price
#                             xxx = collection2.find_one({"Login": Login1})["Balance"]
#                             rrr = collection4.find_one({'_id': chose_product})['Quantity']
#                             if over_all > xxx and quantity < rrr:
#                                 print('Недостаточно средств!')
#                                 break
#                             else:
#                                 collection2.update_one({"Login": Login1}, {'$inc': {"Balance": -over_all}})
#                                 collection4.update_one({"_id": chose_product}, {'$inc': {"Quantity": -quantity}})
#
#                                 q = datetime.datetime.now()
#                                 check_list = [
#                                     {
#                                         'Product': name_product,
#                                         'Quantity': quantity,
#                                         'Prise': over_all,
#                                         'время': q
#                                     }
#                                 ]
#                                 collection1.insert_many(check_list)
#                                 print("Успешно добавлено в корзину!")
#                                 return
#                 elif opetarion == 4:
#
#                     for zz in collection1.find():
#                         print('Название:', zz['Product'], ',', 'Количество:', zz['Quantity'], ',', 'Цена:', zz['Prise'],
#                               ',', 'Цена:', zz['Prise'])
#                 elif opetarion == 5:
#                     collection1.delete_many({})
#                 elif opetarion == 0:
#                     break
#
#         else:
#             print('Такой записи не существует, зарегестрируйтесь!')
#
#     def sign_in_how_admin(self):
#         Login_admin = int(input('Введите логин:'))
#         Password_admin1 = int(input('Введите пароль:'))
#         if collection3.find_one()['Login'] == Login_admin and collection3.find_one()['password'] == Password_admin1:
#             while True:
#                 print('Выберите функцию которую вы хотите сделать:')
#                 print('1. Изменить данные пользователя')
#                 print('2. Удалить данные пользователя')
#                 print('3. Добавление продукта')
#                 print('4. Изменить данные продукта')
#                 print('5. Удалить данные продукта')
#                 print('6. Удаление всех данных')
#                 print('7. добавит количество продукта')
#                 print('0. Выход')
#                 chose = int(input('Выберите операцию которую вы хотите сделать:'))
#                 if chose == 1:
#                     login_user = (input('Введите логин:'))
#                     password_user = (input('Введите пароль:'))
#                     print('Выберите что вы хотите изменить:')
#                     print('1. Логин')
#                     print('2. Пароль')
#                     ch = int(input(':'))
#                     if ch == 1:
#                         if collection2.count_documents({"Login": login_user}) == 0 and collection2.count_documents(
#                                 {"Password": password_user}) == 0:
#                             print('Такой записи не существует!')
#                         else:
#                             new_login = input('Введите новый логин:')
#                             collection2.update_one({'Password': password_user}, {'$set': {'Login': new_login}})
#                             print('Учетная запись успешно изменена!')
#                     elif ch == 2:
#                         if collection2.count_documents({"Login": login_user}) == 0 and collection2.count_documents(
#                                 {"Password": password_user}) == 0:
#                             print('Такой записи не существует!')
#                         else:
#                             new_password = input('Введите новый пароль:')
#                             collection2.update_one({'Login': login_user}, {'$set': {'Password': new_password}})
#                             print('Учетная запись успешно изменена!')
#                 elif chose == 2:
#                     login_user = (input('Введите логин:'))
#                     password_user = (input('Введите пароль:'))
#                     if collection2.count_documents({"Login": login_user}) == 0 and collection2.count_documents(
#                             {"Password": password_user}) == 0:
#                         print('Такой записи не существует!')
#                     else:
#                         collection2.delete_one({'Login': login_user, 'Password': password_user})
#                         print('Учетная запись успешно удалена!')
#                 elif chose == 3:
#                     id = int(input('id:'))
#                     name_product = input('Введите название товара:')
#                     price = int(input('Цена:'))
#                     Quantity = int(input("количество"))
#                     product = [
#                         {
#                             '_id': id,
#                             'Product': name_product,
#                             'Prise': price,
#                             'Quantity': Quantity,
#                         }
#                     ]
#                     if collection4.count_documents({'_id': id}) == 0:
#                         collection4.insert_many(product)
#                         print('Товар успешно добавлен!')
#                     else:
#                         print("такой id уже существует  ")
#                 elif chose == 4:
#                     find_id = int(input('Введите ID товара: '))
#                     if collection4.count_documents({'_id': find_id}) == 1:
#                         print('Что вы хотите изменить?')
#                         print('1. Название продукта')
#                         print('2. Цену продукта')
#                         change_point = int(input(':'))
#                         if change_point == 1:
#                             new_title = input('Введите новое название товара: ')
#                             collection4.update_many({'_id': find_id}, {'$set': {'Product': new_title}})
#                             print('Успешно изменено!')
#                         else:
#                             new_prise = int(input('Введите новую цену:'))
#                             collection4.update_many({'_id': find_id}, {'$set': {'Prise': new_prise}})
#                             print('Успешно изменено!')
#                     else:
#                         print('Такого продукта не существует!')
#                         break
#                 elif chose == 5:
#                     find_id = int(input('Введите ID товара: '))
#                     if collection4.count_documents({'_id': find_id}) == 1:
#                         collection4.delete_one({'_id': find_id})
#                         print('Товар успешно удален!')
#                     else:
#                         print('Такого товара не существует!')
#                 elif chose == 6:
#                     collection1.delete_many({})
#                     collection2.delete_many({})
#                     collection4.delete_many({})
#                     print('Успешно удаленно!')
#                 elif chose == 7:
#                     id1 = int(input('id:'))
#                     Quantity1 = int(input("количество:"))
#                     if collection4.find_one()['_id'] == 0:
#                         collection4.update_one({"_id": id1}, {'$inc': {"Quantity": Quantity1}})
#                     else:
#                         print("Такого товара не существует!")
#                 elif chose == 0:
#                     return
#         else:
#             print('Такой записи не существует!')
#
# t = OnlineShop()
#
# print('Добро пожаловать!')
# while True:
#     print('Выберите операцию которую вы хотите сделать:')
#     print('1. Регистрация')
#     print('2. Войти')
#     print('3. Вход как администратор')
#     choose = int(input(':'))
#     if choose == 1:
#         t.registration()
#     elif choose == 2:
#         t.sign_in()
#     elif choose == 3:
#         t.sign_in_how_admin()
