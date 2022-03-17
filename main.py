from pytube import YouTube
from os import rename

def videoDownloader(video): 
    for stream in video.streams.filter(progressive=True):
        print(f'\033[1;36mResolution: {stream.resolution} - Fps: {stream.fps}\033[m')

    print('\033[1;36mResolution: 1080p - Fps: 30 (May not available)\033[m')
    res = input('\033[1;34mChoose the resolutuon (Example: 720p)\033[m')

    try:
        print('\033[1;34mDownloading\033[m')
        video.streams.filter(res=res).first().download('./videos')
        print('Finished!')
    except AttributeError:
        print('\033[1;31mNot valid resolution, try again\033[m')
        videoDownloader(video)
        return

def songDownloader(video):
    if video != None: 
        vdo = video.streams.filter(only_audio=True).first()

        print('\033[1;34mDownloading\033[m')
        fileName = vdo.download('songs')
        rename(fileName, fileName.replace('.mp4', '.mp3'))
        print('\033[1;34mFinished!\033[m')
    
    else: 
        fileurl = input('File With Urls: ')
        path = input('Path Name: ')
        with open (fileurl, 'r', encoding='utf-8') as file:
            urls = file.readlines()
        print('======================================================')
        print('Starting Downloads...')
        print('------------------------------------------------------')
        for song in urls:
            song = YouTube(song.replace('\n', ''))
            try:
                songMeta = song.metadata[0]
                print(f'\033[1;34mDownloading\033[m - \033[0;32m{songMeta["Song"]}\033[m, \033[0;32m{songMeta["Artist"]}\033[m')
                sng = song.streams.filter(only_audio=True).first()
                fn = ''.join([i for i in f'{songMeta["Song"]} - {songMeta["Artist"]}.mp3' if not i in '\/?:*<>|'])
                fileName = sng.download(f'songs/{path}', filename=fn)
            except IndexError:
                print(f'\033[1;34mDownloading\033[m - \033[0;32m{song.title}\033[m')
                print(f'\033[1;31mMetadata not found! Donwloading with video title\033[m')
                sng = song.streams.filter(only_audio=True).first()
                fn = ''.join([i for i in song.title + '.mp3' if not i in '\/?:*<>|'])
                fileName = sng.download(f'songs/{path}', filename=fn)

            print('\033[1;34mCompleted\033[m')
            print('------------------------------------------------------')
        
        print('\033[1;34mFinished!\033[m')
        
option = input('\033[1;34mWhat option do you want?\033[m\n\033[0;32m[1] Video Downloader\n[2] Songs Downloader\n[3] Download Songs Consecutively\n\033[m')

if option == '1':
    print('======================================================')
    url = input('\033[1;36mYoutube Url: \033[m')
    video = YouTube(url)
    videoDownloader(video)
elif option == '2':
    print('======================================================')
    url = input('\033[1;36mYoutube Url: \033[m')
    video = YouTube(url)
    songDownloader(video)
elif option == '3':
    print('======================================================')
    songDownloader(None)
else: 
    print('\033[1;31mChoose a valid option!\033[m')
