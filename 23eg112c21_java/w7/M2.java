class CustomException extends Exception {
    public CustomException(String message) {
        super(message);
    }
}

public class M2 {
    public static void main(String[] args) {
        try {
            checkValue(5);
            checkValue(15);
        } catch (CustomException e) {
            System.out.println("Caught an exception: " + e.getMessage());
        }
    }

    public static void checkValue(int value) throws CustomException {
        if (value > 10) {
            throw new CustomException("Value is greater than 10");
        } else {
            System.out.println("Value is acceptable: " + value);
        }
    }
} 