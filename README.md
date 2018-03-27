# BlueKiri
Kirikiri2 tools for translators.

BlueKiri is a tool to help translators work with Kirikiri2 files.

# What is Kirikiri?
It is widely used VN engine developed by W. Dee in 1998. Kirikiri2 was its successor with the last stable build being in 2010. It is now continued as KirikiriZ (which this tool will not work with, I assume)

# Features

Firstly, it supports easier use of Kikiriki (which I will not add to this repo). If you download it yourself, this tool will run it for you to extract and repack xp3 files.

The main feature of this tool is to separate the text from the script (code) and allow it to be easily re-added.

For example: if you are working on a translation, but don't want to look through the code while translating, this tool will strip it out so you can work with only the text. 
Once finished with the text, you can add it back into the code file using the tool.

But remember: all files that are to be run through Kirikiri2 must be encoded in UTF-16-LE. UTF-8 files will not work properly.

# TODO
- Automatically re-encode files that are not encoded properly.
- Add line-break support
- Make it easier to work with overall
