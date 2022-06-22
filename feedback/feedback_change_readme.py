from github import Github
import os

g = Github(os.environ["GITHUB_TOKEN"])

repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
contents = repo.get_contents("README.md")
print(contents)
new_file_content = contents.decoded_content.decode()
print(new_file_content)
new_file_content.replace("#Getting Feedback now...", "feedback can be found in wiki")
print(new_file_content)
repo.update_file(contents.path, "update readme",str(new_file_content), contents.sha, branch="main")
#'https://github.com/'+os.environ["GITHUB_REPOSITORY"]+'/wiki'
