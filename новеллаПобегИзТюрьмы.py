def введение():
    print("вы зашли в текстовую игру новеллу")
    print("сегодня вы проснулись в камере тюрьмы")
    print("вам придется выбраться из этого места и решить головоломки")
    print("так же от ваших решений будет зависить будущее")
    print("поскорее выбирайтесь отсюда!")
    print("удачи!")

def комната1():
    print("вы открываете глаза и думаете, что проспали будильник и ваш босс будет опять вас отчитывать")
    print("но что-то не так...")
    print("это тюрьма!?")
    print("вы окидываете взглядом камеру")
    print("в вашей камере две двери, которые можно открыть без ключа")
    print("1-открыть дврь слева")
    print("2-ткрыть дверь справа")
    выбор = input("напишите номер двери: ")

    выборы = {
        "1": комната2,
        "2": комната3
    }
    выборы.get(выбор, неверный_выбор)()
def комната2():
    print("вы входите во вторую комнату")
    print("здесь никого нет")
    print("интересно, почему? неважно")
    print("на первый взгляд комната полностью пустая")
    print("но если присмотреться, то можно в углах комнаты увидеть ключи")
    print("интересно, кто их оставил?")
    print("1-взять синий ключ")
    print("2-вять красный ключ")
    print("3-взять зеленый ключ")
    выбор = input("напишите номер выбора: ")

    выборы = {
        "1": синий_ключ,
        "2": красный_ключ,
        "3": комната4
    }
    выборы.get(выбор, неверный_выбор)()

def комната3():
    print("вы вошли в другую комнату")
    print("и опять ни души, удивительно")
    print("в этой комнате нет ключей")
    print("она была завалена мусором")
    print("но есть и более полезные вещи")
    print("среди мусора были зеркало, отвертка, гвоздь и молоток")
    choice = input("напишите '1' и взять зеркало или '2' и не брать его: ")
    if choice.lower() == "2":
        print("у вас было плохое предчевствие")
        print("вы решли не брать в руки зеркало")
        print("оно осталось лежать в куче мусора")
    elif choice.lower() == "1":
        print("хть у вас и было плохое предчевствие")
        print("но вы решили взять зеркало в руки")
        print("только вы взяли в руки зеркало, как..")
        print("ЗВОНЬК")
        print("зеркало разбилось в ваших руках")
        print("у вас появились небольшие порезы от осколков")
        print("но они не были серьезными")
        print("по крайней мере не требовали медицинского вмешательства")
    else:
        print("теперь вы ранены")
    print("1-взять гвоздь")
    print("2-взять отвертку")
    print("3-взять молоток")
    выбор = input("напишите номер выбора: ")

    выборы = {
        "1": гвоздь,
        "2": отвертка,
        "3": молоток
    }
    выборы.get(выбор, неверный_выбор)()

def комната4():
    print("вы открываете еще одну дверь")
    print("и из нее нет еще одной двери")
    print("это тупик...")
    print("что же вам тепеь делать?")
    print("как вам теперь выбраться из тюрьмы?")
    print("и почему вам до сих пор не попался ни один человек на пути?")
    print("интересно...")
    print("осмотрев стены, вы ничего не нашли кроме паука, одного окурка и какого то математического выражения")
    print("наверное заключенные развликались математикй")
    print("на полу оказался люк, но на нем кодовый замок")
    print("интересно, а какой пароль")
    print("введя несколько неверных паролей, вы вспомнили про пример на стене")
    print("выражение: 5*9+56*18")
    пароль = input("введите пароль: ")

    if пароль == "1053":
        print("супер! вы смогли открыть люк!")
        конец()
    else:
        print("пароль неверный, учите математику")
        комната4()

def молоток():
    print("вы взяли молоток")
    print("и тут что-то затрещало")
    print("вы уже подумали, что вас сейчас поймают")
    print("но звук был совсем не от людей")
    print("это стена начала обваливаться")
    print("похоже, это свобода!")
    print("поздравляю!")
    print("вы сбежали из тюрьмы!")
    print("конец игры!")
    конец()

def неверный_выбор():
    print("неверный выбор. попробуйте ещё раз.")
    комната1()

def ключ_синего():
    print("вы взяли синий ключ")
    print("Фуууу")
    print("он грязненький")
    комната2()

def ключ_красного():
    print("вы взяли красный ключ")
    print("но увы и ах он сломан и буквально развалился у вас в руке")
    комната2()

def гвоздь():
    print("этот гвоздь вось ржавый")
    print("а если вы порежетесь им, то возможно чем то заразитесь")
    print("вы кинули гвоздь обратно в кучу мусора")
    print("а потом вы рушили уйти обратно в первую комнату")
    комната1()

def отвертка():
    print("в руки вы взяли отвертку")
    print("а зачем она вам?")
    print("вы кинули отвертку обратно")
    комната3()

def конец():
    print("вы выбрались из тюрьмы!")
    print("спасибо за игру!!!")
    exit()

def main():
    введение()
    комната1()

if __name__ == "__main__":
    main()