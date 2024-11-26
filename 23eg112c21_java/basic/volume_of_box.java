public class volume_of_box {
    public static void main(String[] args) {
        Box b1 = new Box();
        b1.setData(2, 4, 8);
        double v = b1.getVolume();
        System.out.println("Volume is: "+v);
    }
}
class Box{
    double l,b,h;
    void setData(double  x,double y,double z){
        l = x;
        b = y;
        h = z;

    }
    double getVolume(){
        return l*b*h;
    }
}
