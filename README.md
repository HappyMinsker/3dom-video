# 3dom-video
### 3dom project - Aggregation, hebergement et lecture de videos

---

Développé avec `PyCharm 2023.2.1 (Community Edition)`

Python 3.11.5

python manage.py runscript video3domapp/views2.py

---

## Todo
- [x] get videos sur `Rumble`  
- [ ] get videos sur `Odysee` --> IMPOSSIBLE
- [x] ajout de createurs `Youtube` 
- [x] ajout de createurs `Rumble` 
- [x] Page de visualisation de video  
- [x] paginator
- [x] controle `is_superuser`
- [x] personnaliser interface admin + recherche
- [x] Connexion allauth `Google`  
- [x] commentaire alternatif a la main .. au niveau de créateur de contenu 
- [x] Partials: Svg, .... 
- [ ] 404 
- [ ] enviro 
- [ ] logging / telegram  

                           
## Cleaning / MEP
- [ ] Supprimer les fichiers `ORG`.
- [ ] Supprimer les fichiers `LMC`.
- [ ] Mettre en `prod`  



## Versions ulterieures
- [ ] Les différents modes d'affichage 
- [ ] Trouver un `studio video`
- [ ] Afficher uniquement `is published` 
- [ ] Connexion allauth `github`  
- [ ] Connexion allauth `twitter`  
- [ ] Pub 350*277 : Creer votre propre canal ! Contactez nous.
- [ ] Créer une adresse `email` 3dom
- [ ] Recherche de film ou de tag 
- [ ] Icone carree "3" bords arrondis.


## A sous traiter
- [ ] `Fiverr` - Correctifs template  
- [ ] Opacité sur l'image d'accueil
- [ ] Page de dons ... `paymeacoffee`, `paypal`,  
- [ ] Revoir le footer


## Liens Youtube
- [x] https://www.youtube.com/watch?v=rVBBZKPjzgY
- [x] https://www.youtube.com/watch?v=l-_dRvHEUA8
- [x] https://www.youtube.com/watch?v=kRp1Z2JhnzY  
- [x] https://www.youtube.com/watch?v=E_3sMko5GLo  
- [x] https://www.youtube.com/watch?v=ySOKQ9DFeFQ  
- [x] https://www.youtube.com/watch?v=i5dZktGrZ9s
- [x] https://www.youtube.com/watch?v=ckXzBHb5caA
- [x] https://www.youtube.com/watch?v=G8P3qBkhKC8


## Elements HTML
- [x] Couleur bleue de `WATCH NOW` #24BAEF    
- [x] pip install youtube3  
- [x]   


## Ratio Images

|         | Image 1 | Image 2 | Image 3 |
|:--------|--------:|--------:|--------:|
| Largeur |    1920 |     222 |     225 |
| Hauteur |     676 |     126 |     127 |
| Ratio   |   2,840 |   1,762 |   1,772 |



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





