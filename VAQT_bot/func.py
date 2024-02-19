from telebot import types

#BURGER
def Burger():
    global bur_kol, bur_ord, bur_sum_pr, price_bur#, bur_list
    #bur_list=["min","pls","add_kar"]
    price_bur=13
    bur_ord="🍔 Чикен-Бургер"
    bur_sum_pr=price_bur*bur_kol
    
    #photo=open("chicken_bur.jpg", "rb")
    #b.send_photo(chat_id, photo)
    mar=types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    one=types.KeyboardButton("1")
    two=types.KeyboardButton("2")
    three=types.KeyboardButton("3")
    four=types.KeyboardButton("4")
    five=types.KeyboardButton("5")
    six=types.KeyboardButton("6")
    seven=types.KeyboardButton("7")
    eghit=types.KeyboardButton("8")
    nine=types.KeyboardButton("9")
    back=types.KeyboardButton("⬅️ назад")
    #zero=types.KeyboardButton("0")
    kar=types.KeyboardButton("📥 Карзина")
    mar.add(one,two,three,four,five,six,seven,eghit,nine,back,kar)

    return mar
