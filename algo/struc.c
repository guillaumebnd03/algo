#include <includes.h>

int main(void) {
    type_lst *lst;
    type_lst *lst2;

    lst = (type_lst *)malloc(sizeof(lst));
    lst2 = (type_lst *)malloc(sizeof(lst2));
    lst2->nbr = 2;
    lst->nbr = 1;
    lst->next = lst2;
    lst2->next = NULL;
    while(lst) {
        printf("le nbr = %i\n", lst->nbr);
        lst = lst->next;
    }
    printf("le nbr = %i\n", lst->nbr);
}