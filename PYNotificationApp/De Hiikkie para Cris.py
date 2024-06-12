import random
import time
from plyer import notification

# Variáveis
frases__pro__cris = [
    "Poder ficar ao seu lado é um presente e eu tenho muita sorte de poder dizer isso, eu te amo vida ❤🧡",
    "Eu amo você de um tantãoooooo assimmm: ∞^∞ \n(É infinito a potência de infinito :p)",
    "Você é o meu safe spot e o motivo do meu sorriso, obrigado por ser incrível amor.",
    "Você é a pessoa mais incrível, foda, master blaster, gigantescamente, fodasticamente especial que existe, "
    "você é foda vida 🔥",
    "Não consigo imaginar o futuro da minha vida sem você, meu coração.",
    "Você é o motivo do meu sorriso.",
    "COMIENZA MI LOCURAAAA 🤡",
    "Você é meu pretinho, minha inspiração para conquistar o amanhã e minha alegria.",
    "Meu coração pertence a você e sempre pertencerá ❤.",
    "Amo você mais do que qualquer coisa neste mundo \n(Até mais que Java).",
    "Cada dia que eu passar ao seu lado é um sonho que estou vivendo acordado.",
    "Você é a pessoa que eu escolhi para amar para sempre.",
    "Meu amor por você cresce mais a cada dia.",
    "Você é a razão pela qual acredito no amor.",
    "O tom não para nunca 🏎",
    "Só quero estar nos seus braços, poder sentir seu calor e seu carinho.",
    "Você é meu amor, meu amigo e meu parceiro pra vida e para tudo que vir a acontecer, e estou aqui para você "
    "também meu pretinho.",
    "Eu gosto do jeitinho que você faz as coisas e como você faz eu me sentir amado e cuidado.",
    "Meu amor por você é incondicional. \n(POR MAIS QUE VOCÊ NÃO ME AMARIA SE EU FOSSE UMA MINHOCA 😂😭)",
    "Você é a minha outra metade, meu companheiro para a vida toda.",
    "Cada momento ao seu lado é uma lembrança preciosa.",
    "Você é a pessoa que completa a minha vida.",
    "Não consigo verbalizar o quão grato sou por ter você ao meu lado, quero que você seja o meu namorado e planejar "
    "minha vida junto com você.",
    "Meu coração se enche de alegria e eu fico bobinho cada vez que penso em você.",
    "Você é o amor da minha vida e sempre será ❤",
    "Eu te amo mais a cada dia que passa, meu amor.",
    "Ter você em minha vida é a maior benção que eu poderia receber.",
    "Você faz meu coração bater mais rápido sempre que o vejo. \n(Abre mais a camêra seu panaca :p)",
    "Eu sou a pessoa mais feliz do mundo por ter você ao meu lado.",
    "Seu sorriso é tão bonito. Adoro te ver feliz, me faz sorrir na hora.",
    "Amar você é a melhor coisa que já me aconteceu na vida.",
    "Você é o melhor presente que a vida poderia me dar.",
    "Eu sou muito grato por poder compartilhar minha vida com você, e quero que você faça parte dela para toooooodo o sempre \n(Tu é meu refém agora 🔫, vem pro porão 🥰)",
    "Você é a pessoa que eu quero ao meu lado para sempre.",
    "Você é o meu maior tesouro e minha maior alegria.",
    "Eu amo cada coisinha sua, o seu cabelinho, o seu rostinho, o seu sorriso, o seu jeitinho de falar, o seu jeito de "
    "ser e se expressar, cada forma e jeito seu te faz ser incrível como é.",
    "Você é a razão pela qual acordo feliz todos os dias e é a primeira coisa que penso no meu dia.",
    "Eu não preciso de mais nada além de você para ser feliz.",
    "Você faz meu mundo girar e meu coração acelerar.",
    "Eu sou completo com você, meu amor.",
    "Ter você ao meu lado é um sonho que se tornou realidade.",
    "Você é a melhor parte da minha vida.",
    "Cada momento ao seu lado é uma lembrança que guardo com carinho.",
    "Você é a minha alma gêmea, meu destino, meu amor eterno.",
    "Você é a razão pela qual eu acredito em finais felizes.",
    "Eu não posso imaginar um futuro sem você ao meu lado.",
    "Você é o amor da minha vida, e eu sou eternamente seu.",
    "Meu precioso..... 🧝‍♂️💍",
    "Nosso amor e carinho é a melhor parte da minha vida.",
    "Você é meu lar, onde quer que estejamos. Vem morar num porão comigo 👉👈.",
    "Você é o melhor presente que a vida me deu.",
    "Meu coração é seu, agora e para sempre ❤"
]

icones__para__mensagens = [
    "_internal/assets/img/dragon1.ico",
    "_internal/assets/img/dragon2.ico",
    "_internal/assets/img/dragon3.ico",
    "_internal/assets/img/dragon4.ico",
    "_internal/assets/img/dragon5.ico"
]


#  --!! Runtime Code !!--

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
