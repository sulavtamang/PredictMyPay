# 💼 PredictMyPay

**PredictMyPay** is a sleek and interactive web app built with Streamlit that predicts a person's salary based on various career-related factors. Powered by machine learning, it provides instant salary estimates based on user inputs like age, experience, education, etc.

---

## 📁 Project Folder Structure
```
PredictMyPay/
├── app/
│ ├── assets/
│ ├── components/
│ ├── pages/
│ ├── utils/
│ └── main.py
├── data/
├── env/
├── models/
├── notebooks/
├── requirements.txt
├── LICENSE
└── README.md
```  

---

## 💻 Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/sulavtamang/PredictMyPay.git
cd PredictMyPay
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv env  # Create a virtual environment
source venv/bin/activate  # (Linux/Mac)
env\Scripts\activate  # (Windows)
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```
### **4️⃣ Navigate to the `app` folder inside root**
```bash
cd app
```
### **5️⃣ Run the Streamlit App**
```bash
streamlit run main.py
```
**Open the URL shown in your terminal (usually http://localhost:8501) to access the app.**

---

## 🚀 Features

- 🔍 Predicts salary in real-time using a trained ML model.
- 🎯 Clean, intuitive UI with a modern aesthetic.
- 📊 Visual feedback on prediction accuracy and confidence.
- 🧠 Built with XGBoost regression model.
- 📱 Responsive design — works on desktop and mobile.
- 🛠️ Modular code structure for easy maintenance and scalability.

---

## 🧠 How It Works

1. **User fills a form** with information like:
   - Name
   - Age
   - Education Level
   - Job Title
   - Years of Experience
   

2. **ML Model (XGBoost)** processes the input and predicts an estimated salary.

3. **Prediction is displayed instantly**.

---

## 💻 Tech Stack

| Component     | Tech Used             |
|---------------|----------------------|
| **Frontend**  | Streamlit            |
| **Backend**   | Python (Streamlit)   |
| **ML Model**  | XGBoost   |
| **Deployment**| Streamlit Community Cloud |

---

## 🧪 Testing

- ✅ Tested on desktop (Windows, Mac)
- ✅ Mobile view tested via browser
- ❌ No database or file storage used
- ✅ All predictions happen in-memory with preloaded model

---

## 📎 To-Do / Improvements

- [ ] Add database support for logging predictions
- [ ] Improve validation for all form fields
- [ ] Add user feedback form or ratings
- [ ] Deploy to Hugging Face / Vercel / AWS

---

## 📄 [License](LICENSE)

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for full license information.

---

## 🙌 Acknowledgments

- Streamlit for the awesome framework  
- XGBoost community  
- Your future employer (who’s probably hiring you after seeing this 😎)

---

## 👤 About the Creator

Built with ❤️ by **[Sulav Man Sing Tamang]** — a passionate data scientist and developer, building intuitive and impactful AI-powered applications.
  
🔗 [LinkedIn](https://www.linkedin.com/in/sulav-man-sing-tamang-269bb5190/)  
🔗 [GitHub](https://github.com/sulavtamang)
