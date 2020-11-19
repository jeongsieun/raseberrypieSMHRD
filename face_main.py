from flask import Flask, render_template
import os
import boto3

app = Flask(__name__)
def compare_faces():
    source_file='input.jpg'

    target_file='face.jpg'

 

    client=boto3.client('rekognition')

 

    imageSource=open(source_file,'rb')

    imageTarget=open(target_file,'rb')
    
    try:

        response=client.compare_faces(SimilarityThreshold=0,
                                      SourceImage={'Bytes': imageSource.read()},
                                      TargetImage={'Bytes': imageTarget.read()})
    
        for faceMatch in response['FaceMatches']:
            result = faceMatch['Similarity']

        imageSource.close()
        imageTarget.close()     
        return result
    except:
        return 0

@app.route("/detect")
def detect():
    os.system("raspistill -t 5 -o 'input.jpg'")
    result = compare_faces()
    return str(result)

@app.route("/")
def index():
    return render_template('main2.html')

if __name__ == "__main__":
    app.run(debug=True)
