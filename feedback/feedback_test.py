from github import Github
import os



g = Github(os.environ["GITHUB_TOKEN"])
repository = g.get_repo(os.environ["GITHUB_REPOSITORY"])
print(os.environ["WIKI_DIR"])
print(os.environ["GITHUB_REPOSITORY"])
wiki = os.environ["WIKI_DIR"]
#print(os.environ["WIKI_DIR"]+"feedback.md")
#print(os.environ["GITHUB_REPOSITORY"]+"/"+os.environ["WIKI_DIR"]+"feedback.md")

wiki.create_file("feedback.md", "init commit", "#Add wiki page\ncontent1")

#file_content = repo.get_contents(os.environ["WIKI_DIR"]+"feedback.md")

#print("file_content")
