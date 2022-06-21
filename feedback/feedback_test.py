from github import Github
import os
import git



g = Github(os.environ["GITHUB_TOKEN"])
#repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
repo = git.Repo.clone_from("git@github.com:"+os.environ["GITHUB_REPOSITORY"]+".wiki.git")
repo.index.add(["feedback_wiki"])
repo.index.commit("try push to wiki")
repo.remotes.origin.push()
#repo.create_file("wiki/testwiki.md", "init commit", "#First Test \nfirst test pushing to wiki")
#file_content = repo.get_contents('wiki/testwiki.md')

#print("file_content")
