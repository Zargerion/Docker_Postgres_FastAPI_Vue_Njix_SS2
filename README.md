# Postgres + FastAPI + Vue + NGINX as reverse proxy.
All of this running as microservices with Docker containerization technology.

## Download 

So, now you need "git". If you haven't, google how to get (https://git-scm.com/book/ru/v2/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-Git).

Make a derectory. In this directory using console write:

```git clone https://github.com/Zargerion/TimerToShutDownDesktopAppWPFWithMVVM.git```

## Run

Now you need "docker". If you haven't, google how to get (For linux: https://docs.docker.com/engine/install/ubuntu/, for windows with WSL 2: https://docs.docker.com/desktop/install/windows-install/).

In your directory using console:

```docker-compose up -d```

...to start and run it in docker.

Now just open http://localhost:8082/ in your web browser.

P.S. You can unlock port 8082 for in and out trafic in firewall of your OS and unlock port in your home router to show this to people in internet.



