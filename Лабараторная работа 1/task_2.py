disk = 1.44
LIST = 100
STROK = 50
SYMBOL = 25
sum_symbol = SYMBOL * STROK * LIST
pam_v_bite = sum_symbol * 4
pam_v_mb = pam_v_bite/(1024*1024)
book = disk // pam_v_mb

# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", int(book))
