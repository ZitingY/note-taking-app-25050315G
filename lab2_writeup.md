- Deploying a Flask Project with Supabase on Vercel -

1. Refactor the app to use Postgres in Supabase (Cloud database)
   To connect the app with Supabase easier, if the data of old database that using SQLite is not important, directly connect the app with Supabase using Postgres.
   - create a new project in Supabase
   - click the connect button on the top of the project page
     <img width="153" height="69" alt="截屏2025-10-19 22 44 53" src="https://github.com/user-attachments/assets/109ef133-291d-4df3-b186-c620f27bdf75" />
   - choose "session pooler" in the method block if your app is on Github/Vercel and copy the URL"postgresql://postgres.amhevfolcgjkjokkuikn:[YOUR-PASSWORD]@aws-1-us-east-1.pooler.supabase.com:5432/postgres"
     <img width="1027" height="548" alt="截屏2025-10-19 22 43 09" src="https://github.com/user-attachments/assets/d9593026-8e73-453d-aefb-dbe9621046e2" />
   - save the URL in your .env file like DATABASE_URL = "..."
   - update main.py by adding " app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
                                app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False " and delete the code related to SQLite
   - run the app and check your database table in Supabase
   - type "pip install psycopg2-binary" in your terminal if there is an error saying No module named 'psycopg2'

2. Refactor the app and deploy the app in Vercel
   - Reminder: vercel only can import public repository for free
   - Problem 1: How to convert private fork repository to public one
     - (Actually I tried for even 1 hour to solve this problem asking AI for help, but still cannot find a easy way to solve it perfectly)
      - A method solve the problem completely but wasting time: create a new public repository, copy all the files in private repository and paste them in new public one
   - Problem 2: How to deploy your app on Vercel correctly
      - create a new project
      - import your Git repository
      - fill in all the link information in the environment variables section, for example DATABASE_URL, GITHUB_TOKEN, etc. Or import .env file
      - click the deploy button
      - check logs and error if it cannot deploy correctly
        tips: make sure requirements.txt is complete

3. Notes:
  - Always use environment variables for secrets
  - After editing the code, remember git add . -> git commit -m "...." -> git push origin main/dev -> merge
  - Branch protection and GitHub fork/private repo rules may block direct pushes
