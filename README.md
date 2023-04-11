Ce script permet de rechercher l'origine d'une phrase spécifique dans des livres, ouvrages, romans, etc. Il utilise l'API Google Books pour effectuer cette recherche.

Comment ajouter la clé API :
Pour utiliser ce script, vous devez d'abord obtenir une clé API Google Books en suivant les instructions sur cette page : https://developers.google.com/books/docs/v1/getting_started

Une fois que vous avez votre clé API, suivez ces étapes pour l'ajouter au script :

Ouvrez le fichier ChercheurOriginePhrase.py dans un éditeur de texte ou un environnement de développement intégré (IDE) tel que Visual Studio Code ou PyCharm.
Localisez la ligne suivante dans le script :


api_key = "VOTRE_CLE_API_GOOGLE_BOOKS"  # Remplacez VOTRE_CLE_API_GOOGLE_BOOKS par votre clé API
Remplacez VOTRE_CLE_API_GOOGLE_BOOKS par la clé API que vous avez obtenue précédemment. Par exemple, si votre clé API est abc123, la ligne devrait ressembler à :

api_key = "abc123"

Enregistrez les modifications apportées au fichier ChercheurOriginePhrase.py.
Maintenant, vous pouvez exécuter le script avec votre clé API. Le script recherchera la phrase spécifiée dans la variable phrase et affichera les titres et les auteurs des ouvrages correspondants. Pour rechercher une phrase différente, modifiez simplement la valeur de la variable phrase.
