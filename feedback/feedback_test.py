from github import Github
import os

g = Github(os.environ["GITHUB_TOKEN"])

repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
repo.create_file("wiki/feedback.md", "add/update wiki doc", '#Add wiki pagec\n content1', branch=master)

contents = repo.get_contents("")
while contents:
  file_content = contents.pop(0)
  if file_content.type == "dir":
    contents.extend(repository.get_contents(file_content.path))
  else:
    print(file_content)

