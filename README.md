# AI-Conversation-Model

Assume you are having a set of questions.You can create a CSV file and fetch it from there.
Questions should come in sequence.

- User answers a question asked by a Model.
- Based on User's Answer Model will ask the next set of questions.
Ideally, consider that we need to create an AI-Conversation Model which is smart enough to ask
a question based on the user's answer.

For example,
AI - What is your name ?

User : XYZ

AI - What is your email address?

User : xyz @yahoo.com

AI - What is your gender ?

User : Female

AI - Are you playing football?

user - No

AI - When did you get a visit for your premature delivery ?

User - 24th sep 2009


============================

So in the above example, If a user has selected MALE as gender then
AI MUST NOT ASK "When did you get a visit for your premature delivery ?" question
