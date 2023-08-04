# Authentication using Flask server-sided Sessions

## Authenticated Sessions
Server-sided session: After logging in, the server sets cookie called "session_id". This refers to the new authenticated session opened after logging in, that allows to preform authenticated tasks. 

Requests from client are sent to server with that session id. Server checks for any authenticated session that is linked to that session id. If you have a valid session, you are an authenticated client.