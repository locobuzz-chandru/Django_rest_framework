import json
from .redis import Redis


class RedisSchool:

    def __init__(self):
        self.redis = Redis()

    def save(self, student_id, school_name):
        school_dict = self.get(student_id)
        school_id = school_name.get('id')
        school_dict.update({school_id: school_name})
        self.redis.setter(str(student_id), json.dumps(school_dict))

    def get(self, student_id):
        schools = self.redis.getter(str(student_id))
        if schools is not None:
            return json.loads(schools)
        return {}

    def update(self, schools, student_id):
        school_id = str(schools.get('id'))
        schools_dict = self.get(student_id)
        school = schools_dict.get(school_id)
        if school is not None:
            schools_dict.update({school_id: schools})
            self.redis.setter(str(student_id), json.dumps(schools_dict))

    def delete(self, student_id, school_id):
        schools_dict = self.get(student_id)
        school = schools_dict.get(str(school_id))
        if school is not None:
            schools_dict.pop(str(school_id))
            self.redis.setter(str(student_id), json.dumps(schools_dict))
