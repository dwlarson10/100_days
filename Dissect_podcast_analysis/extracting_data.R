require(spotifyr)
require(tidyverse)
require(ggplot2)
require(geniusr)
require(tidytext)

# Sets the API Keys and authenticates app

Sys.setenv(SPOTIFY_CLIENT_ID = 'c9eb9c91c7d54df9815c742543687f54')
Sys.setenv(SPOTIFY_CLIENT_SECRET = '9778531b27614720be4f7c5224a9c975')
access_token <- get_spotify_access_token()

#Extracts data for each artists, adds a variable for artists and binds them to a single data-frame.
artists <- c('Frank Ocean','Kanye West','Kendrick Lamar','Tyler, The Creator','Lauryn Hill')

dissect_df <- data.frame()
for (artist in artists){
df <- get_artist_audio_features(artist )
df$artist <- artist

dissect_df <- rbind(df,dissect_df)

}


dissect_df <- dissect_df%>%select(
'artist_name', 'artist',
'album_release_date', 'danceability',
'energy', 'loudness', 'speechiness', 'acousticness', "instrumentalness", 'liveness', 'valence', 'tempo','track_name', 'album_name', 'key_name', 'mode_name'
)


## GET DATA ON SONG LYRICS FROM GENIUS

artists_alubms <- dissect_df%>%select('artist_name','album_name')%>%unique()%>%filter(album_name != 'Cherry Bomb + Instrumentals',
                                                                              album_name != 'Live At Splash!',
                                                                              album_name != 'Black Panther The Album Music From And Inspired By',
                                                                              album_name != 'DAMN. COLLECTORS EDITION.',
                                                                              album_name != 'Graduation (Alternative Business Partners)')



library(purrr)
library(ggplot2)

# set lexicon
bing <- get_sentiments("bing")

safe_track <- safely(get_album_tracklist_search,otherwise = NA)



# scrape album tracklist
tracklist = data.frame()
for (artist in artists){
  tmp = artists_alubms[artists_alubms$artist == artist,]
  print(artist)
  for (track in tmp$album_name){
    try( tmp_2 <- get_album_tracklist_search(artist_name = artist,
                                            album_name = track), )
    tracklist = rbind(tracklist,tmp_2)
    Sys.sleep(2)
  }
}


lyrics <- map_df(tracklist$song_lyrics_url, get_lyrics_url)

lyrics = data.frame()
for (track in tracklist$song_lyrics_url){
  print(track)
  try(tmp3 <- get_lyrics_url(track),)
  
  lyrics <- rbind(lyrics,tmp3)
  
}


try(get_lyrics_url('https://genius.com/Frank-ocean-nikes-lyrics'))






