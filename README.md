# API_money
Este é um projeto que converte moedas

Configuração
Requisitos: Docker, Docker Compose e postgresql .

Abra um terminal e siga estas instruções:

# 1. Decida onde colocar o projeto. Usamos "~/Área de trabelho" em nossos exemplos. 
cd  ~ /Área de trabelho"
 # 2. Clone o repositório API_money". 
git clone https://github.com/HelderMenegatti/API_money.git 
# 3. Dentro do diretorio clonado execute os seguintes comandos
docker-compose buil(para isntalar as dependencias).

docker-compose run web python3 manage.py migrate(Para rodar as migrações em seu banco local).
 # 4. Execute o projeto com.
 docker-compose up
# 5. Pares de moedas aceitos.
https://economia.awesomeapi.com.br/xml/available
pares de moedas adicinados nos modelos Django servem como exemplo, mas demais pares da lista acima funionam perfeitamente.
# 6. Ultilização da API
Deve ser realizado um post com a seguinte extrutura de dados:

{

    "from_coins": "USD",
    
    "to_coins": "BRL",
    
    "amount": "10"
}

from_coins é a moeda que  servira de base.

to_coins é a moeda que será convertida.

amount é o valor que será covertido e uma moéda para outra.

A url que dever ser enviado o pos é a 0.0.0.0:8000/api
# 7. Resposta da API.
Se todos os parametros de envios estiverem corretos o response deve parecer como este abaixo:

{

    "from": "EUR",
    
    "to": "USD",
    
    "amount": 2.0,
    
    "result": "2.22"
}

Este Json retorna os pares escolhidos, a quidade escolhida e o resultado da converção.