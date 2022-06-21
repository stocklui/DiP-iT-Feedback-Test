from github import Github
import os
import git



g = Github(os.environ["GITHUB_TOKEN"])
repository = g.get_repo(os.environ["GITHUB_REPOSITORY"])
repository.create_file("tmp/tmp.txt", "init commit", "add tmp directory")
repo = git.Repo.clone_from("https://github.com/"+os.environ["GITHUB_REPOSITORY"]+".wiki.git", "https://github.com/"+os.environ["GITHUB_REPOSITORY"]+"\tmp")
repo.index.add(["feedback_wiki"])
repo.index.commit("try push to wiki")
repo.remotes.origin.push()

#file_content = repo.get_contents('wiki/testwiki.md')

#print("file_content")
