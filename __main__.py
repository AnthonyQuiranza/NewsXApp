import tweepy
import requests

# Credenciales para X (Twitter) API
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAALALwgEAAAAAcQAPiu1irGxWidwavOlzthiT30Y%3Ds2TyQqdyAD0QXBxm45Xt9jYml5WJ1U6mQZJkGMceSXvJugHYt1'
CONSUMER_KEY = 'ccJT2d7NohWjXC3xLA9Q4aTQF'
CONSUMER_SECRET = 'cZF7CnKyXWYbBKRaT9t1flNUTqZewDUuOAxMCSBGZY0qdPrXS9'
ACCESS_TOKEN = '2546963438-m71UY1El0IV5FW6FFbfUrDG54CcF7I0eu6Druwa'
ACCESS_SECRET = 'LM3eO3xyTKfNT0S9lLNYR86IbzDUKymYhF6kctHUwRkQ3'

# Credenciales para Mediastack
MEDIASTACK_API_KEY = '25557c19616062212625b9e9bb67083c'

# Configuración del cliente Tweepy para la API de X
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
        return noticias['data']  # Retorna las noticias
    else:
        print(f"Error al obtener noticias: {response.status_code}")
        return []

# Función para generar un resumen de la noticia
def generar_resumen(noticia):
    resumen = noticia['description']
    if resumen:
        if len(resumen) > 200:
            resumen = resumen[:197] + "..."  # Limita el resumen a 200 caracteres
    else:
        resumen = noticia['title']  # Si no hay descripción, usar el título como resumen
    return resumen

# Función para publicar un tweet en X.com
def post_tweet(mensaje):
    try:
        # Publicar el tweet
        response = twitter_client.create_tweet(text=mensaje)
        tweet_id = response.data['id']
        print(f"Tweet publicado correctamente con ID: {tweet_id}")
        return tweet_id
    except tweepy.TweepyException as e:
        print(f"Error al publicar el tweet: {e.response.text}")
        return None

# Publicar las noticias más recientes en Twitter con un resumen
def publicar_noticias_en_twitter():
    noticias = obtener_noticias_tecnologia()
    
    if noticias:
        for noticia in noticias[:5]:  # Publicar solo las primeras 5 noticias
            titulo = noticia['title']
            url = noticia['url']
            resumen = generar_resumen(noticia)
            mensaje = f"{resumen} {url}"  # Crea el mensaje para el tweet
            if len(mensaje) > 280:
                mensaje = mensaje[:277] + "..."  # Asegurarse que el tweet no supere los 280 caracteres
            post_tweet(mensaje)
    else:
        print("No se encontraron noticias para publicar")

# Ejecutar la publicación de noticias en X.com
if __name__ == "__main__":
    publicar_noticias_en_twitter()