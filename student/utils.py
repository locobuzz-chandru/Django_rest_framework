import logging
import json
from .redis import RedisCode


class Cache:
    def __init__(self):
        self.cache = RedisCode()

    def get_school(self, student_id):
        try:
            schools = self.cache.extract(str(student_id))
            if schools is not None:
                return json.loads(schools)
            return {}

        except Exception as e:
            logging.error(e)

    def add_school(self, student_id, school):
        try:
            school_dict = self.get_school(student_id)
            school_dict.update({school.get('id'): school})
            self.cache.save(str(student_id), json.dumps(school_dict))
        except Exception as e:
            logging.error(e)

    def update_book(self, student_id, schools):
        school_id = str(schools.get('id'))
        schools_dict = self.get_school(student_id)
        school = schools_dict.get(school_id)
        if school is not None:
            schools_dict.update({school_id: schools})
            self.cache.save(student_id, json.dumps(schools_dict))

    def delete_note(self, student_id, id):
        try:
            school_dict = self.get_school(student_id)
            school_dict.pop(str(id))
            self.cache.save(str(student_id), json.dumps(school_dict))

        except Exception as error:
            logging.exception(error)
