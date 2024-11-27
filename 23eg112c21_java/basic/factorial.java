public class factorial {
    static public void main(String args[]){
        int n = 3;
        int f = 1;
        for(int i=1;i<=n;i++){
            f = f * i;

        }
        System.err.println("Factorial of "+n+" is "+f);
    }
    
}