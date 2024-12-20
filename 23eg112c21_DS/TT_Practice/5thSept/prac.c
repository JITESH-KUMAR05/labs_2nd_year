// #include<stdio.h>
// int main()
// {
// int arr[2] = {1, 2, 3, 4, 5};
// printf("%d", arr[3]);
// return 0;
// }

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// int main()
// {
    // char *p;
    // *p = (char)calloc(10);
    // strcpy(p, "HELLO");
    // printf("%s", p);
    // free(p);
    // return 0;

//     char ch[] = "0xC";
//     if (isxdigit(ch[ ]))
//         printf("ch = %s is hexadecimal character \n", ch);
//     else
//         printf("ch = %s is not hexadecimal character \n", ch);
// }

// #include <ctype.h>  

// int main() {  
//     char c = ' ';  
//     if (isspace(c)) {  
//         printf("The character is a whitespace.\n");  
//     }  
//     int iscntrl( int c);
//     return 0;  
// }


// #include<stdio.h>
// int main()
// {
// int i = 0;
// printf("Hello");
// char s[4] = {'\b', '\t', '\r', '\n'};
// for(i = 0;i<4;i++)
// {
// printf("%c", s[i]);
// }
// return 0;
// }

// #include<stdio.h>
// int main()
// {
// char s[] = {'a', 'b', 'c', '\n', 'c', '\0'};
// char *p, *str, *str1;
// p = &s[3];
// str = p;
// str1 = s;
// printf("%d", ++*p + ++*str1-32);
// return 0;
// }

#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char str[100], res[100];
    char vowels[] = "aeiouAEIOU";
    int j = 0;

    // Read the input string from the user
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    // Remove the newline character if present
    str[strcspn(str, "\n")] = '\0';

    // Iterate through each character of the input string
    for (int i = 0; i < strlen(str); i++) {
        int is_vowel = 0;

        // Check if the character is a vowel
        for (int k = 0; k < strlen(vowels); k++) {
            if (tolower(str[i]) == vowels[k]) {
                is_vowel = 1;
                break;
            }
        }

        // If the character is not a vowel, add it to the result string
        if (!is_vowel) {
            res[j++] = str[i];
        }
    }

    // Add a null terminator to the end of the result string
    res[j] = '\0';

    printf("String after removing vowels: %s\n", res);

    return 0;
}

// #include <stdio.h>

// int main() {
//     int N;

//     // Read the number of elements
//     printf("Enter the number of elements: ");
//     scanf("%d", &N);

//     int arr[N];

//     // Read the elements of the array
//     printf("Enter %d elements:\n", N);
//     for (int i = 0; i < N; i++) {
//         scanf("%d", &arr[i]);
//     }

//     // Replace even numbers with 0 and odd numbers with 1
//     for (int i = 0; i < N; i++) {
//         if (arr[i] % 2 == 0) {
//             arr[i] = 0;
//         } else {
//             arr[i] = 1;
//         }
//     }

//     // Print the resultant array
//     printf("Resultant array: ");
//     for (int i = 0; i < N; i++) {
//         printf("%d ", arr[i]);
//     }
//     printf("\n");

//     return 0;
// }