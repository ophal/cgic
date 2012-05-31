CFLAGS=-g -Wall
LUA_CFLAGS=`pkg-config lua5.1 --cflags`
CC=gcc

all: cgic.so install

install: cgic.so
	cp cgic.so /usr/local/lib/lua/5.1/

cgic.so:
	$(CC) $(CFLAGS) $(LUA_CFLAGS) -O3 -fPIC -o cgic.o -c cgic.c
	$(CC) -shared -O3 cgic.o -o cgic.so

clean:
	rm -f *.o *.so
