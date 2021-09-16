# Vision for Steffi

The plan for this project is to make it easy and fast to create GraphQL based services over exisitng SQL tables. In the future, I want this to support many different types of DBs and complex graphs.

# How can you help?

First off, thanks so much for wanting to jump in and help. I really appreciate your effort.

## Help Needed

### Developers / Code reviewers

Right now, Steffi is in it's infancy and first, we need to get an MVP out. Secondly, I would love to expand it's capabilities to cover more db types and more complex table structures. To do that, I'd love some developer help as well as some code review help.

### Adoption

Adoption is going to really help me. Finding things that don't work and edge cases I missed will go a long way to creating a stable and usable project.

### Promotion

Lastly, if you like the project, I'd love some help spreading the word via blogs or tutorials or really anything. Tell your friend you found something cool.

## Please don't

### Misuising the issue tracker

- Problems related to the underlying libraries driving the service (e.g. Flask)
- Problems with your specific domain which made the service not work
- Connection issues to your db

### Campsite PRs

- PRs with code touched that's not related to the issue being solved. For this, open a separate issue and a separate PR. This helps lower the amount of work for the code reviewer and makes your intent more clear

# Code of Conduct

## Interacting with others

1. First and foremost, treat others with respect.
1. Come to every interaction with good intent and assume the person you are interacting with has done the same.
1. Don't intentionally use someone else's time to save time for yourself. Try to find answers on your own and only get help when you're blocked.

## Responsibilities

### Product Owners

1. Ensure timely response to PRs (< 2 week turn around time)
1. Ensure changes that are approved are integrated back into the project.

### Contributors

1. Follow the guidelines set up in this doc
1. Ensure code is passing tests / linter before asking for code review
1. Understand that this is a side project and time to work is limited, it may take a while for your changes to be encorporated

### Code Standards

1. Follow PEP-8 coding standard https://www.python.org/dev/peps/pep-0008/
1. Import statements are in alphabetical order by major library

# Contacting me

Feel free to message me on Twitter `@jonschwartz`. I'm not super active there, but if someone tags me, I'll jump on.

# Setup and Such

## Submitting an issue / Suggesting a new feature

- Submit an issue using the issue template
- Label the issue accordingly using existing labels in the project (especially important for "good first issue" issues)

## Submitting a PR

- Subit a PR using the PR template.
- All PRs must be tied to an issue to be considered for merging. (if one doesn't exist, go make one)

## Setting up your environment

- Have Python3 installed on your machine

## Running the unit tests

- `python3 -m unittest steffi_test.py -v`
