# -*- coding: utf-8 -*-
from sys import exit
from random import randint  
class Scene(object):
''' 각 장면마다 입장을 해야하니깐 이걸 상속해줄거야
    각자 구체적인 내용은 자식클래스에서 쓰는걸로 하고, 여기서는 그냥 함수를 만들어만 놓자. 
'''
    def enter(self):
        pass
        
class Engine(object):
#엔진은 지도를 받아서 다루는 역할을 함. 즉 게임을 진행해나가는 역할을 할거야. 
    def __init__(self, scene_map):
        self.game_map = scene_map
        print('우주선을 탈출할 수 있는 지도를 얻었다!!!')
        print('페르칼 25번 행성에서 온 고던족 쉐끼를 죽이고, 우주선에서 탈출하여 지구로 귀환하자!')
        
    def play(self):
        print('게임을 시작합니다. 긴장하시고 쏘세욤~')
        self.game_map.opening_scene()
    
class Death(Scene):
#죽었을때를 나타내는 장면
    def enter(self):
        print('고던족의 공격을 받고 주인공이 죽습니다')
        print('으윽, 존나게 아프네... 외계인 녀석 죽여버릴테다!')
        exit(0)
        
class CentralCorridor(Scene):
#중앙복도를 나타내는 장면
    def enter(self):
        print('중앙복도입니다. 게임의 시작지점이고 이미 고던인이 복도 중앙에 서있습니다.')
        print('고던인을 물리치고 앞으로 나아가려면 플레이어는 농담 한마디를 해서 이겨야합니다.')
        print('고던인: 나와 가위바위보를 해서 이기면 살려주마 킬킬킬')
        ailen_Ans = random.randint(1, 3)
        print('고던인을 만났다. 어떻게 할까?)
        print('1. 머리를 써서 가위를 낸다.')
        print('2. 남자답게 바위를 낸다.')
        print('3. 쫄보답게 보를 낸다.')
        user_Ans = int(input('번호를 입력하세요: '))
        if((ailen_Ans + 1) % 3 == user_Ans):
            print('고던인: 아니 씨부랭, 나를 이기다니.. 이런 존나게 분하다...')
        else:
            print('고던인: ㅋ. 님 바보? 가위바위보 줜나게 못하시네욤')
            print('레이저 총 맞고 주무세욤 ㅂㅂ~')
            exit(0)
        
class LaserWeaponArmory(Scene):
#레이저 무기고를 나타내는 장면
    def enter(self):
        print('레이저 무기고에 도착했다!')
        print('여기서 중성자탄을 얻으면 우주선을 날려버릴 수 있다고 한다.')
        print('수상해 보이는 상자를 발견했다. 딱봐도 여기에 중성자탄이 들어있을 것만 같다.')
        print('아니 씨부랭, 비밀번호가 걸려있다. 이걸 어떻게 맞추지?')
        print('경고: 비밀번호를 3번안에 못 풀 경우, 중성자탄이 자동으로 폭발합니다.')
        print('힌트: 비밀번호는 멋쟁이 일병 허니비의 생일 xx월 xx일')
        print('총 4자리로 이루어진 xxxx입니다.')
        real_ans = 0928
        for i in range(3):
            user_ans = int(input('답을 입력해주세요:'))
            if(real_ans == user_ans):
                break;
            if(i == 2): #3번 기회동안 못푼경우
                print('고던인: 님 바보? ㅋㅋㅋㅋ 지가 지생일도 모르네 잘가셈 ㅃㅃ~')
                print('중성자탄 자동 폭발 시스템이 발동합니다.')
                print('3초뒤에 터집니다.')
                print('3, 2, 1')
                print('Bammm!!!!')
                print('시스템: 중성자탄이 폭발하며 우주선과 함께 가루가 되어버렸습니다. 다음 기회에...')
                exit(0)
        print('우하하하, 당연히 내가 내 생일을 모를리가 있나. 이 멍청한 외계인 새끼야 ㅋㅋㅋㅋ')
        print('시스템: 중성자탄을 획득했습니다. 우주선에서 탈출하기전에 우주선을 날려버리세요!')
class TheBridge(Scene):
#다리를 나타태는 장면
    def enter(self):
        print('다리에 도착했다!')
        print('슈퍼액션 전문가인 내 시선으로 봤을때, 다리에다가 폭탄 설치하고 런하면 될것같다.')
        print('건방진 고던인 자식을 가루로 만들어버리자')
        print('시스템: 폭탄을 설치합니다.')
        

class EscapePod(Scene):
#구명정을 나타내는 장면
    def enter(self):
        print('드디어 구명정에 도착했다.')
        print('??? 아니 보트가 하나가 아니고 존나게 많네?')
        print('알림: 들어올땐 마음대로지만, 나갈땐 아니라구~~')
        print('여기 있는 10개의 보트 중 한 개만이 올바로 작동하는 보트다.')
        print('우주선의 폭발이 몰려오기전에 어서 탈출하라구~')
        good_boat = random.randint(1, 10)
        for i in range(4):
            print('%d번째 시도입니다. 폭발이 오기전에 얼른 탈출하세요' %(i+1))
            user_ans = int(input('멀쩡한 것 같은 보트의 번호를 입력해주세요!!'))
            if(good_boat == user_ans):
                print('야호! 진짜 구명정을 찾았땅. 나 진짜로 간당 안뇽~~')
                break
            if(i == 3):
                print('화염이 구명정까지 몰려왔습니다.')
                print('모든 구명정이 화염에 휩싸여서 집에 갈 수 없게되었습니다. ㅠㅠ')
                print('씨ㅣㅣㅣ부랭!!!!!!!!!!!!!!')
                exit(0)
        print('시스템: 당신은 고던인을 물리치고 무사히 지구로 귀환할 수 있게 되었습니다. 축하합니다!')
class Map(object):
#지도는 기본적으로 시작하는 장면을 받고, 오프닝씬과 다음씬에 대한 함수를 가지고있음. 
    def __init__(self, start_scene):
        #현재 씬을 시작씬으로 설정해주고, 틀어주면 됨. 
        print('우주선에서 탈출할 수 있는 지도를 만듭니다.')
        print('지도를 따라 구명정에 도착해 탈출하세요!')
        self.current_scene = start_scene
        
    def next_scene(self, scene_name):
        print('지도를 따라 다음 장면으로 넘어갑니다.')
        print('어디서 외계인이 나올지 모르니 항상 긴장을 놓치지 마세요!')
        self.current_scene = scene_name
        
    def opening_scene(self):
        print('이번 씬에 입장합니다.')
        print('외계인이 나온다면 망설이지 말고 쏴 죽여버리세요!!')
        self.current_scene.enter()
        
a_map = Map('central_corridor')
#시작장면이 centarl_corridor인 맵을 만든다.
a_game = Engine(a_map)
#엔진에 지도를 넘겨준다.
a_game.play()