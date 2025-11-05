from random import randint
import time
import os    
import redis 

# Mude sua linha de conexão para isto:
r = redis.Redis(host='10.1.69.134', port=6379, db=0, decode_responses=True)
r.ping()


def front(state: int, user_credits, player2 = 0, player1 = 0):
    choi = ["👊", "🖐", "✌", "??"]
    player2 = choi[player2 - 1]
    player1 = choi[player1 - 1]
    os.system("cls")
    print("+-------------------------------+")
    print(f"+user_credits:{user_credits}\t\t\t+")
    print("+-------------------------------+")
    print("+        ._._.     _|.|_        +")
    if state == 0:
        print("+       (´-_-`)   [´-_-`]       +")
        print("+       \\\\  //     \\\\  //       +")
        print(f"+       [{player2}]//|     |\\\\[{player1}]     +")
    elif state == 1:
        print("+       (´-_-`)   [´-_-`]       +")
        print("+        | \\\\ \\\\  // // |       +")
        print(f"+        +--\\[{player2}][{player1}]/--+       +")
    elif state == 2:
        print("+       (*`_´*) 🖕[ ´-_-]       +")
        print("+     \\\\//   \\\\//  | \\_/|       +")
        print("+        +--+      |+--+|       +")
    elif state == 3:
        print("+       (-_-` )🖕 [*`_´*]       +")
        print("+       |\\_/ |  \\\\//   \\\\//     +")
        print("+        +--+      |+--+|       +")
    print("+       / || \\     / || \\       +")
    print("+_______c_|_|_'___c_|_|_'_______+")    

def ui(typee: int = 1, user_credits = 0):
    if typee== 1:
        while True:
            try:
                select = int(input("1) 👊\n2) 🖐\n3) ✌\nDigite sua jogada: "))
                if select > 0 and select < 4:
                    return user_credits, select
            except:
                pass
    elif typee == 2:
        print("+------------------+\n|######  #  #######|\n|# @ #   #  # # @ #|\n|#####  ##  # #####|")
        print("|# ##  # #  # #  ##|\n|##    #   #  ##  #|\n|#   # #    #   #  |\n|##### #   #   #  #|")
        print("|# @ #   #  #    ##|\n|#####  #   ##    #|\n+------------------+\nRealize o pagamento com o QR code!")
        os.system("pause")
        return user_credits + 1, None
        
def anime(
        user_credits,
        player2,
        player1):
    front(state=0, user_credits=user_credits)
    for ii in range(1, 4):
        front(state=0, user_credits=user_credits, player2=player2, player1=ii)
        time.sleep(0.5)
    for ii in range(1, 4):
        front(state=0, user_credits=user_credits, player2=player2, player1=ii)
        time.sleep(0.5)
    front(state=1, user_credits=user_credits, player2=player2, player1=player1)
    time.sleep(3)
    if player2 == player1:
        return 0
    else:
        if (player2 == 1 and player1 == 2) or (player2 == 2 and player1 == 3) or (player2 == 3 and player1 == 1):
            front(state=3, user_credits=user_credits)
            time.sleep(3)
            return -1
        else:
            front(state=2, user_credits=user_credits)
            time.sleep(3)
            return 1

def generete_win(choi = 1):
    if choi == 3:
        return 1
    else:
        return choi + 1

def generete_lost(choi = 1):
    if choi == 1:
        return 3
    else:
        return choi - 1

r.hset("2367", "p1", "")       
r.hset("2367", "p2", "")
while True:
    user_credits = int(r.hget("2367", "credits") or 0)
    user_credits, player1 = ui(typee=1, user_credits=user_credits)
    r.hset("2367", "p1", player1)
    while True:
        player2 = r.hget("2367", "p2")
        if player2 != "":
            player2 = int(player2)
            r.hset("2367", "p2", "")
            break
        time.sleep(1)
    result = anime(
        user_credits=user_credits,
        player2=player2,
        player1=player1)
    if result == 1:
        user_credits += 1
        print("Você ganhou 1 crédito!")
    elif result == -1:
        user_credits -= 1
        print("Você perdeu 1 crédito!")
    else:
        print("Empate!")
    r.hset("2367", "credits", user_credits)
    os.system("pause")