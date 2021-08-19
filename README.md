# Ellie D

El - ee - dee / LED getit?

Ellie D is an LED control system to power your strips of rainbow magic with an extensible set of effects called pixlets.

A pixlet is a small piece of code that describes the colour output of your LED strip. It runs abstracted from the lower level details of your display hardware like interface or strip length. This lets the effect author focus on a interesting idea that will adapt to run on whatever LED setup the user has.

Pixlets are supplied with some external parameters to drive their effects, these may vary depending on the type of pixlet you are implementing.

Ellie D variants of pixlets:

* Standard pixlets
* Audio pixlets

Standard pixlets are just basic time driven effects with little input from the outside world.

Audio pixlets provide lots of real-time data about an input source allowing for effects that react to parameters like BPM, beats, audio notes, etc.

## Input parameters

* Time
* Strip length

## Future Improvements

* Support 2D, 3D LED matrices
