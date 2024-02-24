import requests
import time 

def search_github_repos(query):
    url = f"https://api.github.com/search/repositories?q={query}"
    response = requests.get(url)
    data = response.json()

    # Process the search results (e.g., extract repo names, descriptions, etc.)
    with open("results.txt", "w", encoding="utf-8") as fout:

        count = 0
        for item in data.get("items", []):
            count += 1
            repo_url = item["svn_url"]
            repo_name = item["full_name"]
            repo_description = item["description"]
            fout.write(str(f"URL: {repo_url}\n"))
            fout.write(str(f"Repository: {repo_name}\n"))
            fout.write(str(f"Description: {repo_description}\n\n"))
            time.sleep(1)
        print(f"Total repos found: {count}")

search_query = input("Search: ") 

search_github_repos(search_query)
