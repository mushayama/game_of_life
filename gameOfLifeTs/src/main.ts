import { GameConfig } from "./constants";
import { Game } from "./game";
import "./style.css";

function main() {
  const canvasElement = document.getElementById("canvas") as HTMLCanvasElement;
  canvasElement.width = GameConfig.CANVAS_WIDTH;
  canvasElement.height = GameConfig.CANVAS_HEIGHT;
  const ctx = canvasElement.getContext("2d");
  if (!ctx) return;

  const game = new Game(ctx);
  game.run();
}

main();
