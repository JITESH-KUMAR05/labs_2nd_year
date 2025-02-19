import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;
/*<applet code="ButtonTest.class" width="300" height="150">
</applet>*/

public class ButtonTest extends Applet implements ActionListener {
// Declare components

public void init() {
// Create components

Button b = new Button("Click Me");

// Add components to the applet

add(b);

// Action listener for the button
b.addActionListener(this);
}
public void actionPerformed(ActionEvent e) {
    System.out.println("hai");
    setBackground(Color.red);

}
}