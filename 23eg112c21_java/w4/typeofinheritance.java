// single inheritance

public class typeofinheritance {
    public static void main(String[] args) {
        human sam = new human();
        System.out.println(sam.hasheart);
        System.out.println(sam.ReqAir);
        sam.canEat();
        sam.canWalk();
        sam.CanTalk();
        
    }
}
abstract class livingBeing{
    final boolean hasheart = true;
    final boolean ReqAir = true;
    abstract boolean canWalk();
    abstract  boolean CanTalk();
    abstract boolean canEat();

}
class human extends livingBeing{
    boolean canWalk(){
        System.out.println(true);
        return true;
    }
    boolean CanTalk(){
        System.out.println(true);
        return true;

    }
    boolean canEat(){
        System.out.println(true);
        return true;
    }
}
