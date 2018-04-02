import requests

BASE_URL = 'https://jobs.github.com/positions.json'


def get_job(location):
    URL = BASE_URL + '?location=' + location
    response = requests.get(URL)
    print response
    job = ''
    json_res = response.json()
    if len(json_res) > 0:
        res = json_res[0]
        Type = res['type']
        title = res['title']
        location = res['location']
        company = res['company']
        apply = res['how_to_apply']
        job = '<Title: ' + title + '> ' + '<Type: ' + Type + '> ' + '<Location: ' + location + '> ' + \
            '<Company: ' + company + '> ' + ' Apply at: ' + apply
    else:
        job = 'No jobs Found'
    return job
