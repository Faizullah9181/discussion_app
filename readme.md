## Discussion App Backend 
# Django 4.0.0
# Python 3.9


## Api Documentation https://documenter.getpostman.com/view/19537571/2s8ZDSdRRu#6347c334-a1af-4a46-9f2a-05eaebffbd97
```
{
	"info": {
		"_postman_id": "9c787747-3fc7-4573-b594-0abd455b40b6",
		"name": "Local",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "23354370"
	},
	"item": [
		{
			"name": "Auth",
			"item": [
				{
					"name": "Register",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "username",
									"value": "alpha7",
									"type": "text"
								},
								{
									"key": "password",
									"value": "bug@9450.",
									"type": "text"
								},
								{
									"key": "email",
									"value": "alpha7@gmail.com",
									"type": "text"
								},
								{
									"key": "last_name",
									"value": "bug",
									"type": "text",
									"disabled": true
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/users/register/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"users",
								"register",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Login",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY5MTI1MzgzLCJqdGkiOiIyMTkyZTk5NjE3Yjg0MDRkODQ1NjI1MzZhZDY3ZWQwOSIsInVzZXJfaWQiOjV9.ObE5GSyKfPDBBWGy6sU4gL7L2TuNxZIkDWcov_VeMKg",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "username",
									"value": "alpha7",
									"description": "enter username/email in username field",
									"type": "text"
								},
								{
									"key": "password",
									"value": "bug@9450.",
									"type": "text"
								},
								{
									"key": "email",
									"value": "bug@gmail.com",
									"type": "text",
									"disabled": true
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/users/login/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"users",
								"login",
								""
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "User",
			"item": [
				{
					"name": "Update",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwNTA4MzA5LCJqdGkiOiJhYWQ4MTFlMzZhZGE0ODkzYTNlZWJkM2E4ZmY4MTRkMCIsInVzZXJfaWQiOjR9.jOG2KqOUBMM0l8iepOk8_6iz_TUpPIZDTPEQo8GOnss",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "username",
									"value": "alpha7",
									"type": "text"
								},
								{
									"key": "first_name",
									"value": "69",
									"type": "text"
								},
								{
									"key": "last_name",
									"value": "69",
									"type": "text"
								},
								{
									"key": "mobile_no",
									"value": "69696969696",
									"type": "text"
								},
								{
									"key": "image",
									"value": "99",
									"type": "text"
								},
								{
									"key": "address",
									"value": "asassdsd",
									"type": "text"
								},
								{
									"key": "dob",
									"value": "2022-01-01",
									"type": "text"
								},
								{
									"key": "email",
									"value": "alpha7@gmail.com",
									"type": "text"
								},
								{
									"key": "gender",
									"value": "M",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/users/profile/update/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"users",
								"profile",
								"update",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Details",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxODA0OTM3LCJqdGkiOiJlMzU4OTBmMTExNjI0YzEzODQ3NmFmYzJiOWY4MzkwOSIsInVzZXJfaWQiOjV9.97OPZ0KowGg4MVYWTRKc2M77NSeoA8TlefN7TeSsFrc",
								"type": "text"
							}
						],
						"url": {
							"raw": "http://127.0.0.1:8000/api/users/details/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"users",
								"details",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Profile",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwNDk4MTM1LCJqdGkiOiI0NjIwMmFkZWRlMzc0N2VjODRmYzhmY2UxMDZkOTNmNSIsInVzZXJfaWQiOjN9.kol6SvhsRXHtuGlkT9hGqvV4o6ftkgsJaeHUKZzyEiY",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/users/profile/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"users",
								"profile",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "GetUserById",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwNzY4Nzg5LCJqdGkiOiJkNWVmMThiNzE1Y2Q0NDdiODA3YmNlZTBmNTU5Yzc0ZCIsInVzZXJfaWQiOjR9.Br2rjUUsDHJ4iBFDsS9tHs-Bo4V12moQn4VoaDW711g",
								"type": "text"
							}
						],
						"url": {
							"raw": "http://127.0.0.1:8000/api/users/getuserbyId/2/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"users",
								"getuserbyId",
								"2",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "UserImage",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwNTY1MTY1LCJqdGkiOiIxMjUzNjZjMzU5YmU0YzBkYTRhMTExMmU4YmUwZGU2YiIsInVzZXJfaWQiOjR9.RqUO8QigstUBDUVckYtKvOjhMB0hmg_ECB3FUM7sIp4",
								"type": "text"
							}
						],
						"url": {
							"raw": "http://127.0.0.1:8000/api/users/usernameImage/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"users",
								"usernameImage",
								""
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Post",
			"item": [
				{
					"name": "Create_Post",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{TOKEN}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxMjAzNjMwLCJqdGkiOiI0ZWEyYTFkYWRlOGQ0YTEwYmUwMzIwY2Y0YzFmMGZiNSIsInVzZXJfaWQiOjZ9.535Z3YYiQoToFkC3uALlBfan6Bb97aQR32WVNhvDwGI",
								"type": "text",
								"disabled": true
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "title",
									"value": "tets5",
									"type": "text"
								},
								{
									"key": "content",
									"value": "check44",
									"type": "text"
								},
								{
									"key": "allow_comments",
									"value": "True",
									"type": "text"
								},
								{
									"key": "post_image",
									"value": "zdsadsadasad",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/post/create/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"post",
								"create",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Update_Post",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwNDg3MjU2LCJqdGkiOiI3ODRiMzVhMGFkNTM0NjE5YjEzMDE5NTllODI3OTI3NSIsInVzZXJfaWQiOjJ9.SemEqn7vWDiUr2MiiPqrvYIvts6AlZQzKHIGBFGMLYM",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "title",
									"value": "asda",
									"type": "text"
								},
								{
									"key": "content",
									"value": "assas",
									"type": "text"
								},
								{
									"key": "allow_comments",
									"value": "True",
									"type": "text"
								},
								{
									"key": "post_image",
									"value": "asasasas",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "https://discusstest.herokuapp.com/api/post/update/1/",
							"protocol": "https",
							"host": [
								"discusstest",
								"herokuapp",
								"com"
							],
							"path": [
								"api",
								"post",
								"update",
								"1",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Get_Post_By_Id",
					"request": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/api/post/getPost/1",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"post",
								"getPost",
								"1"
							]
						}
					},
					"response": []
				},
				{
					"name": "Get_All_User_Posts",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{TOKEN}}",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/api/post/getUserPosts/9",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"post",
								"getUserPosts",
								"9"
							]
						}
					},
					"response": []
				},
				{
					"name": "Get_All_Available_Post",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{TOKEN}}",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwNzY4Nzg5LCJqdGkiOiJkNWVmMThiNzE1Y2Q0NDdiODA3YmNlZTBmNTU5Yzc0ZCIsInVzZXJfaWQiOjR9.Br2rjUUsDHJ4iBFDsS9tHs-Bo4V12moQn4VoaDW711g",
								"type": "text",
								"disabled": true
							}
						],
						"url": {
							"raw": "http://127.0.0.1:8000/api/post/getPosts/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"post",
								"getPosts",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Get_Total_Avalibale_Post_Count",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwNDE0NzM3LCJqdGkiOiJjZTQ0NDk2M2M1NDM0ZmYxOWU2ZGQ1YWY0NGM5YzNkMyIsInVzZXJfaWQiOjEyfQ.ouW5tdRhifj-5kg_4Kwxn3AxvnevimU2UhX_h6OQ04o",
								"type": "text"
							}
						],
						"url": {
							"raw": "http://127.0.0.1:8000/api/post/getpostscount/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"post",
								"getpostscount",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Delete_Posts",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxMjAzNjMwLCJqdGkiOiI0ZWEyYTFkYWRlOGQ0YTEwYmUwMzIwY2Y0YzFmMGZiNSIsInVzZXJfaWQiOjZ9.535Z3YYiQoToFkC3uALlBfan6Bb97aQR32WVNhvDwGI",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "{",
									"value": "",
									"type": "text",
									"disabled": true
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/post/delete/54/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"post",
								"delete",
								"54",
								""
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Comments",
			"item": [
				{
					"name": "Get_Comments",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{TOKEN}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwNTA4MzA5LCJqdGkiOiJhYWQ4MTFlMzZhZGE0ODkzYTNlZWJkM2E4ZmY4MTRkMCIsInVzZXJfaWQiOjR9.jOG2KqOUBMM0l8iepOk8_6iz_TUpPIZDTPEQo8GOnss",
								"type": "text",
								"disabled": true
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "post_id",
									"value": "2",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/comment/get/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"comment",
								"get",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Create_Comments",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{TOKEN}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwNTA4MzA5LCJqdGkiOiJhYWQ4MTFlMzZhZGE0ODkzYTNlZWJkM2E4ZmY4MTRkMCIsInVzZXJfaWQiOjR9.jOG2KqOUBMM0l8iepOk8_6iz_TUpPIZDTPEQo8GOnss",
								"type": "text",
								"disabled": true
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "comment_id",
									"value": "16",
									"type": "text"
								},
								{
									"key": "content",
									"value": "55",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/comment/create/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"comment",
								"create",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Update_Comments",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{TOKEN}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/comment/update/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"comment",
								"update",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Delete_Comments",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{TOKEN}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "child_comment_id",
									"value": "16",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/comment/delete/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"comment",
								"delete",
								""
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Poll",
			"item": [
				{
					"name": "Create_poll",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyNDEzMDg2LCJqdGkiOiJkNzk4N2MzNWY3ZmM0M2QzOTg1YzdjMWNjNDI0OWIxOSIsInVzZXJfaWQiOjF9.4jqb1zI8LqSJMwoMOUHVpPGVK6fVKP2kHhgE7ECzYTQ",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "title",
									"value": "bc_polltest",
									"type": "text"
								},
								{
									"key": "allow_comments",
									"value": "True",
									"type": "text"
								},
								{
									"key": "content",
									"value": "hiiiii",
									"type": "text"
								},
								{
									"key": "poll_option1",
									"value": "aaa1",
									"type": "text"
								},
								{
									"key": "poll_option2",
									"value": "bbb2",
									"type": "text"
								},
								{
									"key": "poll_option3",
									"value": "ccb3",
									"type": "text"
								},
								{
									"key": "poll_option4",
									"value": "ddd4",
									"type": "text"
								},
								{
									"key": "poll_option5",
									"value": "eee5",
									"type": "text"
								},
								{
									"key": "poll_option6",
									"value": "fff7",
									"type": "text"
								},
								{
									"key": "private",
									"value": "False",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/poll/create/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"poll",
								"create",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Get_poll_by_id",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "GET",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxODA0OTM3LCJqdGkiOiJlMzU4OTBmMTExNjI0YzEzODQ3NmFmYzJiOWY4MzkwOSIsInVzZXJfaWQiOjV9.97OPZ0KowGg4MVYWTRKc2M77NSeoA8TlefN7TeSsFrc",
								"type": "text"
							}
						],
						"url": {
							"raw": "http://127.0.0.1:8000/api/poll/getPoll/96/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"poll",
								"getPoll",
								"96",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Get_poll_of_User",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "GET",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxODA0OTM3LCJqdGkiOiJlMzU4OTBmMTExNjI0YzEzODQ3NmFmYzJiOWY4MzkwOSIsInVzZXJfaWQiOjV9.97OPZ0KowGg4MVYWTRKc2M77NSeoA8TlefN7TeSsFrc",
								"type": "text",
								"disabled": true
							}
						],
						"url": {
							"raw": "http://127.0.0.1:8000/api/poll/getUserPolls/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"poll",
								"getUserPolls",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Delete_poll",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{TOKEN}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"url": {
							"raw": "http://192.168.0.124:8000/api/poll/deletePoll/4/",
							"protocol": "http",
							"host": [
								"192",
								"168",
								"0",
								"124"
							],
							"port": "8000",
							"path": [
								"api",
								"poll",
								"deletePoll",
								"4",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Vote",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyNDEzMDg2LCJqdGkiOiJkNzk4N2MzNWY3ZmM0M2QzOTg1YzdjMWNjNDI0OWIxOSIsInVzZXJfaWQiOjF9.4jqb1zI8LqSJMwoMOUHVpPGVK6fVKP2kHhgE7ECzYTQ",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "poll_id",
									"value": "1",
									"type": "text"
								},
								{
									"key": "poll_option_id",
									"value": "2",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/poll/vote/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"poll",
								"vote",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Get_All_Available_Polls",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{TOKEN}}",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxODA1MjA4LCJqdGkiOiIwMTFmODRlY2ZiYTk0ZTg1YTczZWU3OWQ3YzVhYzFhNiIsInVzZXJfaWQiOjJ9.2xwC9xSeM3dBiOot-kKfzNfcYT9bDGuDnksQma5y4sM",
								"type": "text",
								"disabled": true
							}
						],
						"url": {
							"raw": "http://192.168.0.124:8000/api/poll/getallPolls/",
							"protocol": "http",
							"host": [
								"192",
								"168",
								"0",
								"124"
							],
							"port": "8000",
							"path": [
								"api",
								"poll",
								"getallPolls",
								""
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Cloudinary",
			"item": [
				{
					"name": "Delete_cloudinary_image",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxNDM3MTQ0LCJqdGkiOiI5NDhlMTQwYWM0NDU0NWM0YjcxYmI0NzlkY2U1ZTAzMiIsInVzZXJfaWQiOjN9.j1o4ybuVuKl2cPsuwn0dMf0T_vRBfXT9a66Wz8fK3C4",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "public_id",
									"value": "ijlal/kw7lx08jwb6gaorwsy70",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/users/deleteimage/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"users",
								"deleteimage",
								""
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Discussion",
			"item": []
		},
		{
			"name": "Like",
			"item": [
				{
					"name": "Like",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{TOKEN}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\r\n\r\n    \"post_id\":50610\r\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://192.168.0.124:8000/api/post/like/",
							"protocol": "http",
							"host": [
								"192",
								"168",
								"0",
								"124"
							],
							"port": "8000",
							"path": [
								"api",
								"post",
								"like",
								""
							]
						}
					},
					"response": []
				}
			]
		}
	]
}
```

