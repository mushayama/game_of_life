package com.example.life;

import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Game of Life");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(1400, 850);
            frame.setLayout(new BorderLayout());

            GridPanel gridPanel = new GridPanel();
            ControlPanel controlPanel = new ControlPanel(gridPanel);

            frame.add(gridPanel, BorderLayout.CENTER);
            frame.add(controlPanel, BorderLayout.SOUTH);

            frame.addKeyListener(new KeyAdapter() {
                @Override
                public void keyPressed(KeyEvent e) {
                    if (e.getKeyCode() == KeyEvent.VK_ENTER) {
                        controlPanel.togglePlayPause();
                    } else if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
                        controlPanel.step();
                    }
                }
            });

            frame.setFocusable(true);
            frame.setVisible(true);
        });
    }
}
