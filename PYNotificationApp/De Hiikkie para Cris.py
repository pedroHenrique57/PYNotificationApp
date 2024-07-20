import random
import time
from plyer import notification

# Variáveis
frases__pro__cris = [
    ["Quero te falar algo amor",
     "Poder ficar ao seu lado é um presente e eu tenho muita sorte de poder dizer isso, eu te amo vida ❤🧡"],
    ["Quero te falar algo amor", "Eu amo você de um tantãoooooo assimmm: ∞^∞ \n(É infinito a potência de infinito :p)"],
    ["Quero te falar algo amor", "Você é o meu safe spot e o motivo do meu sorriso, obrigado por ser incrível amor."],
    ["Quero te falar algo amor",
     "Você é a pessoa mais incrível, foda, master blaster, gigantescamente, fodasticamente especial que existe, você é foda vida 🔥"],
    ["Quero te falar algo amor", "Não consigo imaginar o futuro da minha vida sem você, meu coração."],
    ["Quero te falar algo amor", "Você é o motivo do meu sorriso."],
    ["Quero te falar algo amor", "COMIENZA MI LOCURAAAA 🤡"],
    ["Quero te falar algo amor", "Você é meu pretinho, minha inspiração para conquistar o amanhã e minha alegria."],
    ["Quero te falar algo amor", "Meu coração pertence a você e sempre pertencerá ❤."],
    ["Quero te falar algo amor", "Amo você mais do que qualquer coisa neste mundo \n(Até mais que Java)."],
    ["Quero te falar algo amor", "Cada dia que eu passar ao seu lado é um sonho que estou vivendo acordado."],
    ["Quero te falar algo amor", "Você é a pessoa que eu escolhi para amar para sempre."],
    ["Quero te falar algo amor", "Meu amor por você cresce mais a cada dia."],
    ["Quero te falar algo amor", "Você é a razão pela qual acredito no amor."],
    ["Quero te falar algo amor", "O tom não para nunca 🏎"],
    ["Quero te falar algo amor", "Só quero estar nos seus braços, poder sentir seu calor e seu carinho."],
    ["Quero te falar algo amor",
     "Você é meu amor, meu amigo e meu parceiro pra vida e para tudo que vir a acontecer, e estou aqui para você "],
    ["Quero te falar algo amor", "também meu pretinho."],
    ["Quero te falar algo amor",
     "Eu gosto do jeitinho que você faz as coisas e como você faz eu me sentir amado e cuidado."],
    ["Quero te falar algo amor",
     "Meu amor por você é incondicional. \n(POR MAIS QUE VOCÊ NÃO ME AMARIA SE EU FOSSE UMA MINHOCA 😂😭)"],
    ["Quero te falar algo amor", "Você é a minha outra metade, meu companheiro para a vida toda."],
    ["Quero te falar algo amor", "Cada momento ao seu lado é uma lembrança preciosa."],
    ["Quero te falar algo amor", "Você é a pessoa que completa a minha vida."],
    ["Quero te falar algo amor",
     "Não consigo verbalizar o quão grato sou por ter você ao meu lado, quero que você seja o meu namorado e planejar minha vida junto com você."],
    ["Quero te falar algo amor", "Meu coração se enche de alegria e eu fico bobinho cada vez que penso em você."],
    ["Quero te falar algo amor", "Você é o amor da minha vida e sempre será ❤"],
    ["Quero te falar algo amor", "Eu te amo mais a cada dia que passa, meu amor."],
    ["Quero te falar algo amor", "Ter você em minha vida é a maior benção que eu poderia receber."],
    ["Quero te falar algo amor",
     "Você faz meu coração bater mais rápido sempre que o vejo. \n(Abre mais a camêra seu panaca :p)"],
    ["Quero te falar algo amor", "Eu sou a pessoa mais feliz do mundo por ter você ao meu lado."],
    ["Quero te falar algo amor", "Seu sorriso é tão bonito. Adoro te ver feliz, me faz sorrir na hora."],
    ["Quero te falar algo amor", "Amar você é a melhor coisa que já me aconteceu na vida."],
    ["Quero te falar algo amor", "Você é o melhor presente que a vida poderia me dar."],
    ["Quero te falar algo amor",
     "Eu sou muito grato por poder compartilhar minha vida com você, e quero que você faça parte dela para toooooodo o sempre \n(Tu é meu refém agora 🔫, vem pro porão 🥰)"],
    ["Quero te falar algo amor", "Você é a pessoa que eu quero ao meu lado para sempre."],
    ["Quero te falar algo amor", "Você é o meu maior tesouro e minha maior alegria."],
    ["Quero te falar algo amor",
     "Eu amo cada coisinha sua, o seu cabelinho, o seu rostinho, o seu sorriso, o seu jeitinho de falar, o seu jeito de ser e se expressar, cada forma e jeito seu te faz ser incrível como é."],
    ["Quero te falar algo amor",
     "Você é a razão pela qual acordo feliz todos os dias e é a primeira coisa que penso no meu dia."],
    ["Quero te falar algo amor", "Eu não preciso de mais nada além de você para ser feliz."],
    ["Quero te falar algo amor", "Você faz meu mundo girar e meu coração acelerar."],
    ["Quero te falar algo amor", "Eu sou completo com você, meu amor."],
    ["Quero te falar algo amor", "Ter você ao meu lado é um sonho que se tornou realidade."],
    ["Quero te falar algo amor", "Você é a melhor parte da minha vida."],
    ["Quero te falar algo amor", "Cada momento ao seu lado é uma lembrança que guardo com carinho."],
    ["Quero te falar algo amor", "Você é a minha alma gêmea, meu destino, meu amor eterno."],
    ["Quero te falar algo amor", "Você é a razão pela qual eu acredito em finais felizes."],
    ["Quero te falar algo amor", "Eu não posso imaginar um futuro sem você ao meu lado."],
    ["Quero te falar algo amor", "Você é o amor da minha vida, e eu sou eternamente seu."],
    ["Quero te falar algo amor", "Meu precioso..... 🧝‍♂️💍"],
    ["Quero te falar algo amor", "Nosso amor e carinho é a melhor parte da minha vida."],
    ["Quero te falar algo amor", "Você é meu lar, onde quer que estejamos. Vem morar num porão comigo 👉👈."],
    ["Quero te falar algo amor", "Você é o melhor presente que a vida me deu."],
    ["Quero te falar algo amor", "Meu coração é seu, agora e para sempre ❤"],
    ["Quero te falar algo amor", "Quando noiz vai ter nossos lagartos?"],
    ["Quero te falar algo amor", "Não quero você para mim, quero você comigo."],
    ["Quero te falar algo amor", "Você é meu nenê."],
    ["Quero te falar algo amor",
     "Roberta Campos - Minha felicidade\nVocê é um pedaço em mim\nEu quero viver em teus braços\npra sempre"],
    ["Quero te falar algo amor",
     "Rubel - Quando Bate Aquela Saudade\nE eu tô com uma saudade apertada\nDe ir dormir bem cansado\nE de acordar do teu lado pra te dizer\nQue eu te amo\nQue eu te amo demais"],
    ["Quero te falar algo amor",
     "Jovem Dionisio - Pontos de Exclamação\nAgarre e não largue essa mão\nToda noite eu quero que você\nDiga que a vida foi feita pra viver\nDói o peito\nSó de olhar o jeito que tu posa\nSaudades, pontos de exclamação\nVocê está maravilhosa"]
]

frases__ligar__pc = [
    ["Quero te falar algo amor", "Oiii amorr, budiaaaaa ❤"],
    ["Quero te falar algo amor", "Inhaiii, bora um vava?"],
    ["Quero te falar algo amor", "PPSPSPSPSPSPS QUE GATINHO É ESSE AQUI?"],
    ["Quero te falar algo amor", "Mim manda mensagi, nunca te pedi nada :3"],
    ["Quero te falar algo amor", "Tô com saudades, bó fica juntin"],
    ["Quero te falar algo amor",
     "Heyy 👋, tipo assim... sabe, Tu não é o google 🤓, mas tem tudo 🌎 que eu tenho procurado"],
    ["Quero te falar algo amor", "Ei 👋, você não é Wi-Fi 📶, mas sinto uma conexão forte 💪 entre nós."],
    ["Quero te falar algo amor", "Desculpa pelos meme cringe de emoji."],
    ["Quero te falar algo amor", "Já tomou água hoje?"],
    ["Quero te falar algo amor",
     "Lembra que você tem que descansar, carregar o peso de ser uma gostosa como você dá trabalho!"],
    ["Quero te falar algo amor", "O que você pensa sobre a invasão alemã de 1941 a URSS?"],
    ["Quero te falar algo amor", "Vem cáaaa pra eu te dar um cheirinho nesse seu pescoço meu lindo"],
    ["Quero te falar algo amor", "E aí meu nenê? Como tá o dia? ❤️"],
    ["Quero te falar algo amor", "Tô morrendo de saudades, vamos ficar juntinhos logooooooo"],
    ["Quero te falar algo amor", "Ei, vamos assistir algo mais tarde depois? adoro ficar com você meu preto"],
    ["Quero te falar algo amor", "Você é o motivo do meu sorriso, obrigado por estar aqui amor, eu te amo"],
    ["Quero te falar algo amor", "Heyyy 👋, se eu fosse uma estrela 🌟, desejaria estar ao seu lado todas as noites 🌠"],
    ["Quero te falar algo amor", "Estou aqui para você, hoje e sempre. Só queria que soubesse"],
    ["Quero te falar algo amor", "Hey, só queria dizer que você é incrível do jeitinho que é"],
    ["Quero te falar algo amor", "Quando fico pensando em você, me pego sorrindo todo bobo ksksksk ❤"],
    ["Quero te falar algo amor", "Feijão por cima do arroz e eu por cima de vc bb"],
    ["Quero te falar algo amor", "Tá fazendo frio né? \nQuer um casaco?\nEntão vem casaco migo skskskksksk"],
    ["Quero te falar algo amor", "O que você pensa sobre o império romano?"],
    ["Quero te falar algo amor", "O que aconteceu no dia 21/03/1854 as 16:32:51?"]
]

icones__para__mensagens = [
    "_internal/assets/img/dragon1.ico",
    "_internal/assets/img/dragon2.ico",
    "_internal/assets/img/dragon3.ico",
    "_internal/assets/img/dragon4.ico",
    "_internal/assets/img/dragon5.ico",
    "_internal/assets/img/furry1.ico",
    "_internal/assets/img/furry4.ico",
    "_internal/assets/img/furry5.ico",
    "_internal/assets/img/furry6.ico",
    "_internal/assets/img/furry7.ico",
    "_internal/assets/img/furry8.ico"
]

#  --!! Runtime Code !!--

# Envia uma mensagem de boas-vindas

notification.notify(
    app_name="De Hiikkie para Cris",
    title="Bum diaaaaaa",
    message=random.choice(frases__ligar__pc),
    app_icon=random.choice(icones__para__mensagens),
    timeout=10
)

time.sleep(1800)

# Envia uma notificação infinitamente
while True:
    # Monta e posta a notificação
    notification.notify(
        app_name="De Hiikkie para Cris",
        title="Quero te falar algo amor",
        message=random.choice(frases__pro__cris),
        app_icon=random.choice(icones__para__mensagens),
        timeout=10
    )

    # Dá uma pausa de 1h 30m entre as notificações
    time.sleep(5400)
