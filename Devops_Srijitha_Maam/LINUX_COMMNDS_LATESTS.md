
# FOR VIM
## INSERT MODE

* `i` → insert text
* `Esc` → exit insert mode

---

## SAVE & EXIT

* `:w` → save
* `:q` → quit
* `:wq` → save & quit
* `:x` → save and exit
* `:q!` → quit without saving

---

## DELETE

* `dd` → delete line
* `5dd` → delete 5 lines
* `dw` → delete word

---

## COPY & PASTE

* `yy` → copy line
* `p` → paste
* `5p` → paste 5 times

---

## UNDO & REDO

* `u` → undo
* `Ctrl+r` → redo

---

## SEARCH

* `/word` → search

---

## CURSOR MOVEMENT

* `h` → left
* `l` → right
* `j` → down
* `k` → up



# Paste the Selected Line in EC2 Instance

* `Ctrl + Shift + V` → paste in terminal

---

# Linux Commands

## Navigation

### Go Inside a Folder

```bash id="mx1"
cd frontend
cd backend
```

### Exit from Current Folder

```bash id="mx2"
cd ..
```

---

# Create Files & Folders

### Create Folder

```bash id="mx3"
mkdir frontend
mkdir backend
```

---

# Verify Location

### Show Current Path

```bash id="mx4"
pwd
```

Example:

```bash id="mx5"
/home/ubuntu/backup/project
```

---

# List Files & Folders

### Show Files & Folders

```bash id="mx6"
ls
```

### Show Hidden Files & Folders

```bash id="mx7"
ls -a
```

---

# Copy Commands

## Copy Folder to Another Directory

```bash id="mx8"
cp -r source_folder destination_directory
cp -r project /home/ubuntu/docs/
```

## Copy & Rename Folder

```bash id="mx9"
cp -r project /home/ubuntu/document/project_backup
```

## Copy Folder to Parent Directory

```bash id="mx10"
cp -r backend ../
cp -r frontend ../
```

## Copy & Rename to Parent Directory

```bash id="mx11"
cp -r backend ../backend_copy
```

## Copy File to Parent Directory

```bash id="mx12"
cp docker-compose.yml ../
```

---

# Move Commands

## Move Folder to Another Directory

```bash id="mx13"
mv source_folder destination_directory
mv project /home/ubuntu/backup/
```

### Verify

```bash id="mx14"
ls /home/ubuntu/backup/project
```

OR

```bash id="mx15"
cd /home/ubuntu/backup/
```

---

## Move File to Another Directory

```bash id="mx16"
mv source_file destination_directory
mv file.txt /home/ubuntu/documents/
```

### Verify

```bash id="mx17"
ls /home/ubuntu/documents/
```

---

## Move Multiple Files

```bash id="mx18"
mv file1.txt file2.txt file3.txt /home/ubuntu/docs/
```

---

## Move & Rename Folder/File

```bash id="mx19"
mv project project_old
mv report.txt report_final.txt
```

---

## Move Folder to Parent Directory

```bash id="mx20"
mv backend ../
mv frontend ../
```

---

# Delete Commands

## Delete File

```bash id="mx21"
rm filename
rm test.txt
```

## Delete Empty Folder

```bash id="mx22"
rmdir folder_name
```

## Delete Folder with Files

```bash id="mx23"
rm -r folder_name
rm -r project
```

## Force Delete Folder

```bash id="mx24"
rm -rf folder_name
rm -rf project
```

## Delete Parent Directory Folder

```bash id="mx25"
rm -r ../backend
rm -r ../frontend
```

---

# Check Files Again

## Show Files & Folders

```bash id="mx26"
ls
```

## Show Hidden Files & Folders

```bash id="mx27"
ls -a
```
