from seleniumbase import BaseCase


# https://www.youtube.com/watch?v=D0-QGMacMxA&t=5338s

class UploadTest(BaseCase):
    def test_visible_upload(self):
        self.open("https://the-internet.herokuapp.com/upload")

        # get file path
        file_path = "./data/sample.png"

        # upload file
        self.choose_file("[id='file-upload']", file_path)

        # click the upload button
        self.click("[id='file-submit']")

        # assert file uploaded text
        self.assert_text("File Uploaded!", "[class='example'] > h3")

    def test_hidden_upload(self):
        self.open("https://practice.automationbro.com/cart/")

        # get file path
        file_path = "./data/sample.png"

        # add javascript code
        remove_hidden_class = "document.getElementById('upfile_1').classList.remove('file_input_hidden')"
        self.add_js_code(remove_hidden_class)

        # upload file
        self.choose_file("[id='upfile_1']", file_path)

        # click the upload button
        self.click("[id='upload_1']")

        # assert file uploaded text
        self.assert_text("File sample.png uploaded successfully but with warnings", "[class='file_messageblock_fileheader_label']")
