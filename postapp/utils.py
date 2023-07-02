import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials
from django.conf import settings
import json

exmp = {

    "type": "service_account",
    "project_id": "noti-discuss",
    "private_key_id": "47d754942305792818431607aafa6d25a9cf346b",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQD6tqpt1hhJKysM\noFASIUmVlL3uF4plJZiJC2Gbpetfehp/Z4WnqRzlHmZ8ya4Ktpr9ZshY5WcV625Y\n4RDEaLf1a1dlmrvVF+p0zQ3cWhjR72OC90rM0xNU1pBRe8DkIQxV5D04A9NRlaEs\ncOP/urpwazUQq7zeaIFBxnLpYQ5dmilu3QP2RnLxNVue2mGNe4bm8nZLh50PFIY0\n3raM0MrD4bO0xajLpJpeYohAludsyVKH+9alxdyg5BZR8l35Mac64PEI0CHGXLRC\nGhCjQuGJ/rsA9AQpg5MFdZqbwXWeJG6T/rIEbHkJHnhiItxyKJOc5h9yUEq1H3Nn\nj4C7P3FbAgMBAAECggEAQkWBtGno3oJyLTK9J6Wz6T25nNONKiJveR5QjU+k8YZ5\ntZ68Ni7eK/RGvAqlnkBZpM0D/XeaMbGbaBQKFhjmM5HNttZZe0EIoRpI5SvNrsSc\nJdTPaWgMDptu55MSUFsqAxRDWGiudbzbLz+iDQmjWa8FBmSXFqVCMYxO+MDGhtgA\n1eZHcxDnzEhlaGoQPljUtNfn6ZxSkYGELjlSVZt8KfbinUn1Z7CWdE4KFNB4KKNp\n5XnOINURpQFFGo9TmV6sbQi1QjeTEUdwVu6pd7ze2NYDKShXJvudm1PZfcGAA2TV\niVNJgUbn7lAfar1xHkRPz/oN7mzU2dyrPQHNg+PKCQKBgQD/sxi533P48rCS2blD\nXETwLAUKIk/IoOeRK+3Hvt+5eBoNBfZi3nn7fEgyji5WIrIE8bIT0HY/7BNI93GE\nQIgVqTG3uiXDgEhUx/12goulX5E8f568HhKtznROzGV3cM18Hl+r0z9nGrd9GgEJ\nQGqnW/IoFJicKK7XygWPfOYV8wKBgQD7AhHOwAVGzyVr5yXaEZpSdmE7G0HU5BmH\nfCPXQeO2REPGRlpfOTg2wwDjrrDvFNL0wq1WptUdCpnXtS/rJCh5cu4mZoL7UU97\nTh5mJiYf/x3ZqnHGhYHs3PVUNaKl55OnklCFR1Q6Rz6XSJ8zSkBodI7ypv7tkn+X\nRKagGMmI+QKBgF3Na+K0MK1BCrm0mZw2eyvIWkjvcWlebdT50o8WXKiDgLsKVurK\nRuGVJD83nZQHwlrB99wA+4BTsHdyHvivW7zmhtCpvzTLGL3RaBBTr7sJJhSVlLva\nJGwScuR9YzO/9AH2eo5kPrwqNunz4jFsqjOfLWS6uYl/+zQ6bnPHE/k1AoGBAMlI\nbZNH9HNF5ZJTt8zZVNFP0MSfJPldOQOmju8tDTe6Ikc7X3kA3406btol2gi+wDQ6\ncNoNytQRDjEmQJjlU/egLE1q4xo5p+0PRd1QNj5uTDeiML6rjPaucaTnpdg4jfVQ\npXVbL7XUL+MM/20X2/JnlcIMHF3SnrJlAOFdPy+xAoGBALw7HF/dpOTw85hcjr40\nMJcqYHl6MMpZuvNxtmwR/OkuqI7yAe13fffXdr02ekKrnhDUU+dglfGi0B53em+8\nbxvZeQyr7o7TjdQlCtDYCqpIYKB+ig7uHV3gD4X73NQbWBialB7fiHn/OefDyoFe\nFPyr6MiicdQxonVwUNOZKHjd\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-l41vv@noti-discuss.iam.gserviceaccount.com",
    "client_id": "104223741460346907036",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-l41vv%40noti-discuss.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"

}


cred = credentials.Certificate(exmp)
firebase_admin.initialize_app(cred)


def send_noti_comments_post(*values):

    message = messaging.Message(
        data={
            "created_by": str({
                "id": (values[1].created_by.id),
                "username": (values[1].created_by.username),
                "image": (values[1].created_by.image)
            }),
            "type": "comment",
            "post":  str({
                "id": (values[1].post.id),
                "title": (values[1].post.title),
                "image": (values[1].post.post_image),
                "content": (values[1].post.content),
                "comment": (values[1].content),
            }),
        },
        token=values[2]
    )
    response = messaging.send(message)
    print('Successfully sent message:', response)


def send_noti_comments_poll(*values):

    message = messaging.Message(
        data={

            "created_by": str({
                "id": (values[1].created_by.id),
                "username": (values[1].created_by.username),
                "image": (values[1].created_by.image)
            }),
            "type": "comment",
            "poll":  str({
                "id": (values[1].poll.id),
                "title": (values[1].poll.title),
                "content": (values[1].poll.content),
                "comment": (values[1].content),
            }),
        },

        token=values[2]
    )
    response = messaging.send(message)
    print('Successfully sent message:', response)


def send_noti_commets_comments(*values):
    message = messaging.Message(
        data={
            "created_by": str({
                "id": (values[1].created_by.id),
                "username": (values[1].created_by.username),
                "image": (values[1].created_by.image)
            }),
            "type": "comment",
            "comment":  str({
                "id": (values[0].id),
                "content": (values[0].content),
                "comment": (values[1].content)
            }),
        },
        token=values[2]
    )
    response = messaging.send(message)
    print('Successfully sent message:', response)


def send_noti_like_post(*values):

    message = messaging.Message(
        data={
            "created_by": str({
                "id": (values[1].created_by.id),
                "username": (values[1].created_by.username),
                "image": (values[1].created_by.image)
            }),
            "type": "like",
            "post": str({
                "id": (values[1].post.id),
                "title": (values[1].post.title),
                "image": (values[1].post.post_image),
                "content": (values[1].post.content),
            }),
        },
        token=values[2]
    )
    response = messaging.send(message)
    print('Successfully sent message:', response)


def send_noti_like_poll(*values):
    message = messaging.Message(
        data={
            "created_by": str({
                "id": (values[1].created_by.id),
                "username": (values[1].created_by.username),
                "image": (values[1].created_by.image)
            }),
            "type": "like",
            "poll": str({
                "id": (values[1].poll.id),
                "title": (values[1].poll.title),
                "content": (values[1].poll.content),

            })
        },
        token=values[2]
    )
    response = messaging.send(message)
    print('Successfully sent message:', response)


def send_noti_like_comments(*values):
    message = messaging.Message(
        data={
            "created_by": str({
                "id": (values[1].created_by.id),
                "username": (values[1].created_by.username),
                "image": (values[1].created_by.image)
            }),
            "type": "like",
            "comment":  str({
                "id": (values[1].id),
                "content": (values[0].content),


            })
        },
        token=values[2]
    )
    response = messaging.send(message)
    print('Successfully sent message:', response)
