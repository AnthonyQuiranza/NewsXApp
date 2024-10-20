import tweepy
import requests
import os

# Cargar las credenciales desde el archivo .env
from dotenv import load_dotenv
load_dotenv()

# Credenciales de la API de Twitter (X.com)
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

# Credenciales para Mediastack
MEDIASTACK_API_KEY = os.getenv('MEDIASTACK_API_KEY')

# Configuración del cliente Tweepy para la API de X.com
twitter_client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

# Función para obtener noticias de tecnología de Mediastack
def obtener_noticias_tecnologia():
    url = f"http://api.mediastack.com/v1/news?access_key={MEDIASTACK_API_KEY}&categories=technology&languages=es"
    response = requests.get(url)
    
    if response.status_code == 200:
        noticias = response.json()
        return noticias['data']  # Retorna la lista de noticias
    else:
        print(f"Error al obtener noticias: {response.status_code}")
        return []

# Función para generar un resumen de la noticia
def generar_resumen(noticia):
    resumen = noticia['description']
    if resumen:
        if len(resumen) > 200:
            resumen = resumen[:197] + "..."  # Limitar el resumen a 200 caracteres
    else:
        resumen = noticia['title']  # Si no hay descripción, usar el título
    return resumen

# Función para publicar un tweet en X.com
def post_tweet(mensaje):
    try:
        # Intentar publicar el tweet
        response = twitter_client.create_tweet(text=mensaje)
        tweet_id = response.data['id']
        print(f"Tweet publicado correctamente con ID: {tweet_id}")
        return tweet_id
    except tweepy.TweepyException as e:
        error_response = e.response.json()
        # Verificar si es un error de contenido duplicado
        if error_response.get('status') == 403 and "duplicate content" in error_response.get('detail', '').lower():
            print(f"Tweet duplicado: {error_response.get('detail')}")
            return "duplicate"
        else:
            print(f"Error al publicar el tweet: {error_response.get('detail')}")
            return "error"

# Función principal para publicar noticias en Twitter
def publicar_noticias_en_twitter():
    noticias = obtener_noticias_tecnologia()
    
    if noticias:
        for noticia in noticias:  # Iterar sobre todas las noticias
            titulo = noticia['title']
            url = noticia['url']
            resumen = generar_resumen(noticia)
            mensaje = f"{resumen} {url}"  # Crear el mensaje del tweet

            # Asegurarse de que el tweet no supere los 280 caracteres
            if len(mensaje) > 280:
                mensaje = mensaje[:277] + "..."

            resultado = post_tweet(mensaje)

            # Si el tweet es duplicado, continuar con la siguiente noticia
            if resultado == "duplicate":
                print("Intentando con la siguiente noticia...")
                continue
            elif resultado == "error":
                print("Se produjo un error al publicar.")
                break
            else:
                print("Tweet publicado correctamente.")
                break  # Detenerse después de publicar correctamente una noticia
    else:
        print("No se encontraron noticias para publicar.")

# Ejecutar la publicación de noticias en Twitter
if __name__ == "__main__":
    publicar_noticias_en_twitter()