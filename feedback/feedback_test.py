from github import Github
import os
import time

g = Github(os.environ["GITHUB_TOKEN"])

repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
contents = repo.get_contents("README.md")
repo.update_file(contents.path, "update readme", '#Getting Feedback now...', contents.sha, branch="main")
# getting feedback and writing into following file
all_files = []
contents1 = repo.get_contents("")
while contents1:
    file_content = contents1.pop(0)
    if file_content.type == "dir":
        contents1.extend(repo.get_contents(file_content.path))
    else:
        file = file_content
        all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))
print(all_files)
if 'wiki/feedback.md' in all_files:
    contents_wiki = repo.get_contents("wiki/feedback.md")
    repo.delete_file(contents.path, "remove wiki", contents.sha, branch="main")
else:
    repo.create_file("wiki/feedback.md", "add tmp feedback", "this should be feedback information")
time.sleep(5)
#


