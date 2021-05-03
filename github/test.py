from github import Github
from pprint import pprint

with open("token.txt", "r") as f:
    token = f.read()

g = Github(token)

user = g.get_user(login="Abhiswain97")

query = "LibtorchDemo"

repo_name_url = {}

for repo in g.search_repositories(query):
    repo_name_url[repo.name] = repo.html_url

pprint(repo_name_url)

