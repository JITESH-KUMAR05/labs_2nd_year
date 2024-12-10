public class staticKeyword {
    static int totalStu = 0;
    String name;
    float marks;

    public staticKeyword(String name , float marks) {
        this.name = name;
        this.marks = marks;
        totalStu++;
    }
    void display(){
        System.out.println("Name: "+ this.name + "\nmarks: "+ this.marks);
    }

    public static void main(String[] args) {
        staticKeyword s1 = new staticKeyword("jk", 93);
        staticKeyword s2 = new staticKeyword("mec", 91);
        s1.display();
        s2.display();
        System.out.println("Total Stu: " + staticKeyword.totalStu);
    }

    
}
