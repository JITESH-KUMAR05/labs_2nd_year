<<<<<<< HEAD
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
=======

class Animal {
    
    void sound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
   
    void sound() {
        System.out.println("Dog barks");
    }
}

// Child class - Cat
class Cat extends Animal {
   
    void sound() {
        System.out.println("Cat meows");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal myAnimal = new Animal();
        myAnimal.sound(); 

        
        Animal myDog = new Dog();
        myDog.sound();

       
        Animal myCat = new Cat();
        myCat.sound(); 
    }
}
>>>>>>> f5b335f12c3b730644e9ec1df2b66468020efa05
