# HLTV

**Número da Lista**: StackSmashingError<br>
**Conteúdo da Disciplina**: Grafos2<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0033620  |  João Henrique C. Paulino |
| 18/0052845  |  Gabriela da Gama Pivetta |

## Sobre 
<img src="https://www.hltv.org/img/static/openGraphHltvLogo.png">

Como tudo que é bom tem parte 2, aqui está a segunda temporada do projeto [CS:GO_Connections](https://github.com/projeto-de-algoritmos/grafos1_csgo_connections). Os dados obtidos são do site da [HLTV](https://www.hltv.org/stats/teams).

As principais funcionalidades adicionadas no sistemas serão:

- Árvore geradora mínima de players que estão presentes na hltv
- Componentes conectados



## Screenshots
### Ainda nao temos imagens comoventes do projeto
![](https://pm1.narvii.com/6302/0bfc3eb6cac07b21188ce5d49e69f4928804a208_hq.jpg)

## Instalação 

**Linguagem**: Python3<br>
**Framework**: Flask<br>
 - Instalacao dos pacotes necessarios
```
  $ sudo apt install virtualenv
  $ virtualen env
  $ source env/bin/activate
  $ pip3 install -r requirements.txt

```
 - Execucao do projeto
```
  $ cd src
  $ python3 app.py
```

## Uso 
Acessar a pagina inicial da aplicacao( localhost:5000 ) usando o seu navegado de preferencia e selecionar a ação aplicada no grafo.

## Outros 
O projeto pode ser separado em 3 partes.

 1. Crawler para capturar os dados providos pela hltv.
 2. Arquivos de processamento interno( BFS, ESTRUTURA GRAFO/PLAYER)
 3. Flask APP para exibicao do projeto com o html/css/js.

Na primeira vez que o seu projeto for executado ele vai demorar um pouco mais do que o normal( mais ou menos uns 50 segundos ou 2 min dependendo da sua maquina e conexao com a internet), pois uma rotina no arquivo app.py esta sendo executada para gerar o arquivo storage.csv ( que seria a base de dados do projeto).

Lembre-se para execucao correta do projeto esteja dentro da pasta src e em seguida execute app.py. A instalacao dos requirements.txt é fundamental.

link para o video de apresentacao: VideoNotFoundError
