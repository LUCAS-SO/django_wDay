import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def palabra_del_dia(request):
    palabra = None
    traduccion = None

    if request.method == "POST":
        # 1) Obtener palabra aleatoria
        resp_word = requests.get(
            "https://random-word-api.herokuapp.com/word",
            params={"number": 1}
        )
        palabra = resp_word.json()[0]  # Ej: "house"

        # 2) Traducir con MyMemory
        resp_trans = requests.get(
            "https://api.mymemory.translated.net/get",
            params={"q": palabra, "langpair": "en|es"}
        )
        data = resp_trans.json().get("responseData", {})
        traduccion = data.get("translatedText", "")

    return render(request, "base.html", {
        "palabra": palabra,
        "traduccion": traduccion
    })
