import requests


url = 'http://127.0.0.1:8000/api/courses/'

r = requests.get(url)
print(r.status_code)
courses = r.json()

course_list = ', '.join(course['title'] for course in courses)
print(course_list)

for course in courses:
    id = course['id']
    title = course['title']
    user = 'hstuan'
    passw = 'hstuan123456'


    url_enroll = 'http://127.0.0.1:8000/api/courses/{}/enroll/'.format(id)
    r_post = requests.post(url_enroll, auth=(user, passw))
    print(r_post.status_code)