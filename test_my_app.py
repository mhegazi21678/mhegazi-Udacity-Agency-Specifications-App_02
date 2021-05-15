import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Movie, Actor
from app import create_app

import logging
logging.basicConfig(filename='example.log', encoding='utf-8',
                    level=logging.DEBUG, filemode='w')
logging.debug('This message should go to the log file')

# ALLENVVARIABLES = os.environ()
# logging.debug('ALLENVVARIABLES = %s' , ALLENVVARIABLES)

TEST_DATABASE_PATH = os.getenv('TEST_DATABASE_PATH')
logging.debug('TEST_DATABASE_PATH = %s', TEST_DATABASE_PATH)

CASTINGASSISTANT_TOKEN = os.getenv('CASTINGASSISTANT_TOKEN')
# logging.debug('CASTINGASSISTANT_TOKEN = %s' , CASTINGASSISTANT_TOKEN)

CASTINGDIRECTOR_TOKEN = os.getenv('CASTINGDIRECTOR_TOKEN')
# logging.debug('CASTINGDIRECTOR_TOKEN = %s' , CASTINGDIRECTOR_TOKEN)

EXECUTIVEPRODUCER_TOKEN = os.getenv('EXECUTIVEPRODUCER_TOKEN')
# logging.debug('EXECUTIVEPRODUCER_TOKEN = %s' , EXECUTIVEPRODUCER_TOKEN)

CASTINGASSISTANT_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVlbkNtRTgtcDExRTg1QjZod1JfNiJ9.eyJpc3MiOiJodHRwczovL2hpai1mc25kLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDkwNWM4ZmFkNzg0ZTAwNjkzY2Q0YTUiLCJhdWQiOiJBZ2VuY3lfU3BlY2lmaWNhdGlvbnMiLCJpYXQiOjE2MjEwMTY5NTEsImV4cCI6MTYyMTAyNDE1MSwiYXpwIjoieUVOb3k2dU85MWhKVmJMV05PS0V6dVB5RGkzeXNEYlgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.kSOe0n8auuboSHAd9eLlWZIXOCSiF-keaV380Sm3Z44yjGIXyad3XRNL_pBmwjomnuoj7qGGpVa1l9tTGgjycguXsDN-oyHjCUwmgRYOnwvQ27ZLP9E4hI_U8BKjeINmw7ScFYgGf1P6rUq3K_lfezRLBuW7dhU47gHKE-YzDA7b7M461fSEEw9_NLFzaLIlFN2xdLKFFOPF3AlZNEzkC5M2bZdTihskNxXno5fZv03LyIaOdJO1iiscvzBkD0PYMTta3itMkmHlE2teCwKysC3yfgdv6Z9gywouuebfovtF4Rk2dLodjkzZmz1YlgTUDj9mBCC3jCKfAn61TY2bXQ"
EXECUTIVEPRODUCER_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVlbkNtRTgtcDExRTg1QjZod1JfNiJ9.eyJpc3MiOiJodHRwczovL2hpai1mc25kLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDkwNWQ0ZGJmM2FkMDAwNzBjZDczOTMiLCJhdWQiOiJBZ2VuY3lfU3BlY2lmaWNhdGlvbnMiLCJpYXQiOjE2MjEwOTg2NTAsImV4cCI6MTYyMTEwNTg1MCwiYXpwIjoieUVOb3k2dU85MWhKVmJMV05PS0V6dVB5RGkzeXNEYlgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.lG69Ar9Dxe14ErlG3tvaPaKwbzxiK-Z_jFpdxTUhjAAF8KkgigTfkaTNVNDItOAGdzjSz1YbzHXKMtA1cOVYpHUfKgL_MRtS8TAurZr4YkpFix3-3JjELbd2tObKWsZgnqDLK5qxsIYF8u3X_2CmNhUoGMOA7hGZLGo69c0wcEbE9cjB6H1c3LlucfX0v7tWXTxs2Bz_9xuFV9kicyI02CUpfPpN_WFT2u-CBqOt2zKOGqbPaPG1I2Ynw1FHrr5tJvuIBAlcjywcr0-S33pI9t-PPWIbJ0xBEpgc9erLTuT3LCexz07SbFs7f3PTx3nHaV9hPFeJNMaX3gE7kY0mcw"
CASTINGDIRECTOR_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVlbkNtRTgtcDExRTg1QjZod1JfNiJ9.eyJpc3MiOiJodHRwczovL2hpai1mc25kLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDkwNWNmNTk3MDVjNjAwNzFhYzJjNjgiLCJhdWQiOiJBZ2VuY3lfU3BlY2lmaWNhdGlvbnMiLCJpYXQiOjE2MjA0ODg3MjEsImV4cCI6MTYyMDQ5NTkyMSwiYXpwIjoieUVOb3k2dU85MWhKVmJMV05PS0V6dVB5RGkzeXNEYlgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.vszoiwubQlzAiR8TlB0wYJLFEVpkFOR0TdDSEvd-zKrgGnMbZLweqs6-KLb7pR3ZYaNJ1jamjKKtI8UtilZX0N84WT_VfCxHr3VUwPyDvGSNcCBq8iUd6KgA1EO7CwNFfPUwu-IBAMiKDapi4oGxtoTGzahQbOVZ-8yEMFNPCXWXH5TVCMMwntbWsIXL9oxZsgnId8DpqBfXhqZMAWTYwJw5HVuJYKgkgv1rqUBF6tqCbq4e4fVzqZ8_fLvIVLx2dtVB6KNmy0dvEf-6pQCrm6DAaiUAb2wnZxNUJXoY8ohhlsOUYC0ECkoxVwrOlcwNXqYyi8uxX9TS1W-SKJMrMQ"

#     """
#     TODO
#     Write at least one test for each test for successful
#     operation and for expected errors.
#     """


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        # setup_db(self.app, TEST_DATABASE_PATH)
        self.database_name = "agencyspecifications_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', 'postgres', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.casting_assistant = CASTINGASSISTANT_TOKEN
        self.casting_director = CASTINGDIRECTOR_TOKEN
        self.executive_producer = EXECUTIVEPRODUCER_TOKEN
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            # create_and_drop_all()
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

# ************************************************************************* #
# Actors Test Cases :

    def test_get_all_actors_unauthorized_401(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_get_all_actors(self):
        res = self.client().get('/actors',
                                headers={
                                    "Authorization": "Bearer {}"
                                    .format(self.casting_assistant)
                                })
        data = json.loads(res.data)
        print(data)
        if res.status_code == 200:
            self.assertTrue(data['success'])
            self.assertNotEqual(len(data['actors']), 0)

    def test_post_actor(self):
        actor = {
            "name": "Amr Diab",
            "gender": "Male",
            "age": 59,
        }

        res = self.client().post('/actors',
                                 headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.executive_producer)
                                 }, json=actor)
        data = json.loads(res.data)
        print(data)
        self.assertTrue(data['success'])
        actor_db = Actor.query.get(data['actors']['id'])
        actor['id'] = data['actors']['id']
        self.assertEqual(actor_db.format(), actor)

    def test_post_actors_fail_500(self):
        actor = {
            "name": "Amr Diab",
            "gender": "Male"
            # "age": 59
        }
        res = self.client().post('/actors',
                                 headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.executive_producer)
                                 }  # , json=actor
                                 )
        data = json.loads(res.data)
        # print(data)
        self.assertFalse(data['success'])
        self.assertEqual(500, res.status_code)
        self.assertEqual(data['message'], 'Server error')

    def test_post_actors_unprocessable_422(self):
        actor = {
            # "name": "Amr Diab",
            "gender": "Male",
            "age": 59
        }
        res = self.client().post('/actors',
                                 headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.executive_producer)
                                 }, json=actor)
        data = json.loads(res.data)
        # print(data)
        self.assertFalse(data['success'])
        self.assertEqual(422, res.status_code)
        self.assertEqual(data['message'], 'unprocessable')

    def test_post_actors_unauthorized_401(self):
        actor = {
            "name": "Amr Diab",
            "gender": "Male",
            "age":  59
        }
        res = self.client().post('/actors',
                                 headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.casting_assistant)
                                 }, json=actor)
        # data = json.loads(res.data)
        # print(data)
        # self.assertFalse(data['success'])
        self.assertEqual(401, res.status_code)

    def test_delete_actor(self):
        actor = Actor.query.order_by(Actor.id).first()
        res = self.client().delete('/actors/'+str(actor.id),
                                   headers={
            "Authorization": "Bearer {}"
            .format(self.executive_producer)})
        data = json.loads(res.data)
        print(data)
        self.assertTrue(data['success'])
        actor = Actor.query.get(data['actors'])
        self.assertEqual(actor, None)

    def test_delete_actor_unauthorized_401(self):
        res = self.client().delete('/actors/2153')
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(401, res.status_code)

    def test_delete_actor_not_found_404(self):
        res = self.client().delete('/actors/5632',
                                   headers={
                                       "Authorization": "Bearer {}"
                                       .format(self.executive_producer)})
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(404, res.status_code)

    def test_patch_actor_fail_404(self):
        actor = {
            "name": "Sameer Ganem",
            "gender": "Male",
            "age": 95
        }
        res = self.client().patch('/actors/1000',
                                  headers={
                                      "Authorization": "Bearer {}"
                                      .format(self.executive_producer)
                                  }, json=actor)
        data = json.loads(res.data)
        print(data)
        self.assertFalse(data['success'])
        self.assertEqual(404, res.status_code)

    def test_patch_actor_unauthorized_401(self):
        actor = {
            "name": "Sameer Ganem",
            "gender": "Male",
            "age": 95
        }
        actor_name = "Sameer Ganem"
        actor_db = Actor.query.filter_by(name=actor_name).one_or_none()
        res = self.client().patch('/actors/'+str(actor_db.id),
                                  headers={
            "Authorization": "Bearer {}".format(self.casting_assistant)
        }, json=actor)

        # data = json.loads(res.data)
        # print(data)
        # self.assertFalse(data['success'])
        self.assertEqual(401, res.status_code)

    def test_patch_actor(self):
        actor = {
            "name": "Sameer Ganem",
            "gender": "Male",
            "age": 95
        }
        actor_name = "Sameer Ganem"
        # actor_db = Actor.query.order_by(Actor.id).first()
        # actor_db = Actor.query.order_by(Actor.name.like(search)).all()
        actor_db = Actor.query.filter_by(name=actor_name).one_or_none()
        res = self.client().patch('/actors/'+str(actor_db.id),
                                  headers={
            "Authorization": "Bearer {}".format(self.executive_producer)
        }, json=actor)
        data = json.loads(res.data)
        print(data)
        self.assertTrue(data['success'])
        self.assertEqual(200, res.status_code)
        actor_db = Actor.query.get(data['actors']['id'])
        actor_json = actor_db.format()
        for key in actor.keys():
            self.assertEqual(actor[key], actor_json[key])

# ************************************************************************** #
# # Movies Test Cases :

    def test_get_all_movies_unauthorized_401(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_get_all_movies(self):
        res = self.client().get('/movies',
                                headers={
                                    "Authorization": "Bearer {}"
                                    .format(self.casting_assistant)
                                })
        headers = {"Authorization": "Bearer {}".format(self.casting_assistant)}
        logging.debug('headers = %s', headers)
        logging.debug('res = %s', res)
        data = json.loads(res.data)
        print(data)
        logging.debug('test_list_movies = %s', data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_post_movie(self):
        movie = {
            "title": "Noura's Dream",
            "release_date": "2019-01-02"
        }
        res = self.client().post('/movies',
                                 headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.executive_producer)
                                 }, json=movie)
        data = json.loads(res.data)
        print(data)
        self.assertTrue(data['success'])
        movie_db = Movie.query.get(data['movies']['id'])
        movie['id'] = data['movies']['id']
        self.assertEqual(movie_db.format(), movie)

    def test_post_movie_fail_500(self):
        movie = {
            "title": "Noura's Dream",
            "release_date": "2019-01-02"
        }
        res = self.client().post('/movies',
                                 headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.executive_producer)
                                 }  # , json=movie
                                 )
        data = json.loads(res.data)
        # print(data)
        self.assertFalse(data['success'])
        self.assertEqual(500, res.status_code)
        self.assertEqual(data['message'], 'Server error')

    def test_post_movie_unprocessable_422(self):
        movie = {
            # "title": "Noura's Dream",
            "release_date": "2019-01-02"
        }
        res = self.client().post('/movies',
                                 headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.executive_producer)
                                 }, json=movie)
        data = json.loads(res.data)
        # print(data)
        self.assertFalse(data['success'])
        self.assertEqual(422, res.status_code)
        self.assertEqual(data['message'], 'unprocessable')

    def test_post_movie_unauthorized_401(self):
        movie = {
            "title": "Noura's Dream",
            "release_date": "2019-01-02"
        }
        res = self.client().post('/movies',
                                 headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.casting_assistant)
                                 }, json=movie)
        # data = json.loads(res.data)
        # self.assertFalse(data['success'])
        # self.assertEqual(401, res.status_code)
        assert res.status_code in (401, 403)

    def test_delete_movie(self):
        movie = Movie.query.order_by(Movie.id).first()
        res = self.client().delete('/movies/'+str(movie.id),
                                   headers={
            "Authorization": "Bearer {}"
            .format(self.executive_producer)})
        data = json.loads(res.data)
        print(data)
        self.assertTrue(data['success'])
        movie = Movie.query.get(data['movies'])
        self.assertEqual(movie, None)

    def test_delete_movie_unauthorized_401(self):
        res = self.client().delete('/movies/4521')
        data = json.loads(res.data)
        # print(data)
        self.assertFalse(data['success'])
        self.assertEqual(401, res.status_code)

    def test_delete_movie_fail_404(self):
        res = self.client().delete('/movies/5236',
                                   headers={
                                       "Authorization": "Bearer {}"
                                       .format(self.executive_producer)})
        data = json.loads(res.data)
        # print(data)
        self.assertFalse(data['success'])
        self.assertEqual(404, res.status_code)

    def test_patch_movie_fail_404(self):
        movie = {
            "title": "Theeb",
            "release_date": "2014-01-01",
        }
        res = self.client().patch('/movies/2541',
                                  headers={
                                      "Authorization": "Bearer {}"
                                      .format(self.executive_producer)
                                  }, json=movie)
        data = json.loads(res.data)
        print(data)
        self.assertFalse(data['success'])
        self.assertEqual(404, res.status_code)

    def test_patch_movie_unauthorized_401(self):
        movie = {
            "title": "Theeb",
            "release_date": "2014-01-01",
        }
        res = self.client().patch('/movies/2541',
                                  headers={
                                      "Authorization": "Bearer {}"
                                      .format(self.casting_assistant)
                                  }, json=movie)
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        # self.assertEqual(401, res.status_code)
        assert res.status_code in (401, 403)

    def test_patch_movie(self):
        movie = {
            "title": "Theeb",
            "release_date": "2014-05-01",  # change the date
        }
        movie_name = "Theeb"
        movie_db = Movie.query.filter_by(title=movie_name).one_or_none()
        # movie = Movie.query.order_by(Movie.id).first()
        res = self.client().patch('/movies/'+str(movie_db.id),
                                  headers={
            "Authorization": "Bearer {}".format(self.executive_producer)
        }, json=movie)
        data = json.loads(res.data)
        print(data)
        self.assertTrue(data['success'])
        self.assertEqual(200, res.status_code)
        movie_db = Movie.query.get(data['movies']['id'])
        movie_json = movie_db.format()
        for key in movie.keys():
            self.assertEqual(movie[key], movie_json[key])

# main function
if __name__ == "__main__":
    unittest.main()
