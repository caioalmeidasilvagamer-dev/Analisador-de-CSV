import pandas as pd

def parseCsv(caminho: str) -> list:
    df = pd.read_csv(caminho)
    return df.to_dict(orient='records')


def normalizarLink(link: str) -> str:
    link_normalizado = link.removeprefix("http://").removeprefix("https://").removeprefix("www.").split("/")[0].lower()
    return link_normalizado

def filtroLink(link: str) -> str:
    link = normalizarLink(link)
    if not link:
        return "Lead-sem-link"
    elif "instagram" in link or "linkedin" in link or "wa.me" in link or "facebook" in link or "twitter" in link or "tiktok" in link:
        return "Lead-certo-redes-sociais"
    elif "wixsite" in link or "wix.com" in link or "wordpress" in link or "weebly" in link or "shopify" in link or "tumblr" in link or "canva" in link or "sites.google" in link or "localo.site" in link or "webnode" in link or "webflow" in link or "jimdo" in link or "strikingly" in link or "site123" in link:
        return "Lead-certo-site-gratis"
    elif "linktr.ee" in link or "linkr.bio" in link or "bit.ly" in link or "tinyurl" in link or "rebrandly" in link or "is.gd" in link or "cutt.ly" in link:
        return "Lead-certo-link-de-redirecionamento"
    elif "youtube" in link or "vimeo" in link or "dailymotion" in link or "twitch" in link or "spotify" in link or "soundcloud" in link:
        return "Lead-certo-plataforma-de-conteudo"
    elif link.endswith(".com") or link.endswith(".org") or link.endswith(".net") or link.endswith(".br") or link.endswith(".io") or link.endswith(".co"):
        return "Site-próprio"
    else:
        return "Lead-certo-outros"
    
def analisarLeads(leads: list) -> dict:
    categorias = {
        "Lead-certo-redes-sociais": [],
        "Lead-sem-link": [],    
        "Lead-certo-site-gratis": [],
        "Lead-certo-link-de-redirecionamento": [],
        "Lead-certo-plataforma-de-conteudo": [],
        "Site-próprio": [],
        "Lead-certo-outros": []
    }
    
    for lead in leads:
        link = lead.get("website", "")
        if pd.isna(link):  # ← aqui, depois de pegar o link
            categorias["Lead-sem-link"].append(lead)
        else:
            categoria = filtroLink(link)
            categorias[categoria].append(lead)

    return categorias