React
===========

You MUST run a file server in addition to the Flask servet you create. To do that, on your local machine (not Vagrant), run the following commands: 

    $ cd react-integration-example
    $ python2 server-override.py 5002

You need to run that server IN ADDITION to your flask server.py file. I have it set to run on port 5002, but you can run it on any free port, just make sure the address you use when you link your jsx files uses the port you're using.

Explanation
-----------

since we're running with `babel-standalone` to translate our JSX
live, Babel makes AJAX requests to get your JSX and convert it. Under Chrome
and Firefox, making AJAX requests does not work with `file://` protocol files.
Running under HTTP makes it work.

If we converted our jsx to js with the command-line (nice but not great for
first-time learners), we wouldn't have this problem (that is, React has no
problem running under `file://`, it's just Babel)

Alternatively, you could start up Chrome with (OSX):

     $ open /Applications/Google\ Chrome.app/ --args --allow-file-access-from-files

server-override.py
Is a file that sets specific html header values to prevent header errors.
