# Plane App API
**What is CS Pro Plane App?**

CS Pro Plane is a versatile and comprehensive project management software built for teams that prioritize delivering exceptional customer
value. Ideal for product development, IT services, professional services, agencies, and design firms, this software enables mission-critical
teams to streamline their workflows, collaborate effectively, and achieve their goals.
With CS Pro Plane, you can seamlessly integrate your workflows, enhance team collaboration, and maintain full visibility over your projects.
Its flexible features cater to various methodologies and processes, ensuring that every team can operate in a way that best suits their
unique needs. By centralizing all project activities in one place, this app helps you stay organized, prioritize tasks effectively, and deliver
outstanding results.



## Features

- Issues: Quickly create issues and add details using a powerful rich text editor that supports file uploads. Add sub-properties and references to problems for better organization and tracking.
- Sprints: Keep up your team's momentum with sprints. Gain insights into your project's progress with burn-down charts and other valuable features.
- Modules: Break down your large projects into smaller, more manageable modules. Assign modules between teams to track and plan your project's progress easily.
- Analytics: Get insights into all your CS Pro Plane data in real-time. Visualize issue data to spot trends, remove blockers, and progress your work.
- Time tracking (coming soon): CS Pro Plane also includes a powerful time tracking feature, allowing teams to monitor the time spent on tasks and projects accurately.


## Windows/Linux/MAC Installation

Setting up local environment is extremely easy and straight forward. Follow the below step and you will be ready to contribute.

1. Clone the code locally using:

```bash
  git clone -b main https://github.com/Cyber-Square-Pro/cspro-plane-api.git
```

2. Create and activate Virtuale Environment:  
   Create:   
```bash
    python -m venv plane_env
```

  Activate:    
  On Windows,
  
```bash
   cd plane_env/scripts
```
On Linux/Mac

```bash
   cd plane_env/scripts
   source activate
```

3. Switch to project folder using:
```bash
  cd ../../cspro-plane-api
```

4. Install psycopg2 library.

```bash
   pip install psycopg2
```

If the above command fails to execute

```bash
   pip install psycopg2-binary
```

5. Install packages from requirements.txt

```bash
   pip install -r requirements.txt
```

6. Run migrations.

```bash
   python manage.py migrate
```

7. Run the development server using.

```bash
  python manage.py runserver
```

8. Open http://localhost:8000 with your browser to see the application.

9. You can test your API using Postman.

## Testing endpoints using Postman

Signup:  http://127.0.0.1:8000/api/user/sign-up/
![a8714280-0b7d-4ac2-8bf6-8366f1d397d3](https://github.com/user-attachments/assets/5d6eccad-f1aa-42df-bffa-f74a37d0830b)

**SMALL CHANGES TO VIEW THE CI Pipeline Run