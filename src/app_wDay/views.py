import os
import requests
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account

# Ruta al JSON de Google credenciales
KEY_PATH = os.path.join(settings.BASE_DIR, 'planar-catbird-459405-n7-74ac6ad57208.json')
credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
translate_client = translate.Client(credentials=credentials)

# Clave de Wordnik API
WORDNIK_API_KEY = os.getenv('WORDNIK_API_KEY')

@csrf_exempt
def palabra_del_dia(request):
    palabra = None
    traduccion = None
    pronunciacion = None

    if request.method == "POST":
        # 1) Obtener palabra aleatoria
        palabra = requests.get(
            "https://random-word-api.herokuapp.com/word",
            params={"number": 1}, timeout=5
        ).json()[0]

        # 2) Traducir con Google Cloud
        result = translate_client.translate(
            palabra, source_language='en', target_language='es'
        )
        traduccion = result.get('translatedText', '')

        # 3) Traer IPA de la Free Dictionary API
        dict_resp = requests.get(
            f"https://api.dictionaryapi.dev/api/v2/entries/en/{palabra}",
            timeout=5
        )
        if dict_resp.status_code == 200:
            entries = dict_resp.json()
            # Busca el primer phonetic.text válido
            phonetic = None
            for p in entries[0].get('phonetics', []):
                text = p.get('text')
                if text:
                    phonetic = text
                    break
            if phonetic:
                # Limpia las barras /…/ y envuelve en corchetes
                pronunciacion = f"[{phonetic.strip('/')}]"

    return render(request, "base.html", {
        "palabra": palabra,
        "traduccion": traduccion,
        "pronunciacion": pronunciacion,
    })


def ejemplos(request, palabra):
    textos = []

    # 1) Intento con Dictionary API
    resp = requests.get(
        f"https://api.dictionaryapi.dev/api/v2/entries/en/{palabra}",
        timeout=5
    )
    if resp.status_code == 200:
        data = resp.json()[0]
        for meaning in data.get('meanings', []):
            for definition in meaning.get('definitions', []):
                ex = definition.get('example')
                if ex:
                    textos.append(ex)

    # 2) Si no hay ejemplos, usamos Wordnik
    if not textos and WORDNIK_API_KEY:
        wn_url = f"https://api.wordnik.com/v4/word.json/{palabra}/examples"
        params = {
            'limit': 5,
            'includeDuplicates': False,
            'useCanonical': False,
            'api_key': WORDNIK_API_KEY,
        }
        wn_resp = requests.get(wn_url, params=params, timeout=5)
        if wn_resp.status_code == 200:
            wn_data = wn_resp.json()
            for ex in wn_data.get('examples', []):
                text = ex.get('text')
                if text:
                    textos.append(text)

    # 3) Traducir en lote los ejemplos obtenidos
    ejemplos = []
    if textos:
        traducciones = translate_client.translate(
            textos,
            source_language='en',
            target_language='es'
        )
        for original, salida in zip(textos, traducciones):
            ejemplos.append({
                'text': original,
                'translation': salida['translatedText']
            })

    return render(request, "ejemplos.html", {
        "palabra": palabra,
        "ejemplos": ejemplos,
    })