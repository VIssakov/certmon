# Certmon

## Description

Small test project to monitor SSL certificates where i learn python, docker, nodejs and how to create beautifull app. 

What this app will do (in future): <br>
1. Add certificate via url;
2. Upload certficiate manualy;
3. Fetch certificates from vault;
4. Notice about expiration via: telegram, slack, mail; 
5. Create different dashboard for different users;
6. Share dashboard with different groups of users;

### Requirements
1. Docker

### How to run
``` 
git clone https://github.com/VIssakov/certmon.git
cd certmon
docker-compose up -d 
```
### ROADMAP

- add requirements file [X]
- Add main page [X]
- Add simple form to add a site for monitoring  [X]
- Add logic for extracting certificate from url [X]
- Print extension from cert (like alt names and etc) [X]
- delete "X509Name object" from subject and issuer [X]
- Add url validator [X]
- Add logic to fetch port from url for non standart port [X]
- Add pupop windows with cert information [X]
- Add error of connection to url []
- Add check error if url is correct, ex: https://yoomoney []
- Add error of fetching certificate []
- Add table with websites on monitoring [X]
- Add save fuctions for certificate [X]
- Update window with certs after save [X]
- Check duplicates [X]
- Add delete fuctions for certificate []
- Add notice about experation via telegramm []
- Add button for recreating CSR for certificate []
- Add auth []
- Add groups and dashboard for groups []
- Update files and functions structure []
- cool front []
- add more logs []
