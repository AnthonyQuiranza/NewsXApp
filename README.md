 # 📰 Mediastack News to X.com Bot

 ![Python Version](https://img.shields.io/badge/python-3.8%2B-blue) ![License](https://img.shields.io/github/license/AnthonyQuiranza/NewsXApp) ![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)

 > **Automatización para publicar noticias de tecnología en X.com (anteriormente Twitter) utilizando Mediastack y Tweepy.**

 Este proyecto permite obtener noticias de tecnología en español utilizando la API de **Mediastack** y publicarlas automáticamente en tu cuenta de **X.com** usando **Tweepy** para interactuar con la API de X.

 ## 🚀 Características

 - 📡 **Integración con Mediastack**: Obtiene las últimas noticias de tecnología en español.
 - 🐍 **Automatización con Python**: Automatiza la publicación en X.com con la API de Twitter.
 - 🛡️ **Manejo de errores**: El bot detecta errores de contenido duplicado y continúa con las siguientes noticias si es necesario.

 ## 🛠️ Tecnologías utilizadas

 - **Python 3.8+**
 - [**Tweepy**](https://www.tweepy.org/) - Cliente para la API de Twitter.
 - [**Mediastack**](https://mediastack.com/) - API para obtener noticias globales.
 - [**python-dotenv**](https://github.com/theskumar/python-dotenv) - Manejo de variables de entorno.

 ## ⚙️ Instalación

 Sigue los siguientes pasos para instalar y configurar el proyecto en tu máquina local.

 1. **Clona este repositorio:**

 ```bash
 git clone https://github.com/AnthonyQuiranza/NewsXApp.git
 cd NewsXApp
 ```

 2. **Crea un entorno virtual:**

 ```bash
 python -m venv venv
 source venv/bin/activate   # En Windows usa `venv\Scripts\activate`
 ```

 3. **Instala las dependencias:**

 ```bash
 pip install -r requirements.txt
 ```

 4. **Configura el archivo `.env`:**

 Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

 ```bash
 BEARER_TOKEN=your_twitter_bearer_token
 CONSUMER_KEY=your_twitter_consumer_key
 CONSUMER_SECRET=your_twitter_consumer_secret
 ACCESS_TOKEN=your_twitter_access_token
 ACCESS_SECRET=your_twitter_access_secret
 MEDIASTACK_API_KEY=your_mediastack_api_key
 ```

 > ⚠️ **Nota:** No olvides añadir el archivo `.env` a tu archivo `.gitignore` para no compartir tus credenciales accidentalmente.

 ## 🚀 Ejecución del proyecto

 Una vez configurado, puedes ejecutar el bot con el siguiente comando:

 ```bash
 python __main__.py
 ```

 El script obtendrá las últimas noticias de tecnología y las publicará en tu cuenta de X.com.

 ## 📄 Licencia

 Este proyecto está bajo la licencia **MIT**. Puedes ver más detalles en el archivo [`LICENSE`](LICENSE).

 ---

 💡 **Consejo:** No dudes en modificar este proyecto para ajustarlo a tus necesidades. Puedes cambiar las fuentes de noticias, la frecuencia de publicación o incluso agregar nuevas funcionalidades.

 ## 👨‍💻 Contribuciones

 ¡Las contribuciones son bienvenidas! Si encuentras algún error o quieres agregar nuevas funcionalidades, abre un **issue** o envía un **pull request**.

 ---

 ### Contacto

 Puedes encontrarme en:

 - [GitHub](https://github.com/anthonyquiranza)
 - [X.com (Twitter)](https://twitter.com/soyanthonyq)

 ---

 Hecho con ❤️ por [**anthonyquiranza**](https://github.com/anthonyquiranza)