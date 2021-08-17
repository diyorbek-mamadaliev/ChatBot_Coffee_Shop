def coffe_bot():
    print("Welcome to Coffe Bar!")
    size = get_size()
    drink_type = get_drink_type()
    print("Tushunarli, coffe hajmi", size, "ga teng, va Coffe turi", drink_type)
    name = input("Ismingizni bilsam bo'ladimi?")
    print("Tashakkur", name, "Sizni ichimligingiz tez orada tayyor bo'ladi.")

def get_size():
    res = input("Coffe hajmini tanlang: \n[a] Kichkina,"
                " \n[b] O'rta va \n[c] Katta \n")
    if res == "a":
        return "Kichkina"
    elif res == "b":
        return "O'rta"
    elif res == "c":
        return "Katta"
    else:
        print("Kechirasiz, hajmni qayta "
              "kiriting iltimos! Sizni tushunmadim")
        return get_size()

def get_drink_type():
    res = input("Coffe turini tanlang: \n[a] Qora, \n[b] Sutli va \n[c] Oddiy \n")
    if res == "a":
        return "Qora"
    elif res == "b":
        return sutli_coffe()
    elif res == "c":
        return "Oddiy"
    else:
        print("Kechirasiz, turini qayta "
              "kiriting iltimos! Sizni tushunmadim")
        return get_drink_type()

def sutli_coffe():
    res = input("Va qanday turdagi Sutni hohlaysiz?"
                "\n[a] 2% Sut \n[b] Yog'siz \n[c] So'ya Suti")
    if res == "a":
        return "2% Sut"
    elif res == "b":
        return "Yog'siz"
    elif res == "c":
        return "So'ya Suti"
    else:
        print("Kechirasiz, Sutni turini qayta "
              "kiriting iltimos! Sizni tushunmadim")
        return sutli_coffe()

coffe_bot()