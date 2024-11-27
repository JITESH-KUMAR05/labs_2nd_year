public class amstrong {
    public static void main(String[] args) {
        int n = 371;
        int tmp = n;
        int ams = 0;
        while (tmp > 0) {
            int digit = tmp % 10;
            ams = (ams ) + (digit * digit * digit);
            tmp = tmp / 10;
            
        }
        if(ams == n){
            System.out.println("amstrong");
        }
        else{
            System.out.println("Not amstrong");
        }
    }
}
