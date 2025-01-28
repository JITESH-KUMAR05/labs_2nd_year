class addng extends Thread  {
    public void run(){
        System.out.println("Thread is running....");
    }    
}
class numbers extends Thread{
    public void run(){
        for(int i = 0;i<=5;i++){
            System.out.println(i);
        }
    }
}
class table implements Runnable{
    public void run(){
        int n = 5;
        for(int i = 1 ; i <= 10 ; i++){
            System.out.println(n + "  X  " + i + "  =  " + n*i);
        }
    }
}
public class m1{
    public static void main(String[] args) {
        System.out.println("Extending the Thread class");
        addng a = new addng();
        a.start();
        numbers n = new numbers();
        n.start();
        System.out.println("Using Runnable interface");
        table t = new table();
        Thread t1 = new Thread(t);
        t1.start();

    }
}