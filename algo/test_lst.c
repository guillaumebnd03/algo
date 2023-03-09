int main(void) {
    int array_int[5] = {5,6,4,2,1};
    int i = 0;

    while (i < 5) {
        printf("%i\n", array_int[i]);
        i++;
    }
    

    while(lst) {
        printf("le nbr = %i\n", lst->nbr);
        lst = lst->next;
    }
}