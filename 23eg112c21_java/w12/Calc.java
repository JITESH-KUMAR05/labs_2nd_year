import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Calc extends JFrame implements ActionListener {
    JFrame frame;
    JTextField display;
    String operator = "";
    double num1 = 0, num2 = 0, result = 0;

    public Calc() {
        frame = new JFrame("Calculator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 600);
        frame.setLayout(new BorderLayout());

        display = new JTextField();
        display.setFont(new Font("Arial", Font.PLAIN, 40));
        display.setEditable(false);
        frame.add(display, BorderLayout.NORTH);

        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(5, 4, 10, 10));

        String[] buttons = {
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C"
        };

        for (String text : buttons) {
            JButton button = new JButton(text);
            button.setFont(new Font("Arial", Font.PLAIN, 30));
            button.addActionListener(this);
            panel.add(button);
        }

        frame.add(panel, BorderLayout.CENTER);
        frame.setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        String command = e.getActionCommand();

        if ((command.charAt(0) >= '0' && command.charAt(0) <= '9') || command.equals(".")) {
            display.setText(display.getText() + command);
        } else if (command.equals("C")) {
            display.setText("");
            num1 = num2 = result = 0;
            operator = "";
        } else if (command.equals("=")) {
            num2 = Double.parseDouble(display.getText());
            switch (operator) {
                case "+":
                    result = num1 + num2;
                    break;
                case "-":
                    result = num1 - num2;
                    break;
                case "*":
                    result = num1 * num2;
                    break;
                case "/":
                    result = num1 / num2;
                    break;
            }
            display.setText(String.valueOf(result));
            operator = "";
        } else {
            if (!operator.equals("")) {
                return;
            }
            num1 = Double.parseDouble(display.getText());
            operator = command;
            display.setText("");
        }
    }

    public static void main(String[] args) {
        new Calc();
    }
}