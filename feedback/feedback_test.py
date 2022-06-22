from github import Github
import os
import time

g = Github(os.environ["GITHUB_TOKEN"])

repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
contents = repo.get_contents("README.md")
repo.update_file(contents.path, "update readme", '#Getting Feedback now...', contents.sha, branch="main")
# getting feedback and writing into following file
repo.create_file("wiki/feedback.md", "add tmp feedback", "this should be feedback information")
time.sleep(5)
#


