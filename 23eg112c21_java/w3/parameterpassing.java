public class parameterpassing {
    public static void main(String args[]){
        // pass by value 
        swap_val sv = new swap_val(2, 1);
        System.out.println("Before Swaping");
        sv.display();
        System.out.println("After Swaping");
        sv.swap();
        sv.display();



        // pass by reference 
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
    void swap(){
        int temp;
        temp = this.a;
        this.a = this.b;
        this.b = temp;
    }
    void display(){
        System.out.println(this.a + "" + this.b);
    }
    
    
}
