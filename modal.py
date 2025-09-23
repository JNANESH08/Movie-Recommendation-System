from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
import numpy as np
import os
import sys
import joblib
import warnings
warnings.simplefilter('ignore')

cwd = sys.path[0]

class Modal:
    __recommender_modal = None
    def train():
        print("Started training the modal")
        movie_data = pd.read_csv(os.path.join(cwd, 'dataset', 'movies_metadata.csv'))

        movie_data['genres'] = movie_data['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])

        movie_data['year'] = pd.to_datetime(movie_data['release_date'], errors='coerce').apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)

        vote_counts = movie_data[movie_data['vote_count'].notnull()]['vote_count'].astype('int')

        minimum_votes = vote_counts.quantile(0.95)

        md = movie_data

        qualified = md[(md['vote_count'] >= minimum_votes) & (md['vote_count'].notnull()) & (md['vote_average'].notnull())][
            ['title', 'year', 'vote_count', 'vote_average', 'popularity', 'genres']]
        qualified['vote_count'] = qualified['vote_count'].astype('int')
        qualified['vote_average'] = qualified['vote_average'].astype('int')

        small_mdf = pd.read_csv(os.path.join(cwd, 'dataset', 'movie_data.csv'))
        small_mdf = small_mdf[small_mdf['tmdbId'].notnull()]['tmdbId'].astype('int')

        def convert_int(x):
            try:
                return int(x)
            except:
                return np.nan

        md['id'] = md['id'].apply(convert_int)
        md = md.drop([19730, 29503, 35587])
        md['id'] = md['id'].astype('int')
        sm_df = md[md['id'].isin(small_mdf)]

        sm_df['tagline'] = sm_df['tagline'].fillna('')
        sm_df['description'] = sm_df['overview'] + sm_df['tagline']
        sm_df['description'] = sm_df['description'].fillna('')

        tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')
        tfidf_matrix = tf.fit_transform(sm_df['description'])

        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

        sm_df = sm_df.reset_index()
        titles = sm_df['title']
        indices = pd.Series(sm_df.index, index=sm_df['title'])

        modal = {
            "cosine_sim": cosine_sim,
            "titles": titles, 
            "indices": indices
        }

        print("Modal Trained")

        # Saving the hash
        joblib.dump(modal, os.path.join(cwd, 'recommender_modal.pkl'))

        print("PKL saved")


    def __init__(self):
        # Check if recommender_modal.pkl file is present or not
        if not os.path.exists(os.path.join(cwd, 'recommender_modal.pkl')):
            # Train the modal
            print("Training the modal")
            Modal.train()

        # Load the modal to shared state if not present
        if Modal.__recommender_modal is None:
            # Load the recommender_modal to shared state
            print("Loading PKL")
            Modal.__recommender_modal = joblib.load(os.path.join(cwd, 'recommender_modal.pkl'))

    def get_recommendations(self, title):
        # print(Modal.__recommender_modal)
        idx = Modal.__recommender_modal['indices'][title]
        sim_scores = list(enumerate(Modal.__recommender_modal['cosine_sim'][idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:51]
        movie_indices = [i[0] for i in sim_scores]
        return Modal.__recommender_modal['titles'].iloc[movie_indices]
    
# if __name__ == '__main__':
#     obj1 = Modal()

#     print(obj1.get_recommendations('Shanghai Triad'))

#     obj2 = Modal()

#     print(obj2.get_recommendations('Four Rooms'))