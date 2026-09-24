from krita import *
from PyQt5.QtCore import Qt, QTimer, QRectF
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QPushButton
)

class VerticalBarSlider(QWidget):
    """Vertical bar with value text written vertically.
    Click or drag anywhere → value jumps to that position."""

    def __init__(self, label_prefix="", is_percent=False, parent=None):
        super().__init__(parent)
        self.label_prefix = label_prefix
        self.is_percent = is_percent
        self._min = 0.0
        self._max = 100.0
        self._value = 50.0
        self._dragging = False

        self.setMinimumHeight(120)
        self.setMinimumWidth(36)
        self.setMaximumWidth(60)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.setCursor(Qt.PointingHandCursor)

    def setRange(self, minimum, maximum):
        self._min = float(minimum)
        self._max = float(maximum)
        self.update()

    def setValue(self, value):
        value = max(self._min, min(self._max, float(value)))
        if abs(value - self._value) > 0.01:
            self._value = value
            self.update()
            self.valueChanged(self._value)

    def value(self):
        return self._value

    def valueChanged(self, value):
        pass

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.fillRect(self.rect(), QColor(40, 40, 40))

        ratio = (self._value - self._min) / (self._max - self._min) if self._max > self._min else 0
        fill_height = int(self.height() * ratio)
        fill_rect = QRectF(3, self.height() - fill_height, self.width() - 6, fill_height)
        painter.setBrush(QColor(70, 140, 210))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(fill_rect, 4, 4)

        painter.setBrush(Qt.NoBrush)
        painter.setPen(QPen(QColor(90, 90, 90), 1))
        painter.drawRoundedRect(QRectF(2, 2, self.width()-4, self.height()-4), 5, 5)

        painter.save()
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        painter.setFont(font)
        painter.setPen(QColor(255, 255, 255))

        if self.is_percent:
            text = f"{self.label_prefix}{int(round(self._value))}%"
        else:
            if self._value < 10:
                text = f"{self.label_prefix}{self._value:.1f} px"
            else:
                text = f"{self.label_prefix}{int(round(self._value))} px"

        painter.translate(self.width() / 2, self.height() / 2)
        painter.rotate(-90)
        fm = painter.fontMetrics()
        text_width = fm.width(text)
        painter.drawText(int(-text_width / 2), int(fm.ascent() / 2), text)
        painter.restore()
        painter.end()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._dragging = True
            self._set_value_from_pos(event.pos().y())
            event.accept()

    def mouseMoveEvent(self, event):
        if self._dragging:
            self._set_value_from_pos(event.pos().y())
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._dragging = False
            event.accept()

    def _set_value_from_pos(self, y):
        ratio = 1.0 - (y / max(1, self.height()))
        ratio = max(0.0, min(1.0, ratio))
        new_value = self._min + ratio * (self._max - self._min)
        self.setValue(new_value)

class ProSlidersDocker(DockWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ProBrushSliders")

        main = QWidget(self)
        self.setWidget(main)
        layout = QVBoxLayout(main)
        layout.setContentsMargins(6, 8, 6, 8)
        layout.setSpacing(12)

        # ---------- SIZE ----------
        size_layout = QVBoxLayout()
        size_layout.setSpacing(3)
        size_layout.setContentsMargins(0, 0, 0, 0)

        # Centered + button
        size_plus_row = QHBoxLayout()
        size_plus_row.addStretch()
        self.size_plus = QPushButton("+")
        self.size_plus.setFixedSize(28, 26)
        self.size_plus.clicked.connect(lambda: self._nudge_size(+1))
        size_plus_row.addWidget(self.size_plus)
        size_plus_row.addStretch()
        size_layout.addLayout(size_plus_row)

        self.size_slider = VerticalBarSlider("Size: ", is_percent=False)
        self.size_slider.setRange(1, 1000)
        self.size_slider.setValue(20)
        self.size_slider.valueChanged = self._on_size_changed
        size_layout.addWidget(self.size_slider, stretch=1)

        # Centered − button
        size_minus_row = QHBoxLayout()
        size_minus_row.addStretch()
        self.size_minus = QPushButton("−")
        self.size_minus.setFixedSize(28, 26)
        self.size_minus.clicked.connect(lambda: self._nudge_size(-1))
        size_minus_row.addWidget(self.size_minus)
        size_minus_row.addStretch()
        size_layout.addLayout(size_minus_row)

        layout.addLayout(size_layout, stretch=1)

        # ---------- OPACITY ----------
        opacity_layout = QVBoxLayout()
        opacity_layout.setSpacing(3)
        opacity_layout.setContentsMargins(0, 0, 0, 0)

        # Centered + button
        opacity_plus_row = QHBoxLayout()
        opacity_plus_row.addStretch()
        self.opacity_plus = QPushButton("+")
        self.opacity_plus.setFixedSize(28, 26)
        self.opacity_plus.clicked.connect(lambda: self._nudge_opacity(+5))
        opacity_plus_row.addWidget(self.opacity_plus)
        opacity_plus_row.addStretch()
        opacity_layout.addLayout(opacity_plus_row)

        self.opacity_slider = VerticalBarSlider("Opacity: ", is_percent=True)
        self.opacity_slider.setRange(0, 100)
        self.opacity_slider.setValue(100)
        self.opacity_slider.valueChanged = self._on_opacity_changed
        opacity_layout.addWidget(self.opacity_slider, stretch=1)

        # Centered − button
        opacity_minus_row = QHBoxLayout()
        opacity_minus_row.addStretch()
        self.opacity_minus = QPushButton("−")
        self.opacity_minus.setFixedSize(28, 26)
        self.opacity_minus.clicked.connect(lambda: self._nudge_opacity(-5))
        opacity_minus_row.addWidget(self.opacity_minus)
        opacity_minus_row.addStretch()
        opacity_layout.addLayout(opacity_minus_row)

        layout.addLayout(opacity_layout, stretch=1)

        # Sync
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._sync_from_krita)
        self._timer.start(250)
        self._updating = False

    def canvasChanged(self, canvas):
        pass

    def _get_view(self):
        win = Application.activeWindow()
        if win and win.views():
            return win.views()[0]
        return None

    def _on_size_changed(self, value):
        if self._updating:
            return
        view = self._get_view()
        if view:
            view.setBrushSize(value)

    def _on_opacity_changed(self, value):
        if self._updating:
            return
        view = self._get_view()
        if view:
            view.setPaintingOpacity(value / 100.0)

    def _nudge_size(self, direction):
        current = self.size_slider.value()
        if current < 20:
            step = 0.5
        elif current < 100:
            step = 2
        else:
            step = 10
        self.size_slider.setValue(current + direction * step)

    def _nudge_opacity(self, direction):
        self.opacity_slider.setValue(self.opacity_slider.value() + direction)

    def _sync_from_krita(self):
        if self._updating:
            return
        view = self._get_view()
        if not view:
            return

        self._updating = True
        try:
            size = view.brushSize()
            if abs(self.size_slider.value() - size) > 0.3:
                self.size_slider.setValue(size)

            opacity = view.paintingOpacity() * 100
            if abs(self.opacity_slider.value() - opacity) > 0.5:
                self.opacity_slider.setValue(opacity)
        finally:
            self._updating = False