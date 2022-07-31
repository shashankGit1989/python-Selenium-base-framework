from seleniumbase import BaseCase


class FileUpload(BaseCase):
    def test_upload(self):
        self.open("https://practice.automationbro.com/cart/")
        # JS code make hidden fileupload button visible
        remove_hidden_class = "document.getElementById('upfile_1').classList.remove('file_input_hidden')"
        self.add_js_code(remove_hidden_class)
        # click on choose file button
        file_path = "./assets/Controller.jpg"
        self.choose_file('#upfile_1', file_path)
        # Click on upload button
        self.click('#upload_1')
        # check message
        self.assert_text("uploaded successfully", '#wfu_messageblock_header_1_label_1')
        print("--------DONE------------")
