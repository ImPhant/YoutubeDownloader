from pytube import YouTube
from os import rename

def videoDownloader(video): 
    for stream in video.streams.filter(progressive=True):
        print(f'Resolution: {stream.resolution} - Fps: {stream.fps}')

    print('Resolution: 1080p - Fps: 30 (May not available)')
    res = input('Choose the quality: ')

    try:
        print('Downloading...')
        video.streams.filter(res=res).first().download('./videos')
        print('Finished!')
    except AttributeError:
        print('Not valid resolution, try again')
        videoDownloader(video)
        return


def songDownloader(video):
    if video != None: 
        vdo = video.streams.filter(only_audio=True).first()

        print('Downloading...')
        fileName = vdo.download('songs')
        rename(fileName, fileName.replace('.mp4', '.mp3'))
        print('Finished!')
    
    else: 
        fileurl = input('File With Urls: ')
        path = input('Path Name: ')
        with open (fileurl, 'r', encoding='utf-8') as file:
            urls = file.readlines()
        print('======================================================')
        print('Starting Downloads...')
        for song in urls:
            song = song.replace('\n', '')
            sng = YouTube(song).streams.filter(only_audio=True).first()
            fileName = sng.download(f'songs\{path}')
            rename(fileName, fileName.replace('.mp4', '.mp3'))
            print('Downloaded - {}'.format(fileName.replace('.mp4', '.mp3')))
        print('Finished!')
        

option = input('What option do you want?\n[1] Video Downloader\n[2] Songs Downloader\n[3] Download Songs Consecutively\n')

if option == '1':
    print('======================================================')
    url = input('Youtube Url: ')
    video = YouTube(url)
    videoDownloader(video)
elif option == '2':
    print('======================================================')
    url = input('Youtube Url: ')
    video = YouTube(url)
    songDownloader(video)
elif option == '3':
    print('======================================================')
    songDownloader(None)
else: 
    print('Choose a valid option!')
