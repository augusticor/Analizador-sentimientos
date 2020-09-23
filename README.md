# Analizador-sentimientos
### NLP (Natural languaje processing)

Este es un analizador de sentimientos basado en procesamiento de lenguaje natural (N.L.P.).


### Introducción
Requiere un texto a evaluar, como por ejemplo un discurso, como el [discurso](https://www.pediatriasocial.es/HtmlRes/Files/DiscursoMalala.pdf) de [Malala Yousafzai](https://es.wikipedia.org/wiki/Malala_Yousafzai) en la recepción del Premio Nobel de la Paz del 2014.

Usa distintos metodos de N.L.P. como ***"stop words"*** o ***"tokenized_words"***.

El texto a evaluar puede estar escrito en inglés o en español, ya que mediante la libreria "googletrans" se puede traducir a inglés para mejor procesamiento.


### Instalando
Aunque en el archivo [Requerimientos](requirements.txt) se encuentra el nombre y la versión de las distintas dependencias, aca se mencionan las mas importantes, para el proceso de instalación y actualizacion usar [PIP](https://pip.pypa.io/en/stable/quickstart/)

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
```
pip install -U Flask 
```

- NLTK
```
pip install nltk
```
Y de NLTK especificamente ( estas se descargan usando nltk.download('nombre dependencia', o si se va a desplegar la app se escriben como esta en el archivo [nltk.txt](nltk.txt)) :
```
punkt
wordnet
stopwords
```

- Googletrans
```
pip install googletrans
```

- Matplotlib
```
pip install matplotlib==3.3.2
```

### Deployment
La aplicacion fue desplegada usando Heroku.
#### Analizador de sentimientos : **_[Sentimenti](https://sentimienti.herokuapp.com/)_**
Para el despliegue correcto de la app se debe crear el archivo [Procfile](Procfile) con el siguiente contenido :
"web: gunicorn app:app", donde :
```
- web es el tipo de app
- gunicorn la libreria para el despliegue
- app el nombre del archivo principal o root
- app el nombre de la aplicacion Flask "app = Flask(__name__)"
```
