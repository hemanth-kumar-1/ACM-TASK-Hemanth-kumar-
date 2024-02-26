# Approaching to challenges
## LEVEL -0
connecting to the host using ssh command, with given username and password.

use ls command to see the files in it.
use cat command to open the file.

## LEVEL -1
use ls to see the files in it. we will se a dash file in it.

To open the dash file use "cat < -" command 

## LEVEL -2
use ls command to see files in it.we will see a file with name spaces in this file.

To open cat 'spaces in this file' 

## LEVEL -3
After moving to the directory inhere.

There will be a hidden file to open it use 'ls -a' command

password = 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

## LEVEL -4
use file./* to see which are the files that are readable.we see file07 is readable.

use cat./-file07 to see content.

password = lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

## LEVEL -5
use find command to search file with 1033 bytes size."find -size 1033c"

c for to check in bytes

passwword = P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU

## LEVEL -6
use find command :- "find / -user bandit7 -group bandit6 -size 33c"

wee will see list of files, most of them are permission denied and one file can be opened.

copy the path use cat command to open it.

password = z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

## LEVEL -7
we use combination of two commands.That are cat and grep.

cat data.txt | grep millionth

password = TESKZC0XvTetK0S9xNwm25STk5iWrBvP

## LEVEL -8
we use uniq command to solve.To use uniq command the checked lines should be adjacent.

uniq -u gives the uniq line in the series.

sort data.txt | uniq -u is the command.

password = EN632PlfYiZbn3PhVK3XOGSlNInNE00t

## LEVEL -9
We use strings command to check out the readable messages in the file.

password = G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s

## LEVEL -10
The given file is a base64 encrypted one.To decrypt it we use base64 -d.

cat data.txt | base64 -d is the command.

output = The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM

password = 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM

## LEVEL -11
The given text is a shift cipher with key 13.After decoding

output = The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv

password = JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv

## LEVEL -12
After creating a temporary working directory.

we should decompress the file many times. It gives zip(.gz),bzip(.bz2),tar(.tar)files.

we need to change the extensions int them to decompress using mv command.

output = The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw

password = wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw

## LEVEL -13
There wil be a file with key in the file store the key in a file.

now connect to level14,with using the key.

sudo ssh -p 2220 -i bandit14 bandit14@bandit.labs.overthewire.org

## LEVEL -14
After connecting to server.open the file by using the given path with cat command.

we will see a temp key that has to be submitted.

now submit the temp key to the server by using "nc" command(nc -v localhost 30000)

password = jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
