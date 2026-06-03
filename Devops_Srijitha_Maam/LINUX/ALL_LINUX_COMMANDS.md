# Paste the Selected line in EC2 Instance
ctrl + shift + v

## Linax Command 
To Go Inside The Folder
<!-- cd frontand  -->
<!-- cd backand  -->
For Exits From Folder
<!-- cd .. -->

# Making
To Makes Files And Folder
<!-- mkdir frontand  -->
<!-- mkdir backand  -->

Verify
Shift:-  <!-- /home/ubuntu/backup/project -->
Check Files And Folder
 <!--- ls -->

 Check Hidden Files And Folder
 <!--- ls -a-->

# Copy

Copy a folder to another directory
<!-- cp -r source_folder destination_directory -->
<!-- cp -r project /home/ubuntu/docs/ -->

Copy and rename of folder to specific directory
<!-- cp -r project /home/ubuntu/document/project_backup -->

Copy folder to parent directory
<!-- cp -r backend ../  -->
<!-- cp -r frontend ../  -->
   
Copy and rename to parent directory
<!-- cp -r backend ../backend_copy  -->

Copy file to parent directory
<!-- cp docker-compose.yml ../   -->




# Moving

Move a folder to another directory
Sould be Present in Source_Folder 
<!-- mv source_folder destination_directory  -->
<!-- mv project /home/ubuntu/backup/  -->Check_By ls /home/ubuntu/backup/project or Shift /home/ubuntu/backup/
project

Move a file to another directory
<!-- mv source_files destination_directory  -->
<!-- mv file.txt /home/ubuntu/documents/ --> Check_By ls /home/ubuntu/documents/

Move multiple files at once
<!-- mv file1.txt file2.txt file3.txt /home/ubuntu/docs/  --> Check_By ls /home/ubuntu/docs/

Move & rename Folder and files at the same time
<!-- mv project project_old  -->
<!-- mv report.txt report_final.txt -->

Move folder to parent directory
<!-- mv backend ../ -->
<!-- mv frontend ../ -->

To Go Inside The Folder
<!-- cd frontand  -->
<!-- cd backend  -->

For Exits From Folder
<!-- cd .. -->


# Delete
Delete Files And Folder
<!-- rm filename -->
<!-- rm test.txt -->

Delete an empty folder
<!-- rmdir folder_name -->

Delete a folder (with files inside)
<!-- rm -r folder_name -->
<!-- rm -r project -->

Force delete (no confirmation)
<!-- rm -rf folder_name -->
<!-- rm -rf project -->


Delete folder of Parent directory
<!-- rm -r ../backend -->
<!-- rm -r ../frontend -->



Check Files and Folder 
<!-- ls -->


Check Hidden Files and Folder 
<!-- ls -a -->


# Rename folder to files
Method 1 – Rename One by One (Simple & Safe)
ebspod -> ebspod.yaml
ebspv  -> ebspv.yaml
ebspvc -> ebspvc.yaml
ebsvolume -> ebsvolume.yaml
Run:

```bash

mv ebspod ebspod.yaml
mv ebspv ebspv.yaml
mv ebspvc ebspvc.yaml
mv ebsvolume ebsvolume.yaml

```


# In Vim/Vi:

Press  to enter command mode
> Esc

Cut everything (gg = go to top, d = delete/cut, G = go to bottom)
> ggdG

Move & paste where you want
> p

# Complete Vim Command Reference

## Opening Files
Open a file
> vim filename

Open file at specific line
> vim +10 filename

Open multiple files
> vim file1 file2 file3

## Modes in Vim

Enter Normal mode (from any mode)
> Esc

Enter Insert mode (start typing)
> i

Enter Insert mode at end of line
> A

Enter Insert mode at beginning of line
> I

Enter Visual mode (select text)
> v

Enter Visual Line mode (select whole lines)
> V

Enter Command mode
> :

## Navigation

Go to top of file
> gg

Go to bottom of file
> G

Go to line 50
> :50

Move left
> h

Move down
> j

Move up
> k

Move right
> l

Move forward one word
> w

Move backward one word
> b

Move to end of line
> $

Move to beginning of line
> 0

Page down
> Ctrl + f

Page up
> Ctrl + b

## Selecting Text

Select all (go to top, visual line, go to bottom)
> ggVG

Select current line
> V

Select from cursor to end of line
> v$

Select from cursor to end of file
> vG

## Copy (Yank)

Copy current line
> yy

Copy all lines
> :%y

Copy 5 lines
> 5yy

Copy selected text (after visual selection)
> y

## Cut (Delete)

Cut current line
> dd

Cut all content
> ggdG

Cut 5 lines
> 5dd

Cut from cursor to end of line
> d$

Cut from cursor to end of file
> dG

Cut selected text (after visual selection)
> d

## Paste

Paste after cursor
> p

Paste before cursor
> P

## Undo & Redo

Undo
> u

Redo
> Ctrl + r

## Search

Search forward for "text"
> /text

Search backward for "text"
> ?text

Find next occurrence
> n

Find previous occurrence
> N

## Replace

Replace first occurrence in line
> :s/old/new

Replace all in line
> :s/old/new/g

Replace all in file
> :%s/old/new/g

Replace all with confirmation
> :%s/old/new/gc

## Save & Quit

Save file
> :w

Save and quit
> :wq

Quit without saving
> :q!

Save as new filename
> :w newfile.txt

Force save (if read-only)
> :w!
 
## Multiple Files

Switch to next file
> :n

Switch to previous file
> :N

List all open files
> :ls

Switch to file #2
> :b2

Open new file
> :e filename

Split window horizontally
> :split filename

Split window vertically
> :vsplit filename

Switch between splits
> Ctrl + w + w

## Other Useful Commands

Delete everything in file
> ggdG

Delete all and start fresh
> ggdG then i

Show line numbers
> :set number

Hide line numbers
> :set nonumber

Go to start of document, delete all, enter insert mode
> ggdGi

Copy entire file to clipboard (if system clipboard available)
> :%y+

Show current line/column
> Ctrl + g

Execute shell command
> :!ls

Read output of command into file
> :r !date



# In Nano:

Press  to start marking
> Ctrl + 6 or Alt + A

Press to select to end
> Ctrl + End or Alt + \ 

Press  to cut
> Ctrl + K

Move to new location & paste
> Ctrl + U

# Complete Nano Command Reference

## Opening Files

Open a file
> nano filename

Open file at specific line
> nano +10 filename

Open as read-only
> nano -v filename

Create new file
> nano

## Basic Editing

Start typing (no special mode needed)
> Just type

Delete character under cursor
> Ctrl + D

Delete character before cursor
> Backspace

Delete from cursor to end of line
> Ctrl + K

Delete entire line
> Ctrl + K (when cursor at line start)

## Navigation

Move left
> Left Arrow or Ctrl + B

Move right
> Right Arrow or Ctrl + F

Move up
> Up Arrow or Ctrl + P

Move down
> Down Arrow or Ctrl + N

Go to beginning of line
> Home or Ctrl + A

Go to end of line
> End or Ctrl + E

Go to beginning of file
> Alt + \ or Ctrl + Home

Go to end of file
> Alt + / or Ctrl + End

Go to specific line
> Ctrl + _ (then type line number)

Page down
> Ctrl + V or Page Down

Page up
> Ctrl + Y or Page Up

Move forward one word
> Ctrl + Space

Move backward one word
> Alt + Space

## Select (Mark) Text

Start marking/selecting
> Ctrl + 6 or Alt + A

Select to end of file
> Ctrl + End or Alt + \

Select to beginning of file
> Ctrl + Home or Alt + ^

Select entire line (mark start, then End)
> Ctrl + 6, then End

Select all (mark start, go to end)
> Alt + A, then Alt + /

Unmark/deselect
> Ctrl + 6 or Alt + A (toggle)

## Cut, Copy & Paste

Cut current line
> Ctrl + K

Cut selected text (after marking)
> Ctrl + K

Cut all content (mark all, then cut)
> Alt + A, Alt + /, Ctrl + K

Copy current line (without deleting)
> Alt + 6

Copy selected text (after marking)
> Alt + 6

Paste
> Ctrl + U

Paste multiple times (keeps in buffer)
> Ctrl + U (repeatedly)

## Undo & Redo

Undo
> Alt + U or Ctrl + _ then U

Redo
> Alt + E or Ctrl + _ then E

## Search & Replace

Search forward
> Ctrl + W (then type search term)

Search backward
> Ctrl + Q (then type search term)

Search and replace
> Ctrl + \ (then type old and new text)

Find next occurrence
> Alt + W

Find previous occurrence
> Alt + Q

## Save & Exit

Save file
> Ctrl + O (then press Enter)

Save as (new filename)
> Ctrl + O (then type new name, Enter)

Exit nano
> Ctrl + X

Save and exit (if modified)
> Ctrl + X, then Y, then Enter

Exit without saving
> Ctrl + X, then N

## File Operations

Insert another file at cursor
> Ctrl + R (then type filename)

Execute command and insert output
> Ctrl + R, then Ctrl + T (type command)

Show current position
> Ctrl + C

## Display Options

Show/hide line numbers
> Alt + # or Alt + C

Enable/disable soft wrapping
> Alt + $ or Alt + L

Show/hide help text at bottom
> Ctrl + G (toggle)

Refresh screen
> Ctrl + L

## Other Useful Commands

Cut from cursor to end of file
> Ctrl + K (repeatedly) or mark to end then cut

Select and delete all
> Alt + A, Alt + /, Ctrl + K

Indent selected text
> Alt + }

Unindent selected text
> Alt + {

Comment selected lines (if syntax highlighting enabled)
> Alt + 3

Count words/lines/characters
> Alt + D

Spell check
> Ctrl + T

Open help
> Ctrl + G

## Tips

Cut entire file
> Alt + A (mark), Alt + / (to end), Ctrl + K (cut)

Copy entire file
> Alt + A (mark), Alt + / (to end), Alt + 6 (copy)

Move text (cut and paste)
> Ctrl + K (cut), move cursor, Ctrl + U (paste)

Duplicate a line
> Alt + 6 (copy line), Ctrl + U (paste)











# Update or install inside a file 
apt update -y > file_name &      " > ":- Redirecting to Files name
apt update -y > /dev/null &      " > ":- Redirecting to /dev/null (Sytem)
apt update -y > file_namet & |
 

To see the process 
< jobs >
ps -ef
killed pid

cd .. 