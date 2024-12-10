class stu {
    int rno;
    String name;
    float marks;

    stu(int x,String y, float z) {
        rno = x;
        name = y;
        marks = z;
    }
    stu(int x,String y){
        rno = x;
        name =  y;

    }
    void display(){
        System.out.println("Rno: " + rno + "\nname: " + name + "\nmarks: " + marks);
    }

}

class constructorOverloading{
    public static void main(String[] args) {
        stu s1 = new stu(10,"abc",2001);
        s1.display();
        stu s2 = new stu(21,"jks");
        s2.display();
        
        
    }
}
