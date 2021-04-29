# Texture-Pack-Color-Visualizer

This was created to visualize the pack.mcmeta files without having to restart the game (it's apparently compiled while running the game, meaning you must restart the whole game in order to see the changes in the GUI). As restarting the game gets annoying, I've made this python script to display to you a colored string inside of the terminal. All color codes can be found online or in the main python file (the "possible" dictionary). I have included all known minecraft color codes up to this point.

# Installing And Running:
The only current requirement is Python 3
Installing Through Git:
```sh
git clone https://github.com/derpferpmerp/Texture-Pack-Color-Visualizer.git;cd "Texture-Pack-Color-Visualizer";python3 main.py
```
You can also either input after running the command (though python input) or supply the argument like this (although it doesn't like exclamation points):
```sh
python3 ./main.py "STRING"
```

# Notes:
I have not currently included bug protection, but if you break it the program just won't work, so do with the program what you want, but understand it will only actually work if you use color codes that are currently allowed. I also plan to make this accept an actual file in the future.
