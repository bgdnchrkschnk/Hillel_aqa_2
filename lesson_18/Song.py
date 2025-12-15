class Song:
    TOTAL_SONGS = 0

    def __init__(self, title, artist, bpm):
        self.title = title
        self.artist = artist
        self.__bpm = bpm # private self.bpm
        self.__class__.TOTAL_SONGS += 1


    @classmethod # тоді коли потрібно знати лише про клас (не про обʼєкт)
    def get_total_songs(cls):
        return cls.TOTAL_SONGS

    @property
    def bpm(self): # .bpm() .bpm
        return self.__bpm

    @staticmethod # незалежний метод
    def convert_bpm_to_miliseconds(bpm):
        return bpm * 1000

    def __str__(self):
        return f"The title is {self.title}, and the artist is {self.artist} (BPM: {self.__bpm})"



rock_song: Song = Song('Die MF!', 'HardFucker', 140)
pop_song: Song = Song("Love 4ever", "Sweetkitty", 100)
rap_song: Song = Song("Street life", "Lil Python", 80)



print(
    pop_song.bpm,
)

print(
    Song.get_total_songs()
)

# print(rock_song)
# print(pop_song)
# print(rap_song)
#
# print(rock_song.bpm)
# print(pop_song.bpm)
# print(rap_song.bpm)
#
# rap_song.bpm = 180
# print(rap_song.bpm)



