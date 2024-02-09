import requests
from plotly.graph_objects import bar
from plotly import offline

url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

#  store API response in variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')
repo_names, repo_links, stars, labels = [], [], [], []


repo_dict = repo_dicts[0]
print(f'\nKeys: {len(repo_dict)}')
for key in sorted(repo_dict.keys()):
    print(key)

# selected info from each repository

print('\nSelected info from each repository:')
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f'<a href="{repo_url}">{repo_name}</a>'
    repo_links.append(repo_link)
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f'{owner}<br />{description}'
    labels.append(label)

    # print(f"Name: {repo_dict['name']}")
    # print(f"Owner: {repo_dict['owner']['login']}")
    # print(f"Stars: {repo_dict['stargazers_count']}")
    # print(f"Repository: {repo_dict['html_url']}")
    # print(f"Created: {repo_dict['created_at']}")
    # print(f"Updated: {repo_dict['updated_at']}")
    # print(f"Description: {repo_dict['description']}")

# visualisation
data =[{
    'type': 'bar',
    # 'x: 'repo_names,
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 24, 12)',
        'line': {'width': 1.5, 'color': 'rgb(20, 20, 20)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most starred python projects on Github',
    'titlefont': {'size': 24},
    'xaxis': {
        'title': "Repository",
        'titlefont': {'size': 20},
        'tickfont': {'size': 12},
        },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 20},
        'tickfont': {'size': 12},
        },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')


print(response_dict.keys())