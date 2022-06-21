from github import Github
import os



g = Github(os.environ["GITHUB_TOKEN"])
repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
repo.create_file("/wiki/testwiki.md", "init commit", "#First Test \nfirst test pushing to wiki")
file_content = repo.get_contents('/wiki/testwiki.md')

print("file_content")
