# Aprendendo Starlette

( projeto em andamento )
<hr>
<br>


## Início

Para começar a entender os conceitos e usos do Starlette, peguei como base a live do youtube: <b> Live de Python #148 - Criando aplicações web assíncronas com Starlette com Marcus Pereira</b>

Essa live pode ser acessado por aqui: https://www.youtube.com/watch?v=1yuv5SFR_zg&list=WL&index=24

<br>

<hr>

## Ambiente Virtual:
<br>

Criar ambiente virtual:

```
python -m venv venv 
```

Entrar no ambiente virtual:

```
source venv/bin/activate
```

<br>
<hr>
<br>


## Para instalar as dependências

- Caso vc esteja clonando esse repositório:
```
pip install -r requirements.txt
```

<br>

- Caso queira seguir as instalações passo-a-passo do vídeo:

Instalando Starlette e Uvicorn:

```
pip install starlette
pip install uvicorn
```

ou apenas 
```
pip install starlette uvicorn
```
<br>


Rodar o arquivo python:
```
python server.py
```
<br>


Instalação para os testes:
```
pip install pytest
pip install requests
```
<br>


Para rodar os testes:
```
pytest -vvv
```

<br>
<br>
<hr>

## Rotas criadas até o momento:

GET - http://localhost:5000/ 
- Status - 200

```
{
    "msg": "welcome to home page"
}
```

<br>

GET - http://localhost:5000/echo
- Status - 200

```
Echo page
```

<br>
continua ...

