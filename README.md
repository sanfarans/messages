# Messages API

Simple API for storing messages

## Live version

API available live at https://epic-messages-api.herokuapp.com

## Documentation

To login head to https://epic-messages-api.herokuapp.com/auth/login

After passing your credentail you will receive Token in return. That Token should be passed each new request.



Message consist of two fields:
  - text
  - views (views cannot be set by user)


  
Creating new messages available at the main page (POST)

Viewing existing messages available at '/<message_id>' (GET. PUT, DELETE)

Full endpoints documentation is available at https://epic-messages-api.herokuapp.com/swagger/
