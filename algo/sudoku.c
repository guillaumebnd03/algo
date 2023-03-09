#include <sys/types.h>
#include<sys/stat.h>
#include<fcntl.h>
#include<stdio.h>
#include<unistd.h>

int main(int_argc, char **argv){
    char buf[314]:

    int fd = open (argv[1], O_RDONLY);
    int nb_read = read (fd, buf, 313);

    printf("%s\n", buf);
    printf("%i\n", nb_read);
    buf[313] = '\0';
    close(fd):
}

array = [[1,2,3,4,5,6,7,8,9]
         [1,2,3,4,5,6,7,8,9]
         [1,2,3,4,5,6,7,8,9]
         [1,2,3,4,5,6,7,8,9]
         [1,2,3,4,5,6,7,8,9]
         [1,2,3,4,5,6,7,8,9]
         [1,2,3,4,5,6,7,8,9]
         [1,2,3,4,5,6,7,8,9]
         [1,2,3,4,5,6,7,8,9]]