import java.util.*;
public class m1 {
    public static void main(String[] args) {
        LinkedList<String > ll = new LinkedList<String>();
        ll.add("hello");
        ll.add("hi");
        ll.add("bye");
        ll.add("teja");
        ll.add("jk");

        Iterator<String> itr = ll.iterator();
        while(itr.hasNext()){
            System.out.println(itr.next());
        }
        System.out.println(ll);
        ll.remove(1);
        System.out.println(ll);
        ll.remove("teja");
        System.out.println(ll);
    }
}