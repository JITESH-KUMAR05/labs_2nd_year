import java.awt.*;
import java.applet.Applet;
import java.awt.event.*;
/*<applet code="fact" width="400" height="300"></applet>*/
public class fact extends Applet implements ActionListener {
    TextField t ;
    TextField r;
    Button b;
    public void init(){
        t = new TextField(10);
        r = new TextField(10);
        b = new Button("Press me");
        
        add(t);
        add(r);
	add(b);
        r.setEditable(false);
        b.addActionListener(this);

    }
    public void actionPerformed(ActionEvent e){
        try{
            int num = Integer.parseInt(t.getText());
            r.setText(String.valueOf(factorial(num)));
        }catch(NumberFormatException exc){
            r.setText("Invalid Input!");
        }
    }
    public long factorial(int n){
        long f = 1;
        for(int i=1;i<=n;i++){
            f *= i;
        }
        return f;
    }
    
}
