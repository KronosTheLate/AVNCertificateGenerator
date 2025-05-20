from nicegui import native, ui
import os
import json
import typst

root = os.path.dirname(os.path.abspath(__file__))

certificate_generator_output = {}

ui.label('Select certificate mode')
certificate_mode = ui.toggle([1, 2, 3], value=1).props('inline')


with ui.column().bind_visibility_from(certificate_mode, 'value', backward=lambda x: x==1):
    username = ui.input('Username')
with ui.column().bind_visibility_from(certificate_mode, 'value', backward=lambda x: x==2):
    ui.label('Number of cats')
    mode2_radio1 = ui.radio([1, 2, 3]).props('inline')
with ui.column().bind_visibility_from(certificate_mode, 'value', backward=lambda x: x==3):
    ui.label('Score of this program')
    mode3_select1 = ui.select([4, 5, 6], value=4)


def update_dict():
    certificate_generator_output["mode"]=certificate_mode.value
    certificate_generator_output["number_of_cats"]=mode2_radio1.value
    certificate_generator_output["score_of_program"]=mode3_select1.value
    certificate_generator_output["username"]=username.value

dict_path = os.path.join(root, "certgen_output_typst_input.json")
def write_dict():
    update_dict()
    with open(dict_path, "w") as f:
        json.dump(certificate_generator_output, f)
    print(f"Wrote dictionary `certificate_generator_output` to file `{dict_path}`")


def compile_document():
    write_dict()
    typst.compile(
        os.path.join(root, "main.typ"), 
        output=os.path.join(root, "main.pdf")
    )
    print(f"Document written.")

ui.button("Compile document", on_click = compile_document)

#ui.run(native=True)
ui.run(native=True, reload=False, port=native.find_open_port())