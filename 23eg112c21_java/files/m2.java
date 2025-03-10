import java.io.*;
public class m2 {
    public static void main(String[] args) {
        FileInputStream source = null;
        FileOutputStream target = null;
        try {
            source = new FileInputStream("file1.txt");
            target = new FileOutputStream("file2.txt");
            int temp;
            while((temp = source.read()) != -1) {
                target.write(temp);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (source != null) source.close();
                if (target != null) target.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    
}
