from pytube import YouTube


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()(output_path=save_directory)
    except:
        print("An error has occurred")
    print("Download is completed successfully")

save_directory = "backend/controllers/videosDonwloaded" 
link = input("Enter the YouTube video URL: ")
Download(link)