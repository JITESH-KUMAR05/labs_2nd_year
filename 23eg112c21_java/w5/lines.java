public class interfacesillu {
    public static void main(String[] args) {
        allLines l1 = new allLines();
        l1.drawline();
        l1.draw();
        l1.drawdotted();
    }
}

public class lines {
    void draw() {
        System.out.println("draw lines");
    }
}

interface dottedlines {
    void drawdotted();
}

class allLines extends lines implements dottedlines {
    public void drawline() {
        System.out.println("All Lines drawing");
    }

    public void drawdotted() {
        System.out.println("dotted lines");
    }
}