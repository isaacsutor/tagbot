from dash import html

class HeaderComponent:
    def __init__(self, header_text):
        self.header_text = header_text

    def get_component(self):
        header = html.H4(
            self.header_text, className="bg-primary text-white p-2 mb-2 text-center"
        )
        return header