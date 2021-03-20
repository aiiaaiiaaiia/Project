from pafy import new

def video_link_url(url):
    video = new(url)
    best = video.getbest(preftype='mp4')
    # print(best.resolution, best.extension)
    best.download()
    # bestaudio = video.getbestaudio() 
    # bestaudio.download()
    video_link_url(url)