![brasil-covid-1279x450](https://github.com/silasmaverick/Projects/blob/master/Covid_Engenharia/img/brasil-covid-1279x450.jpg)







Este projeto tenta replicar as informações, criar tabelas para possível replicação dos dashboards do site público https://covid.saude.gov.br/  que mostra a situação da pandemia de covid-19 no país. 

Com o arquivo público CSV disponível no site, extrai tabelas e apliquei algumas técnicas de engenharia de dados para construção de um pipeline em um cluster hadoop local, que foi construido usando imagens docker, até a construção de um dashboard com Google Data Studio com possibilidade de integração com o kafka e elasticSearch.


![arq](https://github.com/silasmaverick/Projects/blob/master/Covid_Engenharia/img/arq.jpg)
O primeiro passo foi fazer o download do arquivo .csv do site mencionado. Ele vem compactado em um arquivo .zip dividido em quatro arquivos. Fizemos a inserção dos arquivos para um diretório HDFS. Felizmente o Hive consegue enxergar esses arquivos como sendo um só. Fiz uma pré visualização do cabeçalho do csv e criei um schema para ingerir esses arquivos para uma tabela Hive. 

Essa será a tabela Raw e não será alterada para manter a integridade dos dados; 
A partir dela, Efetuei algumas transformações em dataframes spark para obter tabelas mais limpas para o objetivo final do dashboard. Dado o tamanho do arquivo, foi feita também a partição por nome de município, afim de otimizar buscas específicas. Essa tabela intermediária será salva na camada Silver de dados no nosso warehouse. Ela poderá ser usada para modificações e obtenções de dados refinados para análises. Entre as transformações estão: A alteração do tipo data, exclusão de colunas sem relevância (atual) para o projeto, criação de colunas com dados agregados para cálculo de índices relativos a Covid-19. A finalização se dá por dataframes refinados para análise e salvos na saída do spark como .csvs novos e tabelas no warehouse. 

Como desafio extra, as saídas foram replicadas para o kafka através de criação de um tópico próprio para receber mensagens do spark streaming ou batch, e  elasticSearch através de ingestão de .csv no próprio kibana. Foi possível ter uma visão geral dos dados presentes no .csv maiores ocorrências e outros insights. Posteriormente, em uma agregação no spark, é possivel transformar os dados em Json para facilitar buscas específicas do dataset. No caso do kafka, a informação recebida poderia disparar algum evento em aplicação externa que usa os dados recebidos para alguma tomada de decisão. 

Através do .csv gerado, foi feita a criação de um dashboard de demonstração na ferramenta Google DataStudio. Com os dados formatados corretamente e com o carimbo da data, foi possível obter curvas de tendência dos dados de óbitos. (Posteriormente, novos dashboards serão implementados).

Link dados https://covid.saude.gov.br/(* Os dados são atualizados diariamente. Para esse projeto foram utilizados os dados do dia 05/11/2021):  

**Link meus códigos e transformações: https://github.com/silasmaverick/Projects/blob/master/Covid_Engenharia/workinprogres3.ipynb**


**Requisitos recomendados:**

- S.O: Alguma Distribuição Linux 

- Software:  Docker: https://docs.docker.com/get-docker/ e  Docker Compose: https://docs.docker.com/compose/install

- Hardware: 8GB memória Ram (recomendado 16GB), Processador quad-core, 30GB livre no HD.

<br>  
<br>
<br>



***Working Progress: As instruções abaixo ainda estão em desenvolvimento. Não é recomendado segui-las por enquanto***

**Instruções para replicação do projeto**

- Obter a pasta do projeto:

```shel
https://github.com/silasmaverick/Projects/tree/master/Covid_Engenharia
```



- Baixar o cluster local a ser utilizado e imagens docker do elastic 

*Créditos Rodrigo Rebouças da Semantix Academy

``` 
git clone https://github.com/rodrigo-reboucas/docker-bigdata.git spark

docker pull docker.elastic.co/elasticsearch/elasticsearch:7.9.2
docker pull docker.elastic.co/kibana/kibana:7.9.2
docker pull docker.elastic.co/logstash/logstash:7.9.2
```

Setar vm.max_map (*pode variar de sistema pra sistema)

```shell
grep vm.max_map_count /etc/sysctl.conf
vm.max_map_count=262144
```

Entrar na pasta em que foi feito o download do cluster (EX: <>/home/.../spark/</>) e alterar o nome do docker-compose.yml para docker-compose_old.yml

Copiar o arquivo docker-compose.yml da projeto covidBr para a pasta dos arquivos do cluster

Iniciar todos os serviços em background (-d)
$ docker-compose up –d



**Informações extras:** 

Parar os serviços: $ docker-compose stop
Iniciar os serviços: $ docker-compose start

Matar os serviços:$ docker-compose down

Apagar todos os volumes sem uso: $ docker volume prune



- Leitura de dados e Dashboard Elastic
- Arquitetura alternativa na cloud com ingestão de API e atualização automática dos dados e dashboards



