import java.util.*;

public class m2 {
    public static void main(String[] args) {
        LinkedList<Integer> ll = new LinkedList<Integer>();
        ll.add(1);
        ll.add(2);
        ll.add(3);
        // ll.add(2,6);
        System.out.println(ll);
        LinkedList<Integer> ll2 = new LinkedList<Integer>();
        ll2.add(4);
        ll2.add(5);
        ll2.add(6);
        ll.addAll(ll2);
        System.out.println(ll);
        ll.addFirst(0);
        ll.addLast(7);
        System.out.println(ll);
        ll.remove(1);
        System.out.println(ll);
        ll.add(1,8);
        ll.add(2,9);
        System.out.println(ll);
        ll.remove(Integer.valueOf(9));
        System.out.println(ll);
    }
    
}