# Lane-Display-App
An application to control webpage display for vehicle lane instructions

This app is currently deployed at a trash processing facility. It is used to control the webpage displayed on a monitor for incoming trucks to use.

The app takes inputs from a control board through Webhooks. The requests send data which is stored in a JSON and indicates the directions to be displayed.
The application then updates the webpage with the instructions and serves the webpage on a single url for the access control intercom to use.
The intercom takes the webpage displayed in the url and shows it on the monitor.

This application effectively reduced the number of intercom connections from 160 to 1. The intercom could not function with 160 urls to use, but using the single url provided by the
application the control scheme can run smoothely.
