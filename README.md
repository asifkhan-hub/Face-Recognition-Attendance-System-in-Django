# 🚀 Face Recognition Attendance System

A powerful **face recognition-based attendance system** built with Django, utilizing **deep learning** models for secure and accurate face detection and verification. This project supports **multi-camera input, real-time attendance logging, and an intuitive admin dashboard**.

---

## 🔑 Key Features

✅ **Real-Time Face Recognition**: Uses MTCNN for face detection and InceptionResnetV1 for face encoding.

📷 **Multi-Camera Support**: Works with multiple IP and local cameras.

📊 **Automated Attendance Logging**: Records attendance seamlessly without manual input.

📌 **Admin Dashboard**: Manage students, attendance records, and system settings easily.

🔊 **Alert Sound on Recognition**: Plays a sound using Pygame upon successful recognition.

🔒 **Secure Login & Access Control**: Ensures only authorized personnel can manage data.

---

## ⚙️ Installation Requirements

Ensure you have **Python** installed on your system. Then, install dependencies using `requirements.txt`.

### 📌 Prerequisites

- 🐍 Python 3.12.1
- 🏗️ Django
- 🎥 OpenCV
- 🔥 Torch & torchvision
- 🧠 Face recognition libraries (MTCNN, InceptionResnetV1)
- 🔊 Pygame (for alert sounds)

---

## 📥 Installation Steps

### 1️⃣ Clone the Repository
```sh
 git clone https://github.com/asifkhan-hub/Face-Recognition-Attendance-System-in-Django
```

### 2️⃣ Create a Virtual Environment *(Recommended)*
```sh
 python -m venv venv
 source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
 pip install -r requirements.txt
```

### 4️⃣ Apply Migrations
```sh
 python manage.py migrate
```

### 5️⃣ Run the Server
```sh
 python manage.py runserver
```

### 6️⃣ Access the Application
🌐 Open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your browser and log in.

---

## 🎯 Usage

👤 **Add Students**: Upload student images for recognition.

📡 **Start Face Recognition**: Connect a camera and track attendance.

📋 **View Attendance Records**: Check logs and export attendance data.

🔐 **Manage Users**: Control access permissions via the admin panel.

---

## 📜 License

This project is open-source and available under the **[MIT License](LICENSE)**.

---

## 📧 Contact

For inquiries or contributions, feel free to reach out:

📩 **Email**: [asifkhanhdn75@gmail.com](mailto:asifkhanhdn75@gmail.com)

🌍 **Website**: [apycoder.com](https://apycoder.com)

💡 **Follow & Contribute**: *Let's make attendance management smarter!* 🚀
