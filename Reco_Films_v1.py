import pandas as pd
import random
import requests

import streamlit as st
from streamlit_card import card

from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

#rajouter les configurations de la page
st.set_page_config(page_title= "Yanakhasy",
                    page_icon = "https://cdn.discordapp.com/attachments/1243172985502961727/1243173051185762365/logo.webp?ex=665082a0&is=664f3120&hm=fdfbae8bfd6a4ab5941daeb0b85566425615d30cb110951a55b60af2b7097315&",
                    layout="wide")


#lire la donnée
df_film = pd.read_csv(r"C:\Users\sylva\OneDrive\Bureau\IT\Wild_Code_School\P2\Datasets Nettoyés\df_actu.csv", sep=",")
df_intervenants = pd.read_csv(r"C:\Users\sylva\OneDrive\Bureau\IT\Wild_Code_School\P2\Datasets Nettoyés\df_intervenant_f.csv", sep=",")



image_film = df_film["poster_path"].iloc[72]
image_acteur = df_intervenants["images"].iloc[1]
liste_films = df_film["title"]
titre_film = df_film["title"].iloc[72]
names = df_intervenants["name"]
nom_acteur = df_intervenants["name"].iloc[1]


#fonction permettant de retourner une image sous forme de card
def card_accueil(titre, image_url, tmdb, width = "1000px"):
    titre = bool(titre)

    return card(
                title=titre,
                text="",
                image=image_url,
                url=f"https://www.imdb.com/title/{tmdb}/",
                styles={
                    "card": {
                    "width": width,
                    "height": "400px",
                    "border-radius": "20px",
                    "box-shadow": "0 0 10px rgba(0,0,0,0.5)"
                    },
                    "text": {
                            "font-family": "serif",
                            "font-size": "0px"  
                            },
                    "title": {
                            "font-family": "Arial",  # Changer le type de police 
                            "font-size": "24px"      # Changer la taille de police 
                            }
                    }
                )

def card_custom(titre, image_url, tmdb, width = "1000px"):
     
     titre = bool(titre)

     return card(
                    title=liste_films_reco[i],
                    text="",
                    image=image_url,
                    url=f"https://www.imdb.com/title/{tmdb}/",
                    styles={
                        "card": {
                            "width": width,
                            "height": "400px",
                            "border-radius": "20px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)"
                        },
                        "text": {
                            "font-family": "serif",
                            "font-size": "0px"  
                        },
                        "title": {
                            "font-family": "Arial",  # Changer le type de police 
                            "font-size": "24px"      # Changer la taille de police 
                        }
                    }
                )

################################################## Page d'Accueil ####################################################################


#definir un menu en sidebar
page = st.sidebar.selectbox("Choisissez une page", ["Accueil", "Recommandation par Film", "Recommandation par Mots-Clés", "Who's who ?"])
if page == "Accueil":
    col1, col2, col3 = st.columns([0.2,0.2, 0.6])

    with col1:
       image_path = "https://cdn.discordapp.com/attachments/1243172985502961727/1243173051185762365/logo.webp?ex=665082a0&is=664f3120&hm=fdfbae8bfd6a4ab5941daeb0b85566425615d30cb110951a55b60af2b7097315&"
       st.image(image_path)

    with col3:
        st.title("Yanakhasy")
   
    st.title("🎬 Bienvenue à nos cinéphiles de la Creuse ! 🍿")
    st.markdown("""
    Salut et bienvenue dans notre cinémathèque numérique ! 🎥 Laissez-vous embarquer dans un voyage cinématographique unique, spécialement conçu pour nos amis de la Creuse. Explorez notre sélection de films triés sur le volet et découvrez des pépites qui correspondent à vos goûts les plus subtils. 🌟 Préparez-vous à être éblouis par des histoires captivantes, des intrigues palpitantes et des émotions à couper le souffle ! 💫

    🎉 Alors, prêt à plonger dans l'univers magique du cinéma ? Cliquez, découvrez et laissez-vous emporter ! 🎬
    """)

    st.write("------------------------")
    

    col1, col2, col3 =st.columns([0.3, 0.6, 0.1])
    with col2:
        st.title("Exemples d'affichage")

    col1, col2, col3, col4, col5 = st.columns([0.2, 0.2, 0.3, 0.2, 0.1])
    with col2:
        st.header("Films")
    with col4:
        st.header("Acteurs")

    col1, col2 = st.columns([0.5, 0.5])
    with col1:
        hasClicked = card_accueil("", image_film, titre_film, width = "300px")
    with col2:
        hasClicked = card_accueil("", image_acteur, nom_acteur, width = "300px")


    
########################################### Recommandation par Film ###############################################################


elif page == "Recommandation par Film":
    st.title("Recommandation par Film")

    film_choisi = st.selectbox(label="", options = liste_films, index = 0, placeholder = "Choisir un film")
    condition = liste_films == film_choisi
    #condition = df_film["title"] == film_choisi

    col1, col2 = st.columns(2)

    with col1:
        if df_film[condition]["backdrop_path"].isnull().all():
            st.write("Pas de backdrop path disponible.")
        else:
            image_url = df_film[condition]["backdrop_path"].values[0]

            # Utilisation de st.markdown pour ajouter du CSS à l'image
            st.markdown(f"""
                <style>
                    img {{
                        border-radius: 20px;  /* Bords arrondis */
                        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);  /* Ombre */
                        width: 100%;  /* Assurez-vous que l'image prend toute la largeur de la colonne */
                    }}
                </style>
            """, unsafe_allow_html=True)

            # Affichage de l'image avec l'URL récupérée
            st.image(image_url)

    with col2:
        st.write("")
        st.write(f'Année de Sortie: {df_film[condition]["release_date"].values[0]}')
        st.write(f'Note Moyenne: {df_film[condition]["averageRating"].values[0]}')
        st.write(f'Nombre de Votes: {df_film[condition]["numVotes"].values[0]}')
        st.write(f'Durée:  {df_film[condition]["runtime"].values[0]} minutes')
        st.write(f"")

    st.write("Résumé")
    st.write(df_film[condition]["overview"].values[0])

    #je mets df_film en parametre par defaut , ainsi je pourrai le changer plus facilement si le nom du dataframe change
    def recommend(film_choisi, df_film = df_film):
        #rajouter des commentaire niveau des lignes
        index = df_film[df_film["title"]==film_choisi].index[0]
        
        df_dummies = df_film["genres"].str.get_dummies(sep=",")
        df_all = pd.concat([df_film,df_dummies],axis=1)
        X = df_all[["averageRating", "numVotes", "popularity", "release_date", "runtime", "budget", "revenue","vote_count","vote_average",
                        'Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                        'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi',
                        'Sport', 'Thriller', 'War', 'Western']]
       
        scaler = MinMaxScaler()
        X_scaled = scaler.fit_transform(X)
        model = NearestNeighbors(n_neighbors=6).fit(X_scaled)
        var1,var2 = model.kneighbors(X_scaled)
        var2 = var2[:, 1:]
        indice = var2[index]
        df_reco = df_film.iloc[indice]
        films = []
        backdrop_path = []
        id_reco = []
        for i in (df_reco["title"]):
            films.append(i)
        for j in df_reco["backdrop_path"]:
            backdrop_path.append(j)
        for id in df_reco["imdb_id"]: 
            id_reco.append(id)
            

        return id_reco, films, backdrop_path


    id_reco, liste_films_reco, backdrop_path_reco = recommend(film_choisi)
    
    
    for i in range(5):
        url = f"https://www.imdb.com/title/{id}/"
        hasClicked = card_custom(liste_films_reco[i], backdrop_path_reco[i], id_reco[i])



########################################### Recommandation par keywords #########################################################

elif page == "Recommandation par Mots-Clés":
    st.title("Recommandation par Mots-Clés")

    #random_index_2 = random.randint(0, len(df_film) - 1)
    #default_option_2 = df_film.loc[random_index_2, 'title']
    
    #j'ai enlevé cette definition de variable car deja faite plus haut
    #liste_films = df_film["title"]
    film_choisi = st.selectbox(label="", options = liste_films, index = 0, placeholder = "Choisir un film")
    condition = df_film["title"] == film_choisi

    col1, col2 = st.columns(2)

    with col1:
        if df_film[condition]["backdrop_path"].isnull().all():
            st.write("Pas de backdrop path disponible.")
        else:
            image_url = df_film[condition]["backdrop_path"].values[0]

            # Utilisation de st.markdown pour ajouter du CSS à l'image
            st.markdown(f"""
                <style>
                    img {{
                        border-radius: 20px;  /* Bords arrondis */
                        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);  /* Ombre */
                        width: 100%;  /* Assurez-vous que l'image prend toute la largeur de la colonne */
                    }}
                </style>
            """, unsafe_allow_html=True)

            # Affichage de l'image avec l'URL récupérée
            st.image(image_url)

                
    with col2:
        st.write("")
        st.write(f'Année de Sortie: {df_film[condition]["release_date"].values[0]}')
        st.write(f'Note Moyenne: {df_film[condition]["averageRating"].values[0]}')
        st.write(f'Nombre de Votes: {df_film[condition]["numVotes"].values[0]}')
        st.write(f'Durée:  {df_film[condition]["runtime"].values[0]} minutes')
        st.write(f"")

    st.write("Résumé")
    st.write(df_film[condition]["overview"].values[0])

    count = CountVectorizer()
    count_matrix = count.fit_transform(df_film['mot_cle'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)

    def recommend_par_keyword(film_choisi, cosine_sim = cosine_sim):
        recommended_movies = []
        backdrop_path = []
        id_reco = []
        idx = df_film[df_film["title"] == film_choisi].index[0]   # to get the index of the movie title matching the input movie
        score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)   # similarity scores in descending order
        top_5_indices = list(score_series.iloc[1:6].index)   # to get the indices of top 6 most similar movies
        # [1:6] to exclude 0 (index 0 is the input movie itself)
        
        for i in top_5_indices:   # to append the titles of top 10 similar movies to the recommended_movies list
            recommended_movies.append(list(df_film['title'])[i])
            
        for j in top_5_indices : 
            backdrop_path.append(df_film["backdrop_path"][j])
        for id in top_5_indices:
            id_reco.append(df_film["imdb_id"][id])
        return id_reco,recommended_movies,backdrop_path
    
    id_reco, liste_films_reco, backdrop_path = recommend_par_keyword(film_choisi, cosine_sim)
    

    for i in range(5):
        url = f"https://www.imdb.com/title/{id}/"
        hasClicked = card_custom(liste_films_reco[i], backdrop_path[i],id_reco[i])


################################################ Page Acteurs #########################################################################


elif page == "Who's who ?":

    st.title("Sur cette page tu trouveras une photo de l'intervenant.e que tu as choisi")
    st.write("Et si tu as de la chance il y aura peut-être d'autres infos ;)")


    ######################################### présentation de l'image et des affiches de films #############################################

    with st.container():
    
        option = st.selectbox("Choisissez un nom :", names, index = 0)
        df_filter = df_intervenants[df_intervenants["name"] == option]

        def rechercher():  
            recherche_nom = st.text_input("Saisissez votre terme de recherche :")
            if recherche_nom:
                df_filter_2 = df_intervenants[df_intervenants["name"] == recherche_nom]
            return df_filter_2

        col1, col2= st.columns([0.5, 0.5])

        with col1:
            image_path = df_filter["images"].iloc[0]
            img_remp = "https://i.ytimg.com/vi/_g9Bfj1yy-c/hqdefault.jpg"
            if pd.isna(df_filter["images"].iloc[0]) or (df_filter["images"].iloc[0] == '') or (df_filter["images"].iloc[0].endswith("nan")):
                st.image(img_remp)
                st.text("")
                st.write("Désolé nous n'avons pas d'image à te proposer")
                st.write("Nous t'encourageons à aller voir les sites recommandés sur ta droite")
            else:
                st.image(image_path)

        st.write("----------------------------")



    ################################################# informations ######################################################################

        with col2:
            st.title(df_filter["name"].iloc[0])
            st.header("Informations diverses")

            birth = df_filter["birthday"].iloc[0] if not pd.isna(df_filter["birthday"].iloc[0]) else "Pas d'information disponible"
            death = df_filter["deathday"].iloc[0] if not pd.isna(df_filter["birthday"].iloc[0]) else "PAs d'information disponible"
            birth_place = df_filter["place_of_birth"].iloc[0] if not pd.isna(df_filter["birthday"].iloc[0]) else "PAs d'information disponible"

            st.write("----------------------------")

            if not pd.isna(df_filter["birthday"].iloc[0]):
                if not pd.isna(df_filter["place_of_birth"]).iloc[0]:
                    st.write("Né le", birth, "à", birth_place)
                else:
                    st.write("Né le", birth)
            else:
                st.write("Pas d'information disponible")

            if not pd.isna(df_filter["deathday"].iloc[0]):
                st.write("Date de décès :", death)

            st.write("----------------------------")



            homepage = df_filter["homepage"].iloc[0]
            imdb = "https://www.imdb.com/name/" + df_filter["imdb_id"].iloc[0]
            wiki = "https://fr.wikipedia.org/wiki/" + df_filter["name"].iloc[0].replace(" ", "_")
            if not pd.isna(df_filter["homepage"].iloc[0]):
                col1, col2, col3 = st.columns([0.3, 0.3, 0.3])
                with col1:
                    st.markdown(f"[Page Perso]({homepage})")
                with col2:
                    st.markdown(f"[Page imdb]({imdb})")
                with col3:
                    st.markdown(f"[Page Wikipedia]({wiki})")

            else:
                col1, col2, col3, col4, col5 = st.columns([0.05, 0.4, 0.1, 0.4, 0.05])
                with col2:
                    st.markdown(f"[Page imdb]({imdb})")
                with col4:
                    st.markdown(f"[Page Wikipedia]({wiki})")

            st.write("----------------------------")



    ################################### Récupération des titres de films et affichage #################################################
    
    col1, col2, col3 = st.columns([0.35, 0.5, 0.15])
    with col2:
        st.title("Films notables")

    def find_movie_by_id(maliste) :

        list_df = []

        for id in maliste :

            language = "fr"
            key = "e96a78ea12a5b06071ae2278954655a9"
            url = f"https://api.themoviedb.org/3/find/{id}?api_key={key}&external_source=imdb_id&language={language}"
            response = requests.get(url)
            r_js = response.json()
            df_movie_tmdb = pd.json_normalize(r_js, record_path = "movie_results")
            df_movie_tmdb['id_tmdb'] = id
            list_df.append(df_movie_tmdb)
    
        return  pd.concat(list_df)
    

    knownFor = df_filter["knownForTitles"].iloc[0]
    if not pd.isna(knownFor):
        knownFor = knownFor.split(",")                 # transforme la chaîne de caractères en liste
        df_actor = find_movie_by_id(knownFor)          # applique la fonction find_movie_by_id sur la liste
        df_actor = df_actor.reset_index(drop = True)   # utiliser pour éviter d'avoir un nouvel index
        df_actor['poster_path'] = df_actor.poster_path.apply(lambda image : "https://media.themoviedb.org/t/p/w300_and_h450_bestv2" +  image)
        


    result = st.columns(len(df_actor))
    #va adapter le nombre de colonnes au nombre de titres

    if result != 0:
        for i in range(len(df_actor)):                                         # on parcoure df_actor
            with result[i] :                                                   # selon la valeur de i => i est l'indice de la ligne sur laquelle il travaille
                titre = df_actor.iloc[i, -9]                                   # récupère le title dans df_actor
                image_index = list(df_actor.columns).index("poster_path")      # trouve l'indice où se trouve le poster_path => ici 4 
                image_url = df_actor.iloc[i,image_index]                       # créé une variable image_url qui va récupérer dans df_actor i pour la ligne, image_index pour la colonne
                tmdb = df_actor.iloc[i, -1]                                    # récupère pour la ligne d'indice i la dernière colonne: id_tmdb
                url = f"https://www.imdb.com/title/{tmdb}/"                    # concaténation
                
                # Configuration de la carte avec des styles personnalisés
                hasClicked = card_accueil(titre, image_url, tmdb, width = "200px")

    else:
        st.write("Désolé, nous n'avons pas de films à vous présenter")
        pass



    ################################################## biographie #########################################################################

    biography = df_filter["biography"].iloc[0]
    autre = df_filter["known_for_department"].iloc[0]

    if not pd.isna(df_filter["biography"].iloc[0]):
        st.title("Biographie")
        st.markdown(biography)
    else:
        col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
        with col2:
            st.header("Aïe nous n'avons pas de biographie à te proposer")
            st.write("Nous t'encourageons à aller voir les sites recommandés un peu plus haut")


############################################## Améliorations #############################################################

# faire en sorte d'avoir plusieurs fichiers plutôt qu'un seul

# modifier le sytème de choix de film => proposer à l'utilisateur d'entrer un titre de film en plus de la liste
# modifier le système de recommandation par mots-clés pour que l'utilisateur puisse entrer ses mots clés

# problème : les titres des films n'apparaissent plus sur les cards pour les recommandations
# dans la V2 reprendre le format des cartes pour la page acteur
    
    

        


        
        
        
            

