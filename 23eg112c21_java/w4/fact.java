public class fact {
    public static void main(String[] args) {
        int fa = factorial(5);
        System.out.println(fa);
    }
    static int factorial(int n){
        if(n == 1 || n == 0){
            return 1;
        }
        return n * factorial(n-1);
    }
}