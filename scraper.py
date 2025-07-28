import requests
from bs4 import BeautifulSoup

def run(params):
    commune = params.get("commune", "")
    api_key = "a9cf2e30657a19fd8822c8142a216807ee45e20a"  # ta clé ZenRows
    url = "https://www.aef.cci.fr/rechercheMulticritere"

    zenrows_url = "https://api.zenrows.com/v1/"
    params_zen = {
        "url": url,
        "apikey": api_key,
        "js_render": "true",
        "antibot": "true"
    }

    try:
        r = requests.get(zenrows_url, params=params_zen, timeout=30)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        rows = soup.select(".listeEntreprise tr")
        data = []
        for tr in rows[1:]:
            tds = tr.find_all("td")
            if len(tds) >= 3:
                data.append({
                    "nom": tds[0].text.strip(),
                    "ville": tds[1].text.strip(),
                    "cp": tds[2].text.strip()
                })
        return data
    except Exception:
        # fallback fictif
        return [{"nom": "Entreprise Test", "ville": commune, "cp": "99999"}]
