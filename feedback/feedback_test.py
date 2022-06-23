from github import Github
import os
import time

g = Github(os.environ["GITHUB_TOKEN"])

repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
contents = repo.get_contents("README.md")
file_content = contents.decoded_content.decode()
if "[Feedback](../../wiki/feedback)" in file_content:
    new_message = file_content.replace("[Feedback](../../wiki/feedback)",'#Getting Feedback now...')
else:
    new_message = file_content + '\ #Getting Feedback now...'
repo.update_file(contents.path, "update readme", new_message, contents.sha, branch="main")

os.mkdir("../feedback")
f = open("../feedback/feedback.md","w")
f.write("This should contain feedback")
f.close()
# repo.create_file("../feedback/feedback.md", "add tmp feedback", "this should be feedback information")
