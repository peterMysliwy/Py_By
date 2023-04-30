
class Slider:
    def __init__(self, start_btn, hide_btn, frame, anim):
        self.start = start_btn
        self.hide = hide_btn
        self.left_frame = frame
        self.widget_width = 0
        self.slider_anim = anim

        # direct communication between animation asn width
        self.slider_anim.valueChanged.connect(self.adjustWidth)

    def adjustWidth(self, val):
        self.left_frame.setFixedWidth(val)

    def hide_show(self, state):
        if self.left_frame.width() > 0:
            self.widget_width = self.left_frame.width()
            self.slider_anim.setStartValue(self.widget_width)
            self.slider_anim.setEndValue(0)
        else:
            self.slider_anim.setStartValue(0)
            self.slider_anim.setEndValue(self.widget_width)
        self.slider_anim.start()

    def start_changed(self, event):
        self.start.setEnabled(False)
        if self.left_frame.width() > 0:
            self.hide_show(False)

    def stop_changed(self):
        self.start.toggle()
        self.start.setEnabled(True)