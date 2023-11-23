import CHaser
import random
import time

def myget_ready(turn, client):
    turn += 1
    value = client.get_ready()
    return value, turn

def main():
    value = []
    client = CHaser.Client()

    turn = 0

    while(True):
        value, turn = myget_ready(turn, client)
        #Turn Start Programm!!
        #アイテムが見つかったらアイテムを取る。また取れなかったらランダム移動を行う。
        #アイテム式開始
        if value[1]==3:
            client.walk_up()
        elif value[7]==3:
            client.walk_down()
        elif value[5]==3:
            client.walk_right()
        elif value[3]==3:
            client.walk_left()
        elif 3 in value[0::2]:
            # 0 1 2 
            # 3 4 5 
            # 6 7 8
            
            # 斜めにアイテムがあるか
            idou_dekiru = []
            if value[0]==3:
                #左上
                idou_dekiru = [3, 1]

            elif value[2]==3:
                #右上
                idou_dekiru = [5, 1]
            elif value[8]==3:
                #右下
                idou_dekiru = [5, 7]
            else:
                # 左下
                idou_dekiru = [7, 3]
            # 移動先にブロックないか確認
            ugokeru_houkou = []
            if value[1]!=2 and  1 in idou_dekiru:
                ugokeru_houkou.append('up')
            if value[7]!=2 and  7 in idou_dekiru:
                ugokeru_houkou.append('down')
            if value[5]!=2 and  5 in idou_dekiru:
                ugokeru_houkou.append('right')
            if value[3]!=2 and  3 in idou_dekiru:
                ugokeru_houkou.append('left')
            ugoku_houkou = random.choice(ugokeru_houkou)
            print(ugokeru_houkou)
            if ugoku_houkou=='up':
                client.walk_up()
            elif ugoku_houkou=='down':
                client.walk_down()
            elif ugoku_houkou=='right':
                client.walk_right()
            elif ugoku_houkou=='left':
                client.walk_left()
        else:
            print(value)
            if value[1]==1:
                value = client.put_up()
            elif value[7]==1:
                value = client.put_down()
            elif value[5]==1:
                value = client.put_right()
            elif value[3]==1:
                value = client.put_left()
                
            else:
                # ランダム移動　ここから
                random_walk = random.randint(0, 3)
                # 移動できる方向の配列用意する
                ugokeru_houkou = []
                if value[1]!=2:
                    ugokeru_houkou.append('up')
                if value[7]!=2:
                    ugokeru_houkou.append('down')
                if value[5]!=2:
                    ugokeru_houkou.append('right')
                if value[3]!=2:
                    ugokeru_houkou.append('left')
                # ugokeru_houkou = ['up', 'down', 'right', 'left']
                ugoku_houkou = random.choice(ugokeru_houkou)
                print(ugokeru_houkou)
                if ugoku_houkou=='up':
                    client.walk_up()
                elif ugoku_houkou=='down':
                    client.walk_down()
                elif ugoku_houkou=='right':
                    client.walk_right()
                elif ugoku_houkou=='left':
                    client.walk_left()

                # ランダム移動　ここまで

#Stop Program


if __name__ == "__main__":
    main()
    