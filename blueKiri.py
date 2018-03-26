# -*- coding: utf-8 -*-
# Python 3.5+ support only
# Author: BlueM1ST
# Version: 0.6
# Purpose: an easier way to work with kirikiri scripts and files (most suitable for: translations)

import subprocess


def main():
    print('==========================================================================================================\n'
          'BlueKiri Kirikiri2 Visual Novel Engine Tool\n'
          'Meant to simplify some common and not-so-common functions of working with Kirikiri files and scripts.\n'
          'xp3 file extracting and repacking provided by Phiber\'s tool: kikiriki\n'
          'All other tools developed by BlueM1ST\n'
          '==========================================================================================================')
    while True:
        print('\nFunctions:\n\n'
              'help     Display help\n'
              '1        Extract xp3 file\n'
              '2        Package file to xp3\n'
              '3        Text split\n'
              '4        Text reinsert\n'
              '5        TL read\n'
              '6        TL read reinsert\n'
              '7        Insert line-breaks'
              '')

        initialChoice = input('>')
        if initialChoice == 'help':
            # ToDo: write up some help mesage
            print('See the ReadMe that came with the program')
            continue

        try:
            initialChoice = int(initialChoice)
        except ValueError:
            print('Must chose a valid option')
            continue

        if initialChoice == 1:
            extractFile()
        elif initialChoice == 2:
            packageFile()
        elif initialChoice == 3:
            textSplit()
        elif initialChoice == 4:
            textReinsert()
        elif initialChoice == 5:
            tlRead()
        elif initialChoice == 6:
            tlReinsert()
        elif initialChoice == 7:
            insertLinebreaks()
        else:
            print('Must chose a valid option')
            continue

        continue


def insertLinebreaks():
    print('Maybe one day I will add this module here~')
    return


def tlReinsert():
    print('WARNING: both of these files must be encoded with utf-16-LE, like the originals were\n'
          'and if lines were added or removed, this script will not work')
    try:
        print('Enter the name of the mixed text file')
        textFilePath = input('>')
        print('Enter the name of the script file')
        scriptFilePath = input('>')
        textFile = open(textFilePath, 'r', encoding='utf_16_le')
        scriptFile = open(scriptFilePath, 'r', encoding='utf_16_le')

        textMemory = []
        for line in textFile:
            if line == '\n':
                continue
            textMemory.append(line)

        scriptMemory = []
        for line in scriptFile:
            scriptMemory.append(line)

        scriptFile.close()
        textFile.close()

        outputFile = open('krkr_output.ks', 'w', encoding='utf_16_le')
        count = 1
        for value in scriptMemory:
            if value == '$$\n':
                outputFile.write(textMemory[count])
                count += 2
                continue
            outputFile.write(value)

        print('==Text inserted Successfully===')


    except UnicodeDecodeError as a:
        print('Cannot decode file, the file must be encoded in:    utf-16-LE')
        tlReinsert()


def tlRead():
    print('WARNING: both of these files must be plaintext files (like .txt). If one version was written in MS Word\n'
          'or something like it, copy and paste the text into a plaintext file first')
    print('Enter the name of the Chinese text file (the one made with !textsplit)')
    chTextName = input('>')
    print('Enter the name of the English text file that you would like to match')
    enTextName = input('>')
    chText = open(chTextName, 'r', encoding='utf_16_le')
    chTextRead = chText.readlines()
    enText = open(enTextName, 'r', encoding='utf_16_le')
    enTextRead = enText.readlines()

    outputFile = open('krkr_text_mix_output.txt', 'w', encoding='utf_16_le')

    enMemory = []
    for line in enTextRead:
        if line == '\n':
            continue
        enMemory.append(line)

    chMemory = []
    for line in chTextRead:
        if line == '\n':
            continue
        chMemory.append(line)

    chText.close()
    enText.close()

    count = 0
    for value in chMemory:
        try:
            write = value + enMemory[count] + '\n'
            count += 1
            outputFile.write(write)
        except IndexError:
            outputFile.write(value + '\n')

    print('===Text mixed successfully===')



def textReinsert():
    print('WARNING: both of these files must be encoded with utf-16-LE, like the originals were\n'
          'and if lines were added or removed, this script will not work')
    try:
        print('Enter the name of the text file')
        textFilePath = input('>')
        print('Enter the name of the script file')
        scriptFilePath = input('>')
        textFile = open(textFilePath, 'r', encoding='utf_16_le')
        scriptFile = open(scriptFilePath, 'r', encoding='utf_16_le')

        textMemory = []
        for line in textFile:
            if line == '\n':
                continue
            textMemory.append(line)

        scriptMemory= []
        for line in scriptFile:
            scriptMemory.append(line)

        scriptFile.close()
        textFile.close()

        outputFile = open('krkr_output.ks', 'w', encoding='utf_16_le')
        count = 0
        for value in scriptMemory:
            if value == '$$\n':
                outputFile.write(textMemory[count])
                count += 1
                continue
            outputFile.write(value)

        print('==Text inserted Successfully===')


    except UnicodeDecodeError as a:
        print('Cannot decode file, the file must be encoded in:    utf-16-LE')
        textReinsert()


def textSplit():
    print('enter the path of the file to separate:')
    try:
        separateFile = input('Prompt: ')
        try:
            originalFile = open(separateFile, "r", encoding='utf_16_le')
            origLines = originalFile.readlines()
        except UnicodeDecodeError as u:
            print('here')
            originalFile = open(separateFile, "r", encoding='utf-8')
            origLines = originalFile.readlines()
            print('WARNING: selected file is encoded with UTF-8, Kirikiri only supports UTF-16-LE and all output files '
                  'will be encoded with UTF-16-LE')
        fileName = separateFile.split('.')
        textOutputFile = open(fileName[0] + '_text.txt', "w", encoding='utf_16_le')
        scriptOutputFile = open(fileName[0] + '_script.txt', "w", encoding='utf_16_le')
        print('=file read successfully=\n')

        for line in origLines:
            if line == '\n':
                scriptOutputFile.writelines('\n')
            elif (line.startswith('[') and 'namebox' not in line) or line.startswith(';') or line.startswith('var ') \
                    or line.startswith(']') or line == '\n' or '];' in line or line.startswith('ShowSelection(')\
                    or (line.startswith('\t') and '%' not in line) or line.startswith('{')\
                    or line.startswith('kag.') or line.startswith('//') or line.startswith('}') \
                    or line.startswith('for (') or line.startswith('global.') or line.startswith('*|'):
                print('-', end='')
                scriptOutputFile.writelines(line)
            else:
                print('*', end='')
                textOutputFile.writelines(line + '\n')
                scriptOutputFile.writelines('$$\n')

    # if file doesn't exist
    except FileNotFoundError as e:
        print('File not found\n')
        textSplit()

    # if can't decode the file; wrong encoding
    except UnicodeDecodeError as f:
        print('Cannot decode file, the file must be encoded in:    utf-16-LE')
        textSplit()


# Todo: kikiriki is not packaged right now, package it later
def packageFile():
    print('Enter the path of the file to package as an xp3')
    dataFile = input('>')
    print('Enter the path of the xp3 file (ex. patch.xp3)')
    outputFile = input('>')
    try:
        process = subprocess.Popen(['kikiriki.exe', "-c","-i", dataFile, "-o", outputFile], stderr=subprocess.PIPE)
        if process.stderr:
            print(process.stderr.readlines())
    except FileNotFoundError:
        print('Could not find kikiriki, please enter the full path of the executable, '
              'or type \'cancel\' to go back to the main menu')
        kikiriki = input('>')
        if kikiriki == 'cancel':
            main()
        try:
            process = subprocess.Popen([kikiriki, "-c", "-i", dataFile, "-o", outputFile], stderr=subprocess.PIPE)
            if process.stderr:
                print(process.stderr.readlines())
        except FileNotFoundError:
            print('Not found, going back to main menu\n\n')
            main()


# Todo: kikiriki is not packaged right now, package it later
def extractFile():
    print('Enter the path of the xp3 data/patch file')
    dataFile = input('>')
    print('Enter the path of the output file')
    outputFile = input('>')
    try:
        process = subprocess.Popen(['kikiriki.exe', "-i", dataFile, "-o", outputFile], stderr=subprocess.PIPE)
        if process.stderr:
            print(process.stderr.readlines())
    except FileNotFoundError:
        print('Could not find kikiriki, please enter the full path of the executable, '
              'or type \'cancel\' to go back to the main menu')
        kikiriki = input('>')
        if kikiriki == 'cancel':
            main()
        try:
            process = subprocess.Popen([kikiriki, "-i", dataFile, "-o", outputFile], stderr=subprocess.PIPE)
            if process.stderr:
                print(process.stderr.readlines())
        except FileNotFoundError:
            print('Not found, going back to main menu\n\n')
            main()

main()
