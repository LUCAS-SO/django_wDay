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
   git clone https://github.com/tu-usuario/bilingual-pocket.git
   cd bilingual-pocket/src
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
   Visita `http://127.0.0.1:8000/app_wDay/` y haz clic en **"Nueva palabra"** para ver la traducción.

## ⚙️ Configuración interna

* **API de palabra aleatoria**: `https://random-word-api.herokuapp.com/word?number=1`
* **Cliente de traducción**: configurado en `app_wDay/views.py` usando `google-cloud-translate`.
* **Template principal**: `app_wDay/templates/app_wDay/word.html`, con estilos Tailwind CSS.

## 🔐 Seguridad

* **No subir** nunca tu archivo de credenciales JSON al repositorio. Está excluido por `.gitignore`.
* Usa variables de entorno o `local_settings.py` para datos sensibles.

## 📝 Licencia

Este proyecto está bajo la **Licencia MIT**, una licencia de software libre y de código abierto que permite el uso, copia, modificación, fusión, publicación, distribución, sublicenciamiento y/o venta de copias del software.

En términos prácticos, la Licencia MIT otorga a cualquiera los siguientes derechos:

* **Uso libre**: puedes usar el software con cualquier propósito, incluyendo proyectos comerciales.
* **Modificación y distribución**: puedes modificar el código y distribuir tanto el original como las versiones modificadas.
* **Redistribución**: al redistribuir el software, debes incluir la misma licencia y el aviso de copyright.

La licencia se puede consultar en detalle en el archivo [LICENSE](LICENSE) o en línea en:

[https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT)
