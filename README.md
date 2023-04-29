# Artifact-Cruedy

Example code in my DSl are in the `files` folder which is inside of the `DSL Code` folder.

To run the parser, scroll to the bottom of `parser.py` to where the `parser()` function is called and change the input file *the first parameter* to the .txt file that you've written your code in and the output file *the second parameter* to the .jsx file that you want to output. In your terminal, make sure you're in the `DSL Code` folder and run `python parser.py`, and a .jsx file will be outputted. Go to `After Effects`, go to `file -> Scripts-> Run Script File` and select the .jsx that you just created to test your code.

The only library that I use in this parser is `matplotlib`. I used `colors` from `matplotlib` to create rgb values for a color, which is what is needed for `After Effects`.

In order to fully test this parser, and your code in Extended-ExtendScript, the user needs After Effects to run the resulting `.jsx` file in a video project.
