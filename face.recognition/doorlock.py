import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import numpy as np
from deepface import DeepFace

class DoorLock:
    def __init__(self, root):
        self.root = root
        self.root.title("도어락")
        self.code = ""
        self.correct_code = "1234"  # 설정된 비밀번호
        self.change_mode = False
        self.new_password_mode = False
        self.reset_timer = None
        self.registered_face = None

        # 웹캠 피드
        self.cap = cv2.VideoCapture(0)
        self.lmain = tk.Label(root)
        self.lmain.grid(row=0, column=0, columnspan=3)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.show_frame()

        self.display = tk.Entry(root, font=('Helvetica', 18), justify='center')
        self.display.grid(row=1, column=0, columnspan=3, ipadx=5, ipady=5)

        buttons = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '*', '0', '#'
        ]

        row_val = 2
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.button_click(x)
            tk.Button(root, text=button, width=5, height=2, font=('Helvetica', 14), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 2:
                col_val = 0
                row_val += 1

        # 얼굴 등록 버튼
        tk.Button(root, text="얼굴 등록", width=15, height=2, font=('Helvetica', 14), command=self.register_face).grid(row=row_val, column=0, columnspan=3)

    def show_frame(self):
        _, frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        if len(faces) > 0:
            x, y, w, h = faces[0]
            face = frame[y:y+h, x:x+w]
            if self.registered_face is not None:
                result = DeepFace.verify(face, self.registered_face, model_name='VGG-Face', enforce_detection=False)
                if result["verified"]:
                    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                else:
                    cv2image = np.zeros_like(frame)  # 검은 화면
            else:
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        else:
            cv2image = np.zeros_like(frame)  # 검은 화면

        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        self.lmain.after(10, self.show_frame)

    def register_face(self):
        _, frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        if len(faces) > 0:
            x, y, w, h = faces[0]
            self.registered_face = frame[y:y+h, x:x+w]
            messagebox.showinfo("성공", "얼굴이 등록되었습니다!")
        else:
            messagebox.showerror("오류", "얼굴을 인식하지 못했습니다. 다시 시도하세요.")

    def button_click(self, value):
        self.reset_input_timer()
        if value == '#':
            if self.change_mode:
                if self.new_password_mode:
                    self.save_new_password()
                else:
                    self.set_new_password()
            else:
                self.check_code()
        elif value == '*':
            if self.change_mode:
                self.clear_code()
                self.change_mode = False
                self.new_password_mode = False
                messagebox.showinfo("취소", "비밀번호 변경이 취소되었습니다.")
            else:
                self.change_mode = True
                self.clear_code()
                messagebox.showinfo("알림", "비밀번호 변경 모드입니다. 기존 비밀번호를 입력하세요.")
        else:
            self.code += value
            self.display.insert(tk.END, value)

    def check_code(self):
        if self.code.endswith(self.correct_code):
            messagebox.showinfo("성공", "문이 열렸습니다!")
        else:
            messagebox.showerror("오류", "비밀번호가 틀렸습니다.")
        self.clear_code()

    def set_new_password(self):
        if self.code.endswith(self.correct_code):
            self.clear_code()
            messagebox.showinfo("알림", "새 비밀번호를 입력하세요.")
            self.new_password_mode = True
        else:
            messagebox.showerror("오류", "기존 비밀번호가 틀렸습니다.")
            self.clear_code()
            self.change_mode = False

    def save_new_password(self):
        new_password = self.code
        if new_password:
            self.correct_code = new_password
            messagebox.showinfo("성공", "비밀번호가 변경되었습니다!")
        else:
            messagebox.showerror("오류", "새 비밀번호를 입력하세요.")
        self.clear_code()
        self.change_mode = False
        self.new_password_mode = False

    def clear_code(self):
        self.code = ""
        self.display.delete(0, tk.END)
        if self.reset_timer:
            self.root.after_cancel(self.reset_timer)
            self.reset_timer = None

    def reset_input_timer(self):
        if self.reset_timer:
            self.root.after_cancel(self.reset_timer)
        self.reset_timer = self.root.after(10000, self.clear_code)

if __name__ == "__main__":
    root = tk.Tk()
    app = DoorLock(root)
    root.mainloop()