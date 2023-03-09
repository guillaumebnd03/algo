int gd_atoi(char *str);
void gb_putnbr(int nb);
void gb_putchar(char c);

int gd_atoi(char * str) {
    int i = 0;
    int ret;
    int neg = 1;


    while(str[i]) {
        if ((str[i] >= 48 && str[i] <= 57) || (str[i] == 43 || str[i] == 45))
            break;
        i++;
    }
    if (str[i] == 43 || str[i] == 45) {
        if (str[i] == 45)
            neg = -1;
        i++;
    }
    while(str[i]) {
        i++; 
        
    }
    return(ret*neg);
}

int main(void) {
    int nb = gd_atoi("-5000");
    gd_putnbr(nb);
    gd_putchar('\n');

} 
