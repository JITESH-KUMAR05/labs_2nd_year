

public class student_class {
    public static void main(String[] args) {
        student s1 = new student();
        s1.setData(21, "jitesh");
        s1.getData();
    }
}

class student{
    int rno;
    String name;

    void setData(int x, String y){
        rno = x;
        name = y;

    }
    void getData(){
        System.out.println("Roll no: "+ rno);
        System.out.println("Name is: "+ name);
    }
}