from pafy import new

def video_link_url(url):
    video = new(url)
    best = video.getbest(preftype='mp4')
    # print(best.resolution, best.extension)
    title = video.title
    name = 'urlvideo'
    best.download('./static/uploadedvideo/'+ name+'.mp4')
    # bestaudio = video.getbestaudio() 
    # bestaudio.download()
    return(title, name)

# url = 'https://www.youtube.com/watch?v=j8DHsQwWEhY'
# video_link_url(url)

