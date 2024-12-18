public class hierinheritance {
    public static void main(String[] args) {
        child1 c1 = new child1();
        child2 c2 = new child2();
        c1.bike();
        c1.car();
        c2.scooter();
        c2.car();
    }
    
}
class parent{
    void car(){
        System.out.println("Car");
    }
}
class child1 extends parent{
    void bike(){
        System.out.println("bike");
    }
}
class child2 extends parent{
    void scooter(){
        System.out.println("Scooter");
    }
}