CFLAGS=-g -Wall
CC=gcc

all: cgic.so

cgic.so:
	$(CC) $(CFLAGS) -O3 -fPIC -o cgic.o -c cgic.c
	$(CC) -shared -O3 cgic.o -o cgic.so

clean:
	rm -f *.o *.so
