# Authentication using Flask server-sided Sessions

## Authenticated Sessions
Server-sided session: After logging in, the server sets cookie called "session_id". This refers to the new authenticated session opened after logging in, that allows to preform authenticated tasks. 

Requests from client are sent to server with that session id. Server checks for any authenticated session that is linked to that session id. If you have a valid session, you are an authenticated client.

### Comments
UUID stands for Universally Unique Identifier. In Python, UUID is a 128-character string of alphanumeric variable type. Default uuid to return a new unique id.

hex attribute returns the UUID as a 32-character hexadecimal string without any hyphens.

The db init, db migrate, and db upgrade commands help you set up and apply the necessary database changes. After the initial setup, you don't need to run db.create_all() inside create_app() anymore.

This approach separates the database setup and migration logic from the create_app() function, making it more maintainable and suitable for different deployment environments.