
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
