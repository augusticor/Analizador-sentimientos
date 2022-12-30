# Analizador-sentimientos
### NLP (Natural languaje processing)

Este es un analizador de sentimientos basado en procesamiento de lenguaje natural (N.L.P.).


### Introducción
Requiere un texto a evaluar, como por ejemplo un discurso, como el [discurso](https://www.pediatriasocial.es/HtmlRes/Files/DiscursoMalala.pdf) de [Malala Yousafzai](https://es.wikipedia.org/wiki/Malala_Yousafzai) en la recepción del Premio Nobel de la Paz del 2014.

Usa distintos metodos de N.L.P. como ***"stop words"*** o ***"tokenized_words"***.

El texto a evaluar puede estar escrito en inglés o en español, ya que mediante la librería "googletrans" se puede traducir a inglés para mejor procesamiento.


### Instalación
Aunque en el archivo [Requerimientos](requirements.txt) se encuentra el nombre y la versión de las distintas dependencias, acá se mencionan las mas importantes, para el proceso de instalación y actualización usar [PIP](https://pip.pypa.io/en/stable/quickstart/)

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
```
pip install -U Flask 
```

- NLTK
```
pip install nltk
```
Y de NLTK especificamente ( estas se descargan usando nltk.download('nombre dependencia')), o si se va a desplegar la app se escriben como esta en el archivo [nltk.txt](nltk.txt)) :
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

### Integrantes
Este proyecto fue desarrollado en la asignatura **Inteligencia Computacional**, en la carrera universitaria Ingeniería de Sistemas y Computación de la **U.P.T.C.**, con la colaboración del siguiente equipo de trabajo:

- [Elber Leon](https://github.com/Leon30)
- [Angie Huertas](https://github.com/Angie0926)
- Dayan Ramirez
- Jonatán Pinto
