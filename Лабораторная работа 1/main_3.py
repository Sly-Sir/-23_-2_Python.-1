# TODO Найдите количество книг, которое можно разместить на дискете
V_Disk = 1.44
page = 100
str_ = 50
symbol_ = 25
byte_str = 4
V_book = (symbol_ * byte_str * str_ * page) / 1024 / 1024
res_ = V_Disk / V_book
print("Количество книг, помещающихся на дискету:", round(res_))
