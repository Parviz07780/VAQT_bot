import telebot, random, time
from telebot import types
from Menu import Burger15


token="6922316840:AAEuwjMHDa2ZyVSaEfiZ3hYmH8h0exVJ060"
b=telebot.TeleBot(token)

admin=1879819895

back_from_place=False
back_edor=False
back_izbr=0
hz=0
back_menu=0
cont=False

messid_mak4=0
messid_mir=0
messid_uni=0
menu_mess_id=0

language="ru"
integer=123
string="str"

ol=0
g_w=False

del_order=0
write_adres=0
"""
message.from_user.id
message.from_user.first_name
message.from_user.last_name
message.from_user.username
"""

inst_show=""
instr=""

choice_001=""
choice_002=""
choice_003=""
choice_004=""




kril001=""
bur1_ord=""
Zakaz_index=0
fri1_ord=""
fri_index=0
strip_pr1_ord=""
strip_pr_index=0
kril_pr1_ord=""
kril_pr_index=0
strip_kg1_ord=""
strip_kg_index=0
kril_kg1_ord=""
kril_kg_index=0
kombo251_ord=""
kombo25_index=0
kombo351_ord=""
kombo35_index=0



ZAKAZ=""
karzina=""
otp_zakaz=0
chisla_kril=""

order=""
orders=[]
price=0
pay_way=""
place=""
get_way=""
Time=""
adres=""
contact=0
order_story=[]
id_order=random.randint(1000,9999)

pay_ways=["DC", "Alif", "Эсхата", "Наличные"]
places=["ул.Мир","Универмаг","Школа№4"]



bur_kol=1
bur_ord=""
price_bur=13

bur15_kol=1
bur15_ord="🍔 Чикен-Бургер-15см"
price_bur15=15

fri_kol=1
fri_ord="🍟 Фри"
price_fri=8

bul_kol=1
bul_ord="🍞 Булочка-2.5см"
price_bul=2.5

strip_pr_kol=1
strip_pr_ord="🍗 Стрипсы 1пр(250гр)-20см"
price_strip_pr=20

kril_pr_kol=1
kril_pr_ord="🍗 Крылышки 1пр(250гр)-20см"
price_kril_pr=20

strip_kg_kol=1.0
strip_kg_ord="🍗 Стрипсы(1кг)-75см"
price_strip_kg=75

kril_kg_kol=1.0
kril_kg_ord="🍗 Крылышки(1кг)-75см"
price_kril_kg=75

kombo25_kol=1
kombo25_ord="🍗🥤 Комбо 3в1-25см"
price_kombo25=25

kombo35_kol=1
kombo35_ord="🍗🥤 Комбо 5в1-35см"
price_kombo35=35

mm1=0

cof_ord="☕️ Кофе"
cof_kol=1
cof_sum_pr=0
price_cof=3

#coca cola
cc03_ord=""
cc03_kol=1
price_cc03=3
cc03_sum_pr=0

cc05_ord="🥤 Coca Cola 0.5"
cc05_kol=1
cc05_sum_pr=0
price_cc05=5

cc125_ord="🥤 Coca Cola 1.25"
cc125_kol=1
cc125_sum_pr=0
price_cc125=10

cc175_ord="🥤 Coca Cola 1.75"
cc175_kol=1
cc175_sum_pr=0
price_cc175=12

#fanta
fan03_ord="🍊 Fanta 0.3"
fan03_kol=1
fan03_sum_pr=0
price_fan03=3

fan05_ord="🍊 Fanta 0.5"
fan05_kol=1
fan05_sum_pr=0
price_fan05=5

fan125_ord="🍊 Fanta 1.25"
fan125_kol=1
fan125_sum_pr=0
price_fan125=10

fan175_ord="🍊 Fanta 1.75"
fan175_kol=1
fan175_sum_pr=0
price_fan175=12

#Fuse tea
ftea05_ord="🫖 Fuse-tea 0.5"
ftea05_kol=1
ftea05_sum_pr=0
price_ftea05=5

#El-Rio
rio_man_ord="🥭 El-Rio mango"
rio_man_kol=1
rio_man_sum_pr=0
price_rio_man=7

#Sprite

spr1_ord="🍋 Sprite 1"
spr1_kol=1
spr1_sum_pr=0
price_spr1=10

#RC cola

rc1_ord="🥤 RC cola 1"
rc1_kol=1
rc1_sum_pr=0
price_rc1=8

#Bon_aqua
bon05_ord="🧊 Bon-aqua 0.5"
bon05_kol=1
bon05_sum_pr=0
price_bon05=3

bon1_ord="🧊 Bon-aqua 1"
bon1_kol=1
bon1_sum_pr=0
price_bon1=4

bon15_ord="🧊 Bon-aqua 1.5"
bon15_kol=1
bon15_sum_pr=0
price_bon15=5

#Соусы
ostri_s_ord="🌶 Острый соус"
ostri_s_kol=1
ostri_s_sum_pr=0
price_ostri_s=2

chesn_s_ord="🧄 Чесночный соус"
chesn_s_kol=1
chesn_s_sum_pr=0
price_chesn_s=2

sirni_s_ord="🧀 Сырный соус"
sirni_s_kol=1
sirni_s_sum_pr=0
price_sirni_s=2
#####################

#BACK TO MENU
bur_foto=""
BUR_message=""

bur15_foto=""
BUR15_message=""

fri_foto=""
FRI_message=""

bul_foto=""
BUL_message=""

strip_pr_foto=""
strip_pr_message=""

kril_pr_foto=""
kril_pr_message=""

strip_kg_foto=""
strip_kg_message=""

kril_kg_foto=""
kril_kg_message=""

kombo25_foto=""
kombo25_message=""

kombo35_foto=""
kombo35_message=""

chesn_s_foto=""
chesn_s_message=""

ostri_s_foto=""
ostri_s_message=""

sirni_s_foto=""
sirni_s_message=""

cof_foto=""
cof_message=""

cc05_foto=""
cc05_message=""

cc125_foto=""
cc125_message=""

cc175_foto=""
cc175_message=""

fan05_foto=""
fan05_message=""

fan125_foto=""
fan125_message=""

fan175_foto=""
fan175_message=""

rc1_foto=""
rc1_message=""

spr1_foto=""
spr1_message=""

rio_man_foto=""
rio_man_message=""

ftea05_foto=""
ftea05_message=""

bon05_foto=""
bon05_message=""

bon1_foto=""
bon1_message=""

bon15_foto=""
bon15_message=""



#Edit
bur_eddd=False
BUR_del=""

bur15_eddd=False
BUR15_del=""

fri_eddd=False
FRI_del=""

bul_eddd=False
bul_del=""

strip_pr_eddd=False
strip_pr_del=""

kril_pr_eddd=False
kril_pr_del=""

strip_kg_eddd=False
strip_kg_del=""

kril_kg_eddd=False
kril_kg_del=""

kombo25_eddd=False
kombo25_del=""

kombo35_eddd=False
kombo35_del=""

chesn_s_eddd=False
chesn_s_del=""

ostri_s_eddd=False
ostri_s_del=""

sirni_s_eddd=False
sirni_s_del=""

cof_eddd=False
cof_del=""

cc05_eddd=False
cc05_del=""

cc125_eddd=False
cc125_del=""

cc175_eddd=False
cc175_del=""

fan05_eddd=False
fan05_del=""

fan125_eddd=False
fan125_del=""

fan175_eddd=False
fan175_del=""

rc1_eddd=False
rc1_del=""

spr1_eddd=False
spr1_del=""

rio_man_eddd=False
rio_man_del=""

ftea05_eddd=False
ftea05_del=""

bon05_eddd=False
bon05_del=""

bon1_eddd=False
bon1_del=""

bon15_eddd=False
bon15_del=""


izbrannie=[]



back_from_delivery=False
def Edit_ord(lang="ru"):
    #❌🔄
    global chesn_s_eddd, chesn_s_del, ostri_s_eddd, ostri_s_del, sirni_s_eddd, sirni_s_del, BUR_del, bur_eddd, BUR15_del, bur15_eddd, FRI_del, fri_eddd, bul_del, bul_eddd, strip_pr_del, strip_pr_eddd, kril_pr_del, kril_pr_eddd, strip_kg_del, strip_kg_eddd, kril_kg_del, kril_kg_eddd, kombo25_del, kombo25_eddd, kombo35_del, kombo35_eddd, cof_del, cof_eddd, rio_man_del, rio_man_eddd, cc05_eddd, cc125_eddd, cc175_eddd, fan05_eddd, fan125_eddd, fan175_eddd, spr1_del, spr1_eddd, rc1_eddd, ftea05_eddd, bon05_eddd, bon1_eddd, bon15_eddd
    
    mar=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    Zakaz_ed=types.KeyboardButton("🍔 Чикен-Бургер ❌")
    Zakaz15_ed=types.KeyboardButton("🍔 Чикен-Бургер(15) ❌")
    fri_ed=types.KeyboardButton("🍟 Фри ❌")
    bul_ed=types.KeyboardButton("🍞 Булочка ❌")
    stripes_pr=types.KeyboardButton("🍗 Стрипсы (пр) ❌")
    kril_pr=types.KeyboardButton("🍗 Крылышки (пр) ❌")
    stripes_kg=types.KeyboardButton("🍗 Стрипсы (кг) ❌")
    kril_kg=types.KeyboardButton("🍗 Крылышки (кг) ❌")
    kombo25=types.KeyboardButton("🍗🥤 Комбо-25см ❌")
    kombo35=types.KeyboardButton("🍗🥤 Комбо-35см ❌")
    chesn_s=types.KeyboardButton("🧄 Чесночный соус ❌")
    ostri_s=types.KeyboardButton("🌶 Острый соус ❌")
    sirni_s=types.KeyboardButton("🧀 Сырный соус ❌")
    #cc03=types.KeyboardButton("🥤 Coca Cola 0.3")
    coffee_ed=types.KeyboardButton("☕️ Кофе ❌")
    rio_man_ed=types.KeyboardButton("🥭 El-Rio mango ❌")
    cc05=types.KeyboardButton("🥤 Coca Cola 0.5 ❌") 
    cc125=types.KeyboardButton("🥤 Coca Cola 1.25 ❌")
    cc175=types.KeyboardButton("🥤 Coca Cola 1.75 ❌")
    #fan03=types.KeyboardButton("🍊 Fanta 0.3")
    fan05=types.KeyboardButton("🍊 Fanta 0.5 ❌")
    fan125=types.KeyboardButton("🍊 Fanta 1.25 ❌")
    fan175=types.KeyboardButton("🍊 Fanta 1.75 ❌")
    sprite1=types.KeyboardButton("🍋 Sprite 1 ❌")
    ftea05=types.KeyboardButton("🫖 Fuse-tea 0.5 ❌")#🍵
    rc1=types.KeyboardButton("🥤 RC cola 1 ❌")
    bq05=types.KeyboardButton("🧊 Bon-aqua 0.5 ❌")
    bq1=types.KeyboardButton("🧊 Bon-aqua 1 ❌")
    bq15=types.KeyboardButton("🧊 Bon-aqua 1.5 ❌")
    if lang=="ru":
        back=types.KeyboardButton("⬅️ Назад")
        refine=types.KeyboardButton("🔄 очистить корзину")
        add=types.KeyboardButton("🛒 Оформить заказ")
    elif lang=="tj":
        back=types.KeyboardButton("⬅️ Бозгашт")
        refine=types.KeyboardButton("🔄 очистить корзину")
        add=types.KeyboardButton("🛒 Ба расмият даровардан")
    
    if BUR_del in orders:
        bur_eddd=True
        mar.add(Zakaz_ed)
    else:
        pass
    
    if BUR15_del in orders:
        bur15_eddd=True
        mar.add(Zakaz15_ed)
    else:
        pass

    if FRI_del in orders:
        fri_eddd=True
        mar.add(fri_ed)
    else:
        pass
    
    if bul_del in orders:
        bul_eddd=True
        mar.add(bul_ed)
    else:
        pass

    if strip_pr_del in orders:
        strip_pr_eddd=True
        mar.add(stripes_pr)
    else:
        pass
    
    if kril_pr_del in orders:
        kril_pr_eddd=True
        mar.add(kril_pr)
    else:
        pass
    
    if strip_kg_del in orders:
        strip_kg_eddd=True
        mar.add(stripes_kg)
    else:
        pass
    
    if kril_kg_del in orders:
        kril_kg_eddd=True
        mar.add(kril_kg)
    else:
        pass
    
    if kombo25_del in orders:
        kombo25_eddd=True
        mar.add(kombo25)
    else:
        pass
    
    if kombo35_del in orders:
        kombo35_eddd=True
        mar.add(kombo35)
    else:
        pass
    
    if chesn_s_del in orders:
        chesn_s_eddd=True
        mar.add(chesn_s)
    else:
        pass
    
    if ostri_s_del in orders:
        ostri_s_eddd=True
        mar.add(ostri_s)
    else:
        pass

    if cof_del in orders:
        cof_eddd=True
        mar.add(coffee_ed)
    else:
        pass

    if cc05_del in orders:
        cc05_eddd=True
        mar.add(cc05)
    else:
        pass

    if cc125_del in orders:
        cc125_eddd=True
        mar.add(cc125)
    else:
        pass
    
    if cc175_del in orders:
        cc175_eddd=True
        mar.add(cc175)
    else:
        pass
    
    if fan05_del in orders:
        fan05_eddd=True
        mar.add(fan05)
    else:
        pass

    if fan125_del in orders:
        fan125_eddd=True
        mar.add(fan125)
    else:
        pass
    
    if fan175_del in orders:
        fan175_eddd=True
        mar.add(fan175)
    else:
        pass

    if rc1_del in orders:
        rc1_eddd=True
        mar.add(rc1)
    else:
        pass

    if spr1_del in orders:
        spr1_eddd=True
        mar.add(sprite1)
    else:
        pass
    
    if rio_man_del in orders:
        rio_man_eddd=True
        mar.add(rio_man_ed)
    else:
        pass

    if ftea05_del in orders:
        ftea05_eddd=True
        mar.add(ftea05)
    else:
        pass

    if bon05_del in orders:
        bon05_eddd=True
        mar.add(bq05)
    else:
        pass

    if bon1_del in orders:
        bon1_eddd=True
        mar.add(bq1)
    else:
        pass

    if bon15_del in orders:
        bon15_eddd=True
        mar.add(bq15)
    else:
        pass

    if sirni_s_del in orders:
        sirni_s_eddd=True
        mar.add(sirni_s)
    else:
        pass

    if sirni_s_del in orders:
        sirni_s_eddd=True
        mar.add(sirni_s)
    else:
        pass

    

    return mar
def Main_menu(lang="ru"):
    #🛍🛒📜✏️

    mar=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    if lang=="ru":
        to_order=types.KeyboardButton(text="✏️ Заказать")
        my_orders=types.KeyboardButton(text="📜 Мои заказы")
        settings=types.KeyboardButton(text="🌐 Изменить язык")
        o_us=types.KeyboardButton(text="ℹ️ О нас")
        svaz=types.KeyboardButton(text="✍️ Обратная связь")
    elif lang=="tj":
        to_order=types.KeyboardButton(text="✏️ Фармоиш диҳед")
        my_orders=types.KeyboardButton(text="📜 Фармонҳои ман")
        settings=types.KeyboardButton(text="🌐 Забонро иваз кунед")
        o_us=types.KeyboardButton(text="ℹ️ Дар бораи мо")
        svaz=types.KeyboardButton(text="✍️ Назари худро гузоред")
    mar.add(to_order)
    mar.add(my_orders, settings, o_us, svaz)
    
    return mar
def MENU_second():
    #🛍🛒📜✏️

    mar=types.InlineKeyboardMarkup(row_width=2)
    O_us=types.InlineKeyboardButton(text="🧐 О нас", callback_data="O_us")
    Ob_svyaz=types.InlineKeyboardButton(text="✍️ Обратная связь 📞", callback_data="O_S")
    settings=types.InlineKeyboardButton(text="⚙️ Настройки", callback_data="set")
    my_orders=types.InlineKeyboardButton(text="📜 История заказов", callback_data="i_z")
    to_order=types.InlineKeyboardButton(text="✏️ Изменить заказ", callback_data="")
    basket=types.InlineKeyboardButton(text="✅ Подтвердить заказ", callback_data="confirm")
    izbran=types.InlineKeyboardButton(text="⭐ Избранные", callback_data="zvezda")
    mar.add(Ob_svyaz, izbran, to_order)
    mar.add(basket)    
    return mar



#
mar=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
Zakaz=""
fri=""
streepes_pr=""
kril_pr=""
#napitki=""
sous=""
streepes_kg=""
kril_kg=""
kombo25=""
#mar.add(Zakaz,streepes_pr,fri,kril_pr,napitki,streepes_kg,sous,kril_kg,kombo25)
def Menu():
    #🍔🍟🍗❌✔
    global mar, Zakaz, fri, streepes_pr, kril_pr, streepes_kg, kril_kg, kombo25, izbrannie
    mar=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    Zakaz=types.KeyboardButton("🍔 Чикен-Бургер-13см")
    fri=types.KeyboardButton("🍟 Фри-8см")
    streepes_pr=types.KeyboardButton("🍗 Стрипсы 1пр(250гр)-20см ❌")
    kril_pr=types.KeyboardButton("🍗 Крылышки 1пр(250гр)-20см ❌")
    napitki=types.KeyboardButton("🥤 Напитки ❌")
    sous=types.KeyboardButton("Соусы ❌")
    streepes_kg=types.KeyboardButton("🍗 Стрипсы(1кг)-75см ❌")
    kril_kg=types.KeyboardButton("🍗 Крылышки(1кг)-75см ❌")
    kombo25=types.KeyboardButton("🍗🥤 Комбо-25см ❌")
    mar.add(Zakaz,streepes_pr,fri,kril_pr,streepes_kg,kril_kg,kombo25)
    #b.send_message(call.message.chat.id, "Выберите продукт", reply_markup=mar)
    return mar
def meenu(lang="ru"):
    global menu_mess_id
    #🍔🍟🍗🍞🥖
    mar=types.ReplyKeyboardMarkup(row_width=2)
    Zakaz=types.KeyboardButton("🍔 Чикен-Бургер-13см")
    Zakaz15=types.KeyboardButton("🍔 Чикен-Бургер-15см")
    fri=types.KeyboardButton("🍟 Фри-8см")
    bul=types.KeyboardButton("🍞 Булочка-2.5см")
    streepes_pr=types.KeyboardButton("🍗 Стрипсы 1пр(250гр)-20см")
    kril_pr=types.KeyboardButton("🍗 Крылышки 1пр(250гр)-20см")
    napitki=types.KeyboardButton("🥤 Напитки")
    sous=types.KeyboardButton("🌶🧄🧀 Соусы")
    streepes_kg=types.KeyboardButton("🍗 Стрипсы(1кг)-75см")
    kril_kg=types.KeyboardButton("🍗 Крылышки(1кг)-75см")
    kombo25=types.KeyboardButton("🍗🥤 Комбо-25см")
    kombo35=types.KeyboardButton("🍗🥤 Комбо-35см")
    if lang=="ru":
        finish_ord=types.KeyboardButton("🛒 Оформить заказ")
        karzina=types.KeyboardButton("📥 Карзина")
        nazad=types.KeyboardButton("⬅️ Назад")
        domoy=types.KeyboardButton("🏠 Главное меню")
    elif lang=="tj":
        finish_ord=types.KeyboardButton("🛒 Ба расмият даровардан")
        karzina=types.KeyboardButton("📥 Сабад")
        nazad=types.KeyboardButton("⬅️ Бозгашт")
        domoy=types.KeyboardButton("🏠 Менюи асосӣ")
            
    mar.add(Zakaz,Zakaz15,fri,bul,streepes_kg,kril_kg,streepes_pr,kril_pr,kombo25,kombo35,napitki,sous)
    mar.add(karzina, finish_ord, nazad, domoy)
    return mar
markup_z=""

def star():
    global markup_z
    markup_z = types.ReplyKeyboardMarkup(row_width=2)
    otmena = types.KeyboardButton("⬅ назад")
    add_z = types.KeyboardButton("⭐ Добавить в избранные")
    show_iz=types.KeyboardButton("Избранные")
    markup_z.add(add_z, show_iz, otmena)
    return markup_z




def Get_way(lang="ru"):
    mark = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    if lang=="ru":
        sv = types.KeyboardButton("🏫 Самовывоз")
        delivery = types.KeyboardButton("🛵 Доставка")
        back=types.KeyboardButton("⬅️ Назад")
    elif lang=="tj":
        sv = types.KeyboardButton("🏫 Кашида гирифтан")
        delivery = types.KeyboardButton("🛵 Таҳвил")
        back=types.KeyboardButton("⬅️ Бозгашт")
    mark.add(delivery,sv,back)
    return mark

def s_pay(lang="ru"):
    mar = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    if lang=="ru":
        terminal = types.KeyboardButton("💳 Terminal")
        nal = types.KeyboardButton("💵 Наличными")
        back=types.KeyboardButton("⬅️ Назад")
    elif lang=="tj":
        terminal = types.KeyboardButton("💳 Terminal")
        nal = types.KeyboardButton("💵 Пули нақд")
        back=types.KeyboardButton("⬅️ Бозгашт")
    mar.add(terminal,nal,back)
    return mar
"""
def DC_pay():
    mar=types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    r=types.InlineKeyboardButton("⬅️ Отмена", callback_data="otmena")
    pay=types.InlineKeyboardButton("💵 Оплатить заказ онлайн", callback_data="pay_dc")
    mar.add(pay,r)
    return mar

def Alif_pay():
    mar=types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    r=types.InlineKeyboardButton("⬅️ Отмена", callback_data="otmena")
    pay=types.InlineKeyboardButton("💵 Оплатить заказ онлайн", callback_data="pay_alif", url="")
    mar.add(pay,r)
    return mar

def Eskhata_pay():
    mar=types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    r=types.InlineKeyboardButton("⬅️ Отмена", callback_data="otmena")
    pay=types.InlineKeyboardButton("💵 Оплатить заказ онлайн", callback_data="pay_eskhata", url="")
    mar.add(pay,r)
    return mar
"""
komment=""
def show_order(lang="ru", admin=""):
    global order, orders, pay_way, adres, place, komment
    summa=0
    if lang=="ru":
        order="📥 Карзина:\n"
    
        if contact!=0 and admin=="admin":
            order+=f"\nНомер телефона:{contact}"
        else:
            pass
        
        if pay_way!="":
            order+=f"\nСпособ оплаты:{pay_way}"
        else:
            pass
        
        if get_way=="🛵 Доставка":
            order+="\nТип заказа:🛵 Доставка\n"


        if get_way=="🛵 Доставка":
            order+=f"\nАдрес:{adres}"
        
        if get_way=="🏫 Самовывоз":
            order+=f"\nТип заказа:{get_way}\n"
        else:
            pass
        
        
        if Time!="":
            order+=f"\n🕔 Дата доставки:{Time}"
        else:
            pass
        if komment!="":
            order+=f"\n💬 Комментарий к заказу:{komment}"
        for i in range(len(orders)):
            order+=f"\n*{orders[i][0]}*\n{orders[i][1]} x {orders[i][2]} = {orders[i][1]*orders[i][2]}см\n"
            summa+=orders[i][1]*orders[i][2]
        
        order+=f"\n*Итого*:{summa}сомон"

    elif lang=="tj":
        order="📥 Сабад:\n\n"
    
        if contact!=0 and admin=="admin":
            order+=f"\nТелефон:{contact}"
        else:
            pass
        
        if pay_way!="":
            order+=f"\nНавъи пардохт:{pay_way}"
        else:
            pass
        
        if get_way=="🛵 Доставка":
            order+="\nНавъи интиқол:🛵 Доставка\n"


        if get_way=="🛵 Доставка":
            order+=f"\nАдрес:{adres}"
        
        if get_way=="🏫 Самовывоз":
            order+=f"\nНавъи интиқол:{get_way}\n"
        else:
            pass
        for i in range(len(orders)):
            order+=f"\n*{orders[i][0]}*\n{orders[i][1]} x {orders[i][2]} = {orders[i][1]*orders[i][2]}см\n"
            summa+=orders[i][1]*orders[i][2]
        
        order+=f"\n*Умумӣ*:{summa}сомони"

    return order

def send_order(user_name, lang="ru"):
    global order, orders, pay_way, adres, place, komment
    order=f"{contact}\nимя:{user_name}\n\n"
    summa=0
    if lang=="ru":
        if pay_way!="":
            order+=f"Способ оплаты:{pay_way}"
        else:
            pass
        
        if get_way=="🛵 Доставка":
            order+="\nТип заказа:🛵 Доставка\n"


        if get_way=="🛵 Доставка":
            order+=f"\nАдрес:{adres}"
        
        if get_way=="🏫 Самовывоз":
            order+=f"\nТип заказа:{get_way}\n"
        else:
            pass
        
        for i in range(len(orders)):
            order+=f"\n*{orders[i][0]}*\n{orders[i][1]} x {orders[i][2]} = {orders[i][1]*orders[i][2]}см\n"
            summa+=orders[i][1]*orders[i][2]
        
        order+=f"\n*Итого*:{summa}см"
        
        if Time!="":
            order+=f"\n🕔 Дата доставки:{Time}"
        else:
            pass
        if komment!="":
            order+=f"\n💬 Комментарий к заказу:{komment}"

    return order

def cencel(lang="ru"):
    mar=types.ReplyKeyboardMarkup(resize_keyboard=True)
    if lang=="ru":
        c=types.KeyboardButton("⬅️ Назад")
    elif lang=="tj":
        c=types.KeyboardButton("⬅️ Бозгашт")
    mar.add(c)
    return mar
#Zakaz
def Fri():
    global fri_kol, fri_ord, fri_sum_pr, price_fri#, bur_list
    #bur_list=["min","pls","add_kar"]
    price_fri=8
    fri_ord=f"🍟 Фри"
    fri_sum_pr=price_fri*fri_kol

    return mar
#Zakaz15
# def Burger15():
#     global bur15_kol, bur15_ord, bur15_sum_pr, price_bur15#, bur_list
#     #bur_list=["min","pls","add_kar"]
#     price_bur15=15
#     bur15_ord=f"🍔 Чикен-Бургер(с куриной катлетой)"
#     bur15_sum_pr=price_bur15*bur15_kol
#
#     return mar

def Zakaz():
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
    back=types.KeyboardButton("⬅️ Назад")
    #zero=types.KeyboardButton("0")
    kar=types.KeyboardButton("📥 Карзина")
    mar.add(one,two,three,four,five,six,seven,eghit,nine,back,kar)

    return mar
#FRI

def Bul():
    global bul_kol, bul_ord, bul_sum_pr, price_bul#, bur_list
    #bur_list=["min","pls","add_kar"]
    price_bul=2.5
    bul_ord=f"🍞 Булочка"
    bul_sum_pr=price_bul*bul_kol
    
    return mar

def Strip_pr():
    global strip_pr_kol, strip_pr_ord, strip_pr_sum_pr, price_strip_pr#, bur_list
    #bur_list=["min","pls","add_kar"]
    price_strip_pr=20
    strip_pr_ord=f"🍗 Стрипсы ({strip_pr_kol}пр)"
    strip_pr_sum_pr=price_strip_pr*strip_pr_kol
    
    return mar

def Kril_pr():
    global kril_pr_kol, kril_pr_ord, kril_pr_sum_pr, price_kril_pr#, bur_list
    #bur_list=["min","pls","add_kar"]
    price_kril_pr=20
    kril_pr_ord=f"🍗 Крылышки ({kril_pr_kol}пр)"
    kril_pr_sum_pr=price_kril_pr*kril_pr_kol
    
    #photo=open("chicken_bur.jpg", "rb")
    #b.send_photo(chat_id, photo)
    return mar

def Strip_kg():
    global strip_kg_kol, strip_kg_ord, strip_kg_sum_pr, price_strip_kg#, bur_list
    #bur_list=["min","pls","add_kar"]
    price_strip_kg=75
    strip_kg_ord=f"🍗 Стрипсы ({strip_kg_kol}кг)"
    strip_kg_sum_pr=price_strip_kg*strip_kg_kol
    mar = types.InlineKeyboardMarkup(row_width=3)

    pls1 = types.InlineKeyboardButton("+", callback_data="pls1")
    kg = types.InlineKeyboardButton("1кг", callback_data="1kg")
    min1 = types.InlineKeyboardButton("-", callback_data="min1")

    pls01 = types.InlineKeyboardButton("+", callback_data="pls01")
    gr100 = types.InlineKeyboardButton("100гр", callback_data="100gr")
    min01 = types.InlineKeyboardButton("-", callback_data="min01")

    add = types.InlineKeyboardButton("Оформить заказ", callback_data="add")
    mar.add(min1, kg, pls1, min01, gr100, pls01, add)
    #photo=open("chicken_bur.jpg", "rb")
    #b.send_photo(chat_id, photo)
    return mar

def Kril_kg():
    global kril_kg_kol, kril_kg_ord, kril_kg_sum_pr, price_kril_kg#, bur_list
    #bur_list=["min","pls","add_kar"]
    price_kril_kg=75
    kril_kg_ord=f"🍗 Крылышки ({kril_kg_kol}кг)"
    kril_kg_sum_pr=price_kril_kg*kril_kg_kol
    
    #photo=open("chicken_bur.jpg", "rb")
    #b.send_photo(chat_id, photo)
    return mar

# def kril_som():
#     mar=types.InlineKeyboardMarkup(row_width=4, resize_keyboard=True)
#     one=types.InlineKeyboardButton("1", callback_data="one_kril")
#     two=types.InlineKeyboardButton("2", callback_data="two_kril")
#     three=types.InlineKeyboardButton("3", callback_data="three_kril")
#     four=types.InlineKeyboardButton("4", callback_data="four_kril")
#     five=types.InlineKeyboardButton("5", callback_data="five_kril")
#     six=types.InlineKeyboardButton("6", callback_data="six_kril")
#     seven=types.InlineKeyboardButton("7", callback_data="seven_kril")
#     eight=types.InlineKeyboardButton("8", callback_data="eight_kril")
#     nine=types.InlineKeyboardButton("9", callback_data="nine_kril")
#     zero=types.InlineKeyboardButton("0", callback_data="zero_kril")
#     delet=types.InlineKeyboardButton("⬅️", callback_data="del_kril")
#     delet_all=types.InlineKeyboardButton("🔄", callback_data="del_all_kril")
#     kg=types.InlineKeyboardButton("KG", callback_data="kril_kilo")
#     add=types.InlineKeyboardButton("🛒 Добавить в корзину", callback_data="add_kar_kril_sm")
#     mar.add(one, two, three, four, five, six, seven, eight, nine, delet_all, zero, delet, kg)
#     mar.add(add)
#     return mar
def Kombo25():
    global kombo25_kol, kombo25_ord, kombo25_sum_pr, price_kombo25#, bur_list
    #bur_list=["min","pls","add_kar"]
    price_kombo25=25
    kombo25_ord=f"🍗🥤 Комбо 3в1 ({kombo25_kol}пр)"
    kombo25_sum_pr=price_kombo25*kombo25_kol
    
    #photo=open("chicken_bur.jpg", "rb")
    #b.send_photo(chat_id, photo)
    return mar

def Kombo35():
    global kombo35_kol, kombo35_ord, kombo35_sum_pr, price_kombo35#, bur_list
    #bur_list=["min","pls","add_kar"]
    price_kombo35=35
    kombo35_ord=f"🍗🥤 Комбо 5в1 ({kombo35_kol}пр)"
    kombo35_sum_pr=price_kombo35*kombo35_kol
    
    #photo=open("chicken_bur.jpg", "rb")
    #b.send_photo(chat_id, photo)
    return mar
#СОУСЫ
def souses():
    #🌶🧄🧀
    mar=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    ostri=types.KeyboardButton("🌶 Острый соус")
    chestochni=types.KeyboardButton("🧄 Чесночный соус") 
    sirni=types.KeyboardButton("🧀 Сырный соус")
    finish_ord=types.KeyboardButton("🛒 Оформить заказ")
    back=types.KeyboardButton("⬅️ Назад")
    mar.add(finish_ord,back)
    mar.add(chestochni,)
    mar.add(ostri)
    mar.add(sirni)
    return mar

#Острый соус
def Ostri_s():
    global ostri_s_kol, ostri_s_ord, ostri_s_sum_pr, price_ostri_s#, bur_list
    #bur_list=["min","pls","add_kar"]
    price_ostri_s=3
    ostri_s_ord=f"🌶 Острый соус ({ostri_s_kol}шт)"
    ostri_s_sum_pr=price_ostri_s*ostri_s_kol
    
    #photo=open("chicken_bur.jpg", "rb")
    #b.send_photo(chat_id, photo)
    return mar
#Чесночный соус
def Chesn_s():
    global chesn_s_kol, chesn_s_ord, chesn_s_sum_pr, price_chesn_s#, bur_list
    #bur_list=["min","pls","add_kar"]
    price_chesn_s=3
    chesn_s_ord=f"🧄 Чесночный соус ({chesn_s_kol}шт)"
    chesn_s_sum_pr=price_chesn_s*chesn_s_kol
    
    #photo=open("chicken_bur.jpg", "rb")
    #b.send_photo(chat_id, photo)
    return mar
#Сырный соус
def Sirni_s():
    global sirni_s_kol, sirni_s_ord, sirni_s_sum_pr, price_sirni_s#, bur_list
    #bur_list=["min","pls","add_kar"]
    price_sirni_s=3
    sirni_s_ord=f"🧀 Сырный соус ({sirni_s_kol}шт)"
    sirni_s_sum_pr=price_sirni_s*sirni_s_kol
    
    #photo=open("chicken_bur.jpg", "rb")
    #b.send_photo(chat_id, photo)
    
    return mar

    
#НАПИТКИ
def napitki(lang="ru"):
    mar=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    coffee=types.KeyboardButton("☕️ Кофе")
    rio_man=types.KeyboardButton("🥭 El-Rio mango")
    #cc03=types.KeyboardButton("🥤 Coca Cola 0.3")
    cc05=types.KeyboardButton("🥤 Coca Cola 0.5") 
    cc125=types.KeyboardButton("🥤 Coca Cola 1.25")
    cc175=types.KeyboardButton("🥤 Coca Cola 1.75")
    #fan03=types.KeyboardButton("🍊 Fanta 0.3")
    fan05=types.KeyboardButton("🍊 Fanta 0.5")
    fan125=types.KeyboardButton("🍊 Fanta 1.25")
    fan175=types.KeyboardButton("🍊 Fanta 1.75")
    sprite1=types.KeyboardButton("🍋 Sprite 1")
    fuse_tea05=types.KeyboardButton("🫖 Fuse-tea 0.5")#🍵
    rc=types.KeyboardButton("🥤 RC cola 1")
    bq05=types.KeyboardButton("🧊 Bon-aqua 0.5")
    bq1=types.KeyboardButton("🧊 Bon-aqua 1")
    bq15=types.KeyboardButton("🧊 Bon-aqua 1.5")
    if lang=="ru":
        finish_ord=types.KeyboardButton("🛒 Оформить заказ")
        back=types.KeyboardButton("⬅️ Назад")
    elif lang=="tj":
        finish_ord=types.KeyboardButton("🛒 Ба расмият даровардан")
        back=types.KeyboardButton("⬅️ Бозгашт")
    
    mar.add(finish_ord,back)
    
    mar.add(coffee,cc05,cc125,cc175,fan05,fan125,fan175,sprite1,rio_man,fuse_tea05,rc,bq05,bq1,bq15)
    return mar

# Coffee
def Coffee():
    global cof_kol, cof_ord, cof_sum_pr, price_cof
    price_cof=3
    cof_ord=f"☕️ Кофе"
    cof_sum_pr=price_cof*cof_kol
    
    
    return mar



#Coca Cola 03
def cc03():
    global cc03_kol, cc03_ord, cc03_sum_pr#, bur_list
    #bur_list=["min","pls","add_kar"]
    price_cc03=3
    cc03_ord=f"🥤 Coca cola 0.3 ({cc03_kol}шт)"
    cc03_sum_pr=price_cc03*cc03_kol
    
    #photo=open("chicken_bur.jpg", "rb")
    #b.send_photo(chat_id, photo)
    # mar=types.InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
    # inus=types.InlineKeyboardButton("-", callback_data="min_cc03")
    # plus=types.InlineKeyboardButton("+", callback_data="pls_cc03")
    # quantity=types.InlineKeyboardButton(cc03_kol, callback_data="qwerty")
    # zak_price=types.InlineKeyboardButton(f"Coca cola 0.3 {cc03_kol}шт-({cc03_sum_pr}см)", callback_data="qwert")
    # add=types.InlineKeyboardButton("🛒 Добавить в корзину", callback_data="add_kar_cc03")
    # mar.add(minus,quantity,plus,zak_price)
    # mar.add(add)
    # m
    return mar
# Coca cola 05
def CC05():
    global cc05_kol, cc05_ord, cc05_sum_pr, price_cc05
    price_cc05=5
    cc05_ord=f"🥤 Coca cola 0.5"
    cc05_sum_pr=price_cc05*cc05_kol
    
    
    return mar

def Bon_aqua05():
    global bon05_kol, bon05_ord, bon05_sum_pr, price_bon05
    price_bon05=3
    bon05_ord=f"🧊 Bon-aqua 0.5({bon05_kol}шт)"
    bon05_sum_pr=price_bon05*bon05_kol
    
    return mar
def Fan05():
    global fan05_kol, fan05_ord, fan05_sum_pr, price_fan05
    price_fan05=5
    fan05_ord=f"🍊 Fanta 0.5({fan05_kol}шт)"
    fan05_sum_pr=price_fan05*fan05_kol
    
    return mar

def Rio_man():
    global rio_man_kol, rio_man_ord, rio_man_sum_pr, price_rio_man
    price_rio_man=7
    rio_man_ord=f"🥭 El-Rio mango"
    rio_man_sum_pr=price_rio_man*rio_man_kol
    
    return mar

def Ftea05():
    global ftea05_kol, ftea05_ord, ftea05_sum_pr, price_ftea05
    price_ftea05=6
    ftea05_ord=f"🫖 Fuse-tea 0.5({ftea05_kol}шт)"
    ftea05_sum_pr=price_ftea05*ftea05_kol
    
    return mar
# Coca cola 125
def CC125():
    global cc125_kol, cc125_ord, cc125_sum_pr, price_cc125#, bur_list
    #bur_list=["min","pls","add_kar"]
    price_cc125=10
    cc125_ord=f"🥤 Coca cola 1.25 ({cc125_kol}шт)"
    cc125_sum_pr=price_cc125*cc125_kol
    
    #photo=open("chicken_bur.jpg", "rb")
    #b.send_photo(chat_id, photo)
    return mar

def Fan125():
    global fan125_kol, fan125_ord, fan125_sum_pr, price_fan125
    price_fan125=10
    fan125_ord=f"🍊 Fanta 1.25({fan125_kol}шт)"
    fan125_sum_pr=price_fan125*fan125_kol
    
    return mar

def Spr1():
    global spr1_kol, spr1_ord, spr1_sum_pr, price_spr1
    price_spr1=8
    spr1_ord=f"🍋 Sprite 1л({spr1_kol}шт)"
    spr1_sum_pr=price_spr1*spr1_kol
    
    return mar

def RC1():
    global rc1_kol, rc1_ord, rc1_sum_pr, price_rc1
    price_rc1=8
    rc1_ord=f"🥤 RC cola 1л({rc1_kol}шт)"
    rc1_sum_pr=price_rc1*rc1_kol
    
    return mar

def Bon_aqua1():
    global bon1_kol, bon1_ord, bon1_sum_pr, price_bon1
    price_bon1=5
    bon1_ord=f"🧊 Bon-aqua 1л({bon1_kol}шт)"
    bon1_sum_pr=price_bon1*bon1_kol
    
    return mar

def Bon_aqua15():
    global bon15_kol, bon15_ord, bon15_sum_pr, price_bon15
    price_bon15=8
    bon15_ord=f"🧊 Bon-aqua 1.5л({bon15_kol}шт)"
    bon15_sum_pr=price_bon15*bon15_kol
    
    return mar

# Coca cola 175
def CC175():
    global cc175_kol, cc175_ord, cc175_sum_pr, price_cc175#, bur_list
    #bur_list=["min","pls","add_kar"]
    price_cc175=12
    cc175_ord=f"🥤 Coca cola 1.75({cc175_kol}шт)"
    cc175_sum_pr=price_cc175*cc175_kol
    
    #photo=open("chicken_bur.jpg", "rb")
    #b.send_photo(chat_id, photo)
    return mar

def Fan175():
    global fan175_kol, fan175_ord, fan175_sum_pr, price_fan175
    price_fan175=12
    fan175_ord=f"🍊 Fanta 1.75({fan175_kol}шт)"
    fan175_sum_pr=price_fan175*fan175_kol
    
    return mar
def get_contact(lang="ru"):
    mar=types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    if lang=="ru":
        otpr=types.KeyboardButton("Отправить свой номер", request_contact=True)
        back=types.KeyboardButton("⬅️ Назад")
    elif lang=="tj":
        otpr=types.KeyboardButton("Рақами ман", request_contact=True)
        back=types.KeyboardButton("⬅️ Бозгашт")
    
    mar.add(otpr, back)
    return mar
def send_o(lang="ru"):
    mar=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    if lang=="ru":
        back=types.KeyboardButton("⬅️ Назад")
        otmena=types.KeyboardButton("❌ Отмена")
        con=types.KeyboardButton("✅ Подтвердить заказ")
        s_d=types.KeyboardButton("🕔 Самовывоз дата")
        kom_z=types.KeyboardButton("💬 Комментарий к заказу")
    elif lang=="tj":
        back=types.KeyboardButton("⬅️ Бозгашт")
        otmena=types.KeyboardButton("❌ Бекор кардан")
        con=types.KeyboardButton("✅ Тасдиқи фармоиш")
        s_d=types.KeyboardButton("🕔 Вақти гирифтан")
        kom_z=types.KeyboardButton("💬 Дар бораи фармоиш шарҳ диҳед")
        
    mar.add(con)
    mar.add(s_d)
    mar.add(kom_z)
    mar.add(back, otmena)
    return mar
def Location(lang="ru"):
    mar=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    if lang=="ru":
        ot=types.KeyboardButton("⬅️ Назад")
        loc=types.KeyboardButton("📍 Отправить текущее местоположение для доставки", request_location=True)
        loca=types.KeyboardButton("✍️ Написать адрес")
    elif lang=="tj":
        ot=types.KeyboardButton("⬅️ Бозгашт")
        loc=types.KeyboardButton("📍 Ҷойгиршавӣ фиристед", request_location=True)
        loca=types.KeyboardButton("✍️ Написать адрес")
    mar.add(loca,loc,ot)
    return mar

adr=False
def end(lang="ru"):
    mar=types.ReplyKeyboardMarkup(resize_keyboard=True)
    if lang=="ru":
        sam_data=types.KeyboardButton("🕔 Самовывоз дата")
        komm_zak=types.KeyboardButton("💬 Комментарий к заказу")
        back=types.KeyboardButton("⬅️ Назад")
    elif lang=="ru":
        sam_data=types.KeyboardButton("🕔 Вақти гирифтан")
        komm_zak=types.KeyboardButton("💬 Дар бораи фармоиш шарҳ диҳед")
        back=types.KeyboardButton("⬅️ Бозгашт")
    mar.add(sam_data, komm_zak, back)
    return mar

def Back(lang="ru"):

    mar=types.ReplyKeyboardMarkup(resize_keyboard=True)
    if lang=="ru":
        back=types.KeyboardButton("⬅️ Назад")
    elif lang=="tj":
        back=types.KeyboardButton("⬅️ Бозгашт")
    mar.add(back)
    return mar
    
pos="0"
finish=False
def Link():
    mar=types.ReplyKeyboardMarkup(row_width=2)
    instagram=types.InlineKeyboardButton("",url="")
    telegram=types.InlineKeyboardButton("",url="")
    back=types.InlineKeyboardButton("⬅️ Назад", callback_data="main_menu")
    
    mar.add(instagram,telegram,back)
    
    return mar
def Lang(lang="ru"):
    mar=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    ru=types.KeyboardButton("🇷🇺 Русский")
    tj=types.KeyboardButton("🇹🇯 Tоҷикӣ")
    if lang=="ru":
        back=types.KeyboardButton("⬅️ Назад")
    elif lang=="tj":
        back=types.KeyboardButton("⬅️ Бозгашт")
    mar.add(ru, tj, back)
    
    return mar

def Confirm():
    mar=types.InlineKeyboardMarkup(row_width=2)
    confirm=types.InlineKeyboardButton("Подтвердить✅", callback_data="confirm")
    cencel=types.InlineKeyboardButton("Отклонить❌", callback_data="cencel")

    mar.add(confirm, cencel)
    return mar

@b.message_handler(content_types=["contact"])   
def coontact(message):
    global language, contact, ol, pos
    if message.content_type != None:
        pos="7"
        contact=message.contact.phone_number
        if language=="ru":
            b.send_message(message.chat.id, text="Отправьте способ оплаты", reply_markup=s_pay())
        elif language=="tj":
            b.send_message(message.chat.id, text="Отправьте способ оплаты", reply_markup=s_pay("tj"))
        
    else:
        pass
@b.message_handler(content_types=["location"])
def get_location(message):
    global adres, finish, pos
    if message.location is not None:
        adres=message.location
        finish=True
        if language=="ru":
            b.send_message(message.chat.id, text=show_order(), parse_mode="Markdown", reply_markup=send_o())
        elif language=="tj":
            b.send_message(message.chat.id, text=show_order("tj"), parse_mode="Markdown", reply_markup=send_o("tj"))

        pos="9"        

@b.message_handler(content_types=["text"])

def start2(message):
    global order_story, language,BUR15_del,FRI_del,bul_del,chesn_s_del,ostri_s_del,sirni_s_del,cof_del,rio_man_del,spr1_del,karzina, komment, finish, integer, string, contact, cont, g_w, ol, pos, bur_ord, bur_kol, price_bur,fri_ord, fri_kol, price_fri,strip_pr_ord, strip_pr_kol, price_strip_pr,kril_pr_ord, kril_pr_kol, price_kril_pr,strip_kg_ord, strip_kg_kol, price_strip_kg,kril_kg_ord, kril_kg_kol, price_kril_kg,kombo25_ord, kombo25_kol, price_kombo25,kombo35_ord, kombo35_kol, price_kombo35,chesn_s_ord, chesn_s_kol, price_chesn_s,ostri_s_ord, ostri_s_kol, price_ostri_s,sirni_s_ord, sirni_s_kol, price_sirni_s, cof_ord, cof_kol, price_cof, cc05_ord, cc05_kol, price_cc05,cc125_ord, cc125_kol, price_cc125,cc175_ord, cc175_kol, price_cc175, bon05_ord, bon05_kol, price_bon05,bon1_ord, bon1_kol, price_bon1,bon15_ord, bon15_kol, price_bon15, rio_man_ord, rio_man_kol, price_rio_man, ftea05_ord, ftea05_kol, price_ftea05, fan05_ord, fan05_kol, price_fan05, bon05_ord, bon05_kol, price_bon05,bon1_ord, bon1_kol, price_bon1,bon15_ord, bon15_kol, price_bon15,mm1, karzina, price, back_from_place, instr, inst_show, back_from_delivery, ftea05_ord, ftea05_kol, ftea05_sum_pr, fri_eddd, fri, bur_eddd, BUR_del, strip_pr_eddd, strip_pr_del, kril_pr_eddd, kril_pr_del, strip_kg_eddd, strip_kg_del, kril_kg_eddd, kril_kg_del, kombo25_eddd, kombo25_del, kombo35_eddd, kombo35_del, cc05_eddd, cc05_del, cc125_eddd, cc125_del, cc175_eddd, cc175_del, fan05_eddd, fan05_del, fan125_eddd, fan125_del, fan175_eddd, fan175_del, rc1_eddd, rc1_del, ftea05_eddd, ftea05_del, bon05_eddd, bon05_del, bon1_eddd, bon1_del, bon15_eddd, bon15_del, back_edor, choice_001, choice_002, choice_003, choice_004, kril001, orders, del_order, write_adres, place, pay_way, back_izbr, adres, adr, admin, izbrannie, get_way, Time, hz, messid_mak4, messid_mir, messid_uni, back_menu, bur_kol, fri_kol, strip_pr_kol, kril_pr_kol, strip_kg_kol, kril_kg_kol, kombo25_kol, kombo35_kol, cc05_ord, cc05_kol, cc05_sum_pr, cc125_ord, cc125_kol, cc125_sum_pr, cc175_ord, cc175_kol, cc175_sum_pr, ostri_s_ord, ostri_s_kol, ostri_s_sum_pr, chesn_s_ord, chesn_s_kol, chesn_s_sum_pr, sirni_s_ord, sirni_s_kol, sirni_s_sum_pr, izbrannie, bur_foto, bur_message, bur15_foto, bur15_message, fri_foto, FRI_message, bul_foto, BUL_message, strip_pr_foto, strip_pr_message, kril_pr_foto, kril_pr_message, strip_kg_foto, strip_kg_message, kril_kg_foto, kril_kg_message, kombo25_foto, kombo25_message, kombo35_foto, kombo35_message, chesn_s_foto, chesn_s_message, ostri_s_foto, ostri_s_message, sirni_s_foto, sirni_s_message, cof_foto, cof_message, cc05_foto, cc05_message, cc125_foto, cc125_message, cc175_foto, cc175_message, fan05_foto, fan05_message, fan125_foto, fan125_message, fan175_foto, fan175_message, rc1_foto, rc1_message, spr1_foto, spr1_message, rio_man_foto, rio_man_message, ftea05_foto, ftea05_message, bon05_foto, bon05_message, bon1_foto, bon1_message, bon15_foto, bon15_message
    t=message.text
                                            #START
    if t=="/start" or t=="🏠 Главное меню" and language=="ru":
        
        pos="1"
        b.send_message(message.from_user.id, text=f"Привет {message.from_user.first_name}!", reply_markup=Main_menu("ru"))

        orders=[]
        bur_kol=1
        bur15_kol=1
        fri_kol=1
        bul_kol=1
        strip_pr_kol=1
        kril_pr_kol=1
        strip_kg_kol=1
        kril_kg_kol=1
        kombo25_kol=1
        kombo35_kol=1

        cof_kol=1
        rio_man_kol=1
        #coca cola
        cc03_ord=""
        cc03_kol=1
        cc03_sum_pr=0

        
        cc05_kol=1
        cc05_sum_pr=0

        
        cc125_kol=1
        cc125_sum_pr=0

        
        cc175_kol=1
        cc175_sum_pr=0

        #Соусы
        
        ostri_s_kol=1
        ostri_s_sum_pr=0

        
        chesn_s_kol=1
        chesn_s_sum_pr=0

        
        sirni_s_kol=1
        sirni_s_sum_pr=0
        
    elif t=="/start" or "🏠 Менюи асосӣ":
        if language=="tj":
            pos="1"
            b.send_message(message.from_user.id, text=f"Салом {message.from_user.first_name}!", reply_markup=Main_menu("tj"))

            orders=[]
            bur_kol=1
            bur15_kol=1
            fri_kol=1
            bul_kol=1
            strip_pr_kol=1
            kril_pr_kol=1
            strip_kg_kol=1
            kril_kg_kol=1
            kombo25_kol=1
            kombo35_kol=1

            cof_kol=1
            rio_man_kol=1
            #coca cola
            cc03_ord=""
            cc03_kol=1
            cc03_sum_pr=0

            
            cc05_kol=1
            cc05_sum_pr=0

            
            cc125_kol=1
            cc125_sum_pr=0

            
            cc175_kol=1
            cc175_sum_pr=0

            #Соусы
            
            ostri_s_kol=1
            ostri_s_sum_pr=0

            
            chesn_s_kol=1
            chesn_s_sum_pr=0

            
            sirni_s_kol=1
            sirni_s_sum_pr=0
            
    else:
        pass
    ####################################################################################################
    #                           Main Menu
    if t=="✏️ Заказать" and language=="ru":
        pos="2"
        b.send_message(message.chat.id, "С чего начать?", reply_markup=meenu())
    elif t=="⬅️ Назад" and pos=="2":
        pos="1"
        b.send_message(message.chat.id, "🏠 Главное меню", reply_markup=Main_menu())
    
    elif t=="✏️ Фармоиш диҳед":
        if language=="tj":
            pos="2"
            b.send_message(message.chat.id, "Мо аз куҷо сар кунем?", reply_markup=meenu("tj"))
    elif t=="⬅️ Бозгашт" and pos=="2":
        pos="1"
        b.send_message(message.chat.id, "🏠 Менюи асосӣ", reply_markup=Main_menu("tj"))
    


    elif t=="📜 Мои заказы" or t=="📦 Фармонҳои ман":
        if order_story!=[]:
            for i in range(len(order_story)):
                b.send_message(message.chat.id, text=order_story[i], parse_mode="Markdown")
        else:
            if language=="ru":
                b.send_message(message.chat.id, "История заказов пуст :(")
            elif language=="tj":
                b.send_message(message.chat.id, "Шумо ҳоло ягон фармоиш надоред :(")
    
    

    elif t=="✍️ Обратная связь":
        b.send_message(message.chat.id, "Напишите свой фидбэк, жалобу или пожелание. Либо отправьте голосовое, видео либо фото сообщение\n\nВы так же можете связаться с нами позвонив по этому номеру:\n+992922006699", reply_markup=Back())
        pos="5"     
    elif pos=="5":
        if t=="⬅️ Назад":
            pos="1"
            b.send_message(message.chat.id, "🏠 Главное меню", reply_markup=Main_menu())
        else:
            b.send_message(admin, text=f"Сообщение от пользователя {message.from_user.first_name}:\n\n{t}")
            pos="1"
            b.send_message(message.chat.id, "Спасибо за ваш отзыв!", reply_markup=Main_menu())
    
    elif t=="✍️ Назари худро гузоред" and language=="tj":
        b.send_message(message.chat.id, "Назари худро гузоред. Тавассути паёми матнӣ, аудио, видео ё акс\n\nБоз шумо метавонед ба мо занг занед:\n+992922006699", reply_markup=Back("tj"))
        pos="5"     
    elif pos=="5":
        if t=="⬅️ Бозгашт":
            pos="1"
            b.send_message(message.chat.id, "🏠 Менюи асосӣ", reply_markup=Main_menu("tj"))
        else:
            b.send_message(admin, text=f"Сообщение от пользователя {message.from_user.first_name}:\n\n{t}")
            pos="1"
            b.send_message(message.chat.id, "Ташаккур барои шарҳи шумо!", reply_markup=Main_menu("tj"))



    elif t=="ℹ️ О нас":
        #pos="5"
        vaqt_logo=open("vaqt.JPG", "br")
        b.send_photo(message.chat.id, photo=vaqt_logo)
        b.send_message(message.chat.id, "Кафе быстрого питания")
        b.send_message(message.chat.id, "*Электроная почта*:vaqt_tj@gmail.com\n\n*Call-center*:+992 92 200 66 99\n\nInstagram:[https://www.instagram.com/cafe.vaqt](https://www.instagram.com/cafe.vaqt?igsh=OGQ5ZDc2ODk2ZA==)",parse_mode="Markdown")
    elif t=="ℹ️ Дар бораи мо":
        #pos="5"
        vaqt_logo=open("vaqt.JPG", "br")
        b.send_photo(message.chat.id, photo=vaqt_logo)
        b.send_message(message.chat.id, "Кафе быстрого питания")
        b.send_message(message.chat.id, "*Электроная почта*:vaqt_tj@gmail.com\n\n*Call-center*:+992 92 200 66 99\n\nInstagram:[https://www.instagram.com/cafe.vaqt](https://www.instagram.com/cafe.vaqt?igsh=OGQ5ZDc2ODk2ZA==)",parse_mode="Markdown")



    if t=='🌐 Изменить язык':
        pos="language"

        b.send_message(message.chat.id, "Выберите язык", reply_markup=Lang())
    elif t=='🌐 Забонро иваз кунед':
        pos="language"
        b.send_message(message.chat.id, "Забонеро интихоб кунед", reply_markup=Lang("tj"))

    elif pos=="language":
        gg="1"
        if t=="🇷🇺 Русский":
            language="ru"
            b.send_message(message.chat.id, "Вы сменили язык на русский", reply_markup=Main_menu())
            pos="1"
        elif t=="🇹🇯 Tоҷикӣ":
            language="tj"
            b.send_message(message.chat.id, "Шумо забонро ба тоҷикӣ гарондед", reply_markup=Main_menu("tj"))
            pos="1"
        elif t=="⬅️ Назад" and language=="ru":
            pos="1"
            b.send_message(message.chat.id, "🏠 Главное меню", reply_markup=Main_menu())
        elif t=="⬅️ Бозгашт" and language=="tj":
            pos="1"
            b.send_message(message.chat.id, "🏠 Менюи асосӣ", reply_markup=Main_menu())
        else:
            if language=="ru" and gg=="1":
                b.send_message(message.chat.id, "Выберите язык")
            if language=="tj" and gg=="1":
                b.send_message(message.chat.id, "Забонро интихоб кунед")
    else:
        pass
########################################################################################################################    
    if t=="📥 Карзина":
        pos="3"
        karzina = b.send_message(message.chat.id, text=show_order(), parse_mode="Markdown", reply_markup=Edit_ord())
    elif t=="📥 Сабад" and language=="tj":
        pos="3"
        karzina = b.send_message(message.chat.id, text=show_order(), parse_mode="Markdown", reply_markup=Edit_ord("tj"))

    elif t=="🍔 Чикен-Бургер-13см":
        pos="01"
        
        bur_kol=1
        bur_photo=open("chicken_burger.JPG", "br")
        bur_foto=b.send_photo(message.chat.id, photo=bur_photo)
        bur_photo.close()
        bur_message=b.send_message(message.chat.id, "🍔 Чикен-Бургер\n\nСочный бургер на пышной мягкой булочке: 2 куска стрисов, свежие помидоры, солёные огурцы, салатный лист, красный лук. Заправляется чесночным соусом и кетчупом.\n\nЦена:13см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=1
    elif t=="⬅️ Назад" and pos=="01":
        pos="2"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=meenu())
        mm1=0
    elif mm1==1:
        bur_kol=int(t)
        if bur_ord not in orders:
            BUR_del=[bur_ord, bur_kol, price_bur]
            orders.append(BUR_del)
        else:
            pass
        price+=bur_kol*price_bur
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=meenu())
        mm1=0


    elif t=="🍔 Чикен-Бургер-15см":
        pos="bur15"
        
        bur15_kol=1
        bur15_photo=open("chicken_burger(15).JPG", "br")
        bur15_foto=b.send_photo(message.chat.id, photo=bur15_photo)
        bur15_photo.close()
        bur15_message=b.send_message(message.chat.id, "🍔 Чикен-Бургер(с куриной катлетой)\n\nСочный бургер на пышной мягкой булочке: куриная катлета, салатный лист, красный лук. Заправляется чесночным соусом и кетчупом.\n\nЦена:15см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=21
    elif t=="⬅️ Назад" and pos=="bur15":
        pos="2"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=meenu())
        mm1=0
    elif mm1==21:
        bur15_kol=int(t)
        if bur15_ord not in orders:
            BUR15_del=[bur15_ord, bur15_kol, price_bur15]
            orders.append(BUR15_del)
        else:
            pass
        price+=bur15_kol*price_bur15
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=meenu())
        mm1=0
    
    
    elif t=="🍟 Фри-8см":
        pos="02"
        
        fri_kol=1
        fri_photo=open("Fri.jpg", "br")
        b.send_photo(message.chat.id, photo=fri_photo)
        fri_photo.close()
        b.send_message(message.chat.id, "🍟 Фри\n\nКартофель фри- обжаренный картофель, нарезанный соломкой\n\nЦена:8см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=2
    elif t=="⬅️ Назад" and pos=="02":
        pos="2"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=meenu())
        mm1=0
    elif mm1==2:
        fri_kol=int(t)
        if fri_ord not in orders:

            FRI_del=[fri_ord, fri_kol, price_fri]
            orders.append(FRI_del)
        else:
            pass
        price+=fri_kol*price_fri
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=meenu())
        mm1=0


    elif t=="🍞 Булочка-2.5см":
        pos="bul"
        
        bul_kol=1
        bul_photo=open("bul.jpg", "br")
        b.send_photo(message.chat.id, photo=bul_photo)
        bul_photo.close()
        b.send_message(message.chat.id, "🍞 Булочка\n\nСвежая булочка\n\nЦена:2.5см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=22
    elif t=="⬅️ Назад" and pos=="bul":
        pos="2"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=meenu())
        mm1=0
    elif mm1==22:
        bul_kol=int(t)
        if bul_ord not in orders:

            bul_del=[bul_ord, bul_kol, price_bul]
            orders.append(bul_del)
        else:
            pass
        price+=bul_kol*price_bul
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=meenu())
        mm1=0
    
    
    elif t=="🍗 Стрипсы 1пр(250гр)-20см":
        pos="03"
        strip_pr_kol=1
        strip_pr_photo=open("strip_pr.JPG", "br")
        b.send_photo(message.chat.id, photo=strip_pr_photo)
        strip_pr_photo.close()
        b.send_message(message.chat.id, "🍗 Стрипсы пр\n\nКуриное филе в хрустящей панировке.\n\nЦена:25см(200гр)", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=3
    elif t=="⬅️ Назад" and pos=="03":
        pos="2"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=meenu())
        mm1=0
    elif mm1==3:
        strip_pr_kol=int(t)
        if strip_pr_ord not in orders:
            strip_pr_del=[strip_pr_ord, strip_pr_kol, price_strip_pr]
            orders.append(strip_pr_del)
        else:
            pass    
        price+=strip_pr_kol*price_strip_pr
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=meenu())
             
        mm1=0
    
    
    elif t=="🍗 Крылышки 1пр(250гр)-20см":
        pos="04"
        kril_pr_kol=1
        kril_pr_photo=open("strip_pr.PNG", "br")
        b.send_photo(message.chat.id, photo=kril_pr_photo)
        kril_pr_photo.close()
        b.send_message(message.chat.id, "🍗 Крылышки пр\n\nОстрые куриные крылышки в хрустящей панировке\n\nЦена:25см(200гр)", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=4
    elif t=="⬅️ Назад" and pos=="04":
        pos="2"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=meenu())
        mm1=0
    elif mm1==4:
        kril_pr_kol=int(t)
        if kril_pr_ord not in orders:
            kril_pr_del=[kril_pr_ord, kril_pr_kol, price_kril_pr]
            orders.append(kril_pr_del)
        else:
            pass    
        price+=kril_pr_kol*price_kril_pr
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=meenu())
        
        mm1=0
    
    
    elif t=="🍗 Стрипсы(1кг)-75см":
        pos="05"
        strip_kg_kol=1.0
        strip_kg_photo=open("kril_kg.JPG", "br")
        b.send_photo(message.chat.id, photo=strip_kg_photo)
        strip_kg_photo.close()
        b.send_message(message.chat.id, "🍗 Стрипсы кг\n\nКуриное филе в хрустящей панировке\n\nЦена:75см(1кг)", reply_markup=Strip_kg())
        # if language=="ru":
        #     b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        # elif language=="tj":
        #     b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")

        # mm1=5



    elif t=="⬅️ Назад" and pos=="05":
        pos="2"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=meenu())
        mm1=0
    # elif mm1==5:
    #     strip_kg_kol=int(t)
    #     if strip_kg_ord not in orders:
    #         strip_kg_del=[strip_kg_ord, strip_kg_kol, price_strip_kg]
    #         orders.append(strip_kg_del)
    #     else:
    #         pass
    #     price+=strip_kg_kol*price_strip_kg
    #     b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=meenu())
    #
    #     mm1=0
    
    elif t=="🍗 Крылышки(1кг)-75см":
        pos="06"
        kril_kg_kol=1
        kril_kg_photo=open("kril_kg.JPG", "br")
        kril001=b.send_photo(message.chat.id, photo=kril_kg_photo)
        kril_kg_photo.close()
        b.send_message(message.chat.id, "🍗 Крылышки кг\n\nОстрые куриные крылышки в хрустящей панировке\n\nЦена:75см(кг)", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=6
    elif t=="⬅️ Назад" and pos=="06":
        pos="2"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=meenu())
        mm1=0
    elif mm1==6:
        kril_kg_kol=int(t)
        if kril_kg_ord not in orders:
            kril_kg_del=[kril_kg_ord, kril_kg_kol, price_kril_kg]
            orders.append(kril_kg_del)
        else:
            pass    
        price+=kril_kg_kol*price_kril_kg
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=meenu())
        mm1=0
    
    
    elif t=="🍗🥤 Комбо-25см":
        pos="07"
        kombo25_kol=1
        b.send_message(message.chat.id, "🍗🥤 Комбо 3в1-25см\n\nВ Комбо 3в1 входят:\nЧикен-бургер, картошка-фри  и Coca-cola 0.5\n\nЦена:25см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=7
    elif t=="⬅️ Назад" and pos=="07":
        pos="2"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=meenu())
        mm1=0
    elif mm1==7:
        kombo25_kol=int(t)
        if kombo25_ord not in orders:
            kombo25_del=[kombo25_ord, kombo25_kol, price_kombo25]
            orders.append(kombo25_del)
        else:
            pass    
        price+=kombo25_kol*price_kombo25
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=meenu())
        mm1=0
    
    
    elif t=="🍗🥤 Комбо-35см":
        pos="08"
        kombo35_kol=1
        b.send_message(message.chat.id, "🍗🥤 Комбо 5в1-35см\n\nВ Комбо 5в1 входят:\nСтрипсы (1пр), картошка-фри, булочка, сырный соус и Coca-cola 0.5\n\nЦена:35см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=8
    elif t=="⬅️ Назад" and pos=="08":
        pos="2"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=meenu())
        mm1=0
    elif mm1==8:
        kombo35_kol=int(t)
        if kombo35_ord not in orders:
            kombo35_del=[kombo35_ord, kombo35_kol, price_kombo35]
            orders.append(kombo35_del)
        else:
            pass    
        price+=kombo35_kol*price_kombo35
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=meenu())
        mm1=0
    
    
    elif t=="🌶🧄🧀 Соусы":
        pos="8"
        back_menu=1
        b.send_message(message.chat.id, "Наши соусы", reply_markup=souses())
    elif t=="⬅️ Назад" and pos=="5":
        pos="2"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=meenu())
        mm1=0

        
    elif t=="🧄 Чесночный соус":
        pos="0001"
        chesn_s_kol=1
        chesn_s_photo=open("chesn_s.JPG", "br")
        b.send_photo(message.chat.id, photo=chesn_s_photo)
        chesn_s_photo.close()
        b.send_message(message.chat.id, "🧄 Чесночный соус\n\nЦена:2см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=9
    elif t=="⬅️ Назад" and pos=="0001":
        pos="8"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=souses())
    elif mm1==9:
        pos="8"
        chesn_s_kol=int(t)
        if chesn_s_ord not in orders:
            chesn_s_del=[chesn_s_ord, chesn_s_kol, price_chesn_s]
            orders.append(chesn_s_del)
        else:
            pass    
        price+=chesn_s_kol*price_chesn_s
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=meenu())
        mm1=0
    
    
    elif t=="🌶 Острый соус":
        pos="0002"
        ostri_s_kol=1
        ostri_s_photo=open("ostri_s.JPG", "br")
        b.send_photo(message.chat.id, photo=ostri_s_photo)
        ostri_s_photo.close()
        b.send_message(message.chat.id, "🌶 Острый соус\n\nЦена:2см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=10
    elif t=="⬅️ Назад" and pos=="0002":
        pos="8"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=souses())
    elif mm1==10:
        pos="8"
        ostri_s_kol=int(t)
        if ostri_s_ord not in orders:
            ostri_s_del=[ostri_s_ord, ostri_s_kol, price_ostri_s]
            orders.append(ostri_s_del)
        else:
            pass    
        price+=ostri_s_kol*price_ostri_s
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=meenu())
        
        mm1=0
    
    
    elif t=="🧀 Сырный соус":
        pos="0003"
        sirni_s_kol=1
        sirni_s_photo=open("sirni_s.JPG", "br")
        b.send_photo(message.chat.id, photo=sirni_s_photo)
        sirni_s_photo.close()
        b.send_message(message.chat.id, "🧀 Сырный соус\n\nЦена:2см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=11
    elif t=="⬅️ Назад" and pos=="0003":
        pos="8"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=souses())
    elif mm1==11:
        pos="8"
        sirni_s_kol=int(t)
        if sirni_s_ord not in orders:
            sirni_s_del=[sirni_s_ord, sirni_s_kol, price_sirni_s]
            orders.append(sirni_s_del)
        else:
            pass    
        price+=sirni_s_kol*price_sirni_s
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=meenu())
        mm1=0
    

    elif t=="🥤 Напитки" and language=="ru":
        pos="4"
        b.send_message(message.chat.id, "🥤 Выберите продукт", reply_markup=napitki())
    elif t=="⬅️ Назад" and pos=="4" and language=="ru":
        pos="2"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=meenu())
    
    elif t=="🥤 Напитки" and language=="tj":
        pos="4"
        b.send_message(message.chat.id, "🥤 Маҳсулотро интихоб кунед", reply_markup=napitki("tj"))
    elif t=="⬅️ Бозгашт"and pos=="4" and language=="tj":
        pos="2"
        b.send_message(message.chat.id, "Маҳсулотро интихоб кунед", reply_markup=meenu("tj"))


    elif t=="☕️ Кофе":
        pos="coffee"
        coff=open("coffee.JPG", "rb")
        b.send_photo(message.chat.id, photo=coff)
        coff.close()
        b.send_message(message.chat.id, "☕️ Кофе\n\n..........\n...\nЦена:3см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=23
    elif t=="⬅️ Назад" and pos=="coffee":
        pos="4"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=napitki())
    elif mm1==23:
        pos="4"
        cof_kol=int(t)
        if cof_ord not in orders:
            cof_del=[cof_ord, cof_kol, price_cof]
            orders.append(cof_del)
        else:
            pass    
        price+=cof_kol*price_cof
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=napitki())
        mm1=0

    
    elif t=="🥤 Coca Cola 0.5":
        pos="001"
        ccola05=open("cc_05.JPG", "rb")
        b.send_photo(message.chat.id, photo=ccola05)
        ccola05.close()
        b.send_message(message.chat.id, "🥤 Coca cola 0.5\n\nЦена:5см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=12
    elif t=="⬅️ Назад" and pos=="001":
        pos="4"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=napitki())
    elif mm1==12:
        pos="4"
        cc05_kol=int(t)
        if cc05_ord not in orders:
            cc05_del=[cc05_ord, cc05_kol, price_cc05]
            orders.append(cc05_del)
        else:
            pass    
        price+=cc05_kol*price_cc05
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=napitki())
        mm1=0
    
    
    elif t=="🥤 Coca Cola 1.25" :
        pos="002"
        ccola125=open("cc_125.JPG", "rb")
        b.send_photo(message.chat.id, photo=ccola125)
        ccola125.close()
        b.send_message(message.chat.id, "🥤 Coca cola 1.25\n\nЦена:10см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=18
    elif t=="⬅️ Назад" and pos=="002":
        pos="4"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=napitki())
    elif mm1==18:
        pos="4"
        cc125_kol=int(t)
        if cc125_ord not in orders:
            cc125_del=[cc125_ord, cc125_kol, price_cc125]
            orders.append(cc125_del)
        else:
            pass
        price+=cc125_kol*price_cc125
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=napitki())
        
        mm1=0
    
    
    elif t=="🥤 Coca Cola 1.75" :
        pos="003"
        ccola175=open("cc_175.JPG", "rb")
        b.send_photo(message.chat.id, photo=ccola175)
        ccola175.close()
        b.send_message(message.chat.id, "🥤 Coca cola 1.75\n\nЦена:12см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=22
    elif t=="⬅️ Назад" and pos=="003":
        pos="4"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=napitki())
    elif mm1==22:
        pos="4"
        cc175_kol=int(t)
        if cc175_ord not in orders:
            cc175_del=[cc175_ord, cc175_kol, price_cc175]
            orders.append(cc175_del)
        else:
            pass    
        price+=cc175_kol*price_cc175
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=napitki())
        mm1=0
    
    elif t=="🥭 El-Rio mango" :
        pos="rio_man"
        rio_mang=open("elrio_mango.JPG", "rb")
        b.send_photo(message.chat.id, photo=rio_mang)
        rio_mang.close()
        b.send_message(message.chat.id, "🥭 El-Rio mango\n\nЦена:7см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=13
    elif t=="⬅️ Назад" and pos=="rio_man":
        pos="4"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=napitki())
    elif mm1==13:
        pos="4"
        rio_man_kol=int(t)
        if rio_man_ord not in orders:
            rio_man_del=[rio_man_ord, rio_man_kol, price_rio_man]
            orders.append(rio_man_del)
        else:
            pass    
        price+=rio_man_kol*price_rio_man
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=napitki())
        mm1=0
    
    elif t=="🫖 Fuse-tea 0.5" :
        pos="004"
        fftea=open("ftea_05.JPG", "rb")
        b.send_photo(message.chat.id, photo=fftea)
        fftea.close()
        b.send_message(message.chat.id, "🫖 Fuse-tea 0.5\n\nЦена:6см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=13
    elif t=="⬅️ Назад" and pos=="004":
        pos="4"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=napitki())
    elif mm1==13:
        pos="4"
        ftea05_kol=int(t)
        if ftea05_ord not in orders:
            ftea05_del=[ftea05_ord, ftea05_kol, price_ftea05]
            orders.append(ftea05_del)
        else:
            pass    
        price+=ftea05_kol*price_ftea05
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=napitki())
        mm1=0
    
    
    elif t=="🍊 Fanta 0.5" :
        pos="005"
        fant05=open("fan_05.JPG", "rb")
        b.send_photo(message.chat.id, photo=fant05)
        fant05.close()
        b.send_message(message.chat.id, "🍊 Fanta 0.5\n\nЦена:5см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=14
    elif t=="⬅️ Назад" and pos=="005":
        pos="4"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=napitki())
    elif mm1==14:
        pos="4"
        fan05_kol=int(t)
        if fan05_ord not in orders:
            fan05_del=[fan05_ord, fan05_kol, price_fan05]
            orders.append(fan05_del)
        else:
            pass    
        price+=fan05_kol*price_fan05
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=napitki())
        mm1=0
    
    
    elif t=="🍊 Fanta 1.25" :
        pos="006"
        fant125=open("fan_125.jpg", "rb")
        b.send_photo(message.chat.id, photo=fant125)
        fant125.close()
        b.send_message(message.chat.id, "🍊 Fanta 1.25\n\nЦена:10см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=21
    elif t=="⬅️ Назад" and pos=="006":
        pos="4"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=napitki())
    elif mm1==21:
        pos="4"
        fan125_kol=int(t)
        if fan125_ord not in orders:
            fan125_del=[fan125_ord, fan125_kol, price_fan125]
            orders.append(fan125_del)
        else:
            pass    
        price+=fan125_kol*price_fan125
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=napitki())
        mm1=0
    
    
    elif t=="🍊 Fanta 1.75" :
        pos="007"
        fant175=open("fan_175.jpeg", "rb")
        b.send_photo(message.chat.id, photo=fant175)
        fant175.close()
        b.send_message(message.chat.id, "🍊 Fanta 1.75\n\nЦена:12мс", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=23
    elif t=="⬅️ Назад" and pos=="0007":
        pos="4"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=napitki())
    elif mm1==23:
        pos="4"
        fan175_kol=int(t)
        if fan175_ord not in orders:
            fan175_del=[fan175_ord, fan175_kol, price_fan175]
            orders.append(fan175_del)
        else:
            pass    
        price+=fan175_kol*price_fan175
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=napitki())
        mm1=0
    
    
    elif t=="🧊 Bon-aqua 0.5":
        pos="008"
        bon05_ph=open("bon_05.JPG", "rb")
        b.send_photo(message.chat.id, photo=bon05_ph)
        bon05_ph.close()
        b.send_message(message.chat.id, "🧊 Bon-aqua 0.5\n\nЦена:3см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=15
    elif t=="⬅️ Назад" and pos=="008":
        pos="4"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=napitki())
    elif mm1==15:
        pos="4"
        bon05_kol=int(t)
        if bon05_ord not in orders:
            bon05_del=[bon05_ord, bon05_kol, price_bon05]
            orders.append(bon05_del)
        else:
            pass    
        price+=bon05_kol*price_bon05
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=napitki())
        mm1=0
    
    
    elif t=="🧊 Bon-aqua 1":
        pos="009"
        bon1_ph=open("bon_1.JPG", "rb")
        b.send_photo(message.chat.id, photo=bon1_ph)
        bon1_ph.close()
        b.send_message(message.chat.id, "🧊 Bon-aqua 1\n\nЦена:5см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=16
    elif t=="⬅️ Назад" and pos=="009":
        pos="4"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=napitki())
    elif mm1==16:
        pos="4"
        bon1_kol=int(t)
        if bon1_ord not in orders:
            bon1_del=[bon1_ord, bon1_kol, price_bon1]
            orders.append(bon1_del)
        else:
            pass    
        price+=bon1_kol*price_bon1
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=napitki())
        mm1=0
    
    
    elif t=="🧊 Bon-aqua 1.5":
        pos="010"
        bon15_ph=open("bon_15.JPG", "rb")
        b.send_photo(message.chat.id, photo=bon15_ph)
        bon15_ph.close()
        b.send_message(message.chat.id, "🧊 Bon-aqua 1.5\n\nЦена:5см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=17
    elif t=="⬅️ Назад" and pos=="010":
        pos="4"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=napitki())
    elif mm1==17:
        pos="4"
        bon15_kol=int(t)
        if bon15_ord not in orders:
            bon15_del=[bon15_ord, bon15_kol, price_bon15]
            orders.append(bon15_del)
        else:
            pass    
        price+=bon15_kol*price_bon15
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=napitki())
        mm1=0
    
    
    
    elif t=="🍋 Sprite 1":
        pos="011"
        spr_ph=open("sprite_1.JPG", "rb")
        b.send_photo(message.chat.id, photo=spr_ph)
        spr_ph.close()
        b.send_message(message.chat.id, "🍋 Sprite 1\n\nЦена:8см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=19
    elif t=="⬅️ Назад" and pos=="011":
        pos="4"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=napitki())
    elif mm1==19:
        pos="4"
        spr1_kol=int(t)
        if spr1_ord not in orders:
            spr1_del=[spr1_ord, spr1_kol, price_spr1]
            orders.append(spr1_del)
        else:
            pass    
        price+=spr1_kol*price_spr1
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=napitki())
        mm1=0
    
    
    elif t=="🥤 RC cola 1":
        pos="012"
        rc_ph=open("rc_1.JPG", "rb")
        b.send_photo(message.chat.id, photo=rc_ph)
        rc_ph.close()
        b.send_message(message.chat.id, "🥤 RC cola 1л\n\nЦена:8см", reply_markup=Zakaz())
        if language=="ru":    
            b.send_message(message.chat.id, "*Выберите* или *введите* количество", parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.chat.id, "*Интихоб* ё Маблагро *дохил* кунед", parse_mode="Markdown")
        
        mm1=20
    elif t=="⬅️ Назад" and pos=="012":
        pos="4"
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=napitki())
    elif mm1==20:
        pos="4"
        rc1_kol=int(t)
        if rc1_ord not in orders:
            rc1_del=[rc1_ord, rc1_kol, price_rc1]       
            orders.append(rc1_del)
        else:
            pass    
        price+=rc1_kol*price_rc1
        b.send_message(message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=napitki())
        mm1=0
    
    
    
#                            DELETE
    elif t=="🍔 Чикен-Бургер ❌" and bur_eddd==True:
        orders.remove(BUR_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        bur_deleted=b.send_message(message.chat.id, f"{bur_ord} удалён и вашего списка заказов")
        
        b.delete_message(message.chat.id, bur_deleted.id)
    
    elif t=="🍔 Чикен-Бургер(15) ❌" and bur15_eddd==True:
        orders.remove(BUR15_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        bur15_deleted=b.send_message(message.chat.id, f"{bur15_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, bur15_deleted.id)

    elif t=="🍟 Фри ❌" and fri_eddd==True:
        orders.remove(FRI_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        fri_deleted=b.send_message(message.chat.id, f"{fri_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, fri_deleted.id)
    
    elif t=="🍗 Стрипсы (пр) ❌" and strip_pr_eddd==True:
        orders.remove(strip_pr_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        str_pr_deleted=b.send_message(message.chat.id, f"{strip_pr_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, str_pr_deleted.id)
    
    elif t=="🍗 Крылышки (пр) ❌" and kril_pr_eddd==True:
        orders.remove(kril_pr_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        krl_pr_deleted=b.send_message(message.chat.id, f"{kril_pr_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, krl_pr_deleted.id)
    
    elif t=="🍗 Стрипсы (кг) ❌" and strip_kg_eddd==True:
        orders.remove(strip_kg_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        str_kg_deleted=b.send_message(message.chat.id, f"{strip_kg_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, str_kg_deleted.id)
    
    elif t=="🍗 Крылышки (кг) ❌" and kril_kg_eddd==True:
        orders.remove(kril_kg_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        krl_kg_deleted=b.send_message(message.chat.id, f"{kril_kg_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, krl_kg_deleted.id)
    
    elif t=="🍗🥤 Комбо-25см ❌" and kombo25_eddd==True:
        orders.remove(kombo25_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        kombo25_deleted=b.send_message(message.chat.id, f"{kombo25_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, kombo25_deleted.id)
    
    elif t=="🍗🥤 Комбо-35см ❌" and kombo35_eddd==True:
        orders.remove(kombo35_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        kombo35_deleted=b.send_message(message.chat.id, f"{kombo35_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, kombo35_deleted.id)
    
    elif t=="🧄 Чесночный соус ❌" and chesn_s_eddd==True:
        orders.remove(chesn_s_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        chesn_s_deleted=b.send_message(message.chat.id, f"{chesn_s_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, chesn_s_deleted.id)
    
    elif t=="🌶 Острый соус ❌" and ostri_s_eddd==True:
        orders.remove(ostri_s_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        ostri_s_deleted=b.send_message(message.chat.id, f"{ostri_s_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, ostri_s_deleted.id)
    elif t=="🧀 Сырный соус ❌" and sirni_s_eddd==True:
        orders.remove(sirni_s_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        sirni_s_deleted=b.send_message(message.chat.id, f"{sirni_s_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, sirni_s_deleted.id)
    
    elif t=="🥤 Coca Cola 0.5 ❌" and cc05_eddd==True:
        orders.remove(cc05_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        cc05_deleted=b.send_message(message.chat.id, f"{cc05_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, cc05_deleted.id)
    
    elif t=="🥤 Coca Cola 1.25 ❌" and cc125_eddd==True:
        orders.remove(cc125_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        cc125_deleted=b.send_message(message.chat.id, f"{cc125_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, cc125_deleted.id)
    
    elif t=="🥤 Coca Cola 1.75 ❌" and cc175_eddd==True:
        orders.remove(cc175_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        cc175_deleted=b.send_message(message.chat.id, f"{cc175_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, cc175_deleted.id)
    
    elif t=="🍊 Fanta 0.5 ❌" and fan05_eddd==True:
        orders.remove(fan05_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        fan05_deleted=b.send_message(message.chat.id, f"{fan05_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, fan05_deleted.id)
    
    elif t=="🍊 Fanta 1.25 ❌" and fan125_eddd==True:
        orders.remove(fan125_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        fan125_deleted=b.send_message(message.chat.id, f"{fan125_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, fan125_deleted.id)
    
    elif t=="🍊 Fanta 1.75 ❌" and fan175_eddd==True:
        orders.remove(fan175_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        fan175_deleted=b.send_message(message.chat.id, f"{fan175_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, fan175_deleted.id)
    
    elif t=="🍋 Sprite 1 ❌" and spr1_eddd==True:
        orders.remove(spr1_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        spr1_deleted=b.send_message(message.chat.id, f"{spr1_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, spr1_deleted.id)
    
    elif t=="🥭 El-Rio mango ❌" and ftea05_eddd==True:
        orders.remove(ftea05_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        ftea05_deleted=b.send_message(message.chat.id, f"{ftea05_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, ftea05_deleted.id)

    elif t=="🫖 Fuse-tea 0.5 ❌" and ftea05_eddd==True:
        orders.remove(ftea05_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        ftea05_deleted=b.send_message(message.chat.id, f"{ftea05_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, ftea05_deleted.id)
    elif t=="🥤 RC cola 1 ❌" and rc1_eddd==True:
        orders.remove(rc1_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        rc1_deleted=b.send_message(message.chat.id, f"{rc1_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, rc1_deleted.id)
    elif t=="🧊 Bon-aqua 0.5 ❌" and bon05_eddd==True:
        orders.remove(bon05_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        bon05_deleted=b.send_message(message.chat.id, f"{bon05_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, bon05_deleted.id)
    elif t=="🧊 Bon-aqua 1 ❌" and bon1_eddd==True:
        orders.remove(bon1_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        bon1_deleted=b.send_message(message.chat.id, f"{bon1_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, bon1_deleted.id)
    elif t=="🧊 Bon-aqua 1.5 ❌" and bon15_eddd==True:
        orders.remove(bon15_del)
        b.delete_message(message.chat.id, karzina.id)
        b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
        
        bon15_deleted=b.send_message(message.chat.id, f"{bon15_ord} удалён и вашего списка заказов")
        b.delete_message(message.chat.id, bon15_deleted.id)
    

    #elif t=="✏️ Добавить":
    #    b.send_message(message.chat.id, text="Выберите продукт", reply_markup=meenu())
    
    elif t=="🔄 очистить корзину":
        orders=[]
        b.send_message(message.chat.id, "Ваша карзина очищена.\nМожете сделать новый заказ")
        b.send_message(message.chat.id, "Выберите продукт", reply_markup=meenu())
    elif t=="🔄 Тозакунӣ":
        orders=[]
        b.send_message(message.chat.id, "Сабад тоза карда шуд")
        b.send_message(message.chat.id, "Мо аз куҷо сар кунем?", reply_markup=meenu("tj"))
    
    elif t=="⬅️ Назад" and back_edor==True:
        b.delete_message(message.chat.id, instr.id)
        b.delete_message(message.chat.id, inst_show.id)
        #b.delete_message(message.chat.id, message.text.id)
        #b.send_message(message.chat.id, "Menu", reply_markup=MENU_second())
    
    
    #Delet from orders

    
    
    
    
    
    #elif t=="📥Карзина":
    #    inst_show=b.send_message(message.chat.id, text=show_order(), reply_markup=Edit_ord(), parse_mode="Markdown")
    #    instr=b.send_message(message.chat.id, text="«❌ Название продукта» - удалить из корзины\n«🔄 Очистить» - полностью очистить корзину", reply_markup=Edit_ord())
    
    
    elif t=="🛒 Оформить заказ":
        pos="6"
        if orders!=[]:
            b.send_message(message.chat.id, "Пожалуйста, пришлите свой номер телефона", reply_markup=get_contact())        
        else:
            b.send_message(message.chat.id, "Вы ещё ни чего не заказали")
    elif t=="🛒 Ба расмият даровардан":
        pos="6"
        if orders!=[]:
            b.send_message(message.chat.id, "Лутфан рақами телефони худро фиристед", reply_markup=get_contact("tj"))        
        else:
            b.send_message(message.chat.id, "Маҳсулотро ба ароба илова кунед")
    
    elif t=="⬅️ Назад" and pos=="6" and language=="ru":
        pos="2"
        b.send_message(message.chat.id, text="Выберите продукт", reply_markup=meenu())
    elif t=="⬅️ Бозгашт" and pos=="6" and language=="tj":
        pos="2"
        b.send_message(message.chat.id, text="Выберите продукт", reply_markup=meenu())
    
    

#    elif t=="⬅️ Назад" and pos=="8":
#        pos="2"
#        if orders!=[]:
#            b.send_message(message.chat.id, "Оставьте ваш номер чтобы мы связались с вами", reply_markup=get_contact())        
#        else:
#            b.send_message(message.chat.id, "Вы ещё ни чего не заказали")



    elif pos=="7" and orders!=[]:
        if t=="💳 Terminal":
            pay_way="💳 Terminal"
            b.send_message(message.chat.id, "Отправьте тип доставки", reply_markup=Get_way())
            pos="8"
        elif t=="💵 Пули нақд" and language=="ru":
            pay_way="💵 Наличными"
            b.send_message(message.chat.id, "Навъи интиқолро интихоб кунед", reply_markup=Get_way())
            pos="8"
        
        elif t=="💵 Наличными" and language=="ru":
            pay_way="💵 Наличными"
            b.send_message(message.chat.id, "Отправьте тип доставки", reply_markup=Get_way())
            pos="8"
        else:
            b.send_message(message.chat.id, "Отправьте правильный тип оплаты")


    
        

    elif pos=="8":
        if t=="🏫 Самовывоз" and language=="ru":
            get_way="🏫 Самовывоз"
            b.send_message(message.chat.id, text=show_order(), parse_mode="Markdown", reply_markup=send_o())
            pos="9"
        elif t=="🏫 Кашида гирифтан" and language=="tj":
            get_way="🏫 Самовывоз"
            b.send_message(message.chat.id, text=show_order(), parse_mode="Markdown", reply_markup=send_o("tj"))
            pos="9"
        elif t=="🛵 Доставка" and language=="ru":
            get_way="🛵 Доставка"
            b.send_message(message.chat.id, "Пожалуйста, отправьте место доставки", reply_markup=Location())
        
        elif t=="🛵 Таҳвил" and language=="tj":
            get_way="🛵 Доставка"
            b.send_message(message.chat.id, "Пожалуйста, отправьте место доставки", reply_markup=Location())

        else:
            b.send_message(message.chat.id, "Отправьте правильный тип получения заказа")

    elif t=="⬅️ Назад" and pos=="8":
        pos="7"
        b.send_message(message.chat.id, text="Отправьте способ оплаты", reply_markup=s_pay())



    elif t=="✍️ Написать адрес" and orders!=[]:
        b.send_message(message.chat.id, "Напишите ваш точный адрес куда надо доставить:")
        adr=True
    elif adr==True:
        adres=message.text
        b.send_message(message.chat.id, text=show_order(), parse_mode="Markdown", reply_markup=send_o())
        pos="9"
        
    elif t=="⬅️ Назад" and pos=="9":
        pos="8"
        b.send_message(message.chat.id, "Отправьте тип доставки", reply_markup=Get_way())
        
    else:
            pass
    
    
    
    if t=="✅ Подтвердить заказ" and pos=="9":
        sec=time.time()
        order_story.append(f"{time.ctime(sec)}\n{show_order()}")
        otp_zakaz=b.send_message(admin, text=send_order(message.from_user.first_name), reply_markup=Confirm(), parse_mode="Markdown")

        #b.send_message(admin, text=f"Заказ:\n{order}\nСумма заказа:{price}см\nТочка:{place}\nСпособ получения заказа:{get_way}\nВремя:{time}\n\nИмя:"+str(message.from_user.name)+"\nСсылка:@"+str(message.from_user.username))
        b.send_message(message.chat.id, "Ваш запрос успешно отпрален!\nОжидайте звонка", reply_markup=Main_menu())
        #b.send_message(message.chat.id, text="Главная меню", reply_markup=Main_menu())
    
#   
    
    if t=="🕔 Самовывоз дата" and finish==True and language=="ru":
        b.send_message(message.from_user.id, f"🕔 Отправить самовывоз дата")
        hz=3
    elif t=="🕔 Вақти гирифтан" and finish==True and language=="tj":
        b.send_message(message.from_user.id, f"🕔 Вақти гирифтани фармоишро ворид кунед")
        hz=3
    elif hz==3:
        Time=message.text
        hz=0
        if language=="ru":
            b.send_message(message.from_user.id, text=show_order(), reply_markup=send_o(), parse_mode="Markdown")
        elif language=="tj":
            b.send_message(message.from_user.id, text=show_order("tj"), reply_markup=send_o("tj"), parse_mode="Markdown")

#   
    elif t=="💬 Комментарий к заказу" and finish==True and language=="ru":
        pos="kom"
        b.send_message(message.chat.id, "Отправьте коментарии", reply_markup=Back())
        hz=5
    elif t=="💬 Дар бораи фармоиш шарҳ диҳед" and finish==True and language=="tj":
        pos="kom"
        b.send_message(message.chat.id, "Отправьте коментарии", reply_markup=Back("tj"))
        hz=5
    elif t=="⬅️ Назад" and pos=="kom" and language=="ru":
        pos="2"
        b.send_message(message.from_user.id, text=show_order(), reply_markup=send_o(), parse_mode="Markdown")
    elif t=="⬅️ Бозгашт" and pos=="kom" and language=="tj":
        pos="2"
        b.send_message(message.from_user.id, text=show_order("tj"), reply_markup=send_o("tj"), parse_mode="Markdown")
    elif hz==5:
        komment=message.text
        b.send_message(message.from_user.id, text=show_order(), reply_markup=send_o(), parse_mode="Markdown")

#        
    elif t=="❌ Отмена" and pos=="77":
        order=""
        price=0
        adres=""
        pay_way=""
        place=""
        get_way=""
        Time=""
        b.delete_message(chat_id=message.chat.id, message_id=otp_zakaz.id)
        b.send_message(message.chat.id, "Карзина удалён!\nМожете сделать заказ заного", reply_markup=meenu())
    else:
        pass
    

    if t=="🥤 Coca Cola 0.3":          #        Coca cola
        #ccola=open("ccola.JPEG", "rb")
        #b.send_photo(message.chat.id, photo=ccola)
        
        #b.send_message(message.chat.id, "🥤 Coca cola 0.3 (см)", reply_markup=cc03())
        b.send_message(message.chat.id, "Простите но у нас пока нету Coca-Cola 0.3")
    
    
    else:
        pass
            

        
@b.callback_query_handler(func=lambda call:True if call.data=="to_order" else False)
def Order(call):
    global menu_mess_id
    menu_mess_id=b.send_message(call.message.chat.id, "Выберите продукт", reply_markup=meenu())
    #print(call.message.chat.id)

@b.callback_query_handler(func=lambda call:True if call.data=="pls_bur" or call.data=="min_bur" or call.data=="add_kar_bur" else False)

def pl_mi_bur(c):
    global bur_kol, order, price, bur1_ord, Zakaz_index, price_bur, bur_ord, BUR_del
    if c.data=="pls_bur":
        bur_kol=bur_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍔 Чикен-Бургер", reply_markup=Zakaz())
    elif c.data=="min_bur":
        if bur_kol==1:
            pass
        else:
            bur_kol=bur_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍔 Чикен-Бургер", reply_markup=Zakaz())
    elif c.data=="add_kar_bur":
        #Zakaz=[bur1_ord, bur_kol, price_bur]
        if bur_ord in orders:
            #print(bur_ord)
            """burge=[bur_ord, bur_kol, price_bur]
            orders[Zakaz_index]=burge"""
        else:
            
            BUR_del=[bur_ord, bur_kol, price_bur]
            orders.append(BUR_del)
            Zakaz_index=orders.index(BUR_del)
        price+=bur_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")
        

@b.callback_query_handler(func=lambda call:True if call.data=="pls_fri" or call.data=="min_fri" or call.data=="add_kar_fri" else False)

def pl_mi_fri(c):
    global FRI_del, fri_kol, order, price, fri1_ord, fri_index, fri
    if c.data=="pls_fri":
        fri_kol=fri_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍟 Фри", reply_markup=Fri())
    elif c.data=="min_fri":
        if fri_kol==1:
            pass
        else:
            fri_kol=fri_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍟 Фри", reply_markup=Fri())
    elif c.data=="add_kar_fri":
        if fri_ord in orders:
            #print(bur_ord)
            FRI_del=[fri_ord, fri_kol, price_fri]
            orders[fri_index]=fri
        else:
            fri1_ord=fri_ord
            FRI_del=[fri1_ord, fri_kol, price_fri]
            orders.append(FRI_del)
            fri_index=orders.index(FRI_del)
        price+=fri_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")
        

@b.callback_query_handler(func=lambda call:True if call.data=="pls_strip_pr" or call.data=="min_strip_pr" or call.data=="add_kar_strip_pr" else False)

def pl_mi_strip_pr(c):
    global strip_pr_kol, order, price, strip_pr1_ord, strip_pr_index, strip_pr_del
    if c.data=="pls_strip_pr":
        strip_pr_kol=strip_pr_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍗 Стрипсы пр", reply_markup=Strip_pr())
    elif c.data=="min_strip_pr":
        if strip_pr_kol==1:
            pass
        else:
            strip_pr_kol=strip_pr_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍗 Стрипсы пр", reply_markup=Strip_pr())
    elif c.data=="add_kar_strip_pr":
        if strip_pr_ord in orders:
            #print(bur_ord)
            strip_pr=[strip_pr_ord, strip_pr_kol, price_strip_pr]
            orders[strip_pr_index]=strip_pr
        else:
            strip_pr1_ord=strip_pr_ord
            strip_pr_del=[strip_pr1_ord, strip_pr_kol, price_strip_pr]
            orders.append(strip_pr_del)
            strip_pr_index=orders.index(strip_pr_del)
        price+=strip_pr_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")

@b.callback_query_handler(func=lambda call:True if call.data=="pls_kril_pr" or call.data=="min_kril_pr" or call.data=="add_kar_kril_pr" else False)

def pl_mi_kril_pr(c):
    global kril_pr_kol, order, price, kril_pr_del, kril_pr_index
    if c.data=="pls_kril_pr":
        kril_pr_kol=kril_pr_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍗 Крылышки пр", reply_markup=Kril_pr())
    elif c.data=="min_kril_pr":
        if kril_pr_kol==1:
            pass
        else:
            kril_pr_kol=kril_pr_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍗 Крылышки пр", reply_markup=Kril_pr())
    elif c.data=="add_kar_kril_pr":
        if kril_pr_ord in orders:
            #print(bur_ord)
            kril_pr=[kril_pr_ord, kril_pr_kol, price_kril_pr]
            orders[kril_pr_index]=kril_pr
        else:
            kril_pr1_ord=kril_pr_ord
            kril_pr_del=[kril_pr1_ord, kril_pr_kol, price_kril_pr]
            orders.append(kril_pr_del)
            kril_pr_index=orders.index(kril_pr_del)
        price+=kril_pr_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")

@b.callback_query_handler(func=lambda call:True if call.data=="pls1" or call.data=="min1" or call.data=="pls01" or call.data=="min01" or call.data=="add" else False)

def pl_mi_strip_kg(c):
    global strip_kg_kol, order, price, strip_kg_del, strip_kg_ord, mm1, price_strip_kg, orders

    if c.data=="pls1":
        strip_kg_kol = strip_kg_kol+1
        price_strip_kg = strip_kg_kol * 75
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text=f"🍗 Стрипсы кг\n\nКуриное филе в хрустящей панировке\n\n{strip_kg_kol}kg = {price_strip_kg}som", reply_markup=Strip_kg())

    elif c.data=="min1":
        if strip_kg_kol<=1:
            pass
        else:
            strip_kg_kol = strip_kg_kol-1
            price_strip_kg = strip_kg_kol * 75
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text=f"🍗 Стрипсы кг\n\nКуриное филе в хрустящей панировке\n\n{strip_kg_kol}kg = {price_strip_kg}som", reply_markup=Strip_kg())

    elif c.data=="pls01":
        strip_kg_kol = strip_kg_kol+0.10
        price_strip_kg = strip_kg_kol * 75
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text=f"🍗 Стрипсы кгc\n\n{strip_kg_kol}kg = {price_strip_kg}som", reply_markup=Strip_kg())

    elif c.data=="min01":
        if strip_kg_kol==0.1 or strip_kg_kol <= 0.1:
            pass
        else:
            strip_kg_kol = strip_kg_kol-(1/10)
            price_strip_kg = round(strip_kg_kol, 1) * 75
            print(price_strip_kg)
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text=f"🍗 Стрипсы кг\n\nКуриное филе в хрустящей панировке\n\n{strip_kg_kol}kg = {price_strip_kg}som", reply_markup=Strip_kg())



    if c.data=="add":
        if strip_kg_ord not in orders:
            strip_kg_del = [strip_kg_ord, strip_kg_kol, price_strip_kg]
            orders.append(strip_kg_del)
            price_strip_kg += strip_kg_kol * price_strip_kg
            b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?", reply_markup=meenu())
            mm1 = 0
        else:
            pass






    # elif c.data=="add_str_kg":
    #     if strip_kg_ord in orders:
    #         #print(bur_ord)
    #         strip_kg=[strip_kg_ord, strip_kg_kol, price_strip_kg]
    #         orders[strip_kg_index]=strip_kg
    #     else:
    #         strip_kg1_ord=strip_kg_ord
    #         strip_kg_del=[strip_kg1_ord, strip_kg_kol, price_strip_kg]
    #         orders.append(strip_kg_del)
    #         strip_kg_index=orders.index(strip_kg_del)
    #     price+=strip_kg_sum_pr
    #     b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")

@b.callback_query_handler(func=lambda call:True if call.data=="pls_kril_kg" or call.data=="min_kril_kg" or call.data=="add_kar_kril_kg" else False)

def pl_mi_kril_kg(c):
    global kril_kg_kol, order, price, kril_kg_del, mm1
    if c.data=="pls_kril_kg":
        kril_kg_kol=kril_kg_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍗 Крылышки кг", reply_markup=Kril_kg())
    elif c.data=="min_kril_kg":
        if kril_kg_kol==1:
            pass
        else:
            kril_kg_kol=kril_kg_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍗 Крылышки кг", reply_markup=Kril_kg())
    elif c.data=="add_kar_kril_kg":
        pass
        #
        # if kril_kg_ord in orders:
        #     #print(bur_ord)
        #     kril_kg=[kril_kg_ord, kril_kg_kol, price_kril_kg]
        #     orders[kril_kg_index]=kril_kg
        # else:
        #     kril_kg1_ord=kril_kg_ord
        #     kril_kg_del=[kril_kg1_ord, kril_kg_kol, price_kril_kg]
        #     orders.append(kril_kg_del)
        #     kril_kg_index=orders.index(kril_kg_del)
        # price+=kril_kg_sum_pr
        # b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")
@b.callback_query_handler(func=lambda call:True if call.data=="one_kril" or call.data=="two_kril" or call.data=="three_kril" or call.data=="four_kril" or call.data=="five_kril" or call.data=="six_kril" or call.data=="seven_kril" or call.data=="eight_kril" or call.data=="nine_kril" or call.data=="zero_kril" or call.data=="del_kril" or call.data=="del_all_kril" or call.data=="kril_kilo" or call.data=="add_kar_kril_sm" else False)
def sk(call):
    global chisla_kril, kril_som
    c=call.data
    if c=="one_kril":
        chisla_kril+=1
        b.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.chat.id, text=f"{int(chisla_kril)}см = {round(int(chisla_kril)*13.333, 1)}грамм\n{int(chisla_kril)} сомон", reply_markup=kril_som())
    elif c=="two_kril":
        chisla_kril+=2
        b.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.chat.id, text=f"{int(chisla_kril)}см = {round(int(chisla_kril)*13.333, 1)}грамм\n{int(chisla_kril)} сомон", reply_markup=kril_som())
    elif c=="three_kril":
        chisla_kril+=3
        b.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.chat.id, text=f"{int(chisla_kril)}см = {round(int(chisla_kril)*13.333, 1)}грамм\n{int(chisla_kril)} сомон", reply_markup=kril_som())
    elif c=="four_kril":
        chisla_kril+=4
        b.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.chat.id, text=f"{int(chisla_kril)}см = {round(int(chisla_kril)*13.333, 1)}грамм\n{int(chisla_kril)} сомон", reply_markup=kril_som())
    elif c=="five_kril":
        chisla_kril+=5
        b.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.chat.id, text=f"{int(chisla_kril)}см = {round(int(chisla_kril)*13.333, 1)}грамм\n{int(chisla_kril)} сомон", reply_markup=kril_som())
    elif c=="six_kril":
        chisla_kril+=6
        b.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.chat.id, text=f"{int(chisla_kril)}см = {round(int(chisla_kril)*13.333, 1)}грамм\n{int(chisla_kril)} сомон", reply_markup=kril_som())
    elif c=="seven_kril":
        chisla_kril+=7
        b.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.chat.id, text=f"{int(chisla_kril)}см = {round(int(chisla_kril)*13.333, 1)}грамм\n{int(chisla_kril)} сомон", reply_markup=kril_som())
    elif c=="eight_kril":
        chisla_kril+=8
        b.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.chat.id, text=f"{int(chisla_kril)}см = {round(int(chisla_kril)*13.333, 1)}грамм\n{int(chisla_kril)} сомон", reply_markup=kril_som())
    elif c=="nine_kril":
        chisla_kril+=9
        b.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.chat.id, text=f"{int(chisla_kril)}см = {round(int(chisla_kril)*13.333, 1)}грамм\n{int(chisla_kril)} сомон", reply_markup=kril_som())
    elif c=="zero_kril":
        chisla_kril+=0
        b.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.chat.id, text=f"{int(chisla_kril)}см = {round(int(chisla_kril)*13.333, 1)}грамм\n{int(chisla_kril)} сомон", reply_markup=kril_som())



@b.callback_query_handler(func=lambda call:True if call.data=="pls_kombo25" or call.data=="min_kombo25" or call.data=="add_kar_kombo25" else False)

def pl_mi_kombo25(c):
    global kombo25_kol, order, price, kombo25_del,kombo25_index
    if c.data=="pls_kombo25":
        kombo25_kol=kombo25_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍗🥤 Комбо 3в1-25см", reply_markup=Kombo25())
    elif c.data=="min_kombo25":
        if kombo25_kol==1:
            pass
        else:
            kombo25_kol=kombo25_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍗🥤 Комбо 3в1-25см", reply_markup=Kombo25())
    elif c.data=="add_kar_kombo25":
        if kombo25_ord in orders:
            #print(bur_ord)
            kombo25=[kombo25_ord, kombo25_kol, price_kombo25]
            orders[kombo25_index]=kombo25
        else:
            kombo251_ord=kombo25_ord
            kombo25_del=[kombo251_ord, kombo25_kol, price_kombo25]
            orders.append(kombo25_del)
            kombo25_index=orders.index(kombo25_del)
        price+=kombo25_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")

@b.callback_query_handler(func=lambda call:True if call.data=="pls_kombo35" or call.data=="min_kombo35" or call.data=="add_kar_kombo35" else False)

def pl_mi_kombo35(c):
    global kombo35_kol, order, price, kombo35_index
    if c.data=="pls_kombo35":
        kombo35_kol=kombo35_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍗🥤 Комбо 5в1-35см", reply_markup=Kombo35())
    elif c.data=="min_kombo35":
        if kombo35_kol==1:
            pass
        else:
            kombo35_kol=kombo35_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍗🥤 Комбо 5в1-35см", reply_markup=Kombo35())
    elif c.data=="add_kar_kombo35":
        if kombo35_ord in orders:
            #print(bur_ord)
            kombo35=[kombo35_ord, kombo35_kol, price_kombo35]
            orders[kombo35_index]=kombo35
        else:
            kombo351_ord=kombo35_ord
            kombo35_del=[kombo351_ord, kombo35_kol, price_kombo35]
            orders.append(kombo35_del)
            kombo35_index=orders.index(kombo35_del)
        price+=kombo35_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")

#            Coca Cola 03
"""
@b.callback_query_handler(func=lambda call:True if call.data=="pls_cc03" or call.data=="min_cc03" or call.data=="add_kar_cc03" else False)

def pl_mi_cc03(c):
    global cc03_kol, order, price
    if c.data=="pls_cc03":
        cc03_kol=cc03_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🥤 Coca cola 0.3", reply_markup=cc03())
    elif c.data=="min_cc03":
        if cc03_kol==1:
            pass
        else:
            cc03_kol=cc03_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🥤 Coca cola 0.3", reply_markup=cc03())
    elif c.data=="add_kar_cc03":
        if order=="":
            order=cc03_ord
        else:
            order+=", "+cc03_ord
        price+=cc03_sum_pr
        b.send_message(c.message.chat.id, "Добавлено в корзину!")
        b.send_message(c.message.chat.id, "menu", reply_markup=Main_menu()
"""
@b.callback_query_handler(func=lambda call:True if call.data=="pls_cc05" or call.data=="min_cc05" or call.data=="add_kar_cc05" else False)

def pl_mi_cc05(c):
    global cc05_kol, order, price, cc05_del, cc05_index
    if c.data=="pls_cc05":
        cc05_kol=cc05_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🥤 Coca cola 0.5", reply_markup=CC05())
    elif c.data=="min_cc05":
        if cc05_kol==1:
            pass
        else:
            cc05_kol=cc05_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🥤 Coca cola 0.5", reply_markup=CC05())
    elif c.data=="add_kar_cc05":
        if cc05_ord in orders:
            #print(bur_ord)
            cc05=[cc05_ord, cc05_kol, price_cc05]
            orders[cc05_index]=cc05
        else:
            cc051_ord=cc05_ord
            cc05_del=[cc051_ord, cc05_kol, price_cc05]
            orders.append(cc05_del)
            cc05_index=orders.index(cc05_del)
        price+=cc05_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")
@b.callback_query_handler(func=lambda call:True if call.data=="pls_fan05" or call.data=="min_fan05" or call.data=="add_kar_fan05" else False)

def pl_mi_fan05(c):
    global fan05_kol, order, price, fan05_index
    if c.data=="pls_fan05":
        fan05_kol=fan05_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍊 Fanta 0.5", reply_markup=Fan05())
    elif c.data=="min_fan05":
        if fan05_kol==1:
            pass
        else:
            fan05_kol=fan05_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍊 Fanta 0.5", reply_markup=Fan05())
    elif c.data=="add_kar_fan05":
        if fan05_ord in orders:
            #print(bur_ord)
            fan05=[fan05_ord, fan05_kol, price_fan05]
            orders[fan05_index]=fan05
        else:
            fan051_ord=fan05_ord
            fan05_del=[fan051_ord, fan05_kol, price_fan05]
            orders.append(fan05_del)
            fan05_index=orders.index(fan05_del)
        price+=fan05_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")

@b.callback_query_handler(func=lambda call:True if call.data=="pls_bon05" or call.data=="min_bon05" or call.data=="add_kar_bon05" else False)

def pl_mi_bon05(c):
    global bon05_kol, order, price, bon05_del, bon05_index
    if c.data=="pls_bon05":
        bon05_kol=bon05_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🧊 Bon-aqua 0.5", reply_markup=Bon_aqua05())
    elif c.data=="min_bon05":
        if bon05_kol==1:
            pass
        else:
            bon05_kol=bon05_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🧊 Bon-aqua 0.5", reply_markup=Bon_aqua05())
    elif c.data=="add_kar_bon05":
        if bon05_ord in orders:
            #print(bur_ord)
            bon05=[bon05_ord, bon05_kol, price_bon05]
            orders[bon05_index]=bon05
        else:
            bon051_ord=bon05_ord
            bon05_del=[bon051_ord, bon05_kol, price_bon05]
            orders.append(bon05_del)
            bon05_index=orders.index(bon05_del)
        price+=bon05_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")

@b.callback_query_handler(func=lambda call:True if call.data=="pls_bon1" or call.data=="min_bon1" or call.data=="add_kar_bon1" else False)

def pl_mi_bon1(c):
    global bon1_kol, order, price, bon1_del, bon1_index
    if c.data=="pls_bon1":
        bon1_kol=bon1_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🧊 Bon-aqua 1л", reply_markup=Bon_aqua1())
    elif c.data=="min_bon1":
        if bon1_kol==1:
            pass
        else:
            bon1_kol=bon1_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🧊 Bon-aqua 1л", reply_markup=Bon_aqua1())
    elif c.data=="add_kar_bon1":
        if bon1_ord in orders:
            #print(bur_ord)
            bon1=[bon1_ord, bon1_kol, price_bon1]
            orders[bon1_index]=bon1
        else:
            bon11_ord=bon1_ord
            bon1_del=[bon11_ord, bon1_kol, price_bon1]
            orders.append(bon1_del)
            bon1_index=orders.index(bon1_del)
        price+=bon1_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")

@b.callback_query_handler(func=lambda call:True if call.data=="pls_bon15" or call.data=="min_bon15" or call.data=="add_kar_bon15" else False)

def pl_mi_bon15(c):
    global bon15_kol, order, price, bon15_del, bon15_index
    if c.data=="pls_bon15":
        bon15_kol=bon15_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🧊 Bon-aqua 1.5л", reply_markup=Bon_aqua15())
    elif c.data=="min_bon15":
        if bon15_kol==1:
            pass
        else:
            bon15_kol=bon15_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🧊 Bon-aqua 1.5л", reply_markup=Bon_aqua15())
    elif c.data=="add_kar_bon15":
        if bon15_ord in orders:
            #print(bur_ord)
            bon15=[bon15_ord, bon15_kol, price_bon15]
            orders[bon15_index]=bon15
        else:
            bon151_ord=bon15_ord
            bon15_del=[bon151_ord, bon15_kol, price_bon15]
            orders.append(bon15_del)
            bon15_index=orders.index(bon15_del)
        price+=bon15_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")

@b.callback_query_handler(func=lambda call:True if call.data=="pls_cc125" or call.data=="min_cc125" or call.data=="add_kar_cc125" else False)

def pl_mi_cc125(c):
    global cc125_kol, order, price, cc125_del, cc125_index
    if c.data=="pls_cc125":
        cc125_kol=cc125_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🥤 Coca cola 1.25", reply_markup=CC125())
    elif c.data=="min_cc125":
        if cc125_kol==1:
            pass
        else:
            cc125_kol=cc125_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🥤 Coca cola 1.25", reply_markup=CC125())
    elif c.data=="add_kar_cc125":
        if cc125_ord in orders:
            #print(bur_ord)
            cc125=[cc125_ord, cc125_kol, price_cc125]
            orders[cc125_index]=cc125
        else:
            cc1251_ord=cc125_ord
            cc125_del=[cc1251_ord, cc125_kol, price_cc125]
            orders.append(cc125_del)
            cc125_index=orders.index(cc125_del)
        price+=cc125_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")
@b.callback_query_handler(func=lambda call:True if call.data=="pls_spr1" or call.data=="min_spr1" or call.data=="add_kar_spr1" else False)

def pl_mi_spr1(c):
    global spr1_kol, order, price, spr1_del, spr1_index
    if c.data=="pls_spr1":
        spr1_kol=spr1_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍋 Sprite 1л", reply_markup=Spr1())
    elif c.data=="min_spr1":
        if spr1_kol==1:
            pass
        else:
            spr1_kol=spr1_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍋 Sprite 1л", reply_markup=Spr1())
    elif c.data=="add_kar_spr1":
        if spr1_ord in orders:
            #print(bur_ord)
            spr1=[spr1_ord, spr1_kol, price_spr1]
            orders[spr1_index]=spr1
        else:
            spr11_ord=spr1_ord
            spr1_del=[spr11_ord, spr1_kol, price_spr1]
            orders.append(spr1_del)
            spr1_index=orders.index(spr1_del)
        price+=spr1_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")

@b.callback_query_handler(func=lambda call:True if call.data=="pls_rc1" or call.data=="min_rc1" or call.data=="add_kar_rc1" else False)

def pl_mi_rc1(c):
    global rc1_kol, order, price, rc1_del, rc1_index
    if c.data=="pls_rc1":
        rc1_kol=rc1_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🥤 RC cola 1л", reply_markup=RC1())
    elif c.data=="min_rc1":
        if rc1_kol==1:
            pass
        else:
            rc1_kol=rc1_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🥤 RC cola 1л", reply_markup=RC1())
    elif c.data=="add_kar_rc1":
        if rc1_ord in orders:
            #print(bur_ord)
            rc1=[rc1_ord, rc1_kol, price_rc1]
            orders[rc1_index]=rc1
        else:
            rc11_ord=rc1_ord
            rc1_del=[rc11_ord, rc1_kol, price_rc1]
            orders.append(rc1_del)
            rc1_index=orders.index(rc1_del)
        price+=rc1_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")

@b.callback_query_handler(func=lambda call:True if call.data=="pls_fan125" or call.data=="min_fan125" or call.data=="add_kar_cc125" else False)

def pl_mi_fan125(c):
    global fan125_kol, order, price, fan125_del, fan125_index
    if c.data=="pls_fan125":
        fan125_kol=fan125_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍊 Fanta 1.25", reply_markup=Fan125())
    elif c.data=="min_fan125":
        if fan125_kol==1:
            pass
        else:
            fan125_kol=fan125_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍊 Fanta 1.25", reply_markup=Fan125())
    elif c.data=="add_kar_fan125":
        if fan125_ord in orders:
            #print(bur_ord)
            fan125=[fan125_ord, fan125_kol, price_fan125]
            orders[fan125_index]=fan125
        else:
            fan1251_ord=fan125_ord
            fan125_del=[fan1251_ord, fan125_kol, price_fan125]
            orders.append(fan125_del)
            fan125_index=orders.index(fan125_del)
        price+=fan125_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")


@b.callback_query_handler(func=lambda call:True if call.data=="pls_cc175" or call.data=="min_cc175" or call.data=="add_kar_cc175" else False)

def pl_mi_cc175(c):
    global cc175_kol, order, price, cc175_del, cc175_index
    if c.data=="pls_cc175":
        cc175_kol=cc175_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🥤 Coca cola 1.75", reply_markup=CC175())
    elif c.data=="min_cc175":
        if cc175_kol==1:
            pass
        else:
            cc175_kol=cc175_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🥤 Coca cola 1.75", reply_markup=CC175())
    elif c.data=="add_kar_cc175":
        if cc175_ord in orders:
            #print(bur_ord)
            cc175=[cc175_ord, cc175_kol, price_cc175]
            orders[cc175_index]=cc175
        else:
            cc1751_ord=cc175_ord
            cc175_del=[cc1751_ord, cc175_kol, price_cc175]
            orders.append(cc175_del)
            cc175_index=orders.index(cc175_del)
        price+=cc175_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")
@b.callback_query_handler(func=lambda call:True if call.data=="pls_fan175" or call.data=="min_fan175" or call.data=="add_kar_cc175" else False)

def pl_mi_fan175(c):
    global fan175_kol, order, price, fan175_del, fan175_index
    if c.data=="pls_fan175":
        fan175_kol=fan175_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍊 Fanta 1.75", reply_markup=Fan175())
    elif c.data=="min_fan175":
        if fan175_kol==1:
            pass
        else:
            fan175_kol=fan175_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🍊 Fanta 1.75", reply_markup=Fan175())
    elif c.data=="add_kar_fan175":
        if fan175_ord in orders:
            #print(bur_ord)
            fan175=[fan175_ord, fan175_kol, price_fan175]
            orders[fan175_index]=fan175
        else:
            fan1751_ord=fan175_ord
            fan175_del=[fan1751_ord, fan175_kol, price_fan175]
            orders.append(fan175_del)
            fan175_index=orders.index(fan175_del)
        price+=fan175_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")


@b.callback_query_handler(func=lambda call:True if call.data=="pls_chesn_s" or call.data=="min_chesn_s" or call.data=="add_kar_chesn_s" else False)
def pl_mi_chesn_s(c):
    global chesn_s_kol, orders, price, chesn_s_del, chesn_s_index
    if c.data=="pls_chesn_s":
        chesn_s_kol+=1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🧄 Чесночный соус", reply_markup=Chesn_s())
    elif c.data=="min_chesn_s":
        if chesn_s_kol==1:
            pass
        else:
            chesn_s_kol=chesn_s_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🧄 Чесночный соус", reply_markup=Chesn_s())
    elif c.data=="add_kar_chesn_s":
        if chesn_s_ord in orders:
            #print(bur_ord)
            chesn_s=[chesn_s_ord, chesn_s_kol, price_chesn_s]
            orders[chesn_s_index]=chesn_s
        else:
            chesn_s1_ord=chesn_s_ord
            chesn_s_del=[chesn_s1_ord, chesn_s_kol, price_chesn_s]
            orders.append(chesn_s_del)
            chesn_s_index=orders.index(chesn_s_del)
        price+=chesn_s_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")

@b.callback_query_handler(func=lambda call:True if call.data=="pls_ostri_s" or call.data=="min_ostri_s" or call.data=="add_kar_ostri_s" else False)
def pl_mi_ostri_s(c):
    global ostri_s_kol, order, price, ostri_s_del, ostri_s_index
    if c.data=="pls_ostri_s":
        ostri_s_kol=ostri_s_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🌶 Острый соус", reply_markup=Ostri_s())
    elif c.data=="min_ostri_s":
        if ostri_s_kol==1:
            pass
        else:
            ostri_s_kol=ostri_s_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🌶 Острый соус", reply_markup=Ostri_s())
    elif c.data=="add_kar_ostri_s":
        if ostri_s_ord in orders:
            #print(bur_ord)
            ostri_s=[ostri_s_ord, ostri_s_kol, price_ostri_s]
            orders[ostri_s_index]=ostri_s
        else:
            ostri_s1_ord=ostri_s_ord
            ostri_s_del=[ostri_s1_ord, ostri_s_kol, price_ostri_s]
            orders.append(ostri_s_del)
            ostri_s_index=orders.index(ostri_s_del)
        price+=ostri_s_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")

@b.callback_query_handler(func=lambda call:True if call.data=="pls_sirni_s" or call.data=="min_sirni_s" or call.data=="add_kar_sirni_s" else False)
def pl_mi_sirni_s(c):
    global sirni_s_kol, order, price, sirni_s_del, sirni_s_index
    if c.data=="pls_sirni_s":
        sirni_s_kol=sirni_s_kol+1
        b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🧀 Сырный соус", reply_markup=Sirni_s())
    elif c.data=="min_sirni_s":
        if sirni_s_kol==1:
            pass
        else:
            sirni_s_kol=sirni_s_kol-1
            b.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.id, text="🧀 Сырный соус", reply_markup=Sirni_s())
    elif c.data=="add_kar_sirni_s":
        if sirni_s_ord in orders:
            #print(bur_ord)
            sirni_s=[sirni_s_ord, sirni_s_kol, price_sirni_s]
            orders[sirni_s_index]=sirni_s
        else:
            sirni_s1_ord=sirni_s_ord
            sirni_s_del=[sirni_s1_ord, sirni_s_kol, price_sirni_s]
            orders.append(sirni_s_del)
            sirni_s_index=orders.index(sirni_s_del)
        price+=sirni_s_sum_pr
        b.send_message(c.message.chat.id, "Товар добавлен в корзину, что нибудь еще?")

@b.callback_query_handler(func=lambda call:True if call.data=="basket" else False)
def basket(call):
    if order=="":
        b.send_message(call.message.chat.id, "Вы еще ничего на добавили в корзину")
    else:
        b.send_message(call.message.chat.id, f"Заказ:{order}\nСумма заказа:{price}см")
        

@b.callback_query_handler(func=lambda call:True if call.data=="edit_order" else False)
def e_o(call):
    global orders, del_order, chislo_kril, back_edor, instr, inst_show
    back_edor=True
    del_order=1
    ttt=""
    for i in range(len(orders)):
        ttt+=f"{orders[i][0]}\n{orders[i][1]} x {orders[i][2]} = {orders[i][1]*orders[i][2]}\n"
    instr=b.send_message(call.message.chat.id, text="«❌ Название продукта» - удалить из корзины\n«🔄 Очистить» - полностью очистить корзину", reply_markup=Edit_ord())
    #inst_show=b.send_message(call.message.chat.id, text=show_order(), reply_markup=Edit_ord())

@b.callback_query_handler(func=lambda call: True if call.data=="somon_kril_kg" else False)
def som_kril(call):
    global chisla_kril, kril001
    b.edit_message_text(chat_id=call.message.chat.id, message_id=kril001.id, text=f"10см = 133грамм\n{chisla_kril} сомон", reply_markup=kril_som())



@b.callback_query_handler(func=lambda call:True if call.data=="confirm" or call.data=="cencel" else False)
def confirm(call):
    global order, orders
    if call.data=="confirm":
        b.send_message(call.message.chat.id, "Ваш заказ успешно принят!", reply_markup=Main_menu())
    elif call.data=="cencel":
        b.send_message(call.message.chat.id, "Ваш заказ отклонён", reply_markup=Main_menu())
    #b.send_message(message.chat.id, text=order)
    #b.send_message(message.chat.id, text=order, reply_markup=MENU_second())

@b.callback_query_handler(func=lambda call:True if call.data=="Mir" or call.data=="Mak4" or call.data=="Univermag" else False)
def oplataa(call):
    global order,place,price,messid_mak4,messid_mir,messid_uni, choice_001, choice_002, choice_003, choice_004
    b.delete_message(call.message.chat.id, choice_001.id)
    b.delete_message(call.message.chat.id, choice_002.id)
    b.delete_message(call.message.chat.id, choice_003.id)
    b.delete_message(call.message.chat.id, choice_004.id)
    if orders==[]:
        b.send_message(call.message.chat.id, "Вы еще ничего на добавили в корзину")
    elif call.data=="Mir":
        place="куч.Мир"
        b.send_message(call.message.chat.id, text=show_order(), parse_mode="Markdown", reply_markup=send_o())
            
    elif call.data=="Mak4":
        place="Школа№4"
        b.send_message(call.message.chat.id, text=show_order(), pars_mode="Markdown", reply_markup=send_o())
    
    elif call.data=="Univermag":
        place="Универмаг"
        b.send_message(call.message.chat.id, text=show_order(), pars_mode="Markdown", reply_markup=send_o())
    
@b.callback_query_handler(func=lambda call:True if call.data=="otmena" else False)
def sd(call):
    global order,place,price,messid_mak4,messid_mir,messid_uni
    if order=="":
        b.send_message(call.message.chat.id, "Вы еще ничего на добавили в корзину")
    elif call.data=="Mir":
        place="куч.Мир"
        b.send_message(call.message.chat.id, f"Заказ:{order}\nСумма заказа:{price}см\nТочка:{place}\nСпособ получения заказа:{get_way}")
        messid_mir=b.send_message(call.message.chat.id, "Каким способом собираетесь оплпить заказ?", reply_markup=s_pay())
    elif call.data=="Mak4":
        place="Школа№4"
        b.send_message(call.message.chat.id, f"Заказ:{order}\nСумма заказа:{price}см\nТочка:{place}\nСпособ получения заказа:{get_way}")
        messid_mak4=b.send_message(call.message.chat.id, "Каким способом собираетесь оплпить заказ?", reply_markup=s_pay())
    elif call.data=="Univermag":
        place="Универмаг"
        b.send_message(call.message.chat.id, text=show_order())
        messid_uni=b.send_message(call.message.chat.id, "Каким способом собираетесь оплпить заказ?", reply_markup=s_pay())


@b.callback_query_handler(func=lambda call:True if call.data=="zvezda" else False)
def sd(call):
    global back_izbr
    back_izbr=1
    b.send_message(call.message.chat.id, text="Раздел Избраные", reply_markup=star())


@b.callback_query_handler(func=lambda call:True if call.data=="otpravit_" or call.data=="otmena_" else False)
def e_o(call):
    global otp_zakaz, pay_way, adres, admin, order, price, place, get_way, order_story, Time
    if call.data=="otpravit_":
        sec=time.time()
        order_story.append(f"{time.ctime(sec)}\n{show_order()}")
        otp_zakaz=b.send_message(admin, text=show_order(), parse_mode="Markdown")

        #b.send_message(admin, text=f"Заказ:\n{order}\nСумма заказа:{price}см\nТочка:{place}\nСпособ получения заказа:{get_way}\nВремя:{time}\n\nИмя:"+str(call.message.from_user.name)+"\nСсылка:@"+str(call.message.from_user.username))
        b.send_message(call.message.chat.id, "Ваш запрос успешно отпрален!\nОжидайте звонка")
        #b.send_message(call.message.chat.id, text="Главная меню", reply_markup=Main_menu())
    elif call.data=="otmena_":
        order=""
        price=0
        adres=""
        pay_way=""
        place=""
        get_way=""
        Time=""
        b.delete_message(chat_id=call.message.chat.id, message_id=otp_zakaz.id)
        b.send_message(call.message.chat.id, "Карзина удалён!\nМожете сделать заказ заного", reply_markup=meenu())
    else:
        pass
@b.callback_query_handler(func=lambda call:True if call.data=="pay_dc" or call.data=="pay_alif" or call.data=="pay_eskhata" else False)
def dc(c):
    global hz, id_order
    if c.data=="pay_dc":
        b.send_message(c.messae.chat.id, f"Dushanbe City\nоплатите заказ по этому номеру +992927964433 и напишите \n#{id_order} в коментари")
    elif c.data=="pay_alif":
        b.send_message(c.messae.chat.id, f"Alif mobi\nоплатите заказ по этому номеру +992927964433 и напишите \n#{id_order} в коментари")
    elif c.data=="pay_eskhata":
        b.send_message(c.messae.chat.id, f"Эсхата\nоплатите заказ по этому номеру +992927964433 и напишите \n#{id_order} в коментари")
    

@b.callback_query_handler(func=lambda call:True if call.data=="my_orders" else False)
def I_Z(c):
    global order_story
    if order_story!=[]:
        for i in range(len(order_story)):
            b.send_message(c.message.chat.id, text=order_story[i])
    else:
        b.send_message(c.message.chat.id, "История заказов пуст :(")
@b.callback_query_handler(func=lambda call:True if call.data=="O_S" else False)
def Obrantaya_svyaz(c):
    text="Вы можете написать нам в:\n[Instagram](https://instagram.com/cafe.vaqt?igshid=NTc4MTIwNjQ2YQ==)\n\n[Facebook](https://www.facebook.com/cafe.vaqt?mibextid=LQQJ4d)\n\n[Telegram](@p_2_4z)"
    #"Вы можете связаться с нами по номеру:\n+992927963344\n\n+992922006699\n\nИли можете нарисать нам в:\nInstagram"
    b.send_message(c.message.chat.id, text=text, parse_mode="Markdown")

b.infinity_polling()
