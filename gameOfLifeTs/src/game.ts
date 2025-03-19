import { Board } from "./board";
import { GameConfig, Presets } from "./constants";

export class Game {
  private board: Board;
  private ctx: CanvasRenderingContext2D;
  private prevUpdateTime: number;
  private fps: number;
  private pause: boolean = false;
  private advanceOneStep: boolean = false;

  constructor(ctx: CanvasRenderingContext2D) {
    this.ctx = ctx;
    this.ctx.fillStyle = "black";
    this.prevUpdateTime = new Date().getTime();
    this.fps = GameConfig.FPS;
    this.board = new Board();
    this.board.draw(ctx);
  }

  private render(): void {
    let currentTime = new Date().getTime();
    if ((currentTime - this.prevUpdateTime) / 1000 > 1 / this.fps) {
      this.prevUpdateTime = currentTime;

      if (!this.pause) {
        this.board.update();
      } else if (this.advanceOneStep) {
        this.board.update();
        this.advanceOneStep = false;
      }

      this.board.draw(this.ctx);
    }

    requestAnimationFrame(() => {
      this.render();
    });
  }

  private togglePlayPause() {
    this.pause = !this.pause;

    const playPauseButton = document.getElementById("pauseBtn")!;
    if (this.pause) {
      playPauseButton.innerHTML = "Play";
    } else {
      playPauseButton.innerHTML = "Pause";
    }
  }

  run(): void {
    const dropdownButton = document.getElementById("dropdownBtn")!;
    const dropdownContent = document.getElementById("dropdownContent")!;

    Object.entries(Presets).forEach(([key, value]) => {
      const option = document.createElement("a");
      option.innerHTML = value;
      option.href = "#";
      (option as HTMLAnchorElement).setAttribute("data-value", key);
      dropdownContent.appendChild(option);
    });

    dropdownButton.addEventListener("click", () => {
      dropdownContent.style.display =
        dropdownContent.style.display === "block" ? "none" : "block";
    });

    dropdownContent.addEventListener("click", (event) => {
      if (event.target && (event.target as HTMLInputElement).tagName === "A") {
        const selectedKey = (event.target as HTMLInputElement).dataset.value;
        const selectedText = (event.target as HTMLInputElement).textContent;

        dropdownButton.textContent = `Preset: ${selectedText}`;

        if (selectedKey && selectedKey in Presets)
          this.board.loadPreset(Presets[selectedKey as keyof typeof Presets]);

        dropdownContent.style.display = "none";
      }
    });

    document.addEventListener("click", function (event) {
      if (
        !event.target ||
        !dropdownButton.contains(event.target as HTMLInputElement)
      ) {
        dropdownContent.style.display = "none";
      }
    });

    const playPauseButton = document.getElementById("pauseBtn")!;
    playPauseButton.addEventListener("click", () => {
      this.togglePlayPause();
    });
    const stepButton = document.getElementById("stepBtn")!;
    stepButton.addEventListener("click", () => {
      this.advanceOneStep = true;
    });

    document.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        this.togglePlayPause();
      } else if (e.key === "ArrowRight") {
        this.advanceOneStep = true;
      }
    });

    const canvas = document.getElementById("canvas") as HTMLCanvasElement;
    canvas.addEventListener("mousedown", (e) =>
      this.board.onMouseDown(e, canvas)
    );
    canvas.addEventListener("mousemove", (e) =>
      this.board.onMouseMove(e, canvas)
    );

    requestAnimationFrame(() => {
      this.render();
    });
  }
}
