# csgo_connections

**Número da Lista**: NullPointerException<br>
**Conteúdo da Disciplina**: Grafos1<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0033620  |  João Henrique C. Paulino |
| 18/0052845  |  Gabriela da Gama Pivetta |

## Sobre 
<img src="https://img-tlctv1.mncdn.com/mnresize/640/-/upload/20-08/07/cs-go-101-620x350.jpg?0.7478140750624982">

O projeto foi inspirado no conceito de [six degrees of separation](https://en.wikipedia.org/wiki/Six_degrees_of_separation#:~:text=Six%20degrees%20of%20separation%20is,as%20the%20six%20handshakes%20rule.), que curiosamente gerou o problema de [Kevin Bacon](https://blogs.ams.org/mathgradblog/2013/11/22/degrees-kevin-bacon/), que diz que todo ator de Hollywood tem alguma conexão com Kevin. Dado este ponto de partida, o programa tem como cerne saber qual a distancia entre 2 jogadores de [CS:GO](https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/?l=brazilian).

Para criar o grafo e suas conexões são levados em conta os seguintes fatores:
 - Os dados são obtidos pela [hltv](https://www.hltv.org/stats/teams)
 - Se um player **x** já esteve presente na mesma lineup que **y** , então a distância entre eles é 1.
 - A distancia do player **x** ate ele mesmo e 0.
 - O grafo pode nao ser conexo

## Screenshots
Adicione 3 ou mais screenshots do projeto em funcionamento.

## Instalação 
**Linguagem**: Python3<br>
**Framework**: (caso exista)<br>
 - Instalacao dos pacotes necessarios
```
$ virtualen env
$ source env/bin/activate
$ pip3 install -r requirements.txt

```
 - Execucao do projeto
  ```
  $ cd src/
  $ python3 main.py
  ```

## Uso 
Explique como usar seu projeto caso haja algum passo a passo após o comando de execução.

## Outros 
Quaisquer outras informações sobre seu projeto podem ser descritas abaixo.
