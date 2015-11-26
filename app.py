from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    # Show usage
    return 'Usage: /<em>url</em>?<em>data</em>'

@app.route('/<path:path>')
def gettopost(path):
    # Create a form 
    app.logger.debug(request.url)
    app.logger.debug(path)
    app.logger.debug(request.query_string)

    if not path.startswith('http'):
        return redirect('/')

    html = '<!DOCTYPE html>'
    html += '<html><body>'
    html += '<form id="form" action="' + path + '" method="POST">'
    for key, value in request.args.iteritems():
        html += '<input type="hidden" name="' + key + '" value="' + value +'" />'
    html += '<button>Go!</button>' #In case script below to auto-submit fails
    html += '<script>document.getElementById("form").submit();</script>'
    html += '</form>'
    html += '</html></body>'

    return html

if __name__ == '__main__':
    app.debug = True
    app.run()

