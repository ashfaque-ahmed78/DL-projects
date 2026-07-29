from flask import (
    Flask,
    render_template,
    request,
    send_file,
    session
)

import os


from werkzeug.utils import secure_filename


from utils.preprocess import preprocess_image

from utils.predictor import predict_image

from utils.report_generator import generate_report



app = Flask(__name__)


app.secret_key = "brain_tumor_ai_secret"



UPLOAD_FOLDER = "static/uploads"

REPORT_FOLDER = "static/reports"



os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


os.makedirs(
    REPORT_FOLDER,
    exist_ok=True
)




@app.route("/")
def home():

    return render_template(
        "index.html"
    )





@app.route("/predict", methods=["POST"])
def predict():


    image = request.files["image"]



    filename = secure_filename(
        image.filename
    )


    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )


    image.save(filepath)




    # Preprocess

    with open(filepath,"rb") as f:

        image_array, original_image = preprocess_image(f)




    # Prediction

    prediction, confidence, probabilities = predict_image(
        image_array
    )




    # Save session data

    session["image_path"] = filepath

    session["prediction"] = prediction

    session["confidence"] = confidence

    session["probabilities"] = probabilities.tolist()




    # Disease Information


    disease_info = {


        "glioma":{

            "title":"Glioma Tumor",

            "description":
            "Glioma develops from glial cells of the brain.",

            "symptoms":[

                "Headache",

                "Seizures",

                "Vision problems"

            ]

        },



        "meningioma":{

            "title":"Meningioma Tumor",

            "description":
            "Meningioma develops from protective brain membranes.",

            "symptoms":[

                "Head pressure",

                "Weakness",

                "Balance problems"

            ]

        },



        "pituitary":{

            "title":"Pituitary Tumor",

            "description":
            "Pituitary tumors affect hormone regulation.",

            "symptoms":[

                "Vision changes",

                "Fatigue",

                "Hormonal imbalance"

            ]

        },



        "notumor":{

            "title":"No Tumor Detected",

            "description":
            "No tumor pattern detected by AI.",

            "symptoms":[

                "No abnormal pattern detected"

            ]

        }

    }



    info = disease_info.get(

        prediction.lower(),

        disease_info["notumor"]

    )




    return render_template(

        "result.html",

        image_path=filepath,

        prediction=prediction,

        confidence=confidence,

        probabilities=probabilities,

        info=info

    )







@app.route("/download_report")
def download_report():


    report_path = os.path.join(

        REPORT_FOLDER,

        "Brain_Tumor_AI_Report.pdf"

    )



    generate_report(

        filename=report_path,

        image_path=session["image_path"],

        prediction=session["prediction"],

        confidence=session["confidence"],

        probabilities=session["probabilities"]

    )



    return send_file(

        report_path,

        as_attachment=True

    )





if __name__ == "__main__":

    app.run(
        debug=True
    )