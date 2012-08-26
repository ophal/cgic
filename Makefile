CFLAGS= -g -Wall
LUA_CFLAGS= `pkg-config lua5.1 --cflags`
CC= gcc

export SCRIPT_NAME:= index.cgi
export REQUEST_METHOD:= post
export CONTENT_LENGTH:= 1397
export CONTENT_TYPE:= multipart/form-data; boundary=---------------------------1544642457600615447237782214

all: cgic.so 

install: cgic.so
	cp cgic.so /usr/local/lib/lua/5.1/

cgic.so:
	$(CC) $(CFLAGS) $(LUA_CFLAGS) -O2 -fPIC    -c -o cgic.o cgic.c
	$(CC) -o cgic.so   cgic.o -shared -lm

test:
	./tests/index.cgi < tests/post.dat

clean:
	rm -f cgic.o cgic.so

