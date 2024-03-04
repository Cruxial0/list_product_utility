A simple utility to create products of lists using the user's clipboard.
Created as a utility for [Stable Diffusion Wildcards](https://github.com/AUTOMATIC1111/stable-diffusion-webui-wildcards)

## Running
1. Install the python requirements
```
pip install -r requirements.txt
```
2. Run the code with valid input (check [Explanation](#explanation) for more info)
```
python main.py
```
3. Assuming all went well, your output is now in your clipboard. Paste it somewhere to check!

## Explanation

This utility takes the data from the user's clipboard, finds all the unique entries of that list, then outputs a comma- and newline seperated list containing all combinations of the unique values. It then does some minor refactoring, and outputs the result into the user's clipboard

### Procedure
Input data is extracted from clipboard:
```
1900s, 1910s
1920s
1930s, 1910s
1940s
```
Data is parsed, and duplicate values are disposed:
```
1900s
1910s
1920s
1930s
1940s
```
The product is created, and values are sorted according to amount of items in each line (symbolised by commas). Then finally the output is copied to clipboard.
```
1900s
1910s
1920s
1930s
1940s
1900s, 1910s
1910s, 1920s
1920s, 1930s
1930s, 1940s
1900s, 1910s, 1920s
1910s, 1920s, 1930s
1920s, 1930s, 1940s
1900s, 1910s, 1920s, 1930s
1910s, 1920s, 1930s, 1940s
1900s, 1910s, 1920s, 1930s, 1940s
```