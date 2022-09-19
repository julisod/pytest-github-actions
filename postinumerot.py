import urllib.request
import json

def get_postal_data() -> dict:
    json_url = "https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json"

    with urllib.request.urlopen(json_url) as response:
        data = response.read()

    return json.loads(data)

def get_postal_codes(query: str):

    query = query.upper().replace(" ", "")

    postinumerot = get_postal_data()
    for code, district in postinumerot.items():
        postinumerot[code] = district.replace(" ", "")

    if query in postinumerot.values():
        postal_codes = []
        for numero, paikka in postinumerot.items():
            if paikka == query:
                postal_codes.append(numero)
        postal_codes.sort()
        return postal_codes
    else:
        return None

if __name__ == "__main__":
    query = input("Kirjoita postitoimipaikka: ")
    postal_codes = get_postal_codes(query)

    if postal_codes:
        print(f"Postinumerot: {', '.join(postal_codes)}")
    else:
        print("Tuntematon postitoimipaikka")