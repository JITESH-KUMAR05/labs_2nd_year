public class m2 {
    public static void main(String[] args) {
        A a = new A();
        a.start();
        System.out.println("A Priority " + a.getPriority());
        System.out.println("Max Priority Thread : " + a.MAX_PRIORITY);
        System.out.println("A Priority " + a.getPriority());
        a.setPriority(10);
        System.out.println("A Priority " + a.getPriority());

        A b = new A();
        b.start();
        System.out.println("b Priority " + b.getPriority());
        System.out.println("MIN Priority Thread : " + a.MIN_PRIORITY);
        System.out.println("b Priority " + b.getPriority());
        b.setPriority(6);
        System.out.println("b Priority " + b.getPriority());

        A c = new A();
        c.start();
        System.out.println("c Priority " + c.getPriority());
        System.out.println("NORM Priority Thread : " + a.NORM_PRIORITY);
        System.out.println("c Priority " + c.getPriority());
        c.setPriority(2);
        System.out.println("c Priority " + c.getPriority());
        
    }
}
class A extends Thread{
    public void run(){
        System.out.println("Thread is Runnning...");
        System.out.println(Thread.currentThread().getName());
    }
}