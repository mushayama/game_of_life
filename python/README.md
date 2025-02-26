# Game of life: python implementation

to run:

- from game_of_life/python directory:
  - by main file outisde package:
    ```bash
    python3 main.py
    ```
  - running the game_of_life package:
    ```bash
    python3 -m game_of_life
    ```
    This is made possible my including a \_\_main\_\_.py file within the game_of_life package.

## packages utilised

- **pygame**: Cross-platform python library for writing 2d video-games. We use it to visualise game of life grid and cells.
- **mypy**: static type checker for python
  - to run it, run the following command in shell:
    ```bash
    mypy file1_outside_package.py file2_outside_package.py package_name
    ```
    this will check for the whole package package_name and also for the two files outside package. You can add or remove file names and package names as reuired in a similar manner.

## setup

- I have utilised pyenv and pyenv-virtualenv for managing python version and virtual envelope.
- python version used: 3.12.0

## Tidbits

- for CONSTANTS:
  - I am using a Singleton Configuration Manager along with frozen dataclasses and @property methods to calculate dependent values.
  - Perhaps in the future I will find a better way of handling constants but this works well for now.
- Project Structure:
  - Here I have gone for a bare project instead of an src and have forgone any subpackages. That might need to change should this grow much larger at somme point.

## TO-DO

I think this is done basically for now. however, should I ever want to tinker in the future then the following can be picked up:

- Add more functionalities to the toolbar?
  - make it possible to go back certain steps
  - add a reset config button to go back to initial preset?
- Decide on a preset storage format
- Add more presets
