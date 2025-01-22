public class multilevel {
    public static void main(String[] args) {
        child prashant = new child();
        prashant.scooter();
        prashant.bike();
        prashant.car();
        
    }
}

class grandparent{
    void car(){
        System.out.println("Car");
    }
}
class parent extends grandparent{
    void bike(){
        System.out.println("bike");
    }
}
class child extends parent{
    void scooter(){
        System.out.println("Scooter");
    }
}