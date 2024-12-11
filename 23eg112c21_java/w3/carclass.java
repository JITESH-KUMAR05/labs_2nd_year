public class carclass {
    public static void main(String[] args) {
        car obj = new car("creta",2023,2000000,"White","Hyundai");
        obj.display();
        
    }
}
class car{
    String name;
    int modelno;
    float price;
    String color;
    String company;

    car(String name,int modelno,float price,String color,String company){
        this.name = name;
        this.modelno = modelno;
        this.price = price;
        this.color = color;
        this.company = company;
    }

    void display(){
        System.out.println("Car name : " + this.name + "\ncar model number: " + this.modelno + "\nPrice: " + this.price + "\ncolor: " + this.color + "\nCompany: " + this.company);
    }
}
