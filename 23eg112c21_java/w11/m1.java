import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;

/*<applet code = "m1"
        width = "300"
        height = "400" >
        </applet> */

public class m1 extends Applet implements ActionListener {
    public void init(){
        Button b1 = new Button("Click Me");
        add(b1);
        b1.addActionListener(this);
        setLayout(new FlowLayout());
    }
    public void actionPerformed(ActionEvent e){
        setBackground(Color.red);
    }

    public void paint(Graphics g){
        g.drawString("IT-C", 100, 150);
    }
}