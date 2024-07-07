import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("/home/santhosh/vs_code/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://attendance-3d35a-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "2036010073":
        {
            "name": "Santhosh.M",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-02-15 00:54:34"
        },
    "2036010093":
        {
            "name": "Vignes.P.K",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-02-15 00:54:34"
        },
    "2036010094":
        {
            "name": "Vigneskumar.G",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-02-15 00:54:34"
        },
    "2036010101":
        {
            "name": "Vishnu.S",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-02-15 00:54:34"
        },
    "2036010085":
        {
            "name": "Surya.A",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-02-15 00:54:34"
        },
    "2036010096":
        {
            "name": "Vignesh.V",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-02-15 00:54:34"
        },
    "2036010102":
        {
            "name": "Rameez ahamed dar",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-02-15 00:54:34"
        },
    "2136090009":
        {
            "name": "Vignesh.B",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-02-15 00:54:34"
        },
    "2136090007":
        {
            "name": "Aravindhan.S",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-02-15 00:54:34"
        },
    "2136090010":
        {
            "name": "Dhinesh.D",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-02-15 00:54:34"
        },
    "2136090003":
        {
            "name": "Durai selvam K",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-02-15 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)


