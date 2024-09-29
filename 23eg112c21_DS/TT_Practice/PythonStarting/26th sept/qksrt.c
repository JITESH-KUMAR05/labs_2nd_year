#include <stdio.h>

// Function to check if there exists a subarray with exactly k elements greater than A[l]
int is_special(int A[], int n, int k, int l) {
    int count, i, j;
    for (i = 0; i < n; i++) {
        count = 0;
        for (j = i; j < n; j++) {
            if (A[j] > A[l]) {
                count++;
            }
            if (count == k) {
                return 1;
            }
        }
    }
    return 0;
}

int main() {
    int n, k;
    scanf("%d %d", &n, &k);

    int A[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &A[i]);
    }

    int specialty = 0;
    for (int l = 0; l < n; l++) {
        if (is_special(A, n, k, l)) {
            specialty += A[l];
        }
    }

    printf("%d\n", specialty);
    return 0;
}