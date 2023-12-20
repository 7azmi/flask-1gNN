from flask import Flask, jsonify, request
import os
import requests

#from push_ups import pushup  # Import your custom pose detection module

app = Flask(__name__)
VIDEO_PATH = 'downloaded_video.mp4'

def download_video(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open(VIDEO_PATH, 'wb') as file:
            file.write(response.content)
        return True
    return False


@app.route('/count_pushups', methods=['POST'])
def count_pushups():
    data = request.json
    video_url = data.get('video_url')

    if not video_url:
        return jsonify({'error': 'No video URL provided'}), 400

    if download_video(video_url):
        print(video_url)
        from push_ups import pushup
        pushup_count = pushup.calculate_pushups()  # Use your existing function
        os.remove(VIDEO_PATH)  # Clean up by removing the downloaded video
        return jsonify({'pushup_count': pushup_count})
    else:
        return jsonify({'error': 'Failed to download video'}), 500



# Test route to trigger the /count_pushups route for testing
@app.route('/test', methods=['GET'])
def test_count_pushups():
    # Provide a sample JSON data for testing
    sample_data = {'video_url': 'https://example.com/sample_video.mp4'}

    # Send a POST request to /count_pushups for testing
    response = app.test_client().post('/count_pushups', json=sample_data)

    # Return the response from /count_pushups as the test result
    return sample_data


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
