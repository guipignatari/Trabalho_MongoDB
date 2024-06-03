### Criação de um sistema de gestão de estoque em MongoDB por:
    Isadora Moresco
    Evelyn de Gois Meneses
    José Bulgarelli Neto
    Bianca Fernanda Leite 
    Guilherme Vinicius Pignatari

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)    

# Apresentação Introdução
  A criação de um sistema de gestão de estoque eficaz é crucial para o sucesso da operação de uma cadeia de supermercados. Este projeto foi criado para atender a essa necessidade, usando uma abordagem que alia a robustez do MongoDB à flexibilidade da linguagem Python. O MongoDB foi escolhido devido sua utilização em sala de aula e sua capacidade de lidar com grandes volumes de dados, proporcionar alta disponibilidade e escalabilidade, características fundamentais para um sistema de gerenciamento de estoque. O banco de dados foi configurado com três shards, distribuídos de forma a equilibrar a carga e otimizar o tempo de resposta.

# Projeto e Implementação

## Organização do Banco de Dados
Baseado na avaliação, o MongoDB foi dividido em três shards. A opção por sharding teve como objetivo assegurar que o sistema pudesse se expandir horizontalmente, atendendo a um aumento na demanda sem prejudicar o desempenho. Cada shard foi configurado para armazenar um subconjunto dos dados, distribuídos de acordo com a chave de sharding definida para melhorar a distribuição e a eficiência das operações de leitura e escrita.
Para criar e administrar os shards, foi criado um script em Python. O programa automatizou o processo de configuração, incluindo a criação dos shards, a definição das réplicas e a configuração da chave de sharding. 

[Prepara Ambiente](https://github.com/isamoresco25/Trabalho_MongoDB/blob/main/PreparaAmbiente.ipynb)

## Desenvolvimento do Script para inserção de dados
Para popular os dados no MongoDB, foi desenvolvido um script utilizando bibliotecas como random para a criação de dados aleatórios. Esse script gera um conjunto de dados combinando nomes de produtos com descrições de produtos, bem como nomes de filiais com suas respectivas localizações. Dessa forma, ele cria um "cross join" aleatório entre essas listas para a inserção dos dados no banco.

A biblioteca `random` foi fundamental para essa tarefa, pois permite a geração de dados aleatórios, garantindo diversidade e imprevisibilidade nos registros criados. A função random.choice foi usada para selecionar aleatoriamente elementos das listas de nomes de produtos, descrições, nomes de filiais e localizações. Além disso, a função `random.randint` foi utilizada para gerar valores numéricos aleatórios, como IDs de produtos e filiais.

**O script segue o seguinte fluxo:**

_- Criação de listas de dados base:_

Lista de nomes de produtos, lista de descrições de produtos, lista de nomes de filiais, lista de localizações de filiais.
  
_- Geração de combinações aleatórias:_

Utilizando a função `random.choice`, o script seleciona aleatoriamente um nome de produto e uma descrição para formar um registro de produto. De forma similar, seleciona aleatoriamente um nome de filial e uma localização para formar um registro de filial.
  
_- Inserção no MongoDB:_

Os registros gerados aleatoriamente são então inseridos no MongoDB, utilizando a biblioteca `pymongo` para a comunicação com o banco de dados.
  
Com esse método, é possível gerar um volume significativo de dados variáveis para fins de teste ou preenchimento inicial de um banco de dados, facilitando o desenvolvimento e a validação de funcionalidades dependentes desses dados.
O Python foi escolhido devido à sua simplicidade e poderosas bibliotecas de automação, o que facilita a interação com o MongoDB e inserção dos dados.

[Inserção de dados iniciais](https://github.com/isamoresco25/Trabalho_MongoDB/blob/main/carregar_produtos.py)

## Testes

### Inserção de dados
Inclusão de 10.000 registros com script em Python
![image](https://github.com/isamoresco25/Trabalho_MongoDB/assets/33660095/fe947aa9-605d-40cb-81bb-769fdd326c01)

Inserção de milhões de linhas com o mesmo script em Python
![image](https://github.com/isamoresco25/Trabalho_MongoDB/assets/33660095/ceb7073c-f101-4bda-8b2a-82958a0f2f8e)

### Leitura dos dados
![image](https://github.com/isamoresco25/Trabalho_MongoDB/assets/33660095/946a7e2a-7c9f-4f0b-ae97-e9ac826987f0)

### Atualiações de dados
Atualização de produtos com preço de 16.31 para 32.57 (5 linhas afetadas)
![image](https://github.com/isamoresco25/Trabalho_MongoDB/assets/33660095/093fbf8a-455c-4934-aa6a-21fe1f09b0a0)

Atualização com milhões de linhas
![image](https://github.com/isamoresco25/Trabalho_MongoDB/assets/33660095/71631f0b-7c45-4790-97d2-8c5d4d8ba8d4)

### Exclusão de dados
![Badge em Processamento](http://img.shields.io/static/v1?label=STATUS&message=EM%20PROCESSAMENTO&color=GREEN&style=for-the-badge)    


## Os resultados dos testes de desempenho foram apresentados
Após a implantação, o sistema foi submetido a uma série de testes de desempenho para testar sua eficiência em condições operacionais ideais. Os resultados mais relevantes incluem:
Tempo de Resposta: As operações de leitura e escrita tiveram um tempo médio de `__Alterar valor conforme relaidade do banco: 50ms__`, mesmo sob uma grande quantidade de consultas simultâneas.
A configuração com réplicas garantiu uma alta disponibilidade do sistema, com um tempo de inatividade próximo a zero nos testes de failover.

# Sugestões para Melhorias
Apesar de os testes de desempenho terem mostrado resultados satisfatórios, algumas áreas para melhorar foram identificadas:
- Otimização de Consultas: Revisar e otimizar as consultas MongoDB para diminuir ainda mais o tempo de resposta, sobretudo em operações complexas de agregação;
- Adotar um sistema de monitoramento mais eficiente para identificar e responder prontamente a problemas de desempenho ou falhas;
- Escalabilidade: Implementar escalabilidade automática para processar grandes volumes de dados;
Essa abordagem, que combina uma infraestrutura robusta com técnicas de otimização constante, garante que o sistema de gerenciamento de estoque possa evoluir para atender às crescentes demandas da cadeia de supermercados, proporcionando um serviço eficiente e confiável.

# Referências
https://gustavo-leitao.medium.com/criando-um-cluster-mongodb-com-replicaset-e-sharding-com-docker-9cb19d456b56

