from github import Github
import os



g = Github(os.environ["GITHUB_TOKEN"])
repository = g.get_repo(os.environ["GITHUB_REPOSITORY"])
repository.create_file(os.environ["WIKI_DIR"]+"/feedback.md", "init commit", "add wiki page")

file_content = repo.get_contents(os.environ["WIKI_DIR"]+"/feedback.md")

print("file_content")
