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
    play music "audio/nature.flac" fadeout 1.0 fadein 1.0
    $ disclaimer = ["{size=+20}{color=#f00}{b}Дисклеймер{/b}", "\n\n{color=#ffffff}Данная визуальная новелла носит исключительно развлекательный характер. В ней могут присутствовать сцены насилия. \
Авторы не ставят цель кого-то оскорбить или подвергнуть стигматизации и дискриминации. Все персонажи являются вымышленными. Любое сходство с реальными событиями случайно. \
Авторы не несут ответственности за действия, совершённые тихими любителями визуальных новелл подобного рода.", "\n\n{b}16+"]

    show text Text(disclaimer) with dissolve
    pause 6
    hide text
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
