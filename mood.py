import pandas as pd

spotify_df = pd.read_csv('SpotifySongs.csv') 

def determine_mood(row):
    if row['Energy'] > 0.7 and row['Valence'] > 0.6 and row['Danceability'] > 0.6:
        return 'Happy'
    elif row['Energy'] < 0.4 and row['Valence'] < 0.4:
        return 'Sad'
    elif row['Energy'] > 0.8 and row['Danceability'] > 0.7:
        return 'Party'
    elif row['Energy'] > 0.7 and row['Danceability'] > 0.6:
        return 'Dance'
    elif row['Energy'] > 0.8:
        return 'Energetic'
    elif row['Energy'] > 0.6 and row['Valence'] > 0.5:
        return 'Motivation'
    elif row['Energy'] < 0.4 and row['Valence'] > 0.5:
        return 'Relaxed'
    elif row['Energy'] < 0.6 and row['Valence'] > 0.6:
        return 'Romantic'
    elif row['Energy'] < 0.6 and row['Valence'] < 0.4:
        return 'Introspective'
    elif row['Energy'] > 0.6 and row['Valence'] < 0.4:
        return 'Angry'
    elif row['Energy'] > 0.5 and row['Valence'] > 0.6:
        return 'Uplifting'
    elif row['Energy'] < 0.4 and row['Valence'] < 0.6:
        return 'Nostalgic'
    elif row['Energy'] < 0.5 and row['Loudness'] < -8:
        return 'Chill'
    elif row['Energy'] < 0.5 and row['Tempo'] < 80:
        return 'Melancholic'
    elif row['Energy'] > 0.5 and row['Tempo'] > 120:
        return 'Motivational'
    elif row['Energy'] < 0.3 and row['Valence'] < 0.3:
        return 'Melancholic'
    elif row['Energy'] > 0.7 and row['Loudness'] > -5:
        return 'Exciting'
    elif row['Speechiness'] > 0.1 and row['Liveness'] > 0.2:
        return 'Spoken Word'
    elif row['Acousticness'] > 0.5 and row['Instrumentalness'] > 0.5:
        return 'Instrumental'
    elif row['Liveness'] > 0.3 and row['Energy'] < 0.5:
        return 'Ambient'
    elif row['Tempo'] < 100 and row['Energy'] < 0.4:
        return 'Mellow'
    elif row['Mode'] == 1 and row['Valence'] > 0.5:
        return 'Joyful'
    elif row['Mode'] == 0 and row['Valence'] < 0.5:
        return 'Sorrowful'
    else:
        return 'Neutral'  

spotify_df['Mood'] = spotify_df.apply(determine_mood, axis=1)

print(spotify_df.head())

spotify_df.to_csv('Songs with Moods.csv', index=False)