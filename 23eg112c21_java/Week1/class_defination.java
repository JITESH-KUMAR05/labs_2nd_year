public class class_defination{
    public static void main(String args[]){
        employee emp1 = new employee();
        emp1.setData("jitesh", 21, 10000);
        emp1.getData();
    }
}

class employee{
    String EmpName;
    int EmpId;
    double EmpSal;
    void setData(String name,int id,double sal){
        EmpName = name;
        EmpId = id;
        EmpSal = sal;

    }

    void getData(){
        System.out.println("The Employee name is "+EmpName);
        System.out.println("The employee id is "+ EmpId);
        System.out.println("The employee Salary is "+ EmpSal);
    }
}