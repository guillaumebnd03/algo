int loop(int max_int) {
    int i;

    i = 0;
    while (max_int > 0) {
        i = i + 2;
        max_int --;
    }
    return(i);
}

int main(void) {
    int my_return;

    my_return = loop(15);
    return(my_return);
}