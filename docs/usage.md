in order to trigger a new repository creation all u have to do is run the following command:
`curl -X POST -H "Content-Type: application/json" -d '{"repo_name": "< you repo name >", "description": "< some description >"}' http://localhost:80/create`

u should recieve the following respone:
`{"success":"Successfully created repository"}`

and a reponse code of `201`