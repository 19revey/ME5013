CC=g++
CFLAGS=-c -Wall

all: hello
clean: 
	rm -rf *.o hello
hello: main.o factorial.o hello.o
	$(CC) main.o factorial.o hello.o -o hello
main.o: main.cpp
	$(CC) $(CFLAGS) main.cpp
factoral.o:
	$(CC) $(CFLAGS) factorial.cpp
hello.o:
	$(CC) $(CFLAGS) hello.cpp

