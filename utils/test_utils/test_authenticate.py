import unittest
import unittest.mock as mock
import json
from utils.authenticate import Authenticate

TOKEN = 'afd53032060c50872c19e884c35e4ae00c046f73'
USER = 'raphaeljunior'


class FakeCommentResponse:
    def __call__(self, *args, **kwargs):
        return self

    def json(self):
        return [
            {
                "url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/comments/104651064",
                "pull_request_review_id": 25495549,
                "id": 104651064,
                "node_id": "MDI0OlB1bGxSZXF1ZXN0UmV2aWV3Q29tbWVudDEwNDY1MTA2NA==",
                "diff_hunk": "@@ -0,0 +1,19 @@\n+from sqlalchemy import create_engine\n+from sqlalchemy.orm import sessionmaker\n+from Models.Reviews import Review\n+URI = \"postgres://xeeqkeipvcflil:fead0f891152e8f657d7ee59ba256aa36c24fed629a0ee765b6a6aac6da2610f@ec2-54-225-236-102.compute-1.amazonaws.com:5432/d7mipabothqsm0\"",
                "path": "templates/home.py",
                "position": 4,
                "original_position": 4,
                "commit_id": "2f105655c58c3883814c214eb3b579f4695feda0",
                "original_commit_id": "2f105655c58c3883814c214eb3b579f4695feda0",
                "user": {
                    "login": "alanhdu",
                    "id": 1914111,
                    "node_id": "MDQ6VXNlcjE5MTQxMTE=",
                    "avatar_url": "https://avatars1.githubusercontent.com/u/1914111?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/alanhdu",
                    "html_url": "https://github.com/alanhdu",
                    "followers_url": "https://api.github.com/users/alanhdu/followers",
                    "following_url": "https://api.github.com/users/alanhdu/following{/other_user}",
                    "gists_url": "https://api.github.com/users/alanhdu/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/alanhdu/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/alanhdu/subscriptions",
                    "organizations_url": "https://api.github.com/users/alanhdu/orgs",
                    "repos_url": "https://api.github.com/users/alanhdu/repos",
                    "events_url": "https://api.github.com/users/alanhdu/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/alanhdu/received_events",
                    "type": "User",
                    "site_admin": False
                },
                "body": "Traditionally, we stored it in a config file that was `.gitignore`d and that we manually passed distributed around (although this is admittedly a bit of a PITA). The other way to do it is to have a `dev` environment where Postgres lives on the local machine (somewhere on `localhost`) and worry about a `prod` environment later.\r\n\r\nThere are lots of different ways to tackle this problem -- you should ask your mentor about what they think is best.",
                "created_at": "2017-03-07T12:03:46Z",
                "updated_at": "2017-03-07T12:03:47Z",
                "html_url": "https://github.com/ADI-Labs/culpa2/pull/2#discussion_r104651064",
                "pull_request_url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/2",
                "author_association": "NONE",
                "_links": {
                    "self": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/comments/104651064"
                    },
                    "html": {
                        "href": "https://github.com/ADI-Labs/culpa2/pull/2#discussion_r104651064"
                    },
                    "pull_request": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/2"
                    }
                },
                "in_reply_to_id": 104287330
            },
            {
                "url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/comments/104650803",
                "pull_request_review_id": 25495255,
                "id": 104650803,
                "node_id": "MDI0OlB1bGxSZXF1ZXN0UmV2aWV3Q29tbWVudDEwNDY1MDgwMw==",
                "diff_hunk": "@@ -0,0 +1,16 @@\n+from sqlalchemy.ext.declarative import declarative_base\n+from  sqlalchemy import Column, Integer, String\n+\n+\n+Base = declarative_base()\n+\n+\n+class course(Base):\n+    __tablename__ = 'courses'\n+    department_ids = Column(String)\n+    name = Column(String)\n+    id = Column(Integer)\n+    number = Column(Integer)\n+\n+    def __repr__(self):\n+        return str(self.name)",
                "path": "Models/Courses.py",
                "position": 16,
                "original_position": 16,
                "commit_id": "2f105655c58c3883814c214eb3b579f4695feda0",
                "original_commit_id": "2f105655c58c3883814c214eb3b579f4695feda0",
                "user": {
                    "login": "alanhdu",
                    "id": 1914111,
                    "node_id": "MDQ6VXNlcjE5MTQxMTE=",
                    "avatar_url": "https://avatars1.githubusercontent.com/u/1914111?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/alanhdu",
                    "html_url": "https://github.com/alanhdu",
                    "followers_url": "https://api.github.com/users/alanhdu/followers",
                    "following_url": "https://api.github.com/users/alanhdu/following{/other_user}",
                    "gists_url": "https://api.github.com/users/alanhdu/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/alanhdu/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/alanhdu/subscriptions",
                    "organizations_url": "https://api.github.com/users/alanhdu/orgs",
                    "repos_url": "https://api.github.com/users/alanhdu/repos",
                    "events_url": "https://api.github.com/users/alanhdu/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/alanhdu/received_events",
                    "type": "User",
                    "site_admin": False
                },
                "body": "If you're looking for a unique hash, I'd just implement `__hash__` instead. IMO, `__repr__` is most used for debugging and logging (which is the difference between `__repr__` and `__str__` -- `__str__` is end-user facing, while `__repr__` is usually programmer / machine facing).",
                "created_at": "2017-03-07T12:01:53Z",
                "updated_at": "2017-03-07T12:01:54Z",
                "html_url": "https://github.com/ADI-Labs/culpa2/pull/2#discussion_r104650803",
                "pull_request_url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/2",
                "author_association": "NONE",
                "_links": {
                    "self": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/comments/104650803"
                    },
                    "html": {
                        "href": "https://github.com/ADI-Labs/culpa2/pull/2#discussion_r104650803"
                    },
                    "pull_request": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/2"
                    }
                },
                "in_reply_to_id": 104287304
            },
            {
                "url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/comments/104650521",
                "pull_request_review_id": 25494974,
                "id": 104650521,
                "node_id": "MDI0OlB1bGxSZXF1ZXN0UmV2aWV3Q29tbWVudDEwNDY1MDUyMQ==",
                "diff_hunk": "@@ -0,0 +1,16 @@\n+from sqlalchemy.ext.declarative import declarative_base\n+from  sqlalchemy import Column, Integer, String\n+\n+\n+Base = declarative_base()\n+\n+\n+class course(Base):\n+    __tablename__ = 'courses'\n+    department_ids = Column(String)",
                "path": "Models/Courses.py",
                "position": 10,
                "original_position": 10,
                "commit_id": "2f105655c58c3883814c214eb3b579f4695feda0",
                "original_commit_id": "2f105655c58c3883814c214eb3b579f4695feda0",
                "user": {
                    "login": "alanhdu",
                    "id": 1914111,
                    "node_id": "MDQ6VXNlcjE5MTQxMTE=",
                    "avatar_url": "https://avatars1.githubusercontent.com/u/1914111?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/alanhdu",
                    "html_url": "https://github.com/alanhdu",
                    "followers_url": "https://api.github.com/users/alanhdu/followers",
                    "following_url": "https://api.github.com/users/alanhdu/following{/other_user}",
                    "gists_url": "https://api.github.com/users/alanhdu/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/alanhdu/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/alanhdu/subscriptions",
                    "organizations_url": "https://api.github.com/users/alanhdu/orgs",
                    "repos_url": "https://api.github.com/users/alanhdu/repos",
                    "events_url": "https://api.github.com/users/alanhdu/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/alanhdu/received_events",
                    "type": "User",
                    "site_admin": False
                },
                "body": "Well, depends on the database. Postgres supports arrays natively and so does SQLAlchemy (http://docs.sqlalchemy.org/en/latest/core/type_basics.html#sqlalchemy.types.ARRAY)",
                "created_at": "2017-03-07T12:00:08Z",
                "updated_at": "2017-03-07T12:00:09Z",
                "html_url": "https://github.com/ADI-Labs/culpa2/pull/2#discussion_r104650521",
                "pull_request_url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/2",
                "author_association": "NONE",
                "_links": {
                    "self": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/comments/104650521"
                    },
                    "html": {
                        "href": "https://github.com/ADI-Labs/culpa2/pull/2#discussion_r104650521"
                    },
                    "pull_request": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/2"
                    }
                },
                "in_reply_to_id": 104287306
            },
            {
                "url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/comments/104296820",
                "pull_request_review_id": 25132155,
                "id": 104296820,
                "node_id": "MDI0OlB1bGxSZXF1ZXN0UmV2aWV3Q29tbWVudDEwNDI5NjgyMA==",
                "diff_hunk": "@@ -0,0 +1,19 @@\n+from sqlalchemy import create_engine\n+from sqlalchemy.orm import sessionmaker\n+from Models.Reviews import Review\n+URI = \"postgres://xeeqkeipvcflil:fead0f891152e8f657d7ee59ba256aa36c24fed629a0ee765b6a6aac6da2610f@ec2-54-225-236-102.compute-1.amazonaws.com:5432/d7mipabothqsm0\"\n+engine = create_engine(URI)\n+engine.connect()\n+Session = sessionmaker(bind=engine)\n+session = Session()",
                "path": "templates/home.py",
                "position": 8,
                "original_position": 8,
                "commit_id": "2f105655c58c3883814c214eb3b579f4695feda0",
                "original_commit_id": "2f105655c58c3883814c214eb3b579f4695feda0",
                "user": {
                    "login": "Raphaeljunior",
                    "id": 6213945,
                    "node_id": "MDQ6VXNlcjYyMTM5NDU=",
                    "avatar_url": "https://avatars0.githubusercontent.com/u/6213945?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/Raphaeljunior",
                    "html_url": "https://github.com/Raphaeljunior",
                    "followers_url": "https://api.github.com/users/Raphaeljunior/followers",
                    "following_url": "https://api.github.com/users/Raphaeljunior/following{/other_user}",
                    "gists_url": "https://api.github.com/users/Raphaeljunior/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/Raphaeljunior/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/Raphaeljunior/subscriptions",
                    "organizations_url": "https://api.github.com/users/Raphaeljunior/orgs",
                    "repos_url": "https://api.github.com/users/Raphaeljunior/repos",
                    "events_url": "https://api.github.com/users/Raphaeljunior/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/Raphaeljunior/received_events",
                    "type": "User",
                    "site_admin": False
                },
                "body": "Will do. Still figuring out flask. Thanks ",
                "created_at": "2017-03-04T20:49:54Z",
                "updated_at": "2017-03-04T20:49:54Z",
                "html_url": "https://github.com/ADI-Labs/culpa2/pull/2#discussion_r104296820",
                "pull_request_url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/2",
                "author_association": "COLLABORATOR",
                "_links": {
                    "self": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/comments/104296820"
                    },
                    "html": {
                        "href": "https://github.com/ADI-Labs/culpa2/pull/2#discussion_r104296820"
                    },
                    "pull_request": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/2"
                    }
                },
                "in_reply_to_id": 104287326
            },
            {
                "url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/comments/104296815",
                "pull_request_review_id": 25132147,
                "id": 104296815,
                "node_id": "MDI0OlB1bGxSZXF1ZXN0UmV2aWV3Q29tbWVudDEwNDI5NjgxNQ==",
                "diff_hunk": "@@ -0,0 +1,19 @@\n+from sqlalchemy import create_engine\n+from sqlalchemy.orm import sessionmaker\n+from Models.Reviews import Review\n+URI = \"postgres://xeeqkeipvcflil:fead0f891152e8f657d7ee59ba256aa36c24fed629a0ee765b6a6aac6da2610f@ec2-54-225-236-102.compute-1.amazonaws.com:5432/d7mipabothqsm0\"",
                "path": "templates/home.py",
                "position": 4,
                "original_position": 4,
                "commit_id": "2f105655c58c3883814c214eb3b579f4695feda0",
                "original_commit_id": "2f105655c58c3883814c214eb3b579f4695feda0",
                "user": {
                    "login": "Raphaeljunior",
                    "id": 6213945,
                    "node_id": "MDQ6VXNlcjYyMTM5NDU=",
                    "avatar_url": "https://avatars0.githubusercontent.com/u/6213945?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/Raphaeljunior",
                    "html_url": "https://github.com/Raphaeljunior",
                    "followers_url": "https://api.github.com/users/Raphaeljunior/followers",
                    "following_url": "https://api.github.com/users/Raphaeljunior/following{/other_user}",
                    "gists_url": "https://api.github.com/users/Raphaeljunior/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/Raphaeljunior/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/Raphaeljunior/subscriptions",
                    "organizations_url": "https://api.github.com/users/Raphaeljunior/orgs",
                    "repos_url": "https://api.github.com/users/Raphaeljunior/repos",
                    "events_url": "https://api.github.com/users/Raphaeljunior/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/Raphaeljunior/received_events",
                    "type": "User",
                    "site_admin": False
                },
                "body": "Rookie move. How should I store the URI for database connections?",
                "created_at": "2017-03-04T20:49:30Z",
                "updated_at": "2017-03-04T20:49:30Z",
                "html_url": "https://github.com/ADI-Labs/culpa2/pull/2#discussion_r104296815",
                "pull_request_url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/2",
                "author_association": "COLLABORATOR",
                "_links": {
                    "self": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/comments/104296815"
                    },
                    "html": {
                        "href": "https://github.com/ADI-Labs/culpa2/pull/2#discussion_r104296815"
                    },
                    "pull_request": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/2"
                    }
                },
                "in_reply_to_id": 104287330
            },
            {
                "url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/comments/104296801",
                "pull_request_review_id": 25132130,
                "id": 104296801,
                "node_id": "MDI0OlB1bGxSZXF1ZXN0UmV2aWV3Q29tbWVudDEwNDI5NjgwMQ==",
                "diff_hunk": "@@ -0,0 +1,15 @@\n+from sqlalchemy.ext.declarative import declarative_base\n+from sqlalchemy import Column, String, Integer\n+\n+Base = declarative_base()\n+\n+class professor(Base):\n+    __tablename__ = 'professors'\n+    nugget = Column(String)\n+    first_name = Column(String)\n+    middle_name = Column(String)\n+    last_name = Column(String)",
                "path": "Models/Professors.py",
                "position": 11,
                "original_position": 11,
                "commit_id": "2f105655c58c3883814c214eb3b579f4695feda0",
                "original_commit_id": "2f105655c58c3883814c214eb3b579f4695feda0",
                "user": {
                    "login": "Raphaeljunior",
                    "id": 6213945,
                    "node_id": "MDQ6VXNlcjYyMTM5NDU=",
                    "avatar_url": "https://avatars0.githubusercontent.com/u/6213945?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/Raphaeljunior",
                    "html_url": "https://github.com/Raphaeljunior",
                    "followers_url": "https://api.github.com/users/Raphaeljunior/followers",
                    "following_url": "https://api.github.com/users/Raphaeljunior/following{/other_user}",
                    "gists_url": "https://api.github.com/users/Raphaeljunior/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/Raphaeljunior/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/Raphaeljunior/subscriptions",
                    "organizations_url": "https://api.github.com/users/Raphaeljunior/orgs",
                    "repos_url": "https://api.github.com/users/Raphaeljunior/repos",
                    "events_url": "https://api.github.com/users/Raphaeljunior/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/Raphaeljunior/received_events",
                    "type": "User",
                    "site_admin": False
                },
                "body": "Thanks. Nice read. ",
                "created_at": "2017-03-04T20:48:30Z",
                "updated_at": "2017-03-04T20:48:30Z",
                "html_url": "https://github.com/ADI-Labs/culpa2/pull/2#discussion_r104296801",
                "pull_request_url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/2",
                "author_association": "COLLABORATOR",
                "_links": {
                    "self": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/comments/104296801"
                    },
                    "html": {
                        "href": "https://github.com/ADI-Labs/culpa2/pull/2#discussion_r104296801"
                    },
                    "pull_request": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/2"
                    }
                },
                "in_reply_to_id": 104287345
            },
        ]


class FakeRepoResponse:

    def __call__(self, *args, **kwargs):
        return self



    def json(self):
        return [{
            "id": 80330248,
            "node_id": "MDEwOlJlcG9zaXRvcnk4MDMzMDI0OA==",
            "name": "culpa2",
            "full_name": "ADI-Labs/culpa2",
            "private": False,
            "owner": {
                "login": "ADI-Labs",
                "id": 14840390,
                "node_id": "MDEyOk9yZ2FuaXphdGlvbjE0ODQwMzkw",
                "avatar_url": "https://avatars0.githubusercontent.com/u/14840390?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/ADI-Labs",
                "html_url": "https://github.com/ADI-Labs",
                "followers_url": "https://api.github.com/users/ADI-Labs/followers",
                "following_url": "https://api.github.com/users/ADI-Labs/following{/other_user}",
                "gists_url": "https://api.github.com/users/ADI-Labs/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/ADI-Labs/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/ADI-Labs/subscriptions",
                "organizations_url": "https://api.github.com/users/ADI-Labs/orgs",
                "repos_url": "https://api.github.com/users/ADI-Labs/repos",
                "events_url": "https://api.github.com/users/ADI-Labs/events{/privacy}",
                "received_events_url": "https://api.github.com/users/ADI-Labs/received_events",
                "type": "Organization",
                "site_admin": False
            },
            "html_url": "https://github.com/ADI-Labs/culpa2",
            "description": None,
            "fork": False,
            "url": "https://api.github.com/repos/ADI-Labs/culpa2",
            "forks_url": "https://api.github.com/repos/ADI-Labs/culpa2/forks",
            "keys_url": "https://api.github.com/repos/ADI-Labs/culpa2/keys{/key_id}",
            "collaborators_url": "https://api.github.com/repos/ADI-Labs/culpa2/collaborators{/collaborator}",
            "teams_url": "https://api.github.com/repos/ADI-Labs/culpa2/teams",
            "hooks_url": "https://api.github.com/repos/ADI-Labs/culpa2/hooks",
            "issue_events_url": "https://api.github.com/repos/ADI-Labs/culpa2/issues/events{/number}",
            "events_url": "https://api.github.com/repos/ADI-Labs/culpa2/events",
            "assignees_url": "https://api.github.com/repos/ADI-Labs/culpa2/assignees{/user}",
            "branches_url": "https://api.github.com/repos/ADI-Labs/culpa2/branches{/branch}",
            "tags_url": "https://api.github.com/repos/ADI-Labs/culpa2/tags",
            "blobs_url": "https://api.github.com/repos/ADI-Labs/culpa2/git/blobs{/sha}",
            "git_tags_url": "https://api.github.com/repos/ADI-Labs/culpa2/git/tags{/sha}",
            "git_refs_url": "https://api.github.com/repos/ADI-Labs/culpa2/git/refs{/sha}",
            "trees_url": "https://api.github.com/repos/ADI-Labs/culpa2/git/trees{/sha}",
            "statuses_url": "https://api.github.com/repos/ADI-Labs/culpa2/statuses/{sha}",
            "languages_url": "https://api.github.com/repos/ADI-Labs/culpa2/languages",
            "stargazers_url": "https://api.github.com/repos/ADI-Labs/culpa2/stargazers",
            "contributors_url": "https://api.github.com/repos/ADI-Labs/culpa2/contributors",
            "subscribers_url": "https://api.github.com/repos/ADI-Labs/culpa2/subscribers",
            "subscription_url": "https://api.github.com/repos/ADI-Labs/culpa2/subscription",
            "commits_url": "https://api.github.com/repos/ADI-Labs/culpa2/commits{/sha}",
            "git_commits_url": "https://api.github.com/repos/ADI-Labs/culpa2/git/commits{/sha}",
            "comments_url": "https://api.github.com/repos/ADI-Labs/culpa2/comments{/number}",
            "issue_comment_url": "https://api.github.com/repos/ADI-Labs/culpa2/issues/comments{/number}",
            "contents_url": "https://api.github.com/repos/ADI-Labs/culpa2/contents/{+path}",
            "compare_url": "https://api.github.com/repos/ADI-Labs/culpa2/compare/{base}...{head}",
            "merges_url": "https://api.github.com/repos/ADI-Labs/culpa2/merges",
            "archive_url": "https://api.github.com/repos/ADI-Labs/culpa2/{archive_format}{/ref}",
            "downloads_url": "https://api.github.com/repos/ADI-Labs/culpa2/downloads",
            "issues_url": "https://api.github.com/repos/ADI-Labs/culpa2/issues{/number}",
            "pulls_url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls{/number}",
            "milestones_url": "https://api.github.com/repos/ADI-Labs/culpa2/milestones{/number}",
            "notifications_url": "https://api.github.com/repos/ADI-Labs/culpa2/notifications{?since,all,participating}",
            "labels_url": "https://api.github.com/repos/ADI-Labs/culpa2/labels{/name}",
            "releases_url": "https://api.github.com/repos/ADI-Labs/culpa2/releases{/id}",
            "deployments_url": "https://api.github.com/repos/ADI-Labs/culpa2/deployments",
            "created_at": "2017-01-29T05:26:14Z",
            "updated_at": "2017-02-16T17:15:30Z",
            "pushed_at": "2017-04-28T18:04:09Z",
            "git_url": "git://github.com/ADI-Labs/culpa2.git",
            "ssh_url": "git@github.com:ADI-Labs/culpa2.git",
            "clone_url": "https://github.com/ADI-Labs/culpa2.git",
            "svn_url": "https://github.com/ADI-Labs/culpa2",
            "homepage": None,
            "size": 292,
            "stargazers_count": 0,
            "watchers_count": 0,
            "language": "Python",
            "has_issues": True,
            "has_projects": True,
            "has_downloads": True,
            "has_wiki": True,
            "has_pages": False,
            "forks_count": 1,
            "mirror_url": None,
            "archived": False,
            "open_issues_count": 0,
            "license": None,
            "forks": 1,
            "open_issues": 0,
            "watchers": 0,
            "default_branch": "master",
            "permissions": {
                "admin": True,
                "push": True,
                "pull": True
            }
        },
            {
                "id": 43304196,
                "node_id": "MDEwOlJlcG9zaXRvcnk0MzMwNDE5Ng==",
                "name": "Edtech",
                "full_name": "edtechALA/Edtech",
                "private": False,
                "owner": {
                    "login": "edtechALA",
                    "id": 14873695,
                    "node_id": "MDQ6VXNlcjE0ODczNjk1",
                    "avatar_url": "https://avatars1.githubusercontent.com/u/14873695?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/edtechALA",
                    "html_url": "https://github.com/edtechALA",
                    "followers_url": "https://api.github.com/users/edtechALA/followers",
                    "following_url": "https://api.github.com/users/edtechALA/following{/other_user}",
                    "gists_url": "https://api.github.com/users/edtechALA/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/edtechALA/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/edtechALA/subscriptions",
                    "organizations_url": "https://api.github.com/users/edtechALA/orgs",
                    "repos_url": "https://api.github.com/users/edtechALA/repos",
                    "events_url": "https://api.github.com/users/edtechALA/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/edtechALA/received_events",
                    "type": "User",
                    "site_admin": False
                },
                "html_url": "https://github.com/edtechALA/Edtech",
                "description": None,
                "fork": False,
                "url": "https://api.github.com/repos/edtechALA/Edtech",
                "forks_url": "https://api.github.com/repos/edtechALA/Edtech/forks",
                "keys_url": "https://api.github.com/repos/edtechALA/Edtech/keys{/key_id}",
                "collaborators_url": "https://api.github.com/repos/edtechALA/Edtech/collaborators{/collaborator}",
                "teams_url": "https://api.github.com/repos/edtechALA/Edtech/teams",
                "hooks_url": "https://api.github.com/repos/edtechALA/Edtech/hooks",
                "issue_events_url": "https://api.github.com/repos/edtechALA/Edtech/issues/events{/number}",
                "events_url": "https://api.github.com/repos/edtechALA/Edtech/events",
                "assignees_url": "https://api.github.com/repos/edtechALA/Edtech/assignees{/user}",
                "branches_url": "https://api.github.com/repos/edtechALA/Edtech/branches{/branch}",
                "tags_url": "https://api.github.com/repos/edtechALA/Edtech/tags",
                "blobs_url": "https://api.github.com/repos/edtechALA/Edtech/git/blobs{/sha}",
                "git_tags_url": "https://api.github.com/repos/edtechALA/Edtech/git/tags{/sha}",
                "git_refs_url": "https://api.github.com/repos/edtechALA/Edtech/git/refs{/sha}",
                "trees_url": "https://api.github.com/repos/edtechALA/Edtech/git/trees{/sha}",
                "statuses_url": "https://api.github.com/repos/edtechALA/Edtech/statuses/{sha}",
                "languages_url": "https://api.github.com/repos/edtechALA/Edtech/languages",
                "stargazers_url": "https://api.github.com/repos/edtechALA/Edtech/stargazers",
                "contributors_url": "https://api.github.com/repos/edtechALA/Edtech/contributors",
                "subscribers_url": "https://api.github.com/repos/edtechALA/Edtech/subscribers",
                "subscription_url": "https://api.github.com/repos/edtechALA/Edtech/subscription",
                "commits_url": "https://api.github.com/repos/edtechALA/Edtech/commits{/sha}",
                "git_commits_url": "https://api.github.com/repos/edtechALA/Edtech/git/commits{/sha}",
                "comments_url": "https://api.github.com/repos/edtechALA/Edtech/comments{/number}",
                "issue_comment_url": "https://api.github.com/repos/edtechALA/Edtech/issues/comments{/number}",
                "contents_url": "https://api.github.com/repos/edtechALA/Edtech/contents/{+path}",
                "compare_url": "https://api.github.com/repos/edtechALA/Edtech/compare/{base}...{head}",
                "merges_url": "https://api.github.com/repos/edtechALA/Edtech/merges",
                "archive_url": "https://api.github.com/repos/edtechALA/Edtech/{archive_format}{/ref}",
                "downloads_url": "https://api.github.com/repos/edtechALA/Edtech/downloads",
                "issues_url": "https://api.github.com/repos/edtechALA/Edtech/issues{/number}",
                "pulls_url": "https://api.github.com/repos/edtechALA/Edtech/pulls{/number}",
                "milestones_url": "https://api.github.com/repos/edtechALA/Edtech/milestones{/number}",
                "notifications_url": "https://api.github.com/repos/edtechALA/Edtech/notifications{?since,all,participating}",
                "labels_url": "https://api.github.com/repos/edtechALA/Edtech/labels{/name}",
                "releases_url": "https://api.github.com/repos/edtechALA/Edtech/releases{/id}",
                "deployments_url": "https://api.github.com/repos/edtechALA/Edtech/deployments",
                "created_at": "2015-09-28T13:59:04Z",
                "updated_at": "2015-09-28T16:00:15Z",
                "pushed_at": "2015-09-28T16:50:03Z",
                "git_url": "git://github.com/edtechALA/Edtech.git",
                "ssh_url": "git@github.com:edtechALA/Edtech.git",
                "clone_url": "https://github.com/edtechALA/Edtech.git",
                "svn_url": "https://github.com/edtechALA/Edtech",
                "homepage": None,
                "size": 836,
                "stargazers_count": 0,
                "watchers_count": 0,
                "language": "JavaScript",
                "has_issues": True,
                "has_projects": True,
                "has_downloads": True,
                "has_wiki": True,
                "has_pages": True,
                "forks_count": 0,
                "mirror_url": None,
                "archived": False,
                "open_issues_count": 0,
                "license": {
                    "key": "apache-2.0",
                    "name": "Apache License 2.0",
                    "spdx_id": "Apache-2.0",
                    "url": "https://api.github.com/licenses/apache-2.0",
                    "node_id": "MDc6TGljZW5zZTI="
                },
                "forks": 0,
                "open_issues": 0,
                "watchers": 0,
                "default_branch": "gh-pages",
                "permissions": {
                    "admin": False,
                    "push": True,
                    "pull": True
                }
            },
            {
                "id": 112245428,
                "node_id": "MDEwOlJlcG9zaXRvcnkxMTIyNDU0Mjg=",
                "name": "UE-Programmieren-WS17",
                "full_name": "ikeaohnea/UE-Programmieren-WS17",
                "private": True,
                "owner": {
                    "login": "ikeaohnea",
                    "id": 25034299,
                    "node_id": "MDQ6VXNlcjI1MDM0Mjk5",
                    "avatar_url": "https://avatars2.githubusercontent.com/u/25034299?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/ikeaohnea",
                    "html_url": "https://github.com/ikeaohnea",
                    "followers_url": "https://api.github.com/users/ikeaohnea/followers",
                    "following_url": "https://api.github.com/users/ikeaohnea/following{/other_user}",
                    "gists_url": "https://api.github.com/users/ikeaohnea/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/ikeaohnea/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/ikeaohnea/subscriptions",
                    "organizations_url": "https://api.github.com/users/ikeaohnea/orgs",
                    "repos_url": "https://api.github.com/users/ikeaohnea/repos",
                    "events_url": "https://api.github.com/users/ikeaohnea/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/ikeaohnea/received_events",
                    "type": "User",
                    "site_admin": False
                },
                "html_url": "https://github.com/ikeaohnea/UE-Programmieren-WS17",
                "description": None,
                "fork": False,
                "url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17",
                "forks_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/forks",
                "keys_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/keys{/key_id}",
                "collaborators_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/collaborators{/collaborator}",
                "teams_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/teams",
                "hooks_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/hooks",
                "issue_events_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/issues/events{/number}",
                "events_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/events",
                "assignees_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/assignees{/user}",
                "branches_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/branches{/branch}",
                "tags_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/tags",
                "blobs_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/git/blobs{/sha}",
                "git_tags_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/git/tags{/sha}",
                "git_refs_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/git/refs{/sha}",
                "trees_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/git/trees{/sha}",
                "statuses_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/statuses/{sha}",
                "languages_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/languages",
                "stargazers_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/stargazers",
                "contributors_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/contributors",
                "subscribers_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/subscribers",
                "subscription_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/subscription",
                "commits_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/commits{/sha}",
                "git_commits_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/git/commits{/sha}",
                "comments_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/comments{/number}",
                "issue_comment_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/issues/comments{/number}",
                "contents_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/contents/{+path}",
                "compare_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/compare/{base}...{head}",
                "merges_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/merges",
                "archive_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/{archive_format}{/ref}",
                "downloads_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/downloads",
                "issues_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/issues{/number}",
                "pulls_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/pulls{/number}",
                "milestones_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/milestones{/number}",
                "notifications_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/notifications{?since,all,participating}",
                "labels_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/labels{/name}",
                "releases_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/releases{/id}",
                "deployments_url": "https://api.github.com/repos/ikeaohnea/UE-Programmieren-WS17/deployments",
                "created_at": "2017-11-27T20:33:14Z",
                "updated_at": "2017-11-27T20:43:29Z",
                "pushed_at": "2017-12-19T00:53:33Z",
                "git_url": "git://github.com/ikeaohnea/UE-Programmieren-WS17.git",
                "ssh_url": "git@github.com:ikeaohnea/UE-Programmieren-WS17.git",
                "clone_url": "https://github.com/ikeaohnea/UE-Programmieren-WS17.git",
                "svn_url": "https://github.com/ikeaohnea/UE-Programmieren-WS17",
                "homepage": None,
                "size": 448,
                "stargazers_count": 0,
                "watchers_count": 0,
                "language": "C#",
                "has_issues": True,
                "has_projects": True,
                "has_downloads": True,
                "has_wiki": True,
                "has_pages": False,
                "forks_count": 0,
                "mirror_url": None,
                "archived": False,
                "open_issues_count": 0,
                "license": None,
                "forks": 0,
                "open_issues": 0,
                "watchers": 0,
                "default_branch": "master",
                "permissions": {
                    "admin": False,
                    "push": True,
                    "pull": True
                }
            },
            {
                "id": 110898776,
                "node_id": "MDEwOlJlcG9zaXRvcnkxMTA4OTg3NzY=",
                "name": "Web-Dev.-Semesterprojekt-WS1",
                "full_name": "ikeaohnea/Web-Dev.-Semesterprojekt-WS1",
                "private": True,
                "owner": {
                    "login": "ikeaohnea",
                    "id": 25034299,
                    "node_id": "MDQ6VXNlcjI1MDM0Mjk5",
                    "avatar_url": "https://avatars2.githubusercontent.com/u/25034299?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/ikeaohnea",
                    "html_url": "https://github.com/ikeaohnea",
                    "followers_url": "https://api.github.com/users/ikeaohnea/followers",
                    "following_url": "https://api.github.com/users/ikeaohnea/following{/other_user}",
                    "gists_url": "https://api.github.com/users/ikeaohnea/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/ikeaohnea/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/ikeaohnea/subscriptions",
                    "organizations_url": "https://api.github.com/users/ikeaohnea/orgs",
                    "repos_url": "https://api.github.com/users/ikeaohnea/repos",
                    "events_url": "https://api.github.com/users/ikeaohnea/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/ikeaohnea/received_events",
                    "type": "User",
                    "site_admin": False
                },
                "html_url": "https://github.com/ikeaohnea/Web-Dev.-Semesterprojekt-WS1",
                "description": None,
                "fork": False,
                "url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1",
                "forks_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/forks",
                "keys_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/keys{/key_id}",
                "collaborators_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/collaborators{/collaborator}",
                "teams_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/teams",
                "hooks_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/hooks",
                "issue_events_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/issues/events{/number}",
                "events_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/events",
                "assignees_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/assignees{/user}",
                "branches_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/branches{/branch}",
                "tags_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/tags",
                "blobs_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/git/blobs{/sha}",
                "git_tags_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/git/tags{/sha}",
                "git_refs_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/git/refs{/sha}",
                "trees_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/git/trees{/sha}",
                "statuses_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/statuses/{sha}",
                "languages_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/languages",
                "stargazers_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/stargazers",
                "contributors_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/contributors",
                "subscribers_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/subscribers",
                "subscription_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/subscription",
                "commits_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/commits{/sha}",
                "git_commits_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/git/commits{/sha}",
                "comments_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/comments{/number}",
                "issue_comment_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/issues/comments{/number}",
                "contents_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/contents/{+path}",
                "compare_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/compare/{base}...{head}",
                "merges_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/merges",
                "archive_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/{archive_format}{/ref}",
                "downloads_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/downloads",
                "issues_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/issues{/number}",
                "pulls_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/pulls{/number}",
                "milestones_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/milestones{/number}",
                "notifications_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/notifications{?since,all,participating}",
                "labels_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/labels{/name}",
                "releases_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/releases{/id}",
                "deployments_url": "https://api.github.com/repos/ikeaohnea/Web-Dev.-Semesterprojekt-WS1/deployments",
                "created_at": "2017-11-15T23:29:30Z",
                "updated_at": "2017-11-15T23:30:33Z",
                "pushed_at": "2017-11-19T02:11:53Z",
                "git_url": "git://github.com/ikeaohnea/Web-Dev.-Semesterprojekt-WS1.git",
                "ssh_url": "git@github.com:ikeaohnea/Web-Dev.-Semesterprojekt-WS1.git",
                "clone_url": "https://github.com/ikeaohnea/Web-Dev.-Semesterprojekt-WS1.git",
                "svn_url": "https://github.com/ikeaohnea/Web-Dev.-Semesterprojekt-WS1",
                "homepage": None,
                "size": 513,
                "stargazers_count": 0,
                "watchers_count": 0,
                "language": "HTML",
                "has_issues": True,
                "has_projects": True,
                "has_downloads": True,
                "has_wiki": True,
                "has_pages": False,
                "forks_count": 0,
                "mirror_url": None,
                "archived": False,
                "open_issues_count": 1,
                "license": None,
                "forks": 0,
                "open_issues": 1,
                "watchers": 0,
                "default_branch": "master",
                "permissions": {
                    "admin": False,
                    "push": True,
                    "pull": True
                }
            }]


class FakeResponse:
    def json(self):
        return {
            "json": {
                "login": "Raphaeljunior",
                "id": 6213945,
                "node_id": "MDQ6VXNlcjYyMTM5NDU=",
                "avatar_url": "https://avatars0.githubusercontent.com/u/6213945?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/Raphaeljunior",
                "html_url": "https://github.com/Raphaeljunior",
                "followers_url": "https://api.github.com/users/Raphaeljunior/followers",
                "following_url": "https://api.github.com/users/Raphaeljunior/following{/other_user}",
                "gists_url": "https://api.github.com/users/Raphaeljunior/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/Raphaeljunior/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/Raphaeljunior/subscriptions",
                "organizations_url": "https://api.github.com/users/Raphaeljunior/orgs",
                "repos_url": "https://api.github.com/users/Raphaeljunior/repos",
                "events_url": "https://api.github.com/users/Raphaeljunior/events{/privacy}",
                "received_events_url": "https://api.github.com/users/Raphaeljunior/received_events",
                "type": "User",
                "site_admin": False,
                "name": None,
                "company": None,
                "blog": "",
                "location": None,
                "email": None,
                "hireable": None,
                "bio": None,
                "public_repos": 120,
                "public_gists": 1,
                "followers": 7,
                "following": 10,
                "created_at": "2013-12-18T11:31:17Z",
                "updated_at": "2018-10-26T15:13:40Z",
                "private_gists": 3,
                "total_private_repos": 8,
                "owned_private_repos": 8,
                "disk_usage": 167702,
                "collaborators": 2,
                "two_factor_authentication": False,
                "plan": {
                    "name": "developer",
                    "space": 976562499,
                    "collaborators": 0,
                    "private_repos": 9999
                }
            }
        }


class FakePRResponse:
    def __call__(self, *args, **kwargs):
        return self

    def json(self):
        return [
            {
                "url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/2",
                "id": 108917217,
                "node_id": "MDExOlB1bGxSZXF1ZXN0MTA4OTE3MjE3",
                "html_url": "https://github.com/ADI-Labs/culpa2/pull/2",
                "diff_url": "https://github.com/ADI-Labs/culpa2/pull/2.diff",
                "patch_url": "https://github.com/ADI-Labs/culpa2/pull/2.patch",
                "issue_url": "https://api.github.com/repos/ADI-Labs/culpa2/issues/2",
                "number": 2,
                "state": "closed",
                "locked": False,
                "title": "Set up db schema and created models",
                "user": {
                    "login": "Raphaeljunior",
                    "id": 6213945,
                    "node_id": "MDQ6VXNlcjYyMTM5NDU=",
                    "avatar_url": "https://avatars0.githubusercontent.com/u/6213945?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/Raphaeljunior",
                    "html_url": "https://github.com/Raphaeljunior",
                    "followers_url": "https://api.github.com/users/Raphaeljunior/followers",
                    "following_url": "https://api.github.com/users/Raphaeljunior/following{/other_user}",
                    "gists_url": "https://api.github.com/users/Raphaeljunior/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/Raphaeljunior/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/Raphaeljunior/subscriptions",
                    "organizations_url": "https://api.github.com/users/Raphaeljunior/orgs",
                    "repos_url": "https://api.github.com/users/Raphaeljunior/repos",
                    "events_url": "https://api.github.com/users/Raphaeljunior/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/Raphaeljunior/received_events",
                    "type": "User",
                    "site_admin": False
                },
                "body": "",
                "created_at": "2017-03-03T06:54:13Z",
                "updated_at": "2017-03-07T12:03:47Z",
                "closed_at": "2017-03-03T06:54:19Z",
                "merged_at": "2017-03-03T06:54:19Z",
                "merge_commit_sha": "bbc94ae73b748ec249f33712cb51a9dc7ec82bd6",
                "assignee": None,
                "assignees": [],
                "requested_reviewers": [],
                "requested_teams": [],
                "labels": [],
                "milestone": None,
                "commits_url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/2/commits",
                "review_comments_url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/2/comments",
                "review_comment_url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/comments{/number}",
                "comments_url": "https://api.github.com/repos/ADI-Labs/culpa2/issues/2/comments",
                "statuses_url": "https://api.github.com/repos/ADI-Labs/culpa2/statuses/2f105655c58c3883814c214eb3b579f4695feda0",
                "head": {
                    "label": "ADI-Labs:setupDatabase",
                    "ref": "setupDatabase",
                    "sha": "2f105655c58c3883814c214eb3b579f4695feda0",
                    "user": {
                        "login": "ADI-Labs",
                        "id": 14840390,
                        "node_id": "MDEyOk9yZ2FuaXphdGlvbjE0ODQwMzkw",
                        "avatar_url": "https://avatars0.githubusercontent.com/u/14840390?v=4",
                        "gravatar_id": "",
                        "url": "https://api.github.com/users/ADI-Labs",
                        "html_url": "https://github.com/ADI-Labs",
                        "followers_url": "https://api.github.com/users/ADI-Labs/followers",
                        "following_url": "https://api.github.com/users/ADI-Labs/following{/other_user}",
                        "gists_url": "https://api.github.com/users/ADI-Labs/gists{/gist_id}",
                        "starred_url": "https://api.github.com/users/ADI-Labs/starred{/owner}{/repo}",
                        "subscriptions_url": "https://api.github.com/users/ADI-Labs/subscriptions",
                        "organizations_url": "https://api.github.com/users/ADI-Labs/orgs",
                        "repos_url": "https://api.github.com/users/ADI-Labs/repos",
                        "events_url": "https://api.github.com/users/ADI-Labs/events{/privacy}",
                        "received_events_url": "https://api.github.com/users/ADI-Labs/received_events",
                        "type": "Organization",
                        "site_admin": False
                    },
                    "repo": {
                        "id": 80330248,
                        "node_id": "MDEwOlJlcG9zaXRvcnk4MDMzMDI0OA==",
                        "name": "culpa2",
                        "full_name": "ADI-Labs/culpa2",
                        "private": False,
                        "owner": {
                            "login": "ADI-Labs",
                            "id": 14840390,
                            "node_id": "MDEyOk9yZ2FuaXphdGlvbjE0ODQwMzkw",
                            "avatar_url": "https://avatars0.githubusercontent.com/u/14840390?v=4",
                            "gravatar_id": "",
                            "url": "https://api.github.com/users/ADI-Labs",
                            "html_url": "https://github.com/ADI-Labs",
                            "followers_url": "https://api.github.com/users/ADI-Labs/followers",
                            "following_url": "https://api.github.com/users/ADI-Labs/following{/other_user}",
                            "gists_url": "https://api.github.com/users/ADI-Labs/gists{/gist_id}",
                            "starred_url": "https://api.github.com/users/ADI-Labs/starred{/owner}{/repo}",
                            "subscriptions_url": "https://api.github.com/users/ADI-Labs/subscriptions",
                            "organizations_url": "https://api.github.com/users/ADI-Labs/orgs",
                            "repos_url": "https://api.github.com/users/ADI-Labs/repos",
                            "events_url": "https://api.github.com/users/ADI-Labs/events{/privacy}",
                            "received_events_url": "https://api.github.com/users/ADI-Labs/received_events",
                            "type": "Organization",
                            "site_admin": False
                        },
                        "html_url": "https://github.com/ADI-Labs/culpa2",
                        "description": None,
                        "fork": False,
                        "url": "https://api.github.com/repos/ADI-Labs/culpa2",
                        "forks_url": "https://api.github.com/repos/ADI-Labs/culpa2/forks",
                        "keys_url": "https://api.github.com/repos/ADI-Labs/culpa2/keys{/key_id}",
                        "collaborators_url": "https://api.github.com/repos/ADI-Labs/culpa2/collaborators{/collaborator}",
                        "teams_url": "https://api.github.com/repos/ADI-Labs/culpa2/teams",
                        "hooks_url": "https://api.github.com/repos/ADI-Labs/culpa2/hooks",
                        "issue_events_url": "https://api.github.com/repos/ADI-Labs/culpa2/issues/events{/number}",
                        "events_url": "https://api.github.com/repos/ADI-Labs/culpa2/events",
                        "assignees_url": "https://api.github.com/repos/ADI-Labs/culpa2/assignees{/user}",
                        "branches_url": "https://api.github.com/repos/ADI-Labs/culpa2/branches{/branch}",
                        "tags_url": "https://api.github.com/repos/ADI-Labs/culpa2/tags",
                        "blobs_url": "https://api.github.com/repos/ADI-Labs/culpa2/git/blobs{/sha}",
                        "git_tags_url": "https://api.github.com/repos/ADI-Labs/culpa2/git/tags{/sha}",
                        "git_refs_url": "https://api.github.com/repos/ADI-Labs/culpa2/git/refs{/sha}",
                        "trees_url": "https://api.github.com/repos/ADI-Labs/culpa2/git/trees{/sha}",
                        "statuses_url": "https://api.github.com/repos/ADI-Labs/culpa2/statuses/{sha}",
                        "languages_url": "https://api.github.com/repos/ADI-Labs/culpa2/languages",
                        "stargazers_url": "https://api.github.com/repos/ADI-Labs/culpa2/stargazers",
                        "contributors_url": "https://api.github.com/repos/ADI-Labs/culpa2/contributors",
                        "subscribers_url": "https://api.github.com/repos/ADI-Labs/culpa2/subscribers",
                        "subscription_url": "https://api.github.com/repos/ADI-Labs/culpa2/subscription",
                        "commits_url": "https://api.github.com/repos/ADI-Labs/culpa2/commits{/sha}",
                        "git_commits_url": "https://api.github.com/repos/ADI-Labs/culpa2/git/commits{/sha}",
                        "comments_url": "https://api.github.com/repos/ADI-Labs/culpa2/comments{/number}",
                        "issue_comment_url": "https://api.github.com/repos/ADI-Labs/culpa2/issues/comments{/number}",
                        "contents_url": "https://api.github.com/repos/ADI-Labs/culpa2/contents/{+path}",
                        "compare_url": "https://api.github.com/repos/ADI-Labs/culpa2/compare/{base}...{head}",
                        "merges_url": "https://api.github.com/repos/ADI-Labs/culpa2/merges",
                        "archive_url": "https://api.github.com/repos/ADI-Labs/culpa2/{archive_format}{/ref}",
                        "downloads_url": "https://api.github.com/repos/ADI-Labs/culpa2/downloads",
                        "issues_url": "https://api.github.com/repos/ADI-Labs/culpa2/issues{/number}",
                        "pulls_url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls{/number}",
                        "milestones_url": "https://api.github.com/repos/ADI-Labs/culpa2/milestones{/number}",
                        "notifications_url": "https://api.github.com/repos/ADI-Labs/culpa2/notifications{?since,all,participating}",
                        "labels_url": "https://api.github.com/repos/ADI-Labs/culpa2/labels{/name}",
                        "releases_url": "https://api.github.com/repos/ADI-Labs/culpa2/releases{/id}",
                        "deployments_url": "https://api.github.com/repos/ADI-Labs/culpa2/deployments",
                        "created_at": "2017-01-29T05:26:14Z",
                        "updated_at": "2017-02-16T17:15:30Z",
                        "pushed_at": "2017-04-28T18:04:09Z",
                        "git_url": "git://github.com/ADI-Labs/culpa2.git",
                        "ssh_url": "git@github.com:ADI-Labs/culpa2.git",
                        "clone_url": "https://github.com/ADI-Labs/culpa2.git",
                        "svn_url": "https://github.com/ADI-Labs/culpa2",
                        "homepage": None,
                        "size": 292,
                        "stargazers_count": 0,
                        "watchers_count": 0,
                        "language": "Python",
                        "has_issues": True,
                        "has_projects": True,
                        "has_downloads": True,
                        "has_wiki": True,
                        "has_pages": False,
                        "forks_count": 1,
                        "mirror_url": None,
                        "archived": False,
                        "open_issues_count": 0,
                        "license": None,
                        "forks": 1,
                        "open_issues": 0,
                        "watchers": 0,
                        "default_branch": "master"
                    }
                },
                "base": {
                    "label": "ADI-Labs:master",
                    "ref": "master",
                    "sha": "35641af3fe950e5100940ba77d1993e0179ef690",
                    "user": {
                        "login": "ADI-Labs",
                        "id": 14840390,
                        "node_id": "MDEyOk9yZ2FuaXphdGlvbjE0ODQwMzkw",
                        "avatar_url": "https://avatars0.githubusercontent.com/u/14840390?v=4",
                        "gravatar_id": "",
                        "url": "https://api.github.com/users/ADI-Labs",
                        "html_url": "https://github.com/ADI-Labs",
                        "followers_url": "https://api.github.com/users/ADI-Labs/followers",
                        "following_url": "https://api.github.com/users/ADI-Labs/following{/other_user}",
                        "gists_url": "https://api.github.com/users/ADI-Labs/gists{/gist_id}",
                        "starred_url": "https://api.github.com/users/ADI-Labs/starred{/owner}{/repo}",
                        "subscriptions_url": "https://api.github.com/users/ADI-Labs/subscriptions",
                        "organizations_url": "https://api.github.com/users/ADI-Labs/orgs",
                        "repos_url": "https://api.github.com/users/ADI-Labs/repos",
                        "events_url": "https://api.github.com/users/ADI-Labs/events{/privacy}",
                        "received_events_url": "https://api.github.com/users/ADI-Labs/received_events",
                        "type": "Organization",
                        "site_admin": False
                    },
                    "repo": {
                        "id": 80330248,
                        "node_id": "MDEwOlJlcG9zaXRvcnk4MDMzMDI0OA==",
                        "name": "culpa2",
                        "full_name": "ADI-Labs/culpa2",
                        "private": False,
                        "owner": {
                            "login": "ADI-Labs",
                            "id": 14840390,
                            "node_id": "MDEyOk9yZ2FuaXphdGlvbjE0ODQwMzkw",
                            "avatar_url": "https://avatars0.githubusercontent.com/u/14840390?v=4",
                            "gravatar_id": "",
                            "url": "https://api.github.com/users/ADI-Labs",
                            "html_url": "https://github.com/ADI-Labs",
                            "followers_url": "https://api.github.com/users/ADI-Labs/followers",
                            "following_url": "https://api.github.com/users/ADI-Labs/following{/other_user}",
                            "gists_url": "https://api.github.com/users/ADI-Labs/gists{/gist_id}",
                            "starred_url": "https://api.github.com/users/ADI-Labs/starred{/owner}{/repo}",
                            "subscriptions_url": "https://api.github.com/users/ADI-Labs/subscriptions",
                            "organizations_url": "https://api.github.com/users/ADI-Labs/orgs",
                            "repos_url": "https://api.github.com/users/ADI-Labs/repos",
                            "events_url": "https://api.github.com/users/ADI-Labs/events{/privacy}",
                            "received_events_url": "https://api.github.com/users/ADI-Labs/received_events",
                            "type": "Organization",
                            "site_admin": False
                        },
                        "html_url": "https://github.com/ADI-Labs/culpa2",
                        "description": None,
                        "fork": False,
                        "url": "https://api.github.com/repos/ADI-Labs/culpa2",
                        "forks_url": "https://api.github.com/repos/ADI-Labs/culpa2/forks",
                        "keys_url": "https://api.github.com/repos/ADI-Labs/culpa2/keys{/key_id}",
                        "collaborators_url": "https://api.github.com/repos/ADI-Labs/culpa2/collaborators{/collaborator}",
                        "teams_url": "https://api.github.com/repos/ADI-Labs/culpa2/teams",
                        "hooks_url": "https://api.github.com/repos/ADI-Labs/culpa2/hooks",
                        "issue_events_url": "https://api.github.com/repos/ADI-Labs/culpa2/issues/events{/number}",
                        "events_url": "https://api.github.com/repos/ADI-Labs/culpa2/events",
                        "assignees_url": "https://api.github.com/repos/ADI-Labs/culpa2/assignees{/user}",
                        "branches_url": "https://api.github.com/repos/ADI-Labs/culpa2/branches{/branch}",
                        "tags_url": "https://api.github.com/repos/ADI-Labs/culpa2/tags",
                        "blobs_url": "https://api.github.com/repos/ADI-Labs/culpa2/git/blobs{/sha}",
                        "git_tags_url": "https://api.github.com/repos/ADI-Labs/culpa2/git/tags{/sha}",
                        "git_refs_url": "https://api.github.com/repos/ADI-Labs/culpa2/git/refs{/sha}",
                        "trees_url": "https://api.github.com/repos/ADI-Labs/culpa2/git/trees{/sha}",
                        "statuses_url": "https://api.github.com/repos/ADI-Labs/culpa2/statuses/{sha}",
                        "languages_url": "https://api.github.com/repos/ADI-Labs/culpa2/languages",
                        "stargazers_url": "https://api.github.com/repos/ADI-Labs/culpa2/stargazers",
                        "contributors_url": "https://api.github.com/repos/ADI-Labs/culpa2/contributors",
                        "subscribers_url": "https://api.github.com/repos/ADI-Labs/culpa2/subscribers",
                        "subscription_url": "https://api.github.com/repos/ADI-Labs/culpa2/subscription",
                        "commits_url": "https://api.github.com/repos/ADI-Labs/culpa2/commits{/sha}",
                        "git_commits_url": "https://api.github.com/repos/ADI-Labs/culpa2/git/commits{/sha}",
                        "comments_url": "https://api.github.com/repos/ADI-Labs/culpa2/comments{/number}",
                        "issue_comment_url": "https://api.github.com/repos/ADI-Labs/culpa2/issues/comments{/number}",
                        "contents_url": "https://api.github.com/repos/ADI-Labs/culpa2/contents/{+path}",
                        "compare_url": "https://api.github.com/repos/ADI-Labs/culpa2/compare/{base}...{head}",
                        "merges_url": "https://api.github.com/repos/ADI-Labs/culpa2/merges",
                        "archive_url": "https://api.github.com/repos/ADI-Labs/culpa2/{archive_format}{/ref}",
                        "downloads_url": "https://api.github.com/repos/ADI-Labs/culpa2/downloads",
                        "issues_url": "https://api.github.com/repos/ADI-Labs/culpa2/issues{/number}",
                        "pulls_url": "https://api.github.com/repos/ADI-Labs/culpa2/pulls{/number}",
                        "milestones_url": "https://api.github.com/repos/ADI-Labs/culpa2/milestones{/number}",
                        "notifications_url": "https://api.github.com/repos/ADI-Labs/culpa2/notifications{?since,all,participating}",
                        "labels_url": "https://api.github.com/repos/ADI-Labs/culpa2/labels{/name}",
                        "releases_url": "https://api.github.com/repos/ADI-Labs/culpa2/releases{/id}",
                        "deployments_url": "https://api.github.com/repos/ADI-Labs/culpa2/deployments",
                        "created_at": "2017-01-29T05:26:14Z",
                        "updated_at": "2017-02-16T17:15:30Z",
                        "pushed_at": "2017-04-28T18:04:09Z",
                        "git_url": "git://github.com/ADI-Labs/culpa2.git",
                        "ssh_url": "git@github.com:ADI-Labs/culpa2.git",
                        "clone_url": "https://github.com/ADI-Labs/culpa2.git",
                        "svn_url": "https://github.com/ADI-Labs/culpa2",
                        "homepage": None,
                        "size": 292,
                        "stargazers_count": 0,
                        "watchers_count": 0,
                        "language": "Python",
                        "has_issues": True,
                        "has_projects": True,
                        "has_downloads": True,
                        "has_wiki": True,
                        "has_pages": False,
                        "forks_count": 1,
                        "mirror_url": None,
                        "archived": False,
                        "open_issues_count": 0,
                        "license": None,
                        "forks": 1,
                        "open_issues": 0,
                        "watchers": 0,
                        "default_branch": "master"
                    }
                },
                "_links": {
                    "self": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/2"
                    },
                    "html": {
                        "href": "https://github.com/ADI-Labs/culpa2/pull/2"
                    },
                    "issue": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/issues/2"
                    },
                    "comments": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/issues/2/comments"
                    },
                    "review_comments": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/2/comments"
                    },
                    "review_comment": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/comments{/number}"
                    },
                    "commits": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/pulls/2/commits"
                    },
                    "statuses": {
                        "href": "https://api.github.com/repos/ADI-Labs/culpa2/statuses/2f105655c58c3883814c214eb3b579f4695feda0"
                    }
                },
                "author_association": "COLLABORATOR"
            }
        ]


class FakeReviewResponse:
    def __call__(self, *args, **kwargs):
        return self

    def json(self):
        return {'reviews':[]}


class FakeRepoIssuesResponse:
    def __call__(self, *args, **kwargs):
        return self

    def json(self):
        return {'Issues':[]}


class FakeCommentsIssuesResponse:
    def __call__(self, *args, **kwargs):
        return self

    def json(self):
        return {'Comments':[]}


class FakePostPRCommentResponse:
    def __call__(self, *args, **kwargs):
        return self

    def json(self):
        return {'response':{}}


class FakeEditPRCommentResponse:
    def __call__(self, *args, **kwargs):
        return self

    def json(self):
        return {
            'response': {}
        }


class FakeDeletePRCommentResponse:
    def __call__(self, *args, **kwargs):
        return self

    def json(self):
        return {
            'response': {},
            'status_code': 204
        }

    def status_code(self):
        return 204


def mock_delete_pr_response():
    return FakeDeletePRCommentResponse()


def mock_edit_pr_comment_response():
    return FakeEditPRCommentResponse()


def mock_post_pr_comment(*args, **kwargs):
    return FakePostPRCommentResponse()


def mocked_fake_comments_issues_response(*args, **kwargs):
    return FakeCommentsIssuesResponse()


def mocked_fake_repo_issues_response(*args, **kwargs):
    return FakeRepoIssuesResponse()


def mocked_requests_get(*args, **kwargs):
    return FakeResponse()


def mocked_repo_response(*args, **kwargs):
    return FakeRepoResponse()


def mocked_pr_response(*args, **kwargs):
    return FakePRResponse()


def mocked_comment_response(*args, **kwargs):
    return FakeCommentResponse()


def mocked_pr_reviews_response(*args, **kwargs):
    return FakeReviewResponse()


class TestAuthenticate(unittest.TestCase):

    def setUp(self):
        self.authenticate = Authenticate(TOKEN, USER)

    @mock.patch('requests.get', mocked_requests_get)
    def test_get_profile(self):
        self.authenticate.get_profile()
        self.assertDictEqual(self.authenticate.profile, mocked_requests_get().json())

    @mock.patch('requests.get', mocked_repo_response())
    def test_load_repos(self):
        self.authenticate.load_repos()
        self.assertListEqual(self.authenticate.repos, mocked_repo_response().json())

    @mock.patch('requests.get', mocked_pr_response())
    def test_get_pr(self):
        pull_requests = self.authenticate.get_pull_requests('owner', 'repo')
        self.assertListEqual(pull_requests, mocked_pr_response().json())

    @mock.patch('requests.get', mocked_comment_response())
    def test_get_pr_comments(self):
        pr_comments = self.authenticate.get_pr_comments('owner', 'repo', 5)
        print(json.dumps(pr_comments, indent=2))
        self.assertListEqual(pr_comments, mocked_comment_response().json())

    @mock.patch('requests.get', mocked_pr_reviews_response())
    def test_get_pr_reviews(self):
        pr_review = self.authenticate.get_pr_reviews('owner', 'repo', 5)
        self.assertDictEqual(pr_review, mocked_pr_reviews_response().json())

    @mock.patch('requests.get', mocked_fake_repo_issues_response())
    def test_get_repo_issues(self):
        repo_issues = self.authenticate.get_repo_issues('owner', 'repo')
        self.assertDictEqual(repo_issues, mocked_fake_repo_issues_response().json())

    @mock.patch('requests.get', mocked_fake_comments_issues_response())
    def test_get_comments_issues(self):
        issue_comments = self.authenticate.get_comments_on_issue('owner', 'repo', 9)
        self.assertDictEqual(issue_comments, mocked_fake_comments_issues_response().json())

    @mock.patch('requests.post', mock_post_pr_comment())
    def test_post_comment_response(self):
        post_comment_response = self.authenticate.post_pr_comment('owner','repo', 9, 'Comment', 'sha', '/home.c', '90')
        self.assertDictEqual(post_comment_response, mock_post_pr_comment().json())

    @mock.patch('requests.patch', mock_edit_pr_comment_response())
    def test_edit_comment_response(self):
        edit_comment_response = self.authenticate.edit_pr_comment('owner', 'repo', 9, 'Edited')
        self.assertDictEqual(edit_comment_response, mock_edit_pr_comment_response().json())

    @mock.patch('requests.delete', mock_delete_pr_response())
    def test_delete_comment_response(self):
        delete_comment_response = self.authenticate.del_pr_comment('owner', 'repo', 9)
        self.assertEqual(delete_comment_response, mock_delete_pr_response().status_code())

