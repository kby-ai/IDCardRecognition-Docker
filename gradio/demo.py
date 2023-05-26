import gradio as gr
import requests
import datadog_api_client
from PIL import Image

def check_liveness(frame):
    url = "http://127.0.0.1:8080/check_liveness"
    file = {'file': open(frame, 'rb')}

    r = requests.post(url=url, files=file)
    result = r.json().get('face_state').get('result')

    html = None
    faces = None
    if r.json().get('face_state').get('is_not_front') is not None:
        liveness_score = r.json().get('face_state').get('liveness_score')
        eye_closed = r.json().get('face_state').get('eye_closed')
        is_boundary_face = r.json().get('face_state').get('is_boundary_face')
        is_not_front = r.json().get('face_state').get('is_not_front')
        is_occluded = r.json().get('face_state').get('is_occluded')
        is_small = r.json().get('face_state').get('is_small')
        luminance = r.json().get('face_state').get('luminance')
        mouth_opened = r.json().get('face_state').get('mouth_opened')
        quality = r.json().get('face_state').get('quality')

        html = ("<table>"
                    "<tr>"
                        "<th>Face State</th>"
                        "<th>Value</th>"
                    "</tr>"
                    "<tr>"
                        "<td>Result</td>"
                        "<td>{result}</td>"
                    "</tr>"
                    "<tr>"
                        "<td>Liveness Score</td>"
                        "<td>{liveness_score}</td>"
                    "</tr>"
                    "<tr>"
                        "<td>Quality</td>"
                        "<td>{quality}</td>"
                    "</tr>"
                    "<tr>"
                        "<td>Luminance</td>"
                        "<td>{luminance}</td>"
                    "</tr>"
                    "<tr>"
                        "<td>Is Small</td>"
                        "<td>{is_small}</td>"
                    "</tr>"
                    "<tr>"
                        "<td>Is Boundary</td>"
                        "<td>{is_boundary_face}</td>"
                    "</tr>"
                    "<tr>"
                        "<td>Is Not Front</td>"
                        "<td>{is_not_front}</td>"
                    "</tr>"
                    "<tr>"
                        "<td>Face Occluded</td>"
                        "<td>{is_occluded}</td>"
                    "</tr>"
                    "<tr>"
                        "<td>Eye Closed</td>"
                        "<td>{eye_closed}</td>"
                    "</tr>"
                    "<tr>"
                        "<td>Mouth Opened</td>"
                        "<td>{mouth_opened}</td>"
                    "</tr>"
                    "</table>".format(liveness_score=liveness_score, quality=quality, luminance=luminance, is_small=is_small, is_boundary_face=is_boundary_face,
                                      is_not_front=is_not_front, is_occluded=is_occluded, eye_closed=eye_closed, mouth_opened=mouth_opened, result=result))

    else:
        html = ("<table>"
            "<tr>"
                "<th>Face State</th>"
                "<th>Value</th>"
            "</tr>"
            "<tr>"
                "<td>Result</td>"
                "<td>{result}</td>"
            "</tr>"
            "</table>".format(result=result))

    try:
        image = Image.open(frame)        

        for face in r.json().get('faces'):
            x1 = face.get('x1')
            y1 = face.get('y1')
            x2 = face.get('x2')
            y2 = face.get('y2')

            if x1 < 0:
                x1 = 0
            if y1 < 0:
                y1 = 0
            if x2 >= image.width:
                x2 = image.width - 1
            if y2 >= image.height:
                y2 = image.height - 1

            face_image = image.crop((x1, y1, x2, y2))
            face_image_ratio = face_image.width / float(face_image.height)
            resized_w = int(face_image_ratio * 150)
            resized_h = 150

            face_image = face_image.resize((int(resized_w), int(resized_h)))

            if faces is None:
                faces = face_image
            else:
                new_image = Image.new('RGB',(faces.width + face_image.width + 10, 150), (80,80,80))

                new_image.paste(faces,(0,0))
                new_image.paste(face_image,(faces.width + 10, 0))
                faces = new_image.copy()
    except:
        pass

    return [faces, html]

def compare_face(frame1, frame2):
    url = "http://127.0.0.1:8081/compare_face"
    files = {'file1': open(frame1, 'rb'), 'file2': open(frame2, 'rb')}

    r = requests.post(url=url, files=files)

    html = None
    faces = None

    compare_result = r.json().get('compare_result')
    compare_similarity = r.json().get('compare_similarity')

    html = ("<table>"
                "<tr>"
                    "<th>Compare Result</th>"
                    "<th>Value</th>"
                "</tr>"
                "<tr>"
                    "<td>Result</td>"
                    "<td>{compare_result}</td>"
                "</tr>"
                "<tr>"
                    "<td>Similarity</td>"
                    "<td>{compare_similarity}</td>"
                "</tr>"
                "</table>".format(compare_result=compare_result, compare_similarity=compare_similarity))

    try:
        image1 = Image.open(frame1)
        image2 = Image.open(frame2)

        face1 = None
        face2 = None

        if r.json().get('face1') is not None:
            face = r.json().get('face1')
            x1 = face.get('x1')
            y1 = face.get('y1')
            x2 = face.get('x2')
            y2 = face.get('y2')

            if x1 < 0:
                x1 = 0
            if y1 < 0:
                y1 = 0
            if x2 >= image1.width:
                x2 = image1.width - 1
            if y2 >= image1.height:
                y2 = image1.height - 1

            face1 = image1.crop((x1, y1, x2, y2))
            face_image_ratio = face1.width / float(face1.height)
            resized_w = int(face_image_ratio * 150)
            resized_h = 150

            face1 = face1.resize((int(resized_w), int(resized_h)))

        if r.json().get('face2') is not None:
            face = r.json().get('face2')
            x1 = face.get('x1')
            y1 = face.get('y1')
            x2 = face.get('x2')
            y2 = face.get('y2')

            if x1 < 0:
                x1 = 0
            if y1 < 0:
                y1 = 0
            if x2 >= image2.width:
                x2 = image2.width - 1
            if y2 >= image2.height:
                y2 = image2.height - 1

            face2 = image2.crop((x1, y1, x2, y2))
            face_image_ratio = face2.width / float(face2.height)
            resized_w = int(face_image_ratio * 150)
            resized_h = 150

            face2 = face2.resize((int(resized_w), int(resized_h)))

        if face1 is not None and face2 is not None:
            new_image = Image.new('RGB',(face1.width + face2.width + 10, 150), (80,80,80))

            new_image.paste(face1,(0,0))
            new_image.paste(face2,(face1.width + 10, 0))
            faces = new_image.copy()
        elif face1 is not None and face2 is None:
            new_image = Image.new('RGB',(face1.width + face1.width + 10, 150), (80,80,80))

            new_image.paste(face1,(0,0))
            faces = new_image.copy()
        elif face1 is None and face2 is not None:
            new_image = Image.new('RGB',(face2.width + face2.width + 10, 150), (80,80,80))

            new_image.paste(face2,(face2.width + 10, 0))
            faces = new_image.copy()

    except:
        pass

    return [faces, html]

def idcard_recognition(frame):
    url = "http://127.0.0.1:8082/idcard_recognition"
    files = {'file': open(frame, 'rb')}

    r = requests.post(url=url, files=files)

    html = None
    images = None
    mrz = None

    status = r.json().get('Status')
    table_value = ""

    if r.json().get('MRZ') is not None:
        mrz = r.json().get('MRZ')

    for key, value in r.json().items():
        if key == 'Status' or key == 'Images' or key == 'MRZ' or key == 'Position':
            continue

        mrz_value = ''
        if mrz is not None and mrz.get(key) is not None:
            mrz_value = mrz[key]
            del mrz[key]

        row_value = ("<tr>"
                        "<td>{key}</td>"
                        "<td>{value}</td>"
                        "<td>{mrz_value}</td>"
                    "</tr>".format(key=key, value=value, mrz_value=mrz_value))
        table_value = table_value + row_value


    if mrz is not None:
        for key, value in mrz.items():
            if key == 'MRZ':
                value = value.replace('<', '&lt;')
                value = value.replace(',', '<p>')

            row_value = ("<tr>"
                            "<td>{key}</td>"
                            "<td>{value}</td>"
                            "<td>{mrz_value}</td>"
                        "</tr>".format(key=key, value='', mrz_value=value))
            table_value = table_value + row_value
            

    html = ("<table>"
                "<tr>"
                    "<th style=""width:20%"">Field</th>"
                    "<th style=""width:40%"">Value</th>"
                    "<th style=""width:40%"">MRZ</th>"
                "</tr>"
                "<tr>"
                    "<td>Status</td>"
                    "<td>{status}</td>"
                    "<td></td>"
                "</tr>"
                "{table_value}"
                "</table>".format(status=status, table_value=table_value))
    
    table_value = ""
    for key, value in r.json().items():
        if key == 'Images':
            for image_key, image_value in value.items():
                row_value = ("<tr>"
                                "<td>{key}</td>"
                                "<td><img src=""data:image/png;base64,{base64_image} width = '200'  height= '100' /></td>"
                            "</tr>".format(key=image_key, base64_image=image_value))
                table_value = table_value + row_value

    images = ("<table>"
                "<tr>"
                    "<th>Field</th>"
                    "<th>Image</th>"
                "</tr>"
                "{table_value}"
                "</table>".format(table_value=table_value))
    
    return [html, images]

with gr.Blocks() as demo:
    gr.Markdown(
        """
    # KBY-AI Technology
    We offer SDKs for face recognition, liveness detection, and ID card recognition.
    """
    )
    with gr.TabItem("Face Liveness Detection"):
        with gr.Row():
            with gr.Column():
                live_image_input = gr.Image(type='filepath')
                gr.Examples(['live_examples/1.jpg', 'live_examples/2.jpg', 'live_examples/3.jpg', 'live_examples/4.jpg'], 
                            inputs=live_image_input)
                check_liveness_button = gr.Button("Check Liveness")
            with gr.Column():
                liveness_face_output = gr.Image(type="pil").style(height=150)
                livness_result_output = gr.HTML()
        
        check_liveness_button.click(check_liveness, inputs=live_image_input, outputs=[liveness_face_output, livness_result_output])
    with gr.TabItem("Face Recognition"):
        with gr.Row():
            with gr.Column():
                compare_face_input1 = gr.Image(type='filepath')
                gr.Examples(['face_examples/1.jpg', 'face_examples/3.jpg', 'face_examples/5.jpg', 'face_examples/7.jpg', 'face_examples/9.jpg'], 
                            inputs=compare_face_input1)
                compare_face_button = gr.Button("Compare Face")
            with gr.Column():
                compare_face_input2 = gr.Image(type='filepath')
                gr.Examples(['face_examples/2.jpg', 'face_examples/4.jpg', 'face_examples/6.jpg', 'face_examples/8.jpg', 'face_examples/10.jpg'], 
                            inputs=compare_face_input2)
            with gr.Column():
                compare_face_output = gr.Image(type="pil").style(height=150)
                compare_result_output = gr.HTML(label='Result')

        compare_face_button.click(compare_face, inputs=[compare_face_input1, compare_face_input2], outputs=[compare_face_output, compare_result_output])
    with gr.TabItem("ID Card Recognition"):
        with gr.Row():
            with gr.Column(scale=3):
                id_image_input = gr.Image(type='filepath')
                gr.Examples(['idcard_examples/1.jpg', 'idcard_examples/2.jpg', 'idcard_examples/3.jpg'], 
                            inputs=id_image_input)
                id_recognition_button = gr.Button("ID Card Recognition")
            with gr.Column(scale=5):
                id_result_output = gr.HTML()
        
            with gr.Column(scale=2):
                image_result_output = gr.HTML()

        id_recognition_button.click(idcard_recognition, inputs=id_image_input, outputs=[id_result_output, image_result_output])

demo.launch(server_name="0.0.0.0", server_port=9000)