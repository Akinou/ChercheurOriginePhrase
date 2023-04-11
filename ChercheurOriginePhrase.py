import requests
import json

def search_phrase_in_books(phrase):
    api_key = "VOTRE_CLE_API_GOOGLE_BOOKS"  # Remplacez VOTRE_CLE_API_GOOGLE_BOOKS par votre clé API
    base_url = "https://www.googleapis.com/books/v1/volumes"
    
    # Paramètres pour la requête
    params = {
        "q": f"intitle:{phrase}",
        "key": api_key,
        "maxResults": 10  # Nombre maximum de résultats à afficher
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        items = data.get('items')
        
        if items:
            print(f"Résultats pour la phrase '{phrase}':")
            for item in items:
                title = item['volumeInfo'].get('title')
                authors = item['volumeInfo'].get('authors', [])
                author_str = ', '.join(authors)
                print(f"Titre: {title}\nAuteurs: {author_str}\n")
        else:
            print(f"Aucun résultat trouvé pour la phrase '{phrase}'.")
    else:
        print("Erreur dans la requête. Veuillez réessayer plus tard.")

if __name__ == "__main__":
    phrase = "La vie est un songe"  # Remplacez cette phrase par celle que vous voulez rechercher
    search_phrase_in_books(phrase)
