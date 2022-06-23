from github import Github
import os

g = Github(os.environ["GITHUB_TOKEN"])

repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
contents = repo.get_contents("README.md")
print(contents)
new_file_content = contents.decoded_content.decode()
print(new_file_content)
new_message = new_file_content.replace("#Getting Feedback now...",'[Feedback]https://github.com/'+os.environ["GITHUB_REPOSITORY"]+'/wiki')
print(new_file_content)
repo.update_file(contents.path, "update readme",new_message, contents.sha, branch="main")
#'https://github.com/'+os.environ["GITHUB_REPOSITORY"]+'/wiki'
