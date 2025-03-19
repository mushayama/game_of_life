import { GameConfig, Presets } from "./constants";
import {
  getBeacon,
  getBlinker,
  getFunnyFace,
  getGlider,
  getGliderGun,
} from "./presets";

export class Board {
  private grid: boolean[][];
  private height: number;
  private width: number;
  private cellSize: number;
  private color: string;

  constructor() {
    this.cellSize = GameConfig.CELL_SIZE;
    this.height = GameConfig.BOARD_HEIGHT;
    this.width = GameConfig.BOARD_WIDTH;
    this.color = "green";
    this.grid = this.makeBoard(true);
  }

  private makeBoard(randomise: boolean = false): boolean[][] {
    let grid: boolean[][] = [];
    for (let i = 0; i < this.height; i++) {
      let row: boolean[] = [];
      for (let j = 0; j < this.width; j++) {
        if (randomise) {
          row.push(Math.floor(Math.random() * 2) === 1);
        } else {
          row.push(false);
        }
      }
      grid.push(row);
    }
    return grid;
  }

  private getNeighbourCount(x: number, y: number): number {
    let neighbourCount = 0;
    for (let delta_x = -1; delta_x < 2; delta_x++) {
      for (let delta_y = -1; delta_y < 2; delta_y++) {
        let nx = (x + delta_x + this.height) % this.height;
        let ny = (y + delta_y + this.width) % this.width;
        neighbourCount += Number(this.grid[nx][ny]);
      }
    }
    return neighbourCount - Number(this.grid[x][y]);
  }

  update(): void {
    let newGrid: boolean[][] = this.makeBoard();

    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        const neighbourCount = this.getNeighbourCount(i, j);
        if (this.grid[i][j] && neighbourCount >= 2 && neighbourCount <= 3) {
          newGrid[i][j] = true;
        }
        if (!this.grid[i][j] && neighbourCount === 3) {
          newGrid[i][j] = true;
        }
      }
    }

    this.grid = newGrid;
  }

  draw(ctx: CanvasRenderingContext2D): void {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        ctx.fillStyle = this.grid[i][j] ? this.color : "black";
        ctx.fillRect(
          this.cellSize * j,
          this.cellSize * i,
          this.cellSize,
          this.cellSize
        );
      }
    }

    ctx.strokeStyle = "lightgray";
    ctx.lineWidth = 0.2;
    for (let i = 0; i <= this.height; i++) {
      ctx.beginPath();
      ctx.moveTo(0, this.cellSize * i);
      ctx.lineTo(this.width * this.cellSize, this.cellSize * i);
      ctx.stroke();
    }

    for (let j = 0; j <= this.width; j++) {
      ctx.beginPath();
      ctx.moveTo(this.cellSize * j, 0);
      ctx.lineTo(this.cellSize * j, this.height * this.cellSize);
      ctx.stroke();
    }
  }

  loadPreset(preset: Presets): void {
    if (preset === Presets.random) {
      this.grid = this.makeBoard(true);
    } else if (preset === Presets.blank) {
      this.grid = this.makeBoard();
    } else if (preset === Presets.gliderGun) {
      const gliderGun = getGliderGun();
      this.grid = this.makeBoard();
      for (let i = 0; i < gliderGun.length; i++) {
        for (let j = 0; j < gliderGun[0].length; j++) {
          this.grid[i][j] = gliderGun[i][j] === 1;
        }
      }
    } else if (preset === Presets.glider) {
      const glider = getGlider();
      this.grid = this.makeBoard();
      for (let i = 0; i < glider.length; i++) {
        for (let j = 0; j < glider[0].length; j++) {
          this.grid[i][j] = glider[i][j];
        }
      }
    } else if (preset === Presets.beacon) {
      const beacon = getBeacon();
      this.grid = this.makeBoard();
      for (let i = 0; i < beacon.length; i++) {
        for (let j = 0; j < beacon[0].length; j++) {
          this.grid[i][j] = beacon[i][j];
        }
      }
    } else if (preset === Presets.blinker) {
      const blinker = getBlinker();
      this.grid = this.makeBoard();
      for (let i = 0; i < blinker.length; i++) {
        for (let j = 0; j < blinker[0].length; j++) {
          this.grid[i][j] = blinker[i][j];
        }
      }
    } else if (preset === Presets.funnyFace) {
      const funnyFace = getFunnyFace()
        .split(";")
        .map((x) => x.split(",").map((x) => Number(x)));
      this.grid = this.makeBoard();
      const xOffset = 50,
        yOffset = 25;
      for (let i = 0; i < funnyFace.length; i++) {
        this.grid[xOffset + funnyFace[i][1]][yOffset + funnyFace[i][0]] = true;
      }
    }
  }

  private setCell(x: number, y: number): void {
    if (x < this.width && y < this.height) {
      this.grid[y][x] = true;
    }
  }

  onMouseDown(event: MouseEvent, canvas: HTMLCanvasElement): void {
    this.setCell(
      Math.floor((event.offsetX * this.width) / canvas.width),
      Math.floor((event.offsetY * this.height) / canvas.height)
    );
  }

  onMouseMove(event: MouseEvent, canvas: HTMLCanvasElement): void {
    if (event.buttons != 1) return;
    this.setCell(
      Math.floor((event.offsetX * this.width) / canvas.width),
      Math.floor((event.offsetY * this.height) / canvas.height)
    );
  }
}
