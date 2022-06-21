from github import Github
import os



g = Github(os.environ["GITHUB_TOKEN"])
repository = g.get_repo(os.environ["GITHUB_REPOSITORY"])
print(os.environ["WIKI_DIR"])
#print(os.environ["WIKI_DIR"]+"feedback.md")
#print(os.environ["GITHUB_REPOSITORY"]+"/"+os.environ["WIKI_DIR"]+"feedback.md")
#repository.create_file(os.environ["WIKI_DIR"]+"feedback.md", "init commit", "add wiki page")

#file_content = repo.get_contents(os.environ["WIKI_DIR"]+"feedback.md")

#print("file_content")
