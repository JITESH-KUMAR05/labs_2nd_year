public class callbyref {
    public static void main(String args[]){
        // pass by value 
        swap_val sv = new swap_val(2, 1);
        System.out.println("Before Swaping");
        sv.display();
        System.out.println("After Swaping");
        sv.swap(2,1);
        // sv.display();


        System.out.println("now let's see with call by ref \n\n");
        // pass by reference 
        swap_ref sr = new swap_ref(2, 1);
        System.out.println("Before Swaping");
        sr.display();
        System.out.println("After Swaping");
        sr.swap(sr);
        sr.display();

    }
    
}

class swap_val{
    int a;
    int b;

    swap_val(int x,int y) {
        this.a = x;
        this.b = y;
        // swap(this.a,this.b);
    }
    void swap(int x,int y){
        int temp;
        temp = x;
        x = y;
        y = temp;
        System.out.println(x + " " + y);
    }
    void display(){
        System.out.println(this.a + " " + this.b);
    }
    
    
}

class swap_ref{
    int a,b;
    swap_ref(int x , int y){
        this.a = x;
        this.b = y;
    }
    void swap(swap_ref ref){
        int temp;
        temp = ref.a;
        ref.a = ref.b;
        ref.b = temp;

    }
    void display(){
        System.out.println(a + " " + b);
    }
}
