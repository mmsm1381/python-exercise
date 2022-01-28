from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Media:
    name : str
    location : str
    rating : float


@dataclass
class MediaPlayer(ABC):
    media_list : list

    def set_media_list(self):
        param = self.__class__.param
        media_list = []
        for media in self.media_list:
            if media.location.startswith(param):
                media_list.append(media)
        self.media_list = media_list

    def play_by_name(self):
        self.media_list = sorted(self.media_list,key= lambda media : media.name )
        print("runnig by name order")
        self.__class__.play(self)   

    def play_by_rating(self):
        self.media_list = sorted(self.media_list,key= lambda media : media.rating,reverse=True )
        print("running by rating order")
        self.__class__.play(self)  

    @abstractmethod
    def play(self):
        pass


class WebMediaPlayer(MediaPlayer):
    param = ("https://")

    def play(self):
        for media in self.media_list:
            print(f"running web media {media}" )



class LocalMediaPlayer(MediaPlayer):
    param = ("/","C:\\")

    def play(self):
        for media in self.media_list:
            print(f"running local media {media}" )
 


media1 = Media("a","https://a",4.5)
media2 = Media("b","/home/mahdi/python/OPP",5)
media3 = Media("d","/",4.5)
media4 = Media("c","C:\media",2.5)
test_media_list = [media1,media2,media3,media4]

webmediaplayer = WebMediaPlayer(test_media_list)
webmediaplayer.set_media_list()

webmediaplayer.play()
webmediaplayer.play_by_name()
webmediaplayer.play_by_rating()

print("----------------------------------------")

localmediaplayer = LocalMediaPlayer(test_media_list)
localmediaplayer.set_media_list()

localmediaplayer.play()
localmediaplayer.play_by_name()
localmediaplayer.play_by_rating()