# -*- coding: utf-8 -*-
from musixmatch import Musixmatch
import json

api_key = ''

musixmatch = Musixmatch(api_key)

# Belgium
# Canada
# Germany
# United Kingdom
# Mexico
# Norway
# Russia
# Sweden
# United States
# Australia
# United Arab Emirates
# Switzerland
# Uganda
# New Zealand
countries = ['BE','CA','DE','GB','MX','NO','RU','SE','US','AU','AE','CH','UG','NZ']

genre_names = {}

out = open('canciones.csv','w')
out.write('lyrics_string,genre_class\n')

for country in countries:
  j = 0

  while True:
    j += 1

    tracks = musixmatch.chart_tracks_get(page=j,page_size=100,f_has_lyrics=1,country=country)

    track_list = tracks['message']['body']['track_list']

    if len(track_list) == 0:
      break

    for i in range(len(track_list)):
      track = track_list[i]['track']
      id = track['track_id']
      genre_list = track['primary_genres']['music_genre_list']
      # Ignoramos canciones sin género asigando
      if len(genre_list) > 0:
        genre_track = genre_list[0]['music_genre']
        genre = genre_track['music_genre_id']
        # Diccionario de nombres
        genre_names[genre] = genre_track['music_genre_name']
        lyrics_message = musixmatch.track_lyrics_get(id)
        lyrics_object = lyrics_message['message']['body']['lyrics']
        # Quitamos canciones que no están en inglés
        if lyrics_object['lyrics_language'] != 'en':
          continue
        lyrics_track = lyrics_object['lyrics_body']
        out.write('"{}",C{}\n'
          .format(lyrics_track\
            .replace('\n','\\n') # Eliminamos saltos de linea
            .replace('"','')     # Eliminamos comillas
            # Mensaje que aparece por usar el plan gratuito (para TESTING)
            .replace('******* This Lyrics is NOT for Commercial use *******','')
            .replace('\n...\n',''),
            genre))

out.close()
with open('genre_names.json','w') as dictionary:
  json.dump(genre_names,dictionary)
