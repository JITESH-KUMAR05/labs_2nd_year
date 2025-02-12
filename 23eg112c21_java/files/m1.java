import java.io.*;
public class m1 {
    public static void main(String[] args) {
        try{
            File f1 = new File("file1.txt");
            String str = "Hello this is jitesh and i am tesing this program";
            FileWriter fw = new FileWriter(f1);
            fw.write(str);
            fw.close();
        }catch(IOException e){
            System.out.println(e);
        }
    }
        }
