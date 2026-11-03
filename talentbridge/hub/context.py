from .i18n import LANGS, lang, texts


def i18n(request):
    code = lang(request)
    return {
        "t": texts(request), "lang": code, "dir": LANGS[code][1],
        "LANGS": [(c, n) for c, (n, _) in LANGS.items()],
        "path": request.get_full_path(),
    }
