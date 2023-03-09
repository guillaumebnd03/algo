function declare_lst_new(nbr)
    declar *lst_ret

    lst_ret = (type_lst *)malloc(sizeof(lst_ret))
    lst_ret->nbr = nbr
    lst_ret->next = NULL
    ret lst_ret

function looping(*lst, *lst_new)
    declar *lst_tmp

    lst_tmp = lst
    loop lst_tmp->next exist
        lst_tmp = lst_tmp->next
    lst_tmp->next = lst_new

function main
    declar *lst
    declar *lst_tmp

    array = {...}
    qsort
    array => array_sort

    lst = (type_lst *)malloc(sizeof(lst))
    lst->nbr = array[0]
    lst->next = NULL

    loop sur array i de 1->max_len
        lst_new = declare_lst_new(array[i])
        looping(lst, lst_new)
    
    loop lst
        lst_tmp = lst->next
        free(lst)
        lst = lst_tmp