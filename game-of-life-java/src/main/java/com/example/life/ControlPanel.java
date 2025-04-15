package com.example.life;

import javax.swing.*;
import java.awt.*;

public class ControlPanel extends JPanel {
    private final JButton playPauseButton;
    private final JButton stepButton;
    private final JComboBox<Preset> presetSelector;

    private final Timer timer;
    private final GridPanel gridPanel;

    private boolean isRunning = true;
    private Preset lastSelectedPreset;

    public ControlPanel(GridPanel gridPanel) {
        this.gridPanel = gridPanel;

        setLayout(new FlowLayout(FlowLayout.CENTER, 75, 10));

        playPauseButton = new JButton("Pause");
        stepButton = new JButton("Step");

        timer = new Timer(200, e -> {
            gridPanel.step();
            gridPanel.repaint();
        });
        timer.start();

        playPauseButton.addActionListener(e -> togglePlayPause());
        stepButton.addActionListener(e -> step());

        add(playPauseButton);
        add(stepButton);

        presetSelector = new JComboBox<>(Preset.values());
        presetSelector.setSelectedItem(Preset.RANDOM);
        lastSelectedPreset = Preset.RANDOM;
        presetSelector.addActionListener(e -> {
            Preset selected = (Preset) presetSelector.getSelectedItem();
            if (selected != lastSelectedPreset) {
                gridPanel.loadPreset(selected);
                lastSelectedPreset = selected;
            }
        });
        add(presetSelector);
    }

    public void togglePlayPause() {
        if (isRunning) {
            timer.stop();
            playPauseButton.setText("Play");
        } else {
            timer.start();
            playPauseButton.setText("Pause");
        }
        isRunning = !isRunning;
    }

    public void step() {
        if (!isRunning) {
            gridPanel.step();
            gridPanel.repaint();
        }
    }
}
