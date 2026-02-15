# task_02_requests.py

import requests
import csv

# Fonction pour récupérer et afficher les titres des posts
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()  # convertir la réponse en JSON
        
        # Afficher tous les titres
        for post in posts:
            print(post['title'])
    else:
        print("Erreur lors de la récupération des posts")

# Fonction pour récupérer et sauvegarder les posts dans un fichier CSV
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # Créer une liste de dictionnaires avec id, title et body
        data_to_save = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        # Écrire dans posts.csv
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for row in data_to_save:
                writer.writerow(row)
        
        print("Les posts ont été sauvegardés dans posts.csv")
    else:
        print("Erreur lors de la récupération des posts")
