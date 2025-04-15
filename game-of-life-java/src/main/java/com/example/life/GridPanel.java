package com.example.life;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class GridPanel extends JPanel {
    public static final int ROWS = 150;
    public static final int COLS = 280;
    public static final int CELL_SIZE = 5;

    private boolean[][] grid = new boolean[ROWS][COLS];
    private boolean isMouseDown = false;
    private int lastRow = -1;
    private int lastCol = -1;

    public GridPanel() {
        setPreferredSize(new Dimension(ROWS * CELL_SIZE, COLS * CELL_SIZE));

        loadRandom();

        addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                isMouseDown = true;
                int col = e.getX() / CELL_SIZE;
                int row = e.getY() / CELL_SIZE;
                drawLinesBetweenCells(row, col, row, col);
                lastRow = row;
                lastCol = col;
            }

            @Override
            public void mouseReleased(MouseEvent e) {
                isMouseDown = false;
                lastRow = -1;
                lastCol = -1;
            }
        });

        addMouseMotionListener(new MouseAdapter() {
            @Override
            public void mouseDragged(MouseEvent e) {
                if (isMouseDown) {
                    int col = e.getX() / CELL_SIZE;
                    int row = e.getY() / CELL_SIZE;

                    if (row != lastRow || col != lastCol) {
                        drawLinesBetweenCells(lastRow, lastCol, row, col);
                        lastRow = row;
                        lastCol = col;
                    }
                }
            }
        });
    }

    public boolean getCell(int row, int col) {
        return grid[row][col];
    }

    public void setCell(int row, int col) {
        grid[row][col] = true;
    }

    /**
     * Utilising Bresenham's line algorithm to interpolate cells between last
     * row/col and current row/col
     */
    private void drawLinesBetweenCells(int prevR, int prevC, int r, int c) {
        int dx = Math.abs(c - prevC);
        int dy = Math.abs(r - prevR);
        int sx = prevC < c ? 1 : -1;
        int sy = prevR < r ? 1 : -1;
        int err = dx - dy;

        int x = prevC, y = prevR;

        while (true) {
            if (x >= 0 && x < COLS && y >= 0 && y < ROWS) {
                grid[y][x] = true;
            }

            if (x == c && y == r)
                break;

            int e2 = 2 * err;
            if (e2 > -dy) {
                err -= dy;
                x += sx;
            }
            if (e2 < dx) {
                err += dx;
                y += sy;
            }
        }

        repaint();
    }

    public void step() {
        boolean[][] next = new boolean[ROWS][COLS];

        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                int neighbours = countLiveNeighbours(row, col);

                if (grid[row][col]) {
                    next[row][col] = neighbours == 2 || neighbours == 3;
                } else {
                    next[row][col] = neighbours == 3;
                }
            }
        }

        grid = next;
    }

    private int countLiveNeighbours(int row, int col) {
        int neighbourCount = 0;
        for (int dr = -1; dr <= 1; dr++) {
            for (int dc = -1; dc <= 1; dc++) {
                if (!(dc == 0 && dr == 0) && grid[(row + dr + ROWS) % ROWS][(col + dc + COLS) % COLS])
                    neighbourCount++;
            }
        }

        return neighbourCount;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                g.setColor(grid[row][col] ? Color.GREEN : Color.BLACK);
                g.fillRect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE);
                g.setColor(Color.DARK_GRAY);
                g.drawRect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE);
            }
        }
    }

    public void loadPreset(Preset preset) {
        clearGrid();

        switch (preset) {
        case RANDOM -> loadRandom();
        case BLINKER -> loadBlinker(20, 20);
        case BEACON -> loadBeacon(20, 20);
        case GLIDER -> loadGlider(20, 20);
        case GLIDER_GUN -> loadGliderGun(20, 20);
        case FUNNY_FACE -> loadFunnyFace(50, 50);
        case BLANK -> {
        }
        }

        repaint();
    }

    private void clearGrid() {
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                grid[row][col] = false;
            }
        }
    }

    private void loadRandom() {
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                grid[row][col] = Math.random() < 0.2;
            }
        }
    }

    private void loadBlinker(int row, int col) {
        boolean[][] blinker = { { false, false, false, false, false }, { false, false, true, false, false },
                { false, false, true, false, false }, { false, false, true, false, false },
                { false, false, false, false, false }, };

        for (int i = 0; i < blinker.length; i++) {
            for (int j = 0; j < blinker[0].length; j++) {
                grid[row + i][col + j] = blinker[i][j];
            }
        }
    }

    private void loadBeacon(int row, int col) {
        boolean[][] beacon = { { false, false, false, false, false, false }, { false, true, true, false, false, false },
                { false, true, false, false, false, false }, { false, false, false, false, true, false },
                { false, false, false, true, true, false }, { false, false, false, false, false, false }, };

        for (int i = 0; i < beacon.length; i++) {
            for (int j = 0; j < beacon[0].length; j++) {
                grid[row + i][col + j] = beacon[i][j];
            }
        }
    }

    private void loadGlider(int row, int col) {
        grid[row][col + 1] = true;
        grid[row + 1][col + 2] = true;
        grid[row + 2][col] = true;
        grid[row + 2][col + 1] = true;
        grid[row + 2][col + 2] = true;
    }

    private void loadGliderGun(int row, int col) {
        boolean[][] glider_gun = {
                { false, false, false, false, false, false, false, false, false, false, false, false, false, false,
                        false, false, false, false, false, false, false, false, false, false, false, true, false, false,
                        false, false, false, false, false, false, false, false, false, false, },
                { false, false, false, false, false, false, false, false, false, false, false, false, false, false,
                        false, false, false, false, false, false, false, false, false, true, false, true, false, false,
                        false, false, false, false, false, false, false, false, false, false, },
                { false, false, false, false, false, false, false, false, false, false, false, false, false, true, true,
                        false, false, false, false, false, false, true, true, false, false, false, false, false, false,
                        false, false, false, false, false, false, true, true, false, },
                { false, false, false, false, false, false, false, false, false, false, false, false, true, false,
                        false, false, true, false, false, false, false, true, true, false, false, false, false, false,
                        false, false, false, false, false, false, false, true, true, false, },
                { false, true, true, false, false, false, false, false, false, false, false, true, false, false, false,
                        false, false, true, false, false, false, true, true, false, false, false, false, false, false,
                        false, false, false, false, false, false, false, false, false, },
                { false, true, true, false, false, false, false, false, false, false, false, true, false, false, false,
                        true, false, true, true, false, false, false, false, true, false, true, false, false, false,
                        false, false, false, false, false, false, false, false, false, },
                { false, false, false, false, false, false, false, false, false, false, false, true, false, false,
                        false, false, false, true, false, false, false, false, false, false, false, true, false, false,
                        false, false, false, false, false, false, false, false, false, false, },
                { false, false, false, false, false, false, false, false, false, false, false, false, true, false,
                        false, false, true, false, false, false, false, false, false, false, false, false, false, false,
                        false, false, false, false, false, false, false, false, false, false, },
                { false, false, false, false, false, false, false, false, false, false, false, false, false, true, true,
                        false, false, false, false, false, false, false, false, false, false, false, false, false,
                        false, false, false, false, false, false, false, false, false, false, }, };

        for (int i = 0; i < glider_gun.length; i++) {
            for (int j = 0; j < glider_gun[0].length; j++) {
                grid[row + i][col + j] = glider_gun[i][j];
            }
        }
    }

    private void loadFunnyFace(int row, int col) {
        String funny_face = "5,1;5,2;5,3;5,7;5,8;5,9;1,5;2,5;3,5;7,5;8,5;9,5;6,2";

        String[] pairs = funny_face.split(";");

        for (String pair : pairs) {
            String[] parts = pair.split(",");

            if (parts.length != 2)
                continue;

            try {
                int c = col + Integer.parseInt(parts[0].trim());
                int r = row + Integer.parseInt(parts[1].trim());

                if (r >= 0 && r < ROWS && c >= 0 && c <= COLS) {
                    grid[r][c] = true;
                }
            } catch (NumberFormatException e) {
                System.err.println("Invalid cell coordinate: " + pair);
            }
        }
    }
}
