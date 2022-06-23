from github import Github
import os
import time

g = Github(os.environ["GITHUB_TOKEN"])

repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
contents = repo.get_contents("README.md")
file_content = contents.decoded_content.decode()
if ("[Feedback](../../wiki/feedback)" and "Feedback Section") in file_content:
    print("readme already initialized")
    new_message = file_content.replace("Click here to get your Feedback -> [Feedback](../../wiki/feedback)",'Getting Feedback now...')
else:
    print("readme not initialized")
    new_message = file_content + "## Feedback Section  <br>Getting Feedback now...  "
repo.update_file(contents.path, "update readme", new_message, contents.sha, branch="main")

os.mkdir("../feedback")
f = open("../feedback/feedback.md","w")
f.write("This should contain feedback")
f.close()
