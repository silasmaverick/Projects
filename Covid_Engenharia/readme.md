![brasil-covid-1279x450](/home/silas/Área de trabalho/Covid_Engenharia/img/brasil-covid-1279x450.jpg)







Este projeto tenta replicar as informações, criar tabelas para possível replicação dos dashboards do site público https://covid.saude.gov.br/  que mostra a situação da pandemia de covid-19 no país. 

Com o arquivo público CSV disponível no site, extrai tabelas e apliquei algumas técnicas de engenharia de dados para construção de um pipeline em um cluster hadoop local até a construção de um dashboard com o Elastic Search. 

![arq](/home/silas/Área de trabalho/Covid_Engenharia/img/arq.jpg)

Link dados (* Os dados são atualizados diariamente. Para esse projeto foram utilizados os dados do dia 05/11/2021):  

**Requisitos recomendados:**

- S.O: Alguma Distribuição Linux 

- Software:  Docker: https://docs.docker.com/get-docker/ e  Docker Compose: https://docs.docker.com/compose/install

- Hardware: 8GB memória Ram (recomendado 16GB), Processador quad-core, 30GB livre no HD.

  



Working Progress: As instruções abaixo ainda estão em produção

**Instruções para replicação do projeto**

- Obter a pasta do projeto:

```shel
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



