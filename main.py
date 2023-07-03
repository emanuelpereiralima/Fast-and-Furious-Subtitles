family_count = 0
for films in range(9):
    film_name = "F" + str(films + 1) + ".srt"
    film = open(film_name, 'r')
    film_content = film.readlines()
    for line in film_content:
        if 'família' in line:
            family_count += 1
    print("Em Velozes e Furiosos",films + 1,"falaram família",family_count,"vezes.")