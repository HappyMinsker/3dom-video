# 3dom-video
### 3dom project - Hebergement et lecture de videos

---

Développé avec `PyCharm 2023.2.1 (Community Edition)`

Python 3.11.5

---

## Todo
- [x] get videos sur Rumble  
- [ ] get videos sur Odysee --> IMPOSSIBLE
- [x] ajout de createurs Youtube 
- [x] ajout de createurs Rumble 


- [ ] Les differents modes d'affichage 
- [ ] Connexion allauth `Google`  
- [ ] Mettre en prod  
- [ ] Fiverr - Correctifs template  
- [ ] Page de visualisation de video  
- [ ] page de sons .. paymeacoffee, paypal,  
- [ ] creer une adresse email 3dom
- [ ] revoir le footer
- [ ] trouver un studio video
- [ ] paginator
- [ ] opacite sur l'image d'accueil
- [ ] 

Search
https://odysee.com/$/search?q=vivre%20sainement
Createur
https://odysee.com/@Vivresainement:f
Video
https://odysee.com/@Vivresainement:f/suicides:2


## Liens Youtube
- [x] https://www.youtube.com/watch?v=rVBBZKPjzgY
- [x]   
- [x] https://www.youtube.com/watch?v=kRp1Z2JhnzY  
- [x] https://www.youtube.com/watch?v=E_3sMko5GLo  
- [x] https://www.youtube.com/watch?v=ySOKQ9DFeFQ  
- [x]   
- [x]   
- [x]   
- [x] https://www.youtube.com/watch?v=G8P3qBkhKC8  


## Elements HTML
- [x] Couleur bleue de `WATCH NOW` #24BAEF    
- [x]   
- [x] pip install youtube3  
- [x]   

## Ratio Images

|         | Image 1 | Image 2 | Image 3 |
|:--------|--------:|--------:|--------:|
| Largeur |    1920 |     222 |     225 |
| Hauteur |     676 |     126 |     127 |
| Ratio   |   2,840 |   1,762 |   1,772 |


## Data Google
- [x] Cle API : AIzaSyCO487FSltOzZTdqmoY3sc1KcPAMqZXGV8
          
      Use this key in your application by passing it with the key=API_KEY parameter.

- [x] Project ID: dom-youtube-398307
- [x] Project name: 3dom Youtube
- [x] Name of your OAuth 2.0 client : 3dom Youtube

- [x] Client ID: 948379921087-pt95t7ppnaup6qmv3hdi35sjnf4skvr1.apps.googleusercontent.com
- [x] Client secret: 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

C:\Users\OMEN\PycharmProjects\3dom-video\venv\Scripts\python.exe C:\Users\OMEN\PycharmProjects\3dom-video\app_test.
py -2XW85xVrSk


---

## Technique
- [ ] Video5 8'50 : ModelForm permet  .. `profile = Profile.Objects.create(**form.cleaned_data_)`.  💖💖
- [ ] Video8 14'29 : Lorem Ipsum `{% lorem 1 %}`
- [ ] Video9 2'05 : except Movie.DoesNotExist

        <main class='bg-primary_black h-full w-full '>
            {{movie|json_script:'movie_data'}}
            <video  controls class="w-full h-screen player"></video>
            
        </main>
        <script>
            const videoEl = document.querySelector('video')
            const movie_data = JSON.parse(document.getElementById('movie_data').textContent);
            const url = new URL(location.href)
            const video_param = parseInt(url.searchParams.get('epi'))?parseInt(url.searchParams.get('epi')):0
            videoEl.setAttribute('src', `http://localhost:8000/media/${movie_data[video_param].file}`)
        </script>

                           
## ToDO
- [ ] Icone carree "3".



## Cleaning
- [ ] Supprimmer les fichiers `ORG`.
- [ ] Supprimmer les fichiers `LMC`.
- [ ] 



