P=database
CFLAGS=`pkg-config --cflags Qt5Widgets`
LDLIBS=`pkg-config --libs Qt5Widgets`
CC=g++

make main:
	$(CC) $(P).cpp -o $(P) $(LDLIBS) $(CFLAGS) -l sqlite3 -fPIC
