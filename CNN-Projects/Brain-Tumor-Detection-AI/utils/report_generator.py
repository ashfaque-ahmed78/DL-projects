from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib.pagesizes import letter

import os



def generate_report(
        filename,
        image_path,
        prediction,
        confidence,
        probabilities
):

    doc = SimpleDocTemplate(
        filename,
        pagesize=letter
    )


    styles = getSampleStyleSheet()


    content = []


    # Title

    content.append(

        Paragraph(
            "Brain Tumor Detection AI Report",
            styles["Title"]
        )

    )


    content.append(
        Spacer(1,20)
    )



    # MRI Image

    if os.path.exists(image_path):

        img = Image(
            image_path,
            width=250,
            height=250
        )

        content.append(img)


    content.append(
        Spacer(1,20)
    )



    # Prediction

    content.append(

        Paragraph(

            f"Predicted Disease: {prediction.upper()}",

            styles["Heading2"]

        )

    )


    content.append(

        Paragraph(

            f"Confidence Score: {confidence:.2f}%",

            styles["Normal"]

        )

    )



    content.append(
        Spacer(1,20)
    )



    # Probability Table


    table_data = [

        ["Class","Probability"],

        [
            "Glioma",
            f"{probabilities[0]*100:.2f}%"
        ],

        [
            "Meningioma",
            f"{probabilities[1]*100:.2f}%"
        ],

        [
            "No Tumor",
            f"{probabilities[2]*100:.2f}%"
        ],

        [
            "Pituitary",
            f"{probabilities[3]*100:.2f}%"
        ]

    ]



    table = Table(
        table_data
    )


    table.setStyle(

        TableStyle([

            (
                "GRID",
                (0,0),
                (-1,-1),
                1,
                None
            ),

            (
                "ALIGN",
                (0,0),
                (-1,-1),
                "CENTER"
            )

        ])

    )



    content.append(table)



    content.append(
        Spacer(1,30)
    )



    # Model Information


    content.append(

        Paragraph(
            "AI Model: EfficientNetB0",
            styles["Normal"]
        )

    )


    content.append(

        Paragraph(
            "Framework: TensorFlow",
            styles["Normal"]
        )

    )


    content.append(

        Paragraph(
            "Task: Brain MRI Tumor Classification",
            styles["Normal"]
        )

    )



    content.append(
        Spacer(1,20)
    )



    # Disclaimer


    content.append(

        Paragraph(

            "Medical Disclaimer: This AI output is only for educational and research purposes. It should not replace professional medical diagnosis.",

            styles["Normal"]

        )

    )



    doc.build(content)