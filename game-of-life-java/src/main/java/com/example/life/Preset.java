package com.example.life;

public enum Preset {
    BLANK, RANDOM, BLINKER, BEACON, GLIDER, GLIDER_GUN, FUNNY_FACE;

    @Override
    public String toString() {
        return switch (this) {
        case BLANK -> "Blank";
        case RANDOM -> "Random";
        case BLINKER -> "Blinker";
        case BEACON -> "Beacon";
        case GLIDER -> "Glider";
        case GLIDER_GUN -> "Glider Gun";
        case FUNNY_FACE -> "Funny Face";
        };
    }
}
