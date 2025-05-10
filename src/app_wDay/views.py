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
