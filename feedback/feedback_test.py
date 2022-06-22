from github import Github
import os

g = Github(os.environ["GITHUB_TOKEN"])

repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
#repo.create_file("test_create_file/test.md", "add testfile", "test 1")
contents = repo.get_contents("README.md")
repo.update_file(contents.path, "update readme", "\\n new content added by script", contents.sha, branch="main")
#contents = repo.get_contents("")
#print(contents)

#repo.create_file("wiki/feedback.md", "add/update wiki doc", '#Add wiki pagec\n content1', branch="main")

# repo.update_file(contents.path, "more tests", "more tests", contents.sha, branch="test")

#contents = repo.get_contents("")
#while contents:
#  file_content = contents.pop(0)
#  if file_content.type == "dir":
#    contents.extend(repository.get_contents(file_content.path))
#  else:
#    print(file_content)

