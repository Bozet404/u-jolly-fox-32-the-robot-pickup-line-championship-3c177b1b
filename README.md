# The Robot Pickup Line Championship

My entry for the Robot Pickup Line Championship: a program that writes
one pickup line, in the voice of a robot, to `/output/entry.txt`.

## The line

A robot that spent the whole day scanning faces, and whose sensors
only overheated for one person — so it asks to become that person's
favourite system update. Robot vocabulary (scanning, sensors,
overheating, system update) carries the joke, and the line stays
charming instead of technical.

## How it works

`main.py` holds the line as a single string, checks it is one line of
1–200 characters, creates the output folder if it is missing, and
writes the line to `entry.txt` in UTF-8.

## Run it

```sh
python3 main.py
```

That writes `/output/entry.txt`. To test locally without touching the
system `/output` folder, set `OUTPUT_PATH`:

```sh
OUTPUT_PATH=./output/entry.txt python3 main.py
```

## Checks

- One line only, no line breaks inside it.
- 1–200 characters (this line is well inside the limit).
- UTF-8 plain text, nothing but the line.
