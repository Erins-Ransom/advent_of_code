// day_1.c 
#include <stdio.h>

// For this one, we're goig to stream the input from the file rather
// than loading the full contents into memory so we can avoid memory 
// management among other reasons.  
int main() {

    // Firest we open up our input stream in read-only mode.
    FILE* input = fopen("input_1.txt", "r");
    if (!input) {
        fprintf(stderr, "ERROR: Could not open file \"input_1.txt\"\n");
        return 1;
    }

    /************************* PART 1 *******************************/
    // Next we initilaize our varibles and counter, retrieving the first 
    // integer and resetting our file pointer to the beinging of the stream.
    int current_number = 0, next_number = 0, counter = 0; 
    fscanf(input, "%d", &current_number);
    fseek(input, 0, SEEK_SET);
    

    // We then continue to read in subsequent integers from the stream, 
    // comparing them to the previous, until there are no integers left 
    // to be read from the stream.
    while(1 == fscanf(input, "%d", &next_number)) {
        if (next_number > current_number)
            counter++;
        current_number = next_number;
    }

    fprintf(stdout, "Total increases in depth:\t%d", counter);

    /************************* PART 2 *******************************/
    // We initialize our variables and reset our counter as before, 
    // but now we need to read in the next 3 integers and sum them
    fseek(input, 0, SEEK_SET);
    counter = 0;
    int current_sum, next_sum, v0, v1, v2 = 0;
    long int offset = ftell(input);
    fscanf(input, "%d\n%d\n%d", &v0, &v1, &v2);
    fseek(input, 0, SEEK_SET);
    current_sum = v0 + v1 + v2;

    // Unlike before, we now need to rewind the file pointer after each 
    // read since the next window will start in the middle of the current 
    // window. We proceed until there are fewer than 3 inputs left, comparing
    // sums as we compared individual values before.  
    while(3 == fscanf(input, "%d\n%d\n%d", &v0, &v1, &v2)) {
        next_sum =  v0 + v1 + v2;
        if (next_sum > current_sum)
            counter++;
        current_sum = next_sum;
        // Here is where we redwind to the previous position, then step up 
        // up one value and save the current offset. 
        fseek(input, offset, SEEK_SET); 
        fscanf(input, "%*d");
        offset = ftell(input);
    }

    fprintf(stdout, "\nTotal window-sum increases:\t%d", counter);

    return 0;
}