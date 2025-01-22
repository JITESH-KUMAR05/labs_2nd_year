public class singleinherit {
    public static void main(String[] args) {
        child v = new child();
        v.bike();
        v.scooter();
    }
    
}

class parent {
    void bike(){
        System.out.println("bike");
    }
}
class child extends parent{
    void scooter(){
        System.out.println("Scooter");
    }
}