#include <unistd.h>

void gd_putchar(char c) {
    write(1, &c, 1);
}

int gd_putstr(char *str) {
}
int main(void) {
    int nb_put = gd_putstr("coucou");
    /*nb=put =6*/  
}