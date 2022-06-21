from github import Github
import os



g = Github(os.environ["GITHUB_TOKEN"])
repository = g.get_repo(os.environ["GITHUB_REPOSITORY"])
print(os.environ["GITHUB_REPOSITORY"])
#wiki = g.get_repo(os.environ["GITHUB_REPOSITORY"]+"/wiki")
contents = repository.get_contents("")
while contents:
  file_content = contents.pop(0)
  if file_content.type == "dir":
    contents.extend(repository.get_contents(file_content.path))
  else:
    print(file_content)


#wiki.create_file("feedback.md", "init commit", "#Add wiki page\ncontent1")

#file_content = repo.get_contents(os.environ["WIKI_DIR"]+"feedback.md")

#print("file_content")
