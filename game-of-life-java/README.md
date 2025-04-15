# Game of life: java implementation

makes use of java 17 and maven with junit 5 for testing

to run:

- make use of maven lifecycle commands
  - cleans the project
  ```bash
  mvn clean
  ```
  - compiles the source code
  ```bash
  mvn compile
  ```
  - runs tests
  ```bash
  mvn test
  ```
  - alternatively, the above three commands can be run together
  ```bash
  mvn clean compile test
  ```
  - runs the main project file
  ```bash
  mvn exec:java -Dexec.mainClass="com.example.life.Main"
  ```
- can also package into a jar file and run from that - to package into jar file:
  `bash
    mvn clean compile test package
    ` - to run jar file:
  `bash
    java -jar target/game-of-life-java-1.0-SNAPSHOT.jar
    `
  We can also build the project into an executable desktop app using something like launch4j or jpackage.

## packages/features utilised

- **maven**: A tool for building and managing any Java-based project. It aids in maintaining, compiling, testing and packaging your application.
- **junit**: unit testing framework in Java. We have utilised junit 5 here as it is the latest at this time.
- **swing**: GUI widget toolkit that is part of Oracle's Java Foundation Classes(JFC)
- **awt**: (Abstract Window Toolkit) A set of classes and interfaces in Java used for creating GUI. It's the foundation upon which Swing is built.
- **surefire plugin**: The Surefire Plugin is used during the maven test phase of the build lifecycle to execute the unit tests of an application. It generates reports in two different file formats Plain text files (.txt) XML files (.xml).

## TO-DO

I think this is done basically for now. however, should I ever want to tinker in the future then the following can be picked up:

- Add more functionalities to the toolbar?
  - make it possible to go back certain steps
  - add a reset config button to go back to initial preset?
- Decide on a preset storage format
- Add more presets
