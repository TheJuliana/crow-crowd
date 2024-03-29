# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define Philip = Character('Филипп Нельсон', color="#4B0082")

image logo = "bg/logo.png"
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Спрайты Филипп
image Philip = "Philip/philip.png"

# Игра начинается здесь:
label start:
    scene logo
    Philip "Привет"
    #scene bg room

    #show eileen happy
    show Philip
    with dissolve

    Philip "Эй"

    # hide Philip
    # show PhilipLaugh
    # with dissolve


#label something:

    menu:
        "Мы знакомы?":
            Philip "Нет"
        "Как дела?":
            Philip "Хорошо"
    

    return
