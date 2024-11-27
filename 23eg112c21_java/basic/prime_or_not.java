
public class prime_or_not {
    public static void main(String[] args) {
        int n = 25;
        int c = 0;
        int i;
        for (i = 1; i < n; i++) {
            if (n % i == 0) {
                c = c + 1;
            }
        }
        if (c == 1) {
            System.out.println("Prime");

        } else {
            System.out.println("Not Prime");
        }
    }
}