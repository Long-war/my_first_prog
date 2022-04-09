import random

health = 200
damage = 10
exp = 0
exp_troll = 5
exp_2_lvl = 20
exp_3_lvl = 80
exp_4_lvl = 160
exp_5_lvl = 300
lvl = 1
skill_weapon = 2
skill_defence = 1



while True :
    x = int(input("Нажми 1 чтобы играть. Для выхода нажми любую цифру "))
    if x == 1:
        while True: 
            zone = int(input("Куда бить 1 - голова 2 - тело 3 - ноги? 4 выход "))
            zone_2 = random.randrange(3) + 1
            print(zone_2)
            if zone == zone_2 and health > 0 :
                health -= damage
                print("Вы попали! ", health )

            elif health <= 0:
                health = 100
                exp = exp + exp_troll

                if exp == exp_2_lvl:
                    lvl += 1
                    drop = random.randrange(3) + 1
                    print("Победа! Получено опыта ", exp_troll, "Всего опыта ", exp, "Ваш уровень повысился!", lvl, drop)
                    if skill_weapon == drop:
                        damage += 10
                        print("Вы получили навык обращения с оружием и увеличили урон на 10.")
                    elif skill_defence == drop:
                        health += 50
                        print("Вы научились выдерживать сильные удары")
                    
                

                elif exp == exp_3_lvl:
                    lvl += 1
                    drop = random.randrange(3) + 1
                    print("Победа! Получено опыта ", exp_troll, "Всего опыта ", exp, "Ваш уровень повысился!", lvl, drop)
                    if skill_weapon == drop:
                        damage += 10
                        print("Вы получили навык обращения с оружием и увеличили урон на 10.")
                    elif skill_defence == drop:
                        health += 50
                        print("Вы научились выдерживать сильные удары")

                    
                elif exp == exp_4_lvl:
                    lvl += 1
                    drop = random.randrange(3) + 1
                    print("Победа! Получено опыта ", exp_troll, "Всего опыта ", exp, "Ваш уровень повысился!", lvl, drop)
                    if skill_weapon == drop:
                        damage += 10
                        print("Вы получили навык обращения с оружием и увеличили урон на 10.")
                    elif skill_defence == drop:
                        health += 100
                        print("Вы научились выдерживать сильные удары")

                elif exp == exp_5_lvl:
                    lvl += 1
                    drop = random.randrange(3) + 1
                    print("Победа! Получено опыта ", exp_troll, "Всего опыта ", exp, "Ваш уровень повысился!", lvl, drop)
                    if skill_weapon == drop:
                        damage += 10
                        print("Вы получили навык обращения с оружием и увеличили урон на 10.")
                    elif skill_defence == drop:
                        health += 100
                        print("Вы научились выдерживать сильные удары")

                else:
                    drop = random.randrange(3) + 1
                    print("Победа! Получено опыта ", exp_troll, "Всего опыта ", exp , lvl, drop)
                    if skill_weapon == drop:
                        damage += 10
                        print("Вы получили навык обращения с оружием и увеличили урон на 10.")
                    elif skill_defence == drop:
                        health += 100
                        print("Вы научились выдерживать сильные удары")

            elif zone == 4:
                break
            else:
                print("Промах")
    else:
        break

input()
    




    

