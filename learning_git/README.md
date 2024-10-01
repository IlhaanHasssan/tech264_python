from ctypes import c_double

# *Git Learning:*

* [Markdown](../learning_markdown/README)
* [Python](../learning_python/README.md)
### *Doing your first commit:*
python


1. Check if you have git on your machine `git --version`
2. Change into the correct directory in Git Bash/Command Prompt/Terminal `cd`
3. Ensure you are in the right directory `ls`
4. Add your details to track the author of the commits `git config user.name "Ilhaan Hassan" and  
    git config user.email "IlhaanHassanA@outlook.com"`
4. Initialise your git repo `git init` or clone from an online repo `git clone`, use `ls -a` to check if git repo has been initialised
5. Create a README.md file in the IDE or in Git Bash`touch README.md`
6. You can create a change in the file in the IDE or Git Bash `echo <insert content>`
7. Check the status of your files using `git status`
8. Track the changes made to your files `git add . #tracks all files`
9. Commit these changes with a relevant comment `git commit -m "..."`
10. Once you make changes to your file, you should commit again to have an updated snapshot of your work
11. Check the differences between your commits `git diff <commit ID 1> <commit ID 2>`
12. Use git checkout to checkout out a previous commit `git checkout <commit ID>`
13. Use git checkout to return to a previous commit or restore a specific file to its state in a previous commit `git checkout HEAD~1 --<FILENAME>`
14. Use git checkout to also return to the original HEAD(most recent commit) `git checkout <commit ID>`
15. Use `git log` to check all commits and commit IDs
16. Can use `git restore` to restore files in the working directory or the staging area (index) to their last committed state



### *How to clone an existing repo:*

1. Make sure you are in the correct directory using `pwd` or create a new one using `mkdir`
2. If not, you can change your current directory with `cd`
3. Sign up/Log in to github.com
4. Go to the repositories section of you profile and click `new`
5. Best practice denotes using the same name for local and online repos
6. Once you've named your repo, you can now connect the local to the online
7. You must select HTTPS option.
8. You need to run these commands in a CLI:
```commandline
    i.  $ git remote add origin https://github.com/<name of github repo>
    ii. $ git branch -M main
    iii.$ git push -u origin main
```
    


### ***What are some things we would want to avoid pushing to git?***

- anything sensitive like passwords, credentials etc
- really large files/folders that we don't need to be push to a remote repo
- some files/folders related to building/running eg: /bin, /out, etc
- Hidden system files
#### *Solution = .gitignore files*
 ***When you want a file to be ignored, you can put a . in front of a file or directory.***

If the file is still accessible in a previous commit, what can you do?
- you can run the command below to erase the cache/history of all the commits of a file.

```bash
git rm --cached -r <filename>
```
- #### option 1:
```bash
git reset
``` 
- This removes all previous commits of that file ***BEWARE - DANGEROUS COMMAND***
- #### option 2:
  1. remove GitHub repo from online repo
  2. remove sensitive info from your local file
  3. remove ```.git``` from your local repo


