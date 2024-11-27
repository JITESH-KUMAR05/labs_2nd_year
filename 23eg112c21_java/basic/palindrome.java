public class palindrome {
    public static void main(String [] args){
        int n = 125;
        int rev = 0;
        int tmp = n;
        while(tmp > 0){
            int digit = tmp % 10;
            rev = (rev * 10) + digit;
            tmp = tmp/10;
        }
        if(rev == n){
            System.out.println("Palindrome");
        }
        else{
            System.out.println("Not Palindrome");
        }
    }
}
