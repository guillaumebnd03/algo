#ifndef includes.h
#define includes.h
#include <unistd.h>
#include <stdlib.h> 
#include <stdio.h>

void gd_putsre (char str);

void gd_putstr(char *str);
// int gd_strlen(char *str);
int gd_atoi(char *str);

typedef struct my_struct{
    int minutes;
    int hours;
}   type_struct;

typedef struct my_lst {
    int nbr;
    struct my_lst *next;
}   type_lst;

#endif