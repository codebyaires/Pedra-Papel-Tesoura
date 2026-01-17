# Pedra, Papel e Tesoura
# 🎮 Pedra, Papel e Tesoura em Rede com Redis 👊🖐✌️

Projeto acadêmico desenvolvido para a disciplina de Banco de Dados do Curso Técnico em Desenvolvimento de Sistemas - SENAI.

O objetivo foi aplicar os conhecimentos de **Bancos de Dados NoSQL** e **Integração de Sistemas Distribuídos** para evoluir um jogo local de "Pedra, Papel e Tesoura" para uma versão multiplayer em rede, utilizando **Redis** como principal meio de comunicação e persistência de estado.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)

---

## 🎯 Conceito Principal: A Arquitetura Distribuída

Diferente de uma abordagem tradicional com *sockets*, este projeto utiliza o **Redis como um intermediário (broker)** para gerenciar o estado do jogo e a comunicação entre os jogadores.

O fluxo de uma rodada funciona da seguinte maneira:

1.  **Seleção de Papel:** Ao iniciar, cada jogador escolhe ser "Jogador 1" ou "Jogador 2".
2.  **Envio da Jogada:** O Jogador 1 faz sua escolha (Pedra, Papel ou Tesoura) e a escreve em um *hash* específico no Redis (ex: `hset "2367" "p1" "1"`).
3.  **Polling (Consulta):** O Jogador 2 faz o mesmo, escrevendo sua jogada no campo `"p2"`. Simultaneamente, ambos os scripts ficam em um loop, consultando (fazendo *polling*) o Redis a cada meio segundo, esperando a jogada do oponente aparecer.
4.  **Resolução:** Assim que um script detecta que a jogada do oponente foi registrada no Redis, ele processa o resultado (vitória, derrota ou empate).
5.  **Animação e Persistência:** O script exibe a animação em ASCII art correspondente e atualiza os "créditos" (pontuação) no Redis.
6.  **Limpeza:** As jogadas `"p1"` e `"p2"` são limpas do Redis, e o loop recomeça para a próxima rodada.

---

## ✨ Funcionalidades

* **Multiplayer em Rede:** Permite que dois jogadores em máquinas diferentes (conectadas ao mesmo servidor Redis) joguem em tempo real.
* **Interface Gráfica de Terminal:** O jogo utiliza `os.system('cls')` e `time.sleep()` para criar animações em ASCII art diretamente no terminal.
* **Persistência de Estado com Redis:**
    * As jogadas (`p1`, `p2`) são armazenadas temporariamente.
    * A pontuação ("créditos") é armazenada de forma persistente.
* **Sincronização via Polling:** O jogo demonstra um método de integração de sistemas distribuídos onde os clientes consultam ativamente o banco de dados para sincronizar o estado.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem Principal:** Python 3
* **Banco de Dados NoSQL:** Redis
* **Bibliotecas Python:**
    * `redis`: O driver oficial do Redis para Python, usado para toda a comunicação com o banco.
    * `time`: Utilizado para os `sleeps` que controlam a velocidade da animação e o *rate* do *polling*.
    * `os`: Usado para limpar a tela do terminal (`cls` ou `clear`) a cada frame da animação.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

* Python 3.x
* Um servidor Redis acessível na rede (local ou remoto).
* A biblioteca Python `redis`.

### 1. Instalar a Biblioteca

Se você ainda não a possui, instale a biblioteca `redis` via pip:

```bash```

pip install redis
### 2. Configurar a Conexão

Antes de executar, você **DEVE** alterar a linha de conexão do Redis no código para apontar para o seu servidor.

Abra o arquivo `.py` e edite esta linha:

```python```
# Mude o 'host' para o IP do seu servidor Redis
r = redis.Redis(host='SEU_IP_DO_REDIS_AQUI', port=6379, db=0, decode_responses=True)

3. Como Jogar
Abra dois terminais separados. Eles podem estar na mesma máquina ou em máquinas diferentes, desde que ambas tenham acesso ao servidor Redis configurado.

Execute o script Python em ambos os terminais:

Bash

python nome_do_arquivo.py
No primeiro terminal, digite 1 e pressione Enter para se tornar o Jogador 1.

No segundo terminal, digite 2 e pressione Enter para se tornar o Jogador 2.

Pressionem Enter quando ambos estiverem prontos.

Façam suas jogadas (1, 2 ou 3) e assistam ao resultado!

O jogo continuará automaticamente para a próxima rodada.

## 👥 Autores

[Victor Aires] - (https://github.com/codebyaires)

[Vitor] - (https://github.com/Vitor-ALucn)

[Peterson] - (https://github.com/ruivocodespace)
