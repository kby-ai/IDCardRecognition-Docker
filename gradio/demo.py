import gradio as gr
import requests
import datadog_api_client
from PIL import Image


def idcard_recognition(frame1, frame2):
    if frame1 is None:
        return ["Front Image Empty", None]
    
    url = "http://127.0.0.1:8080/idcard_recognition_multi_page"
    if frame2 is None:
        files = {'file1': open(frame1, 'rb')}
    else:
        files = {'file1': open(frame1, 'rb'), 'file2': open(frame2, 'rb')}

    r = requests.post(url=url, files=files)

    html = None
    images = None
    mrz = None
    barcode = None

    status = r.json().get('Status')
    table_value = ""

    if r.json().get('MRZ') is not None:
        mrz = r.json().get('MRZ')

    if r.json().get('Barcode') is not None:
        barcode = r.json().get('Barcode')
        
    for key, value in r.json().items():
        if key == 'Status' or key == 'Images' or key == 'MRZ' or key == 'Position' or key == 'Barcode':
            continue

        mrz_value = ''
        if mrz is not None and mrz.get(key) is not None:
            mrz_value = mrz[key]
            del mrz[key]

        barcode_value = ''
        if barcode is not None and barcode.get(key) is not None:
            barcode_value = barcode[key]
            del barcode[key]

        if mrz is not None and barcode is not None:
            row_value = ("<tr>"
                            "<td>{key}</td>"
                            "<td>{value}</td>"
                            "<td>{mrz_value}</td>"
                            "<td>{barcode_value}</td>"
                        "</tr>".format(key=key, value=value, mrz_value=mrz_value, barcode_value=barcode_value))
        elif mrz is not None:
            row_value = ("<tr>"
                            "<td>{key}</td>"
                            "<td>{value}</td>"
                            "<td>{mrz_value}</td>"
                        "</tr>".format(key=key, value=value, mrz_value=mrz_value))
        elif barcode is not None:    
            row_value = ("<tr>"
                            "<td>{key}</td>"
                            "<td>{value}</td>"
                            "<td>{barcode_value}</td>"
                        "</tr>".format(key=key, value=value, barcode_value=barcode_value))
        else:
            row_value = ("<tr>"
                            "<td>{key}</td>"
                            "<td>{value}</td>"
                        "</tr>".format(key=key, value=value))

        table_value = table_value + row_value    

    if mrz is not None and barcode is not None:
        for key, value in mrz.items():
            if key == 'MRZ':
                value = value.replace('<', '&lt;')
                value = value.replace(',', '<p>')
    
            row_value = ("<tr>"
                            "<td>{key}</td>"
                            "<td>{value}</td>"
                            "<td>{mrz_value}</td>"
                            "<td></td>"
                        "</tr>".format(key=key, value='', mrz_value=value))
            table_value = table_value + row_value
    
        for key, value in barcode.items():
            if key == 'Barcode':
                value = value.replace('<', '&lt;')
                value = value.replace(',', '<p>')
    
            row_value = ("<tr>"
                            "<td>{key}</td>"
                            "<td>{value}</td>"
                            "<td></td>"
                            "<td>{barcode_value}</td>"
                        "</tr>".format(key=key, value='', barcode_value=value))
            table_value = table_value + row_value
    elif mrz is not None:
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
    elif barcode is not None:
        for key, value in barcode.items():
            if key == 'Barcode':
                value = value.replace('<', '&lt;')
                value = value.replace(',', '<p>')
    
            row_value = ("<tr>"
                            "<td>{key}</td>"
                            "<td>{value}</td>"
                            "<td>{barcode_value}</td>"
                        "</tr>".format(key=key, value='', barcode_value=value))
            table_value = table_value + row_value
    
    if mrz is not None and barcode is not None:
        html = ("<table>"
                    "<tr>"
                        "<th>Field</th>"
                        "<th>OCR</th>"
                        "<th>MRZ</th>"
                        "<th>Barcode</th>"
                    "</tr>"
                    "{table_value}"
                    "</table>".format(table_value=table_value))
    elif mrz is not None:
        html = ("<table>"
                    "<tr>"
                        "<th style=""width:20%"">Field</th>"
                        "<th style=""width:40%"">OCR</th>"
                        "<th style=""width:40%"">MRZ</th>"
                    "</tr>"
                    "{table_value}"
                    "</table>".format(table_value=table_value))
    elif barcode is not None:
        html = ("<table>"
                    "<tr>"
                        "<th style=""width:20%"">Field</th>"
                        "<th style=""width:40%"">OCR</th>"
                        "<th style=""width:40%"">Barcode</th>"
                    "</tr>"
                    "{table_value}"
                    "</table>".format(table_value=table_value))
    else:
        html = ("<table>"
                    "<tr>"
                        "<th>Field</th>"
                        "<th>OCR</th>"
                    "</tr>"
                    "{table_value}"
                    "</table>".format(table_value=table_value))
    
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
    # KBY-AI
    We offer SDKs for Face Recognition, Face Liveness Detection(Face Anti-Spoofing), and ID Card Recognition.<br/>
    Besides that, we can provide several AI models and development services in machine learning.

    ## Simple Installation & Simple API
    ```
    sudo docker pull kbyai/idcard-recognition:latest
    sudo docker run -e LICENSE="xxxxx" -p 8082:8080 -p 9002:9000 kbyai/idcard-recognition:latest
    ```      
    ## KYC Verification Demo
    https://github.com/kby-ai/KYC-Verification    
    """
    )
    with gr.TabItem("ID Card Recognition"):
        with gr.Row():
            with gr.Column(scale=3):
                id_image_input1 = gr.Image(type='filepath', label='Front')
                id_image_input2 = gr.Image(type='filepath', label='Back')
                gr.Examples(['idcard_examples/1.jpg', 'idcard_examples/2.jpg', 'idcard_examples/3.jpg'], 
                            inputs=id_image_input1)
                id_recognition_button = gr.Button("ID Card Recognition")
            with gr.Column(scale=5):
                id_result_output = gr.HTML()
        
            with gr.Column(scale=2):
                image_result_output = gr.HTML()

        id_recognition_button.click(idcard_recognition, inputs=[id_image_input1, id_image_input2], outputs=[id_result_output, image_result_output])

demo.launch(server_name="0.0.0.0", server_port=9000)
