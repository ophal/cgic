CFLAGS=-g -Wall
LUA_CFLAGS=`pkg-config lua5.1 --cflags`
CC=gcc

export SCRIPT_NAME:= index.cgi
export REQUEST_METHOD:= post
export CONTENT_LENGTH:= 1397
export CONTENT_TYPE:= multipart/form-data; boundary=---------------------------1544642457600615447237782214

all: cgic.so 

install: cgic.so
	cp cgic.so /usr/local/lib/lua/5.1/

cgic.so:
	$(CC) $(CFLAGS) $(LUA_CFLAGS) -O3 -fPIC -o cgic.o -c cgic.c
	$(CC) -shared -O3 cgic.o -o cgic.so

test:
	./tests/index.cgi < tests/post.dat

clean:
	rm -f *.o *.so

