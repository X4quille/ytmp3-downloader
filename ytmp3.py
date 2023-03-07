from pytube import YouTube 

import os 
  
yt = YouTube( 

    str(input("Enter the URL of the YouTube video you want to convert : \n>> "))) 

 
video = yt.streams.filter(abr = '160kbps').last() 

out_file = video.download() 


base, ext = os.path.splitext(out_file) 


new_file = base + '.mp3'
os.rename(out_file, new_file) 
 
 
print("Download Was Successful", new_file)
