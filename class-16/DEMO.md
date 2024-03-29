# Serverless Functions

The completed demo is provided for reference. But the live demo should be built out from scratch.

## Create Project Skeleton

- > mkdir serverless
- > cd serverless
- > git init
- > mkdir api
- > touch api/date.py
- Follow the code from <https://vercel.com/docs/concepts/functions/supported-languages#python>.
- Type into `/api/date.py`
  - Explain each line of file.
- Add & commit changes.
- To push we need a Github repo.
  - Create EMPTY one at Github.
  - Make sure to skip adding README, etc steps.
  - Follow steps to push an existing repository from the command line.

## Vercel Dashboard

- Talk through process to Sign Up for Vercel Account at <https://vercel.com>
- Open browser at <https://vercel.com>
- Click `New Project` with GitHub as provider.
  - First timers will require an authorization step.
- In `Import Git Repository` click import button for `serverless`
  - Briefly mention how organization can be used, but it requires a paid plan.
- Leave default settings as is and click `Deploy` button.
- After a bit (30 seconds or so, usually) you'll see a success screen.
- Click `Go to Dashboard` button.
- Then the `Visit` button.
- At first you'll get a 404.
- But add `/api/date` to end of path and...
- Victory, the date shows!

## Add Another Function

- > touch api/howdy.py
- Follow the code from reference `api/howdy.py` and add it line by line with explanations.
- If we want to see it work then ACP.
- Now browse to dashboard for `serverless` project and note that project is rebuilding.
  - E.g. <https://vercel.com/your-github-name/serverless>
- Once done rebuilding browse to site + `/api/howdy` and should get "howdy"

## Add a Function that (optionally) parses query string

- > touch api/aloha.py
- Follow the code from reference `api/aloha.py` and add it line by line with explanations.
- Even though ACP + rebuild goes really fast all things considered, it's still too slow when early in development. We need something that shows our current work in a few seconds at most.
- It is possible to run a simple Python server to host our functions, but that would be pretty differerent from how it will run when hosted by Vercel.
- Thankfully, Vercel has a CLI client.
  - <https://vercel.com/cli>
  - > npm install --global vercel
  - From root of project...
  - > vercel
  - Then follow prompts entering `y` when asked.
  - This will trigger a remote build.
  - But you can also preview on a local server.
  - > vercel dev
  - Browse to <http://localhost:3000/api/aloha?name=Guido>.
  - If you make local changes and things looks good then ACP which will trigger build.

## Add a function with Dependencies

- So far we've been using standard library, no external dependencies.
- But often that won't be the case.
- For our next function we're going to build a handy word definer that makes use of `Requests` library.
- First let's initialize the project the usual way:
- Follow Lab Submission steps.
- Then let's add `requests` library
  - > pip install requests
- Record the addition in requirements
  - > pip freeze > requirements.txt
- > touch api/define.py
  - Copy code from reference `/api/define.py` and add line by line with explanations.
  - Run locally to make sure everything works.
    - E.g. <http://localhost:3000/api/define?word=python>
  - ACP and bask in glory of several serverless functions deployed to the cloud.
