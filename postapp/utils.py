import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials
from django.conf import settings
import json

exmp = {
    "type": "service_account",
    "project_id": "discussion-noti-94921",
    "private_key_id": "89a5322b6f65228b3b7b726e58268267a2645667",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDIQ2LpBl4VlkbM\n4XL76jE2gT+o0fkPtusfpfOVlDNztyCeKtCLDQ+zp2orDCz75hH00/yzGd9lUXxk\nlNfhpgZXV9MZYnXTkgIk9M9h1DGjDcLuSsQava37j1CFuddVrkG6M/tPsWjT7RAI\nE6YhJ25mR4wN2f9iPVHgMbc9zR/mNVKVR5VJGJI2+5hQ0NIKRgku+lPnF4tyEMV9\nMEgoLgaxBXXjcpowRFz3D65vv+De6j+dJQu8gtQf1XkwNVDDMsXx9sr8iY89XtYa\n6yvjeBZRa8sM8aAKYtu8mwgtuhYfT2Tgp//PvrNQ+bFeqXO3KnGw/F8gZICx3VhN\nhVm29osHAgMBAAECggEAPe3MyAfej2ll4pSzVKDC8Dp+36tzDD+CLUrJ7U8jrByM\n2yydSerTmLhkVgSRYqJumhn2EsKk+TV+NLJsogyP+HGhx79RdYg43onQGc4fPW+T\ngNIhG63dgCX8/iWOqCHXlIffpvDTXHn6U60T2jvR4ZIthtkLpysURzLImjV1MGBv\n4E2zQ2QAl6E3Y3LNrfkQsvuo1UnJ/RrCEZUri7BDVP27aFQ7mH+83G6DqutSxlwi\nkTsFjKaDzraV4rMZly10+iyy4yPn7j+jRoxN4CFcGrofWISUR2iJ5jPgWPj4klA1\nA20CMGRmSvsa4g4heCbWoSFdQLaadkUHXJ0NZ100CQKBgQDoPGsK2QMuo8beNvra\nxz3f8YyNXNxRcxDPw5qsBQsJhnX3f9MXFYRonNWOYlcgPnOw1JRG8gBgxdscBbS3\n6AKFT5J7J5EOAI08P7wa+nBzZ4WQN8EvSA8NsJuI6Nk/AzSQZ3ZGsB2Yw75AEYj+\nJkQdTLkdBZ1YifDvZjlCSLeLnwKBgQDcwWtVtKn2iWMisguPe5ZPP4Itk8eET0PG\n9Uj4zHq8Em1INgo2gMcs3usLFaoC91HYPQdLaTnRpoIlnvQ5ToClFg03MiNoTpc1\n8yoCDmXPFee+pIH2KzRHU7EmA/djJBp8G1cuUlGy2Nph6FUE9RJHLecBE2JIyqBA\nb6ULKpVHmQKBgQDIRPH6VNKNseaZUshZSmBtcpxGe8Hy60ugH4qOtXqjKDUqzix3\nR7L7k+QF+YAw6ipSX7/Ovnrc+ULOk40Y2xbxZ4FmeuR4MrmZL01D5px6qNdhWvNZ\nlsaEg7xdAI/36we1T8OLiey8BHFYRsbghJdQvQ0VnfXmmG4RxRGzu4ms+QKBgQDQ\nr8BKGyn5N9ORvwKSt2BWtlDXyTX5a/1EnihHmvYDyN+qPfvVnlOrpWhI6Ef52ddz\nNe4paeYQvPmXmvaBHica6QfBQBKczn6/r4nsu7Oe2rRjUpzRG/Kl4wY6S9GX1U98\nN1RpI8S776gymjGVKCAJTels6Ogmq/ZmM6SwM6c/MQKBgQDVeGinM4Q0veQn5NQB\nA3lLgZveevlxJu3srR7rCpwvRc2Fsdpfz8Hi44GsxYWV1MSsYOwsAXmW6nGE560q\npEIKEtJLOA0WC0oonWh8jum9+4Tau2ZOVKoewOMHqAoCA6qSCL/PhmU7SWMUZbMa\nQv+PI5aLZJwKubgvn8s0rLxQNA==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-ox85o@discussion-noti-94921.iam.gserviceaccount.com",
    "client_id": "108762647299071594926",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ox85o%40discussion-noti-94921.iam.gserviceaccount.com"
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
                "comment": (values[1].content),
            }),
        },

        token=values[2]
    )
    response = messaging.send(message)
    print('Successfully sent message:', response)


def send_noti_commets_comments(*values):
    print("1111",values[0].content)
    print("2222",values[1].content)
    print("3333",values[2])
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
                "comment":(values[1].content)
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
                "content": (values[1].content),
            })
        },
        token=values[2]
    )
    response = messaging.send(message)
    print('Successfully sent message:', response)
