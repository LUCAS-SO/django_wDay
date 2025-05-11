# Bilingual Pocket

Aplicación Django minimalista para aprender una nueva palabra en inglés cada día, obteniendo una palabra aleatoria y traduciéndola al español con un formato tipo diccionario.

## 🎯 Características

* **Palabra aleatoria**: obtiene una palabra en inglés de la [Random Word API](https://random-word-api.herokuapp.com/).
* **Traducción de alta calidad**: utiliza la Google Cloud Translation API para traducir al español.
* **Diseño responsivo**: layout limpio con Tailwind CSS.
* **Fácil configuración**: sin dependencias complejas.

## 🚀 Inicio rápido

1. **Clona el repositorio**

   ```bash
   git clone https://github.com/tu-usuario/django_wDay.git
   cd django_wDay/src
   ```

2. **Coloca tu clave de servicio**

   * Descarga tu archivo JSON de cuenta de servicio de Google Cloud (p. ej. `planar-catbird-...json`).
   * Sitúalo en el directorio `src/` (junto a `manage.py`).

3. **Instala dependencias**

   ```bash
   python -m venv venv
   # Windows PowerShell:
   .\venv\Scripts\Activate.ps1
   # macOS/Linux:
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Configura las credenciales**

   * **Opción A (recomendada)**: define la variable de entorno:

     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="$PWD/planar-catbird-...json"
     ```

   * **Opción B**: la app carga automáticamente el JSON desde `src/` por defecto.

5. **Aplica migraciones (opcional)**

   ```bash
   python manage.py migrate
   ```

6. **Ejecuta el servidor**

   ```bash
   python manage.py runserver
   ```

7. **Abre en el navegador**
   Visita `http://127.0.0.1:8000/` y haz clic en **"Nueva palabra"** para ver la traducción.

## ⚙️ Configuración interna

* **API de palabra aleatoria**: `https://random-word-api.herokuapp.com/word?number=1`
* **Cliente de traducción**: configurado en `app_wDay/views.py` usando `google-cloud-translate`.
* **Template principal**: `app_wDay/templates/base.html`, con estilos Tailwind CSS.
