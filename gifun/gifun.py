from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def upload():
    return render_template('index.html')


@app.route('/outcome', methods=['GET', 'POST'])
def userupload():
    f = request.files['file']

    f.save(f.filename)
    key = 'acc_3db164ecf62e32f'
    secret = 'a5942582b76e3b9bc1d04ff110b86aff'

    r = requests.post('https://api.imagga.com/v2/uploads',
                      auth=(key, secret),
                      files={'image': open(f.filename, 'rb')})
    res_post = r.json()['result']['upload_id']

    response = requests.get('https://api.imagga.com/v2/tags',
                            auth=(key, secret),
                            params={'image_upload_id': res_post})
    re = response.json()['result']['tags'][0]['tag']['en']

    response = requests.get('http://api.giphy.com/v1/gifs/search',
                            params={'q': re,
                                    'api_key': 'UTDa1aD9R7s7ccsu1tHtzfugWUSMMBMO'})
    res = response.json()['data']

    address = []
    for i in range(0, 10):
        resp = res[i]['images']['fixed_height']['url']
        address.append(resp)

    return render_template('outcome.html', resp=tuple(address))


if __name__ == '__main__':
    app.run(debug=True)
