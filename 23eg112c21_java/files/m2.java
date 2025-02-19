import java.io.*;
public class m2 {
    public static void main(String[] args) {
        FileInputStream source = null;
        FileOutputStream target = null;
        try {
            source = new FileInputStream("file1.txt");
            target = new FileOutputStream("file2.txt");
            char temp;
            while((temp = source.read(null)))
        } catch (Exception e) {
            // TODO: handle exception
        }
    }
    
}
