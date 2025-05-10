Bilingual Pocket

Aplicación Django minimalista para aprender una nueva palabra en inglés cada día, obteniendo una palabra aleatoria y traduciéndola al español con un formato tipo diccionario.

🎯 Características

Palabra aleatoria: obtiene una palabra en inglés de la Random Word API.

Traducción de alta calidad: utiliza la Google Cloud Translation API para traducir al español.

Diseño responsivo: layout limpio con Tailwind CSS.

Fácil configuración: sin dependencias complejas.

🚀 Inicio rápido

Clona el repositorio

git clone https://github.com/tu-usuario/django_wDay.git
cd django_wDay/src

Coloca tu clave de servicio

Descarga tu archivo JSON de cuenta de servicio de Google Cloud (p. ej. planar-catbird-...json).

Sitúalo en el directorio src/ (junto a manage.py).

Instala dependencias

python -m venv venv
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt

Configura las credenciales

Opción A (recomendada): define la variable de entorno:

export GOOGLE_APPLICATION_CREDENTIALS="$PWD/planar-catbird-...json"

Opción B: la app carga automáticamente el JSON desde src/ por defecto.

Aplica migraciones (opcional)

python manage.py migrate

Ejecuta el servidor

python manage.py runserver

Abre en el navegador
Visita http://127.0.0.1:8000/ y haz clic en "Nueva palabra" para ver la traducción.

⚙️ Configuración interna

API de palabra aleatoria: https://random-word-api.herokuapp.com/word?number=1

Cliente de traducción: configurado en app_wDay/views.py usando google-cloud-translate.

Template principal: app_wDay/templates/base.html, con estilos Tailwind CSS.

🔐 Seguridad

No subir nunca tu archivo de credenciales JSON al repositorio. Está excluido por .gitignore.
