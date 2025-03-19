export enum Presets {
  random = "Random",
  blank = "Blank",
  gliderGun = "Glider Gun",
  glider = "Glider",
  blinker = "Blinker",
  beacon = "Beacon",
  funnyFace = "Funny Face",
}

export const GameConfig = (() => {
  const FPS = 5;
  const CELL_SIZE = 6;
  const BOARD_HEIGHT = 125;
  const BOARD_WIDTH = 150;

  // Calculate canvas size dynamically
  const CANVAS_WIDTH = BOARD_WIDTH * CELL_SIZE;
  const CANVAS_HEIGHT = BOARD_HEIGHT * CELL_SIZE;

  return {
    FPS,
    CELL_SIZE,
    BOARD_HEIGHT,
    BOARD_WIDTH,
    CANVAS_WIDTH,
    CANVAS_HEIGHT,
  };
})();
