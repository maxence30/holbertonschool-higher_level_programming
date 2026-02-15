

## 1. HTTP vs HTTPS

Alors HTTP c’est le protocole qui permet à ton navigateur de parler avec un serveur pour afficher une page web ou récupérer des données. Le problème avec HTTP, c’est que toutes les infos passent **en clair**, donc si quelqu’un intercepte, il peut voir ce que tu envoies.

HTTPS, c’est la version sécurisée de HTTP. Il ajoute un chiffrement (SSL/TLS) pour que personne ne puisse lire les données. C’est utilisé sur les sites où il y a des infos sensibles, comme les banques ou les emails. Le "S" à la fin veut dire **Secure**, donc sécurisé.

En résumé :
- HTTP : pas sécurisé, port 80, pas de certificat  
- HTTPS : sécurisé, port 443, certificat SSL/TLS, données cryptées  

---

## 2. La structure d’une requête et d’une réponse

Quand tu envoies une requête HTTP (comme quand tu ouvres une page), ça ressemble à ça :

GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html


Ici on voit :
- GET = la méthode (on veut récupérer quelque chose)  
- /index.html = le fichier demandé  
- Host = le site  
- User-Agent = info sur ton navigateur  

La réponse du serveur ressemble à ça :

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1024


Ça veut dire que la requête a réussi (200 OK) et qu’il y a du contenu HTML dans la réponse.

---

## 3. Méthodes HTTP principales

Les plus utilisées sont :  
- **GET** : récupérer des données, par exemple charger une page web  
- **POST** : envoyer des données, comme remplir un formulaire ou créer un compte  
- **PUT** : modifier quelque chose qui existe déjà, par exemple mettre à jour un profil  
- **DELETE** : supprimer une ressource, comme supprimer un compte  

---

## 4. Codes de statut HTTP courants

Quelques codes qu’on voit souvent :  
- **200** : OK, tout est normal  
- **201** : Created, une ressource a été créée  
- **301** : Moved Permanently, redirection vers un autre site  
- **404** : Not Found, la page demandée n’existe pas  
- **500** : Internal Server Error, il y a un problème sur le serveur  

Les codes sont classés par type :  
- 1xx → infos  
- 2xx → succès  
- 3xx → redirection  
- 4xx → erreur côté client  
- 5xx → erreur côté serveur
