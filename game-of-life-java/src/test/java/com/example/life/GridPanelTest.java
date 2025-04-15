package com.example.life;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class GridPanelTest {
    private GridPanel gridPanel;

    @BeforeEach
    public void setUp() {
        gridPanel = new GridPanel();
        gridPanel.loadPreset(Preset.BLANK);
    }

    @Test
    public void testRandomPresetCreatesSomeLiveCells() {
        gridPanel.loadPreset(Preset.RANDOM);
        int count = 0;
        for (int r = 0; r < GridPanel.ROWS; r++) {
            for (int c = 0; c < GridPanel.COLS; c++) {
                if (gridPanel.getCell(r, c)) {
                    count++;
                }
            }
        }
        assertTrue(count > 0, "Random preset should create some live cells");
    }

    @Test
    public void testClearGrid() {
        gridPanel.loadPreset(Preset.RANDOM);
        gridPanel.loadPreset(Preset.BLANK);

        for (int row = 0; row < GridPanel.ROWS; row++) {
            for (int col = 0; col < GridPanel.COLS; col++) {
                assertFalse(gridPanel.getCell(row, col));
            }
        }
    }

    @Test
    public void testBlinkerOscillation() {

        // Load blinker at (20, 20)
        gridPanel.loadPreset(Preset.BLINKER);

        // Capture initial state
        boolean[][] initial = getGridSnapshot(gridPanel);

        // Advance one step
        gridPanel.step();
        boolean[][] afterStep = getGridSnapshot(gridPanel);

        // Advance another step (should return to original state)
        gridPanel.step();
        boolean[][] afterTwoSteps = getGridSnapshot(gridPanel);

        // Check if first and second snapshots differ
        assertFalse(gridsEqual(initial, afterStep), "Grid should change after one step");

        // Check if original and after two steps are the same
        assertTrue(gridsEqual(initial, afterTwoSteps), "Blinker should return to original state after two steps");
    }

    @Test
    public void testIsCellAliveAfterManualSet() {
        gridPanel.loadPreset(Preset.BLANK);
        assertFalse(gridPanel.getCell(10, 10));
        gridPanel.step(); // should do nothing
        assertFalse(gridPanel.getCell(10, 10));
    }

    @Test
    public void testCellSurvivesWithTwoOrThreeNeighbors() {
        // Setup: Alive center with two neighbors
        setAlive(10, 10);
        setAlive(10, 11);
        setAlive(11, 10);

        gridPanel.step();

        assertTrue(gridPanel.getCell(10, 10), "Cell with 2 neighbors should survive");
    }

    @Test
    public void testCellDiesWithFewerThanTwoNeighbors() {
        setAlive(5, 5); // Lone cell

        gridPanel.step();

        assertFalse(gridPanel.getCell(5, 5), "Cell with fewer than 2 neighbors should die");
    }

    @Test
    public void testCellDiesWithMoreThanThreeNeighbors() {
        setAlive(8, 8);
        setAlive(8, 9);
        setAlive(9, 8);
        setAlive(9, 9);
        setAlive(7, 8); // 5 neighbors

        gridPanel.step();

        assertFalse(gridPanel.getCell(8, 8), "Cell with more than 3 neighbors should die");
    }

    @Test
    public void testDeadCellBecomesAliveWithThreeNeighbors() {
        setAlive(15, 15);
        setAlive(15, 16);
        setAlive(16, 15);

        gridPanel.step();

        assertTrue(gridPanel.getCell(16, 16), "Dead cell with 3 neighbors should become alive");
    }

    @Test
    public void testEdgeWrappingWorks() {
        setAlive(0, 0);
        setAlive(0, GridPanel.COLS - 1);
        setAlive(GridPanel.ROWS - 1, 0);

        gridPanel.step();

        assertTrue(gridPanel.getCell(GridPanel.ROWS - 1, GridPanel.COLS - 1),
                "Edge wrapping should cause corner cell to become alive");
    }

    private boolean[][] getGridSnapshot(GridPanel grid) {
        boolean[][] snapshot = new boolean[GridPanel.ROWS][GridPanel.COLS];
        for (int row = 0; row < GridPanel.ROWS; row++) {
            for (int col = 0; col < GridPanel.COLS; col++) {
                snapshot[row][col] = grid.getCell(row, col);
            }
        }
        return snapshot;
    }

    private boolean gridsEqual(boolean[][] a, boolean[][] b) {
        for (int i = 0; i < GridPanel.ROWS; i++) {
            for (int j = 0; j < GridPanel.COLS; j++) {
                if (a[i][j] != b[i][j])
                    return false;
            }
        }
        return true;
    }

    private void setAlive(int row, int col) {
        gridPanel.setCell(row, col);
    }
}
