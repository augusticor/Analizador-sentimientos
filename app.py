# Importacion de framework Flask
from flask import Flask, render_template, request, Response

# NLP Importaciones necesarias
import re
import matplotlib.pyplot as plt
import nltk
from googletrans import Translator
from string import punctuation, digits
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from os.path import join, dirname, realpath

nltk.download('vader_lexicon')

app = Flask(__name__)

# Variables globales con rutas de archivos estaticos y textos que se envian al frontend
sentiment = 'Escribe algo :D'
graph = 'graph.png'
input_user = ''
response = Response()
emotions_super_file = join(dirname(realpath(__file__)), 'static/files/emotions.txt')
default_speech = join(dirname(realpath(__file__)), 'static/files/text.txt')
static_deploy_graph = join(dirname(realpath(__file__)), 'static/graph.png')


# Le decimos al navegador que no guarde cache
# Principalmente para que cada vez que se actualize la pagina se actualize el grafico tambien
@app.after_request
def cache_bug(r):
	r.headers["Cache-Control"] = "no-store"
	return r


# La ruta home cuando entra el usuario
@app.route('/')
def hello_world():
	return render_template('index.html', sentiment=sentiment, graph=graph)


# EL metodo POST que recibe el mensaje del usuario al cual se le van a analizar los sentimientos
@app.route("/analyze", methods=['POST'])
def analyze():
	cache_bug(response)
	input_text = request.form['text_box']
	if input_text == '':
		input_text = open(default_speech, encoding='utf-8').read()
	sentiment_found = work(input_text)
	return render_template('index.html', input_user=input_text, sentiment=sentiment_found, graph=graph)


def work(input_texto):
	# Entrada del usuario
	translated_text = translate_to_spanish(input_texto)

	# Entrada limpia del usuario, sin caracteres especiales
	cleaned_text = try_input(translated_text)

	# Dividir el texto en palabras
	tokenized_words = word_tokenize(cleaned_text, 'english')

	# Traer los stops words de nltk
	stop_words = stopwords.words('english')

	# Eliminar los stop words de las palabras separadas (tokenized_words)
	final_words = []
	for word in tokenized_words:
		if word not in stop_words:
			final_words.append(word)

	# Expresion regular para tratar el archivo de emociones y separarlo en clave valor
	# Palabra comun : emocion que expresa
	reg_express = re.compile('[^(:|\w)]')

	# Mirar que emociones se presentan en el texto resultante luego de los stop words
	emotions_list = []
	with open(emotions_super_file, 'r') as emotions_file:
		for line in emotions_file:
			clear_line = reg_express.sub('', line).strip()
			word, emotion = clear_line.split(':')

			if word in final_words:
				for times in range(0, final_words.count(word)):
					emotions_list.append(emotion)

	# Contar la cantidad de veces que esta un sentimiento
	count = Counter(emotions_list)
	final = {k: v for k, v in sorted(count.items(), key=lambda item: item[1])}
	sentiment_found = list(final.keys())[-1]

	# Realizar la grafica de los sentimientos y guardarla en un archivo de imagen
	fig1, ax1 = plt.subplots()
	ax1.pie([float(v) for v in count.values()], labels=[k for k in count], autopct='%1.1f%%', startangle=90,
			wedgeprops={'alpha': 0.9})
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
	fig1.set_facecolor('#3782FF')
	plt.savefig(static_deploy_graph)

	return sentiment_found


# Traduce el texto del usuario al ingles
def translate_to_spanish(input_texto):
	translator = Translator()
	text = input_texto
	return translator.translate(text, dest='en').text


# Tratar el texto luego de traducirlo para eliminar caracteres especiales
def try_input(translated_text):
	# Convirtiendo a minuscula la entrada del usuario
	lower_case_text = translated_text.lower()
	# Eliminando caracteres especiales
	return lower_case_text.translate(str.maketrans('', '', punctuation))


# Metodo que se llama cada vez que el usuario da click en el boton limpiar
@app.route("/clear")
def clear_input():
	input_user = ''
	return render_template('index.html', input_user=input_user, sentiment=sentiment, graph=graph)


# Corre el programa
if __name__ == '__main__':
	app.run()