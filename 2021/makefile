CC = gcc
CFLAGS = -Wall -g


%.o: %.c
	$(CC) -c -o $@ $< $(CFLAGS)

day_1: day_1.o
	$(CC) -o $@ $^ $(CFLAGS)

clean:
	rm *.o day_1