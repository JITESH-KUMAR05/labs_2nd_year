public class constructorUse {
    public static void main(String[] args) {
        emp e1 = new emp();
        e1.display();
        emp e2 = new emp(21,"jk");
        e2.display();

        
    }
    
}

class emp{
    int EmpId;
    String empName;
    static String company = "TCS";

    emp() {
        System.out.println("New Employee ");

    }

    emp(int EmpId, String empName) {
        this.EmpId = EmpId;
        this.empName = empName;
    }
    void display(){
        System.out.println("EmpId: " + EmpId + "\nEmpName: " + empName + "\nCompany: " + company);
        // System.out.println(company);
    }
    
    
}