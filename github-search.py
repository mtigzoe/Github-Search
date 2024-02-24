import requests
import time 

def search_github_repos(query):
    url = f"https://api.github.com/search/repositories?q={query}"
    response = requests.get(url)
    data = response.json()

    # Process the search results (e.g., extract repo names, descriptions, etc.)
    count = 0
    for item in data.get("items", []):
        count += 1
        repo_url = item["svn_url"]
        repo_name = item["name"]
        repo_description = item["description"]
        print(f"URL: {repo_url}")
        print(f"Repository: {repo_name}")
        print(f"Description: {repo_description}\n")
        time.sleep(1)
    print(f"Total repos found: {count}")

search_query = input("Search: ") 

search_github_repos(search_query)
