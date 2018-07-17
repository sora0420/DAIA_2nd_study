import random
import time

class Player:
    pName = []
    def __init__(self,id):
        self.id = id
        self.hp = 100
        self.mp = 100
        self.stemina = 30
        self.attackPower = 4
        Player.pName.append(id)
        #if id in Player.pName:
        #   id = Player.pName[id]

    def randomAttack(self):
        num = random.choice("12")
        if num=="1":
            Player.normalattack(self)
        elif num=="2":
            Player.skill1(self)

    def normalattack(self):
        print("player"+str(self.id) + " 노말공격")
        self.stemina -= 5
        print("player"+str(self.id)+"의 현재 스테미너 : "+str(self.stemina))
        return self.attackPower

    def skill1(self):
        print("player"+str(self.id) + " 스킬1 공격")
        self.mp -= 30
        print("player"+str(self.id) + "의 현재 mp : " + str(self.mp))
        return self.attackPower*3

    def playerIdReturn(self):
        print(self.pName)

class Monster:
    mName = []
    def __init__(self,id):
        self.id = id
        Monster.mName.append(id)
        self.hp = 100
        self.mp = 100
        self.stemina = 30
        self.attackPower = 4
        #if id in Monster.mName:
        #    id = Monster.mName[id]

    def randomAttack(self):
        num = random.choice("12")
        if num=="1":
            Monster.normalattack(self)
        elif num=="2":
            Monster.skill1(self)

    def normalattack(self):
        print("monster"+str(self.id) + " 노말공격")
        self.stemina -= 5
        print("monster"+str(self.id)+"의 현재 스테미너 : "+str(self.stemina))
        return self.attackPower

    def skill1(self):
        print("monster"+str(self.id) + " 스킬1 공격")
        self.mp -= 30
        print("monster"+str(self.id) + "의 현재 mp : " + str(self.mp))
        return self.attackPower*3

    def monsterIdReturn(self):
        print(self.mName)


class GameManager:
    def run(self, timeSet):
        startTime = time.time()
        while(timeSet > (time.time()-startTime)):
            GameManager.randomMonsterGen(self)
            GameManager.randomPlayerGen(self)


    def randomMonsterGen(self):
        while True:
            while True:
                randomid = random.randint(1, 10)
                if randomid in Monster.mName:
                    continue
                else:
                    break
            Monster.mName.append(randomid)
            if len(Monster.mName)==10:
                break

        i = random.randint(0,9)
        i = Monster.mName[i]
        id = Monster(i)
        id.randomAttack()
        a = GameManager
        a.randomMosterAttack(self, id)

    def randomPlayerGen(self):
        while True:
            while True:
                randomid = random.randint(1, 10)
                if randomid in Player.pName:
                    continue
                else:
                    break
            Player.pName.append(randomid)
            if len(Player.pName)==10:
                break

        i = random.randint(0,9)
        i = Player.pName[i]
        id = Player(i)
        id.randomAttack()
        a = GameManager
        a.randomPlayerAttack(self, id)

    def randomMosterAttack(self, id):
        num = random.randint(1, 10)
        while int(id.hp) > 0:
            p = Player(num)
            attack = id.normalattack()
            p.hp -= int(attack)
            print("현재 player의 hp : "+str(p.hp))
            skill = id.skill1()
            p.hp -= int(skill)
        if int(id.hp) > 0:
            return GameManager.gameRsult("Monster")

    def randomPlayerAttack(self, id):
        num = random.randint(1, 10)
        while int(id.hp) > 0:
            m = Monster(num)
            attack = id.normalattack()
            m.hp -= int(attack)
            print("현재 monster의 hp : " + str(m.hp))
            skill = id.skill1()
            m.hp -= int(skill)
        if int(id.hp) > 0:
            return GameManager.gameRsult("Player")

    def gameRsult(self, winner):
        return print(winner + "승리!")

a = GameManager()
a.run(100)
print(a.result)
