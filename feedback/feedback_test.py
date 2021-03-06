from github import Github
import os
import time

g = Github(os.environ["GITHUB_TOKEN"])

repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])

all_files = []
allcontents = repo.get_contents("")
while allcontents:
    all_file_content = allcontents.pop(0)
    if all_file_content.type == "dir":
        allcontents.extend(repo.get_contents(all_file_content.path))
    else:
        file = all_file_content
        all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))

if "README.md" in all_files:
    contents = repo.get_contents("README.md")
    file_content = contents.decoded_content.decode()
    if ("[Feedback](../../wiki/feedback)" and "Feedback") in file_content:
        print("readme already initialized")
        new_message = file_content.replace("Click here to get your Feedback -> [Feedback](../../wiki/feedback)",'Getting Feedback now...')
    else:
        print("readme not initialized")
        append_text = r"""
"""
        append_text = append_text + """### Getting Feedback now..."""
        new_message = file_content + append_text
    repo.update_file(contents.path, "update readme", new_message, contents.sha, branch="main")

else:
    readme_content = r"""# Feedback """
    readme_content= readme_content+r"""
"""
    readme_content= readme_content + r"""### Getting Feedback now... """
    repo.create_file("README.md", "create README", readme_content, branch="main")


os.mkdir("../feedback")
f = open("../feedback/feedback.md","w")
f.write("This should contain feedback")
f.close()
