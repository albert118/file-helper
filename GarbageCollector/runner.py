from os import listdir
from os.path import join
from GarbageCollector import MovieLibraryTrasher

# dirty run and check every subdir

dir = "\\\\DAEDALUS2\\Media\\Movies"
t = MovieLibraryTrasher.MovieLibraryTrasher()

for subdir in listdir(dir):
    t.collect_garbage(join(dir, subdir))
