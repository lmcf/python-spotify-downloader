import enquiries
import os

# Const
ln = '\n'

# Functions
def descargar_lista(params,types = None, url_or_name = None):
    command_song = 'spotdl '

    print(url_or_name)

    if types is not None:
        if types < 3:   
            url_or_name = url_or_name.split(",")
            for song in url_or_name:
                command_song += params[0]+' "'+song+'" '
            print(command_song + ln)
            os.popen(command_song).read()
            input('Press Enter to continue..')

        if 2 < types:
            if url_or_name is not None:
                command_song += params[types] + url_or_name + params[2]
                print(command_song + ln)
                os.popen(command_song).read()
                descargar_lista(params,types)
            
            if url_or_name is None:
                command_song += params[1]
                print(command_song + ln)
                os.popen(command_song).read()
                os.remove('songs_list.txt')
                input('Press Enter to continue..')
                types = None   
   

def print_and_return(value):
    print(value)
    return value

# Arrays info
options = [
        'Track - By Name', 
        'Track - By Spotify URL ', 
        'Track - By Youtube Link',
        'PlayList - By Playlist URL ',
        'Album - By Album URL ',
        'All albums - By Artist URL ',
        'Exit']

helpInfo  = [
        'Can also accept multiple tracks separated by commas.',
        'You can copy this URI from your Spotify desktop or mobile app by right clicking or long tap on the song and copy HTTP link.',
        'You can copy the YouTube URL  or ID of a video.',
        'You can copy the Spotify URI of the playlist.',
        'You can copy the Spotify URI of the album.',
        'You can copy the Spotify URI of the artis to get all albums.']

examples = [
        'EX: Dance Monkey, Whine Up, Roxanne (separated by commas)',
        'EX: https://open.spotify.com/track/2lfPecqFbH8X4lHSpTxt8l',
        'EX: https://www.youtube.com/watch?v=lc4Tt-CU-i0',
        'EX: https://open.spotify.com/user/nocopyrightsounds/playlist/7sZbq8QGyMnhKPcLJvCUFD',
        'EX: https://open.spotify.com/album/499J8bIsEnU7DSrosFDJJg',
        'EX: https://open.spotify.com/artist/1feoGrmmD8QmNqtK2Gdwy8']

params = [
    ' --overwrite skip --song ',
    ' --overwrite skip --list=songs_list.txt ',
    ' --write-to=songs_list.txt ',
    ' --playlist ',
    ' --overwrite force --album ',
    ' --overwrite force --all-albums ']


# Main
while True:

    #Clean console
    print(os.popen('clear').read())
    # Menu
    choice = print_and_return(enquiries.choose('Choose one of these options: ', options))
    for option in options:
        if option == choice:
            choice = options.index(option)

    # Exit or Print options and actions
    if choice == 6 : quit()
    print(helpInfo[choice])
    print(examples[choice] + ln)
    descargar_lista(params,choice, input(' -> '))




       

