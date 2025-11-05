from random import randint
import time
import os    
import redis 

r = redis.Redis(host='10.1.69.134', port=6379, db=0, decode_responses=True)
r.ping()

# --- (mantenha suas funções front, ui, anime, etc. exatamente como estão) ---

def front(state: int, user_credits, player2=0, player1=0):
    choi = ["👊", "🖐", "✌", "??"]
    # Evita erro se player for 0
    p2_icon = choi[player2 - 1] if player2 >= 1 else "??"
    p1_icon = choi[player1 - 1] if player1 >= 1 else "??"
    os.system("cls" if os.name == "nt" else "clear")
    print("+-------------------------------+")
    print(f"+user_credits:{user_credits}\t\t\t+")
    print("+-------------------------------+")
    print("+        ._._.     _|.|_        +")
    if state == 0:
        print("+       (´-_-`)   [´-_-`]       +")
        print("+       \\\\  //     \\\\  //       +")
        print(f"+       [{p2_icon}]//|     |\\\\[{p1_icon}]     +")
    elif state == 1:
        print("+       (´-_-`)   [´-_-`]       +")
        print("+        | \\\\ \\\\  // // |       +")
        print(f"+        +--\\[{p2_icon}][{p1_icon}]/--+       +")
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
    if typee == 1:
        while True:
            try:
                select = int(input("1) 👊\n2) 🖐\n3) ✌\nDigite sua jogada: "))
                if 1 <= select <= 3:
                    return user_credits, select
            except:
                pass
    elif typee == 2:
        print("QR CODE SIMULADO...")
        os.system("pause")
        return user_credits + 1, None

def anime(user_credits, player2, player1):
    front(state=0, user_credits=user_credits)
    for ii in range(1, 4):
        front(state=0, user_credits=user_credits, player2=0, player1=ii)
        time.sleep(0.3)
    for ii in range(1, 4):
        front(state=0, user_credits=user_credits, player2=0, player1=ii)
        time.sleep(0.3)
    front(state=1, user_credits=user_credits, player2=player2, player1=player1)
    time.sleep(2)
    if player2 == player1:
        return 0
    elif (player2 == 1 and player1 == 2) or (player2 == 2 and player1 == 3) or (player2 == 3 and player1 == 1):
        front(state=2, user_credits=user_credits)  # Vitória do Jogador 1
        time.sleep(2)
        return 1
    else:
        front(state=3, user_credits=user_credits)  # Vitória do Jogador 2
        time.sleep(2)
        return -1

# --- LÓGICA PRINCIPAL CORRIGIDA ---
if __name__ == '__main__':
    # Escolhe se é Jogador 1 ou Jogador 2
    print("Selecione seu papel:")
    role = input("Digite '1' para Jogador 1 ou '2' para Jogador 2: ").strip()

    if role not in ('1', '2'):
        print("Papel inválido. Saindo...")
        exit()

    is_player1 = (role == '1')

    # Inicializa créditos (compartilhado, mas pode ser por jogador se quiser)
    user_credits = int(r.hget("2367", "credits") or 0)

    print(f"Você é o {'Jogador 1' if is_player1 else 'Jogador 2'}")
    input("Pressione Enter quando ambos estiverem prontos...")

    while True:
        # 1. Faz sua jogada
        print(f"\n>>> Sua vez, {'Jogador 1' if is_player1 else 'Jogador 2'}! <<<")
        _, minha_jogada = ui(typee=1, user_credits=user_credits)

        # 2. Salva no Redis
        chave_minha = "p1" if is_player1 else "p2"
        chave_outro = "p2" if is_player1 else "p1"
        r.hset("2367", chave_minha, minha_jogada)

        print("Aguardando o outro jogador...")

        # 3. Aguarda a jogada do outro
        while True:
            jogada_outro = r.hget("2367", chave_outro)
            if jogada_outro and jogada_outro != "":
                jogada_outro = int(jogada_outro)
                break
            time.sleep(0.5)

        # 4. Resolve o jogo
        if is_player1:
            p2 = jogada_outro
            p1 = minha_jogada
        else:
            p2 = minha_jogada
            p1 = jogada_outro

        resultado = anime(user_credits=user_credits, player2=p2, player1=p1)

        # 5. Atualiza créditos (opcional: pode ser por jogador)
        if resultado == 1:
            print("\nJogador 1 venceu!")
            if is_player1:
                user_credits += 1
        elif resultado == -1:
            print("\nJogador 2 venceu!")
            if not is_player1:
                user_credits += 1
        else:
            print("\nEmpate!")

        r.hset("2367", "credits", user_credits)

        # 6. Limpa as jogadas para a próxima rodada
        r.hset("2367", "p1", "")
        r.hset("2367", "p2", "")

        input("\nPressione Enter para jogar novamente...")