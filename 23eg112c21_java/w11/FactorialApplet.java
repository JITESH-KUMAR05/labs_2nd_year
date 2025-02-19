import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;
/*<applet code="FactorialApplet.class" width="300" height="150">
</applet>*/

public class FactorialApplet extends Applet implements ActionListener{
// Declare components

TextField t;
TextField r ;
Button b;

public void init() {
// Create components
t = new TextField(10);

r = new TextField(10);
b = new Button("Compute");

// Add components to the applet
add(t);
add(r);
add(b);

// Disable result field so it's not editable
r.setEditable(false);

// Action listener for the button
b.addActionListener(this);
}
public void actionPerformed(ActionEvent e) {
try {
// Parse the integer from inputField
int num = Integer.parseInt(t.getText());

// Compute and display the factorial
r.setText(String.valueOf(factorial(num)));
} catch (NumberFormatException ex) {
r.setText("Invalid Input");
}
}

// Method to calculate factorial
public long factorial(int n) {
long fact = 1;
for (int i = 1; i <= n; i++) {
fact *= i;
}
return fact;
}
}