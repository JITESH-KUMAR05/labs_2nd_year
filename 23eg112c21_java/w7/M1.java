public class M1 {
    public static void main(String[] args) {
        try {
            M1.divide(10, 0);
        } catch (ArithmeticException e) {
            System.out.println("Caught an exception: " + e.getMessage());
        } finally {
            System.out.println("This is the finally block.");
        }
    }

    public static void divide(int a, int b) throws ArithmeticException {
        if (b == 0) {
            throw new ArithmeticException("Division by zero is not allowed.");
        } else {
            System.out.println("Result: " + a / b);
        }
    }
} 