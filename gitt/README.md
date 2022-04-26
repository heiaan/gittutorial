Repositories in Git are a snapshot of the folder in which you are working on your project. You can track the progress and changes made to the project by making commits and also revert changes if not satisfactory.
Repositories can be divided into two types based on the usage on a server. These are:

Non-bare Repositories
Bare Repositories
What is a Non-bare repository?
A non-bare or default git repository has a .git folder, which is the backbone of the repository where all the important files for tracking the changes in the folders are stored. It stores the hashes of commits made in the branches and a file where the hash of the latest commit is stored.
The file structure of the default repository should look something like this:

