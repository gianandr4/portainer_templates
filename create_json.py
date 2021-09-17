import json, requests, os


repos=['https://raw.githubusercontent.com/portainer/templates/master/templates-2.0.json',
       'https://raw.githubusercontent.com/Qballjos/portainer_templates/master/Template/template.json',
       'https://raw.githubusercontent.com/dnburgess/dbtechtemplate/master/Template/v2/templates.json']


final_repo = {'version': '2','templates':[]}

for repo in repos:
    dict = json.loads(requests.get(repo).text)
    final_repo['templates'].extend(dict['templates'])



with open('portainer.json','w+') as f:
    f.truncate(0)
    json.dump(final_repo,f)