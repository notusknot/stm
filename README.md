# Simple theme manager
## _The best way to manage complex rices_


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

STM is a command-line tool for storing and easily switching between many different complex sets of configurations. 
It is easy to use and support any window manager or software you may use, as long as it has a configuration file.

- Built with python
- Blazing fast
- Easy to use and contribute

## How to install

### Dependencies:
- ```pip3``` to install the package
- ``` python3``` to run the code
- (Optional) ```git``` to clone the repository

### Instructions: 
- Clone this repository with ```git clone https://notusknot/stm``` or by downloading and extracting the .zip file
- Enter into the directory with ```cd stm```
- Type ```pip3 install . ``` to automatically install all the dependencies
- Done!

_Note: if you get an error saying stm is not in your PATH, be sure to add it to your PATH in your shell config file_
## How to use

In order to use stm, you must first declare create a new theme and add some paths to it. 
Stm works by creating sets of configuration files, then storing them and referencing them through stm. Once they are referenced, you can easily load them and all the files will be copied to their correct places and applied. 

The ```theme_name``` can be whatever you like and is used later to identify and load themes.
The ```file_destination``` is where you want your file to end up once it is loaded (i.e. /home/user/.config)
The ```file_location``` is where the current configuration file is (i.e. /home/user/themes/theme_name)

If you want to add more than one configuration, simply append more file destinations and locations at the end of the ```stm add``` command.
It is recommended, but not necessary, that you create a new directory to store all the configuration files for stm, just for oraganization's sake.
To create a new theme, follow these instructions:
- Type ```stm new theme_name file_destination:file_location```
- If you want to declare more themes, repeat step 1 until satisfied
- When you want to load your themes, simply type ```stm load theme_name```
- Reload your window manager to view the changes. Some applications may need to be restarted to view the changes.
    

## Development

Want to contribute? Great!

The project is made with Click to make development of the CLI more intuitive. If you want to contribute, feel free to modify the code on your own, make a pull request on GitHub, or contact me on Discord: ```notusknot#5622```

## License

MIT
The code is entirely free and open source, meaning you are able to modify or distribute the software to your desire.


