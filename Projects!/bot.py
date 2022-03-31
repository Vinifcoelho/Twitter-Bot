import tweepy
import lyricsgenius
import requests
import random
import json

#config file keeps API login data
import config

twit = config.twitter_keys
gen = config.genius_keys


def get_random_song():
    #open text file containing list of songs
    path = "mobo.txt"
    songs_list = []

    with open(path, "r") as file:
        for line in file:
            #save each song to a list
            sl = line.strip()
            songs_list.append(sl)


    genius_access_token = gen["ACCESS_TOKEN"]
    genius = lyricsgenius.Genius(genius_access_token)
    genius.verbose = False #Keeps statement that reads *searching for song...* from printing
    random_song = random.choice(songs_list)

    #search for song extracted from list along with artist name to ensure the right song is grabbed
    lyrics = genius.search_song(random_song,"Modern Baseball").lyrics

    #return list of songs
    return lyrics




def create_tweet(lyrics):
    lines = lyrics.split('\n')
    for index in range(len(lines)):
        #find empty lines or lines beginning with '[' (usually lines that say like [Chorus] or something

        if lines[index] == "" or "[" in lines[index]:
            lines[index] = "XXX"
    lines = [i for i in lines if i!="XXX"]

    r_num = random.randrange(0,len(lines)-1)
    tweet_text = lines[r_num] + "\n" +  lines[r_num+1] +"\n"+ lines[r_num+2]
    #replace '\' char with empty char
    tweet_text = tweet_text.replace("\\","")

    return(tweet_text)


#AWS lambda function
def send():
    auth = tweepy.OAuthHandler(
        twit["CONSUMER_API_KEY"],
        twit["CONSUMER_API_KEY_SECRET"]
    )

    auth.set_access_token(
        twit["ACCESS_TOKEN"],
        twit["ACCESS_TOKEN_SECRET"]
    )

    api = tweepy.API(auth)

    lyrics = get_random_song()

    tweet = create_tweet(lyrics)
    status = api.update_status(tweet)

    return tweet

send()