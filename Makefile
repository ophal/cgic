CFLAGS=-g -Wall
LUA_CFLAGS=`pkg-config lua5.1 --cflags`
CC=gcc

export SCRIPT_NAME:= cgictest.cgi
export REQUEST_METHOD:= post
export CONTENT_LENGTH:= 1342
export CONTENT_TYPE:= multipart/form-data; boundary=-----------------------------8287539502325421911076543375

all: cgic.so install

install: cgic.so
	cp cgic.so /usr/local/lib/lua/5.1/

cgic.so:
	$(CC) $(CFLAGS) $(LUA_CFLAGS) -O3 -fPIC -o cgic.o -c cgic.c
	$(CC) -shared -O3 cgic.o -o cgic.so

test:
	./test/index.cgi < post.txt

clean:
	rm -f *.o *.so
