from random import randint
import time
import os    


def front(state: int, user_credits, user_j = 0, machine_j = 0):
    choi = ["👊", "🖐", "✌", "??"]
    user_j = choi[user_j - 1]
    machine_j = choi[machine_j - 1]
    os.system("cls")
    print("+-------------------------------+")
    print(f"+user_credits:{user_credits}\t\t\t+")
    print("+-------------------------------+")
    print("+        ._._.     _|.|_        +")
    if state == 0:
        print("+       (´-_-`)   [´-_-`]       +")
        print("+       \\\\  //     \\\\  //       +")
        print(f"+       [{user_j}]//|     |\\\\[{machine_j}]     +")
    elif state == 1:
        print("+       (´-_-`)   [´-_-`]       +")
        print("+        | \\\\ \\\\  // // |       +")
        print(f"+        +--\\[{user_j}][{machine_j}]/--+       +")
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
        user_j,
        machine_j):
    front(state=0, user_credits=user_credits)
    for ii in range(1, 4):
        front(state=0, user_credits=user_credits, user_j=user_j, machine_j=ii)
        time.sleep(0.5)
    for ii in range(1, 4):
        front(state=0, user_credits=user_credits, user_j=user_j, machine_j=ii)
        time.sleep(0.5)
    front(state=1, user_credits=user_credits, user_j=user_j, machine_j=machine_j)
    time.sleep(3)
    if user_j == machine_j:
        return 0
    else:
        if (user_j == 1 and machine_j == 2) or (user_j == 2 and machine_j == 3) or (user_j == 3 and machine_j == 1):
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

if __name__ == '__main__':
    user_credits = 0
    cw = 0
    cl = 0
    while True:
        front(state=0, user_credits=user_credits)
        if user_credits > 0:
            user_credits, user_j = ui(1, user_credits)
            machi_j = randint(1, 3)
            
            # Manipulação dos resultados
            if cw > 2:
                machine = generete_win(user_j)
                cw = 0
            if cl > 4:
                machine = generete_lost(user_j)
                cl = 0
            
            resul = anime(user_credits=user_credits, user_j=user_j, machine_j=machi_j)
            if resul < 0:
                cw +=1
            else:
                cl +=1    
            user_credits += resul
        else:
            user_credits, select = ui(2, user_credits)

