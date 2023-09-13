# 3dom-video
### 3dom project - Hebergement et lecture de videos

---

Développé avec `PyCharm 2023.2.1 (Community Edition)`

Python 3.11.5

---

## Todo
- [x] get videos sur `Rumble`  
- [ ] get videos sur `Odysee` --> IMPOSSIBLE
- [x] ajout de createurs `Youtube` 
- [x] ajout de createurs `Rumble` 

- [ ] Connexion allauth `Google`  
- [x] Page de visualisation de video  
- [ ] creer une adresse `email` 3dom
- [x] paginator
- [ ] commentaire alternatif a la main .. au niveau de createur de contenu 
- [ ] 404 
- [x] controle `is_superuser`
- [ ] 
- [ ] Mettre en `prod`  


## Versions ulterieures
- [ ] Les differents modes d'affichage 
- [ ] trouver un `studio video`


## A sous traiter
- [ ] `Fiverr` - Correctifs template  
- [ ] opacite sur l'image d'accueil
- [ ] page de dons .. `paymeacoffee`, `paypal`,  
- [ ] revoir le footer



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



