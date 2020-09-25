# -*- coding: utf-8 -*-

from sys import exit
from random import randint  

class Scene(object):
# 각 장면마다 입장을 해야하니깐 이걸 상속해줄거야
#각자 구체적인 내용은 자식클래스에서 쓰는걸로 하고, 여기서는 그냥 함수를 만들어만 놓자.

    def enter(self):
        print('아직 만들지 않은 장면입니다. 상속해 enter()를 구현하세요.')
        exit(1)
        
class Engine(object):
#엔진은 지도를 받아서 다루는 역할을 함. 즉 게임을 진행해나가는 역할을 할거야. 
    def __init__(self, scene_map):
        print('엔진 __init__의 scene_map', scene_map)
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()
        print('play의 첫 장면', current_scene)
        
        while True:
            print('\n------------')
            next_scene_name = current_scene.enter()
            print('다음 장면', next_scene_name)
            current_scene = self.scene_map.next_scene(next_scene_name)
            print('지도에서 받은 새 장면', current_scene)
            
    
class Death(Scene):
#죽었을때를 나타내는 장면
    quips = [
    '사망. 이거 진짜 못하네요.',
    '어머니가 자랑스러워 하시겠어요... 좀 더 똑똑하셨다면요.',
    '패배자 같으니.',
    '제가 기르는 강아지도 이거보단 잘 해요.'
    ]
    
    def enter(self):
        print (Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)
        
class CentralCorridor(Scene):
#중앙복도를 나타내는 장면
    def enter(self):
        print('''페르칼 25번 행성의 고던족은 여러분의 우주선에 침략하고 모든 승무원을
        죽였습니다. 당신은 마지막 생존자이며 마지막 임무로 무기고에서 중성자탄을
        가져와 다리에 설치하고 구명정에 타기 전에 우주선을 폭파해야 합니다.\n
        붉은 비늘 피부, 시커먼 때가 낀 이빨, 증오로 가득 찬 몸에서 물 흐르듯 
        이어지는 사악한 광대 복장의 고던인이 뛰쳐나오는 동안 당신은 중앙
        복도에서 무기고로 내달리고 있습니다. 고던인은 무기고로 가는 문을 가로막고
        당신을 날려버리려 무기를 겨누는 참입니다.''')
        action = input('>')
        
        if action == '발사!':
            print('''당신은 광선총을 빼들기가 무섭게 고던인을 쏘아버립니다. 광대옷이 날려
            몸가로 밀려나 당신의 조준을 흩뜨립니다.광선은 광대옷은 맞추었지만
            고던인은 완전히 놓쳐버립니다. 고던인은 어머니가 사 준 신상 옷이 모조리 
            망가지자 광기 어린 분노에 빠져들어 당신이 죽을 때까지 얼굴을 쏘아 
            댑니다. 그리고는 당신을 먹어 치웁니다.''')
            return 'death'
            
        elif action == '회피!':
            print('''세계적인 권투 선수처럼 달리고 피하고 구르고 오른족으로 미끄러져
            고던인의 광선총이 당신의 머리 옆으로 빗겨 나도록 합니다. 예술적으로 회피하는 
            동안 발이 미끄러져 금속 벽에 머리를 치고 기절합니다. 잠시 후 정신을 
            차리지만 고던인에게 머리를 짓밟혀 죽고 잡아 먹힙니다.''')
            return 'death'
            
        elif action == '농담하기':
            print('''운 좋게도 당신은 학교에서 고던어 욕설을 배웠습니다. 아는 고던 농담을
            하나 합니다.
            Lbhe zbgure vf fb sng jura fur fvgf nebhaq gur ubhfr, 
            fur fvgf negbharq gur ubhfr.
            고던인은 멈춰서 웃지 않으려 하지만, 결국 웃음이 터지자 움직이지 못합니다.
            당신은 고던인이 웃는 동안 뛰쳐나가 머리를 정통으로 맞춰 쓰러뜨리고 무기고
            문으로 뛰어듭니다.''')
            return 'laser_weapon_armory'
            
        else:
            print('처리할 수 없습니다!')
            return 'centarl_corridor'
            
class LaserWeaponArmory(Scene):
#레이저 무기고를 나타내는 장면
    def enter(self):
      print("""당신은 무기고로 뛰어 굴러 들어가 쪼그려 앉고 방을 살피며 숨어 있을지도
      모르는 고던인을 찾습니다. 쥐죽은 듯이, 지나치게 조용합니다.
      일어서서는  문 건너편으로 달려가 컨테이너에서 중성자탄을 찾습니다.
      상자는 비밀번호로 잠겨 있고 폭탄을 꺼내려면 비밀번호를 알아내야만
      합니다. 비밀번호를 10번 틀리면 자물쇠는 영원히 잠기고 폭탄을 꺼낼 수 
      없습니다. 비밀번호는 3자리수 입니다.""")
      
      code = "%d%d%d" %(randint(1, 9), randint(1,9), randint(1,9))
      #변수선언할때 이렇게도 할 수 있따는거 너무 신기하지 않냐?
      
      guess = input('[번호판]>')
      guesses = 0
      while (guess != code and guesses < 10):
        print("삐비비빅!")
        guesses+= 1
        guess = input('[번호판]>')

        if guess == code:
          print("""철컥하며 컨테이너가 열리고 틈새로 공기가 새어나옵니다. 
          중성자탄을 움켜쥐고 설치해야 할 장소인 다리를 향해 할 수 있는 한
          가장 빠른 속도로 달립니다. """)
          return 'the_bridge'
          
        else:
          print("""마지막 순간에 자물쇠가 웅웅거리고 기계장치가 엉겨 붙으며 녹아내리는 
          역겨운 소리가 들립니다. 당신은 그대로 앉아 있기로 결정했고, 결국 
          고던 우주선이 당신의 우주선을 날려버려 죽게 됩니다.""")
          return 'death'

class TheBridge(Scene):
#다리를 나타내는 장면
    def enter(self):
      print("""당신은 팔에 중성자탄을 끼고 달리로 뛰어들어 우주선 조종권을
      빼앗으려던 고던인 5명을 놀라게 합니다. 그 모두가 방금 전에 본
      고던인보다 더 못생긴 광대 복장을 하고 있습니다. 아직 무기를 뽑지는 
      않았지만 당신이 팔에 낀 활성화된 폭탄을 보고 터뜨리지 않고 싶어 
      합니다""")

      action = input('>')

      if action == '폭탄 던지기':
        print("""당신은 당황해서 고던인 무리에 폭탄을 집어 던지고 문으로 펄쩍
        뛰어 오릅니다. 폭탄을 놓자마자 고던인이 뒤에서 당신을 쏴 맞추어 
        죽여버립니다.
        죽어가는 동안 다른 고던인이 미친듯이 폭탄을 해체하려는 것을 
        봅니다. 당신은 폭탄이 터지면 고던인 모두가 터져 나가리라고 
        깨달으며 죽습니다.""")
        return 'death'
      elif action == '천천히 폭탄 설치하기':
        print("""팔에 낀 폭탄을 광선총으로 겨누자 고던인들은 팔을 들고 땀을 흘리기 
        시작합니다. 당신은 문 뒤에 바짝 붙어 열고 광선총을 겨눈 채로
        조심스럽게 폭탄을 바닥에 설치합니다.
        다음으로 문 밖으로 뛰쳐 나와 닫기 버튼을 두드리고 잠금장치를
        쏴버려 고던인들이 나올 수 없게 만들어버립니다.
        이제 폭탄을 설치되었고 당신은 이 깡통에서 벗어나기 위해 구명정으로 
        달려갑니다.""")
        return 'escape_pod'
      else:
        print('처리할 수 없습니다!')
        return 'the_bridge'

class EscapePod(Scene):
#구명정을 나타내는 장면
    def enter(self):
        print('''우주선이 통째로 폭발하기 전에 구명정에 닿기 위해 우주선을 가로질러
        필사적으로 달립니다. 우주선에는 고던인이 거의 없어 방해받지 않고
        질주합니다. 당신은 구명정이 있는 방에 도달하고 이제 하나를 골라야
        합니다. 이 중 몇개는 손상되었을 수 있지만 살펴볼 시간이 없습니다.
        구명정이 5대 있습니다. 몇 번을 타겠습니까?
        ''')
        
        good_pod = randint(1, 5)
        guess = input('[구명정 번호]>')
        
        if int(guess) != good_pod:
            print(f"""{guess}번 구명정으로 뛰어들어 탈출 단추를 누릅니다.
            구명정은 우주의 진공으로 빠져나가고, 콩깍지가 터지듯 안으로 
            무너지며 당신을 곤약처럼 으스러뜨립니다.""")
            return 'death'
            
        else:
            print(f"""{guess}번 구명정으로 뛰어들어 탈출 단추를 누릅니다.
            구명정은 가볍게 우주로 미끄러져 나가며 아래의 행성으로 향합니다.
            행성으로 날아가는 동안 뒤돌아보니 우주선이 파괴되면서 밝은 별처럼
            폭발하고 고던 우주선까지 없애버리는 것을 확인합니다.
            당신이 이겼습니다!""")
            
            return 'finished'
            
class Map(object):
#지도는 기본적으로 시작하는 장면을 받고, 오프닝씬과 다음씬에 대한 함수를 가지고있음. 
    
    scenes = {
        'centarl_corridor': CentralCorridor(), 
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge' : TheBridge(),
        'escape_pod' : EscapePod(),
        'death' : Death()
        }
    '''뼈대만 주어지고 나혼자 짜볼때 막혔던 부분이 어떻게 다음부분으로 넘어갈것이냐였는데,
    그문제를 딕셔너리를 활용해서 해결했네. 
    딕셔너리의 value 값에 함수호출을 넣을수 있다는게 이번에 알게된 사실임. ㅈㄹ 신기하다.
    '''
    
    def __init__(self, start_scene):
        #현재 씬을 시작씬으로 설정해주고, 틀어주면 됨. 
        self.start_scene = start_scene
        print("__init__의 start_scene", self.start_scene)
        
    def next_scene(self, scene_name):
        print("next_scene의 start_scene")
        val = Map.scenes.get(scene_name)
        print("next_scene 결과는 ", val)
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
a_map = Map('central_corridor')
#시작장면이 centarl_corridor인 맵을 만든다.
a_game = Engine(a_map)
#엔진에 지도를 넘겨준다.
a_game.play()
