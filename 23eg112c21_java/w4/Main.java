public class Main{
    public static void main(String[] args){
        methods obj = new methods();
        System.out.println(obj.add(1,2));
        System.out.println(obj.add(1,2,3));
    
    }
}
class methods{
    public int add(int a, int b){
        return a+b;
    }
    public int add(int a, int b, int c){
        return a+b+c;
    }
}