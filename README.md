# Twitter-Bot
A Python script that utilizes the lyricsgenius API to grab random lyrics from songs by Modern Baseball and tweets them to an account using the Twitter API and Tweepy Python library

bot.py is the driver code. It contains a function to access 'mobo.txt' (which contains a list of songs by the band Modern Baseball) and saves each line as a new value in a list. It then takes this list, queries the lyricsgenius API to locate the song, and grabs 3 lines of song lyrics while cleaning it up and removing things like '[Chorus]'. The final function handles the accessing of the Twitter API and calls the previous two functions in order to create a tweet then posts them to the twitter page. 

config.py contains API keys and access tokens for accessing the Twitter and Lyricsgenius API.

mobo.txt contains a list of songs by the band Modern Baseball with a new song on each line to make traversing easier.
