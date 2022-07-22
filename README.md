# Split Combiner

A simple tool for combining LiveSplit split files.

# Setup

Head to the Releases tab and download the latest release and unzip everything

Navigate to the "splits" folder. This folder will be where every split file that will be combined resides. Pay attention to the format of the filenames. The files currently in there represent some template splits from the 602 Multimario route, and will be combined in the order of the numbers at the beginning of the filename (1, 2, 3, 4). Anything beyond the number will be used for the Subsplit name (i.e `1 Super Mario 64` will generate a section with the name `Super Mario 64`).

![Split Files](https://user-images.githubusercontent.com/31007296/117376209-aa4a6480-ae9e-11eb-8735-f1e6911976d0.png)

Replace the files with splits of your choosing, navigate back to the initial folder, and run `main.exe`. If all goes well, the file `output.lss` will be generated and can be opened with LiveSplit.