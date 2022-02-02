![](https://github.com/silasmaverick/Projects/blob/master/5_events_site/img/pipelineAws.png)

**Objetivo:**

Manuseio e prática de construção de um pipeline de dados em ambiente real AWS. Documentação de processos, pacotes e bibliotecas usados para realizar o estudo. Aplicar na prática um projeto básico de dbt com arquitetura ELT.



**O Pipeline de dados na Aws**

A idéia é ingerir eventos de um script python (créditos André Sionek) com o kinesis Firehose, Salvar em um bucket de dados brutos no s3, fazer um catálogo de dados no glue catalog e execultar queries no Athena.  Na sequência, carregar dados no Redshift fazer pequenas transformações e aplicar modelagem para na saída se obtenha dados limpos para plataformas de BI e outos consumidores, tal como powerBi, C-level, analistas de dados. O ambiente AWS foi configurado via painel dos serviços em web browser. 



**O script**

Trata-se de um script de Stream de eventos ocorrido em um determinado site de e-commerce. O fake events simula atividades de usuários através de cookies simulados tais como: cliques, navegação por páginas (página do produto, carrinho, sessões etc) entre outros eventos. Algumas das informações presentes nesse stream são: da onde o cliente veio, id do clique, timezone, endereço de ip, endereço de email, latitude e longitude e ID do cookie.   



**O boto3**

O boto3 é uma biblioteca  que facilita a integração de sua aplicação, biblioteca ou script  Python (ou outras linguagens) aos serviços da AWS, incluindo Amazon S3, Amazon EC2 e Amazon  DynamoDB, entre outros. Nesse projeto, o boto3 foi utilizado para interagir com o Redshift. 



**O bucket no S3**

Serviço de armazenamento da AWS. O Amazon Simple Storage Service (Amazon S3) é um serviço de  armazenamento de objetos que oferece escalabilidade, disponibilidade de  dados, segurança que entre outros itens oferece a possibilidade de ser base de um data lake. Servirá para armazenamento geral de dados e metadados. *acesso publico bloqueado. 



**O Kinesis firehose**

O Amazon Kinesis Data Firehose é a maneira mais fácil de carregar de  forma confiável dados de streaming em data lakes, armazenamentos de  dados e serviços de análise. Ele pode capturar, transformar e entregar  dados de streaming para os serviços Amazon S3, Amazon Redshift Ele  também pode separar em lotes, compactar, transformar e criptografar  streams de dados antes de carregá-los, o que minimiza o volume de  armazenamento usado e aumenta a segurança. No nosso caso, o firehose será responsável por receber os dados do stream gerado pelo script e salvá-lo no Amazon S3.



**O Glue Crawler**

O AWS Glue Data Catalog contém referências a dados que são usados como fontes e destinos dos seus trabalhos de extração, transformação e  carregamento (ETL) no AWS Glue. Para criar o data warehouse ou o data  lake, é necessário catalogar esses dados. O AWS Glue Data Catalog é um  índice para as métricas de localização, esquema, dentre outros, para preencher o AWS Glue Data Catalog com tabelas. Um crawler Glue pode  rastrear vários armazenamentos de dados em uma única execução. Após a  conclusão, o crawler cria ou atualiza uma ou mais tabelas no Data  Catalog. No nosso caso, o Crawler do glue, irá inferir o esquema dos dados do stream e salvá-lo como tabela no bucket. update all new and existing partitions.



**O Amazon Athena**

O Amazon Athena é um serviço de consultas interativas que facilita a  análise de dados no Amazon S3 usando SQL padrão. O Athena não precisa de servidor. Portanto, não há infraestrutura para gerenciar e você paga  apenas pelas consultas executadas.O Athena é fornecido já integrado ao [AWS Glue](https://aws.amazon.com/pt/glue/) Data Catalog. Vamos usá-lo para fazer consultas básicas nos dados que chegam do streaming no bucket do s3.  



O Amazon Redshift

O Amazon Redshift usa SQL para analisar dados estruturados e  semiestruturados em data warehouses, bancos de dados operacionais e data lakes, usando hardware e machine learning projetados pela AWS para  oferecer a melhor performance de preço em qualquer escala.  Com a utilização do spectrum, vamos conseguir queries direto no data lake evitando assim materializar grande volume de dados cortando custos.       



**O DBT**

Ferramenta de Transformação de dados que se preocupa com documentação e Data Quality. Nessa fase serão aplicadas regras de negócio, documentação (catálogo) de transformações claras para tornar os dados confiáveis com governança e testes. Alguns dos requisitos são: Dados já salvos no data lake ou warehouse, dado não muda no momento da execução e transformação feita em SQL. Algumas transformações e regras aplicadas: 

- Limpeza : 
  - 'event_timestamp ' string para timestamp
  - 'user_domain_id' nome para 'cookie_id'
  - 'landing_date' string para data
- Modelagem de dados:
  - Se a diferença entre o timestamp do id de um cookie e  outro for maior do que 30 minutos, considerar como nova sessão no site. 
  - Verificar quais sessões converteram pra venda.
