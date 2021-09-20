P=weather
CFLAGS=`pkg-config --cflags Qt5Widgets`
LDLIBS=`pkg-config --libs Qt5Widgets`
CURLCONFIGS=`curl-config --libs`
CC=g++

make main:
	$(CC) $(P).cpp -o $(P) $(LDLIBS) $(CFLAGS) $(CURLCONFIGS) -fPIC
