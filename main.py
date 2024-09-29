from flask import Flask

app = Flask(__name__)

@app.route("/launch")
def launch():
    """
    Setup a receiving point at some URL that will accept an HTTP POST message from a Tool Consumer.
    The script at this page should first verify that the received request is an LTI request.
    The POST request should contain `lti_message_type` with a value of 'basic-lti-launch-request',
    `lti_version` with a value of 'LTI-1p0' for LTI 1, `oauth_consumer_key`, and a `resource_link_id`,
    which is a unique id referencing the link, or placement, of the tool within the consumer's pages.

    If any of these are missing, then the request is not a valid LTI request. 
    """
    if request.method == 'POST':
        return "TODO!"
    else:
        return "Some kind of error!"
