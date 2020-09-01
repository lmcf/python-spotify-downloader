import enquiries
import sys
import os
import getpass

options = [
    'Track - By Name', 
    'Track - By Spotify URL', 
    'Track - By Youtube Link',
    'PlayList - By Playlist URL',
    'PlayList - By Album URL',
    'All albums - By Artist URL']

choice = enquiries.choose('Choose one of these options: ', options)

print('\n',choice)


def descargar_lista(param, songs = None):
    print('\n')
    command_song = ' spotdl '
   
    if param == ' --song ':   
        songs = songs.split(",")
        for song in songs:
            command_song += ' "'+song+'" '

    if param != ' --song ':
        if songs is not None:
            command_song += param[0] + songs + param[2]
        if songs is None:
            command_song += param[1]
    
    print(command_song)
    stream = os.popen(command_song)
    output = stream.read()
    print(output)

if choice == options[0]:
    print('\n Can also accept multiple tracks separated by commas')
    songs = input('\n EX: soundtrack champions league, ritmo, waka waka \n ')
    parametros = [' --song ']
    descargar_lista(parametros, songs)

if choice == options[1]:
    print('\n You can copy this URI from your Spotify desktop or mobile app by right clicking or long tap on the song and copy HTTP link.')
    songs = input('\n EX: https://open.spotify.com/track/2lfPecqFbH8X4lHSpTxt8l \n ')
    parametros = [' --song ']
    descargar_lista(parametros, songs)

if choice == options[2]:
    print('\n You can copy the YouTube URL or ID of a video')
    songs = input('\n EX: https://www.youtube.com/watch?v=lc4Tt-CU-i0 \n ')
    parametros = [' --song ']
    descargar_lista(parametros, songs)

if choice == options[3]:
    print('\n You can copy the Spotify URI of the playlist')
    songs = input('\n EX: https://open.spotify.com/user/nocopyrightsounds/playlist/7sZbq8QGyMnhKPcLJvCUFD \n ')
    parametros = [' --playlist ' , ' --list=songs.txt ', ' --write-to=songs.txt ']
    descargar_lista(parametros, songs)

if choice == options[4]:
    print('\n You can copy the Spotify URI of the album')
    songs = input('\n EX: https://open.spotify.com/album/499J8bIsEnU7DSrosFDJJg \n ')
    parametros = [' --album ' , ' --list=songs.txt ', ' --write-to=songs.txt ']
    descargar_lista(parametros, songs)

if choice == options[5]:
    print('\n You can copy the Spotify URI of the artis to get all albums')
    songs = input('\n EX: https://open.spotify.com/artist/1feoGrmmD8QmNqtK2Gdwy8 \n ')
    parametros = [' --all-albums ' , ' --list=songs.txt ', ' --write-to=songs.txt ']
    descargar_lista(parametros, songs)

if choice == options[3] or choice == options[4] or choice == options[5]:
    descargar_lista(parametros)

exit()
