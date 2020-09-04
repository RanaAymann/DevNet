git --version
git --help

git init
git status
git commit -m "  msg   "
git checkout -- file.py
git add .
git reset HEAD
git log 
git reset 525d067

##### using  multiple braches #####

git checkout -b dollars
git log --all --decorate --online --graph
git config --global alias.hist " log --all --decorate --online --graph "
git hist
git branch 
vim database.py
git status
git commit -am "  msg " 
tail database.py
git checkout master
git merge dollars

git branch -d dollars 
git branch
git hist 


#### Tool for comparing files - diff command is a bash and git command ####

1 file and made changes

git diff 
git checkout -- .

! as a bash command will compare between two files

diff -u database.py database2.py





