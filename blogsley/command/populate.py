from blogsley.config import db
from blogsley.user import User
from blogsley.post import Post

model = '''
{
  "type": "page",
  "id": "FlvecVm25UUdxaHPkK372",
  "_value": null,
  "html": "",
  "children": [
    {
      "type": "title",
      "id": "AyvlfqRvbeGiA3qz3Hcoz",
      "_value": "New Post",
      "html": "<h1>New Post</h1>",
      "children": []
    },
    {
      "type": "paragraph",
      "id": "FfL-2TYOAcqq0JCbZ5JwF",
      "_value": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
      "html": "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>",
      "children": [],
      "content": {
        "type": "doc",
        "content": [
          {
            "type": "paragraph",
            "content": [
              {
                "type": "text",
                "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
              }
            ]
          }
        ]
      }
    },
    {
      "type": "image",
      "id": "Cu8rpdKFpRZVYaIE5J3pR",
      "_value": null,
      "html": "",
      "children": [],
      "src": "statics/images/journal-on-desk.jpg",
      "width": 256,
      "height": 256
    },
    {
      "type": "heading",
      "id": "DYtlZEO5sl2Px2tKbs8pc",
      "_value": "Heading",
      "html": "<h2>Heading</h2>",
      "children": [],
      "content": {
        "type": "doc",
        "content": [
          {
            "type": "heading",
            "attrs": {
              "level": 2
            },
            "content": [
              {
                "type": "text",
                "text": "Heading"
              }
            ]
          }
        ]
      }
    },
    {
      "type": "paragraph",
      "id": "ziJ1QdChrCeqcga6RSDth",
      "_value": "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
      "html": "<p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>",
      "children": [],
      "content": {
        "type": "doc",
        "content": [
          {
            "type": "paragraph",
            "content": [
              {
                "type": "text",
                "text": "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
              }
            ]
          }
        ]
      }
    },
    {
      "type": "html",
      "id": "gAqzLTydpx4ROvrD50aRk",
      "_value": null,
      "html": "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p><p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>",
      "children": [],
      "content": {
        "type": "doc",
        "content": [
          {
            "type": "paragraph",
            "content": [
              {
                "type": "text",
                "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
              }
            ]
          },
          {
            "type": "paragraph",
            "content": [
              {
                "type": "text",
                "text": "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
              }
            ]
          }
        ]
      }
    },
    {
      "type": "list",
      "id": "KdC9aI7RS9osTwSMKBxEG",
      "_value": [
        "Get Milk",
        "Get Bread",
        "Get Butter"
      ],
      "html": "<ul><li><p>Get Milk</p></li><li><p>Get Bread</p></li><li><p>Get Butter</p></li></ul>",
      "children": [],
      "content": {
        "type": "doc",
        "content": [
          {
            "type": "bullet_list",
            "content": [
              {
                "type": "list_item",
                "content": [
                  {
                    "type": "paragraph",
                    "content": [
                      {
                        "type": "text",
                        "text": "Get Milk"
                      }
                    ]
                  }
                ]
              },
              {
                "type": "list_item",
                "content": [
                  {
                    "type": "paragraph",
                    "content": [
                      {
                        "type": "text",
                        "text": "Get Bread"
                      }
                    ]
                  }
                ]
              },
              {
                "type": "list_item",
                "content": [
                  {
                    "type": "paragraph",
                    "content": [
                      {
                        "type": "text",
                        "text": "Get Butter"
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      }
    }
  ]
}
'''
@db_session
def populate():
  u = User(username='admin',
    first_name='The',
    last_name='Admin',
    email='admin@example.com',
    role='Admin',
    about_me='I am the Admin'
  )
  u.set_password('admin')

  u = User(username='john',
    first_name='John',
    last_name='Doe',
    email='john@example.com',
    role='Editor',
    about_me='I am an Editor'
  )
  u.set_password('x')

  p = Post(
    title='Pugsley, a python user group webapp',
    model=model,
    body='Pugsley is a webapp written in Python',
    author=u
  )

  u = User(
    username='susan',
    first_name='Susan',
    last_name='Smith',
    email='susan@example.com',
    role='Author',
    about_me='I am an Author'
  )
  u.set_password('x')

  p = Post(
    title='Python is cool!',
    model=model,
    body='I love writing programs in Python',
    author=u
  )

  u = User(
    username='joe',
    first_name='Joe',
    last_name='Jackson',
    email='joe@example.com',
    role='Reader',
    about_me='I am a Reader'
  )
  u.set_password('x')

  users = User.query.all()
  print(users)

  posts = Post.query.all()
  for p in posts:
    print(p.id, p.author.username, p.body)