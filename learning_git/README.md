# *Git Learning:*

* [Markdown](../learning_markdown/README)
* [Python](../learning_python/README.md)
### *Do your first commit:*
1. Check if you have git on your machine `git --version`
2. Change into the correct directory in Git Bash/Command Prompt/Terminal `cd`
3. Ensure you are in the right directory `ls`
4. Initialise your git repo `git init` or clone from an online repo `git clone`
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

