# git-repository-details
Short recruitment task #1

### Instruction
Create a simple REST service which will return details of given Github repository. Details should include:
* full name of repository
* description of repository
* git clone url
* number of stargazers
* date of creation (ISO format)

The API of the service should look as follows:
```
GET /repositories/{owner}/{repository-name}
```
```
{
  "fullName": "...",
  "description": "...",
  "cloneUrl": "...",
  "stars": 0,
  "createdAt": "..."
}
```
